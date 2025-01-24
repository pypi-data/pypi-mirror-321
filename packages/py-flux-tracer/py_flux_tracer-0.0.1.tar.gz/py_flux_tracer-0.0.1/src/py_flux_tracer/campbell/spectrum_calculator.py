import numpy as np
import pandas as pd
from scipy import signal


class SpectrumCalculator:
    def __init__(
        self,
        df: pd.DataFrame,
        fs: float,
        lag_second: float,
        apply_lag_keys: list[str],
        apply_window: bool = True,
        plots: int = 30,
        window_type: str = "hamming",
    ):
        """
        データロガーから取得したデータファイルを用いて計算を行うクラス。

        Args:
            df (pd.DataFrame): pandasのデータフレーム。解析対象のデータを含む。
            apply_lag_keys (list[str]): コスペクトルの遅れ時間補正を適用するキーのリスト。
            fs (float): サンプリング周波数（Hz）。データのサンプリングレートを指定。
            lag_second (float): 遅延時間（秒）。データの遅延を指定。
            apply_window (bool, optional): 窓関数を適用するフラグ。デフォルトはTrue。
            plots (int): プロットする点の数。可視化のためのデータポイント数。
        """
        self._df: pd.DataFrame = df
        self._fs: float = fs
        self._apply_lag_keys: list[str] = apply_lag_keys
        self._apply_window: bool = apply_window
        self._lag_second: float = lag_second
        self._plots: int = plots
        self._window_type: str = window_type

    def calculate_co_spectrum(
        self,
        key1: str,
        key2: str,
        dimensionless: bool = True,
        frequency_weighted: bool = True,
        interpolate_points: bool = True,
        scaling: str = "spectrum",
    ) -> tuple:
        """
        DataFrameから指定されたkey1とkey2のコスペクトルを計算する
        fft.cと同様のロジックで実装

        Args:
            key1 (str): データの列名1
            key2 (str): データの列名2
            dimensionless (bool, optional): Trueの場合、分散で割って無次元化を行う。デフォルトはTrue。
            frequency_weighted (bool, optional): 周波数の重みづけを適用するかどうか。デフォルトはTrue。
            interpolate_points (bool, optional): 等間隔なデータ点を生成するかどうか（対数軸上で等間隔）
            scaling (str): "density"でスペクトル密度、"spectrum"でスペクトル。デフォルトは"spectrum"。

        Returns:
            tuple: (freqs, co_spectrum, corr_coef)
                - freqs (np.ndarray): 周波数軸（対数スケールの場合は対数変換済み）
                - co_spectrum (np.ndarray): コスペクトル（対数スケールの場合は対数変換済み）
                - corr_coef (float): 変数の相関係数
        """
        freqs, co_spectrum, _, corr_coef = self.calculate_cross_spectrum(
            key1=key1,
            key2=key2,
            dimensionless=dimensionless,
            frequency_weighted=frequency_weighted,
            interpolate_points=interpolate_points,
            scaling=scaling,
        )
        return freqs, co_spectrum, corr_coef

    def calculate_cross_spectrum(
        self,
        key1: str,
        key2: str,
        dimensionless: bool = True,
        frequency_weighted: bool = True,
        interpolate_points: bool = True,
        scaling: str = "spectrum",
    ) -> tuple:
        """
        DataFrameから指定されたkey1とkey2のコスペクトルとクアドラチャスペクトルを計算する
        fft.cと同様のロジックで実装

        Args:
            key1 (str): データの列名1
            key2 (str): データの列名2
            dimensionless (bool, optional): Trueの場合、分散で割って無次元化を行う。デフォルトはTrue。
            frequency_weighted (bool, optional): 周波数の重みづけを適用するかどうか。デフォルトはTrue。
            interpolate_points (bool, optional): 等間隔なデータ点を生成するかどうか（対数軸上で等間隔）
            scaling (str): "density"でスペクトル密度、"spectrum"でスペクトル。デフォルトは"spectrum"。

        Returns:
            tuple: (freqs, co_spectrum, quadrature_spectrum, corr_coef)
                - freqs (np.ndarray): 周波数軸（対数スケールの場合は対数変換済み）
                - co_spectrum (np.ndarray): コスペクトル（対数スケールの場合は対数変換済み）
                - quadrature_spectrum (np.ndarray): クアドラチャスペクトル（対数スケールの場合は対数変換済み）
                - corr_coef (float): 変数の相関係数
        """
        # バリデーション
        valid_scaling_options = ["density", "spectrum"]
        if scaling not in valid_scaling_options:
            raise ValueError(
                f"'scaling'は次のパラメータから選択してください: {valid_scaling_options}"
            )

        fs: float = self._fs
        df: pd.DataFrame = self._df.copy()
        # key1とkey2に一致するデータを取得
        data1: np.ndarray = np.array(df[key1].values)
        data2: np.ndarray = np.array(df[key2].values)

        # 遅れ時間の補正
        if key2 in self._apply_lag_keys:
            data1, data2 = SpectrumCalculator._correct_lag_time(
                data1=data1, data2=data2, fs=fs, lag_second=self._lag_second
            )

        # トレンド除去
        data1 = SpectrumCalculator._detrend(data=data1, fs=fs, first=True)
        data2 = SpectrumCalculator._detrend(data=data2, fs=fs, first=True)

        # トレンド除去後のデータでパラメータを計算
        data_length: int = len(data1)  # データ長
        corr_coef: float = np.corrcoef(data1, data2)[0, 1]  # 相関係数の計算

        # 窓関数の適用
        window_scale = 1.0
        if self._apply_window:
            window = SpectrumCalculator._generate_window_function(
                type=self._window_type, data_length=data_length
            )
            data1 *= window
            data2 *= window
            window_scale = np.mean(window**2)

        # FFTの計算
        fft1 = np.fft.rfft(data1)
        fft2 = np.fft.rfft(data2)

        # 周波数軸の作成
        freqs: np.ndarray = np.fft.rfftfreq(data_length, 1.0 / self._fs)

        # fft.cと同様のコスペクトル計算ロジック
        co_spectrum = np.zeros(len(freqs))
        quad_spectrum = np.zeros(len(freqs))

        for i in range(1, len(freqs)):  # 0Hz成分を除外
            z1 = fft1[i]
            z2 = fft2[i]
            z1_star = np.conj(z1)
            z2_star = np.conj(z2)

            # x1 = z1 + z1*, x2 = z2 + z2*
            x1 = z1 + z1_star
            x2 = z2 + z2_star
            x1_re = x1.real
            x1_im = x1.imag
            x2_re = x2.real
            x2_im = x2.imag

            # y1 = z1 - z1*, y2 = z2 - z2*
            y1 = z1 - z1_star
            y2 = z2 - z2_star
            # 虚部と実部を入れ替え
            y1_re = y1.imag
            y1_im = -y1.real
            y2_re = y2.imag
            y2_im = -y2.real

            # コスペクトルとクァドラチャスペクトルの計算
            conj_x1_x2 = complex(
                x1_re * x2_re + x1_im * x2_im, x1_im * x2_re - x1_re * x2_im
            )
            conj_y1_y2 = complex(
                y1_re * y2_re + y1_im * y2_im, y1_im * y2_re - y1_re * y2_im
            )

            # スケーリングパラメータを計算
            scale_factor = 0.5 / (len(data1) * window_scale)  # spectrumの場合
            # スペクトル密度の場合、周波数間隔で正規化
            if scaling == "density":
                df = freqs[1] - freqs[0]  # 周波数間隔
                scale_factor = 0.5 / (len(data1) * window_scale * df)

            # スケーリングを適用
            co_spectrum[i] = conj_x1_x2.real * scale_factor
            quad_spectrum[i] = conj_y1_y2.real * scale_factor

        # 周波数の重みづけ
        if frequency_weighted:
            co_spectrum[1:] *= freqs[1:]
            quad_spectrum[1:] *= freqs[1:]

        # 無次元化
        if dimensionless:
            cov_matrix: np.ndarray = np.cov(data1, data2)
            covariance: float = cov_matrix[0, 1]  # 共分散
            co_spectrum /= covariance
            quad_spectrum /= covariance

        if interpolate_points:
            # 補間処理（0Hz除外の前に実施）
            log_freq_min = np.log10(0.001)
            log_freq_max = np.log10(freqs[-1])
            log_freq_resampled = np.logspace(log_freq_min, log_freq_max, self._plots)

            # コスペクトルとクアドラチャスペクトルの補間
            co_resampled = np.interp(
                log_freq_resampled, freqs, co_spectrum, left=np.nan, right=np.nan
            )
            quad_resampled = np.interp(
                log_freq_resampled, freqs, quad_spectrum, left=np.nan, right=np.nan
            )

            # NaNを除外
            valid_mask = ~np.isnan(co_resampled)
            freqs = log_freq_resampled[valid_mask]
            co_spectrum = co_resampled[valid_mask]
            quad_spectrum = quad_resampled[valid_mask]

        # 0Hz成分を除外
        nonzero_mask = freqs != 0
        freqs = freqs[nonzero_mask]
        co_spectrum = co_spectrum[nonzero_mask]
        quad_spectrum = quad_spectrum[nonzero_mask]

        return freqs, co_spectrum, quad_spectrum, corr_coef

    def calculate_power_spectrum(
        self,
        key: str,
        dimensionless: bool = True,
        frequency_weighted: bool = True,
        interpolate_points: bool = True,
        scaling: str = "spectrum",
    ) -> tuple:
        """
        DataFrameから指定されたkeyのパワースペクトルと周波数軸を計算する
        scipy.signal.welchを使用してパワースペクトルを計算

        Args:
            key (str): データの列名
            dimensionless (bool, optional): Trueの場合、分散で割って無次元化を行う。デフォルトはTrue。
            frequency_weighted (bool, optional): 周波数の重みづけを適用するかどうか。デフォルトはTrue。
            interpolate_points (bool, optional): 等間隔なデータ点を生成するかどうか（対数軸上で等間隔）
            scaling (str, optional): "density"でスペクトル密度、"spectrum"でスペクトル。デフォルトは"spectrum"。

        Returns:
            tuple: (freqs, power_spectrum)
                - freqs (np.ndarray): 周波数軸（対数スケールの場合は対数変換済み）
                - power_spectrum (np.ndarray): パワースペクトル（対数スケールの場合は対数変換済み）
        """
        # バリデーション
        valid_scaling_options = ["density", "spectrum"]
        if scaling not in valid_scaling_options:
            raise ValueError(
                f"'scaling'は次のパラメータから選択してください: {valid_scaling_options}"
            )

        # データの取得とトレンド除去
        data: np.ndarray = np.array(self._df[key].values)
        data = SpectrumCalculator._detrend(data, self._fs)

        # welchメソッドでパワースペクトル計算
        freqs, power_spectrum = signal.welch(
            data, fs=self._fs, window=self._window_type, nperseg=1024, scaling=scaling
        )

        # 周波数の重みづけ（0Hz除外の前に実施）
        if frequency_weighted:
            power_spectrum = freqs * power_spectrum

        # # 無次元化（0Hz除外の前に実施）
        if dimensionless:
            variance = np.var(data)
            power_spectrum /= variance

        if interpolate_points:
            # 補間処理（0Hz除外の前に実施）
            log_freq_min = np.log10(0.001)
            log_freq_max = np.log10(freqs[-1])
            log_freq_resampled = np.logspace(log_freq_min, log_freq_max, self._plots)

            power_spectrum_resampled = np.interp(
                log_freq_resampled, freqs, power_spectrum, left=np.nan, right=np.nan
            )

            # NaNを除外
            valid_mask = ~np.isnan(power_spectrum_resampled)
            freqs = log_freq_resampled[valid_mask]
            power_spectrum = power_spectrum_resampled[valid_mask]

        # 0Hz成分を最後に除外
        nonzero_mask = freqs != 0
        freqs = freqs[nonzero_mask]
        power_spectrum = power_spectrum[nonzero_mask]

        return freqs, power_spectrum

    @staticmethod
    def _correct_lag_time(
        data1: np.ndarray,
        data2: np.ndarray,
        fs: float,
        lag_second: float,
    ) -> tuple:
        """
        相互相関関数を用いて遅れ時間を補正する
        コスペクトル計算に使用

        Args:
            data1 (np.ndarray): 基準データ
            data2 (np.ndarray): 遅れているデータ
            fs (float): サンプリング周波数
            lag_second (float): data1からdata2が遅れている時間（秒）。負の値は許可されない。

        Returns:
            tuple: (data1, data2)
                - data1 (np.ndarray): 補正された基準データ
                - data2 (np.ndarray): 補正された遅れているデータ

        Raises:
            ValueError: lag_secondが負の値の場合
        """
        if lag_second < 0:
            raise ValueError("lag_second must be non-negative.")
        # lag_secondをサンプリング周波数でスケーリングしてインデックスに変換
        lag_index: int = int(lag_second * fs)
        # データ1とデータ2の共通部分を抽出
        data1 = data1[lag_index:]
        data2 = data2[:-lag_index]
        return data1, data2

    @staticmethod
    def _detrend(
        data: np.ndarray, fs: float, first: bool = True, second: bool = False
    ) -> np.ndarray:
        """
        データから一次トレンドおよび二次トレンドを除去します。

        Args:
            data (np.ndarray): 入力データ
            fs (float): サンプリング周波数
            first (bool, optional): 一次トレンドを除去するかどうか. デフォルトはTrue.
            second (bool, optional): 二次トレンドを除去するかどうか. デフォルトはFalse.

        Returns:
            np.ndarray: トレンド除去後のデータ

        Raises:
            ValueError: first と second の両方がFalseの場合
        """

        if not (first or second):
            raise ValueError("少なくとも一次または二次トレンドの除去を指定してください")

        detrended_data: np.ndarray = data.copy()

        # 一次トレンドの除去
        if first:
            detrended_data = signal.detrend(detrended_data)

        # 二次トレンドの除去
        if second:
            # 二次トレンドを除去するために、まず一次トレンドを除去
            detrended_data = signal.detrend(detrended_data, type="linear")
            # 二次トレンドを除去するために、二次多項式フィッティングを行う
            coeffs_second = np.polyfit(
                np.arange(len(detrended_data)), detrended_data, 2
            )
            trend_second = np.polyval(coeffs_second, np.arange(len(detrended_data)))
            detrended_data = detrended_data - trend_second

        return detrended_data

    @staticmethod
    def _generate_window_function(type: str, data_length: int) -> np.ndarray:
        """
        指定された種類の窓関数を適用する

        Args:
            type (str): 窓関数の種類 ('hanning', 'hamming', 'blackman')
            data_length (int): データ長

        Returns:
            np.ndarray: 適用された窓関数

        Notes:
            - 指定された種類の窓関数を適用し、numpy配列として返す
            - 無効な種類が指定された場合、警告を表示しHann窓を適用する
        """
        if type == "hanning":
            return np.hanning(data_length)
        elif type == "hamming":
            return np.hamming(data_length)
        elif type == "blackman":
            return np.blackman(data_length)
        else:
            print('Warning: Invalid argument "type". Return hanning window.')
            return np.hanning(data_length)

    @staticmethod
    def _smooth_spectrum(
        spectrum: np.ndarray, frequencies: np.ndarray, freq_threshold: float = 0.1
    ) -> np.ndarray:
        """
        高周波数領域のみ3点移動平均を適用する
        """
        smoothed = spectrum.copy()  # オリジナルデータのコピーを作成

        # 周波数閾値以上の部分のインデックスを取得
        high_freq_mask = frequencies >= freq_threshold

        # 高周波数領域のみを処理
        high_freq_indices = np.where(high_freq_mask)[0]
        if len(high_freq_indices) > 2:  # 最低3点必要
            for i in high_freq_indices[1:-1]:  # 端点を除く
                smoothed[i] = (
                    0.25 * spectrum[i - 1] + 0.5 * spectrum[i] + 0.25 * spectrum[i + 1]
                )

            # 高周波領域の端点の処理
            first_idx = high_freq_indices[0]
            last_idx = high_freq_indices[-1]
            smoothed[first_idx] = 0.5 * (spectrum[first_idx] + spectrum[first_idx + 1])
            smoothed[last_idx] = 0.5 * (spectrum[last_idx - 1] + spectrum[last_idx])

        return smoothed
