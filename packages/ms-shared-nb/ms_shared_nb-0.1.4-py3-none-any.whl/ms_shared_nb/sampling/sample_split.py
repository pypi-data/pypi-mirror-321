import pandas as pd

class Sampler:
    def __init__(self, dataframe, date_col, default_freq='D'):
        self.dataframe = dataframe
        self.date_col = date_col
        self.default_freq = default_freq
        self.time_series = None

    def convert_to_time_series(self):
        time_series = self.dataframe.copy()
        time_series[self.date_col] = pd.to_datetime(time_series[self.date_col])
        time_series.set_index(self.date_col, inplace=True)
        time_series.sort_index(ascending=True, inplace=True)
        time_series = time_series.asfreq(self.default_freq)
        return time_series

    def split_sample_into_two(self, last_sample_size):
        """
        Split the sample into two samples. The first sample will have `last_sample_size` data points,
        and the second sample will have the remaining data points.

        Args:
            last_sample_size (int): Number of data points in the first sample

        Returns:
            tuple: Two samples as pandas DataFrames
        """
        time_series = self.convert_to_time_series()
        first_sample = time_series.iloc[:-last_sample_size]
        last_sample = time_series.iloc[-last_sample_size:]
        return first_sample, last_sample

    def split_sample_into_n(self, n, n_data_points=None):
        """
        Split the sample into `n` samples. If `n_data_points` is not None, then split the sample into
        `n` samples of `n_data_points` each.

        Args:
            n (int): Number of samples
            n_data_points (int): Number of data points in each sample (default: None)

        Returns:
            tuple: `n` samples as pandas DataFrames
        """
        time_series = self.convert_to_time_series()

        if n_data_points is None:
            n_data_points = len(time_series) // n

        samples = [time_series.iloc[i * n_data_points: (i + 1) * n_data_points] for i in range(n)]
        return tuple(samples)

    def split_sample_into_n_equal_parts(self, n):
        """
        Split the sample into `n` equal parts.

        Args:
            n (int): Number of samples

        Returns:
            tuple: `n` samples as pandas DataFrames
        """
        time_series = self.convert_to_time_series()

        n_data_points = len(time_series) // n
        samples = [time_series.iloc[i * n_data_points: (i + 1) * n_data_points] for i in range(n)]
        return tuple(samples)

    def split_sample_into_n_periods(self, n, period):
        """
        Split the sample into `n` periods. Samples are calculated from the end of the sample.

        Args:
            n (int): Number of samples
            period (str): Period, e.g., '1w', '2w', '1m', '6m', '1y'

        Returns:
            tuple: `n` samples as pandas DataFrames
        """
        time_series = self.convert_to_time_series()

        freq_map = {'D': 'D', 'W': 'W', 'M': 'M', 'Y': 'Y'}
        freq = freq_map[period[-1]]
        period_value = int(period[:-1])

        samples = []
        for i in range(n - 1):
            end_date = time_series.index[-1 - i * period_value]
            start_date = time_series.index[-1 - (i + 1) * period_value]
            period_sample = time_series.loc[start_date:end_date]
            samples.append(period_sample[::-1])

        remaining_sample = time_series.iloc[:-n * period_value]
        samples.append(remaining_sample[::-1])

        return tuple(samples[::-1])

    def split_sample_into_periods(self, period):
        """
        Split the sample into periods.

        Args:
            period (str): Period, e.g., '1w', '2w', '1m', '6m', '1y'

        Returns:
            tuple: Samples as pandas DataFrames, each sample of size `period`
        """
        time_series = self.convert_to_time_series()

        freq_map = {'D': 'D', 'W': 'W', 'M': 'M', 'Y': 'Y'}
        freq = freq_map[period[-1]]
        period_value = int(period[:-1])

        samples = []
        for i in range(len(time_series) // period_value):
            end_date = time_series.index[-1 - i * period_value]
            start_date = time_series.index[-1 - (i + 1) * period_value]
            period_sample = time_series.loc[start_date:end_date]
            samples.append(period_sample[::-1])

        return tuple(samples[::-1])
