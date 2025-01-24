import numpy as np
import warnings
from typing import Union, List, Tuple
from scipy import sparse

class DataValidator:
    def __init__(self):
        pass

    def check_device_cpu(self, device):
        if device not in {"cpu", None}:
            raise ValueError(f"Unsupported device: {device!r}. Only 'cpu' is supported.")

    def is_1d_array(self, array: Union[np.ndarray, list], warn: bool = False) -> np.ndarray:
        """
        Ensures input is a 1D array. Raises an error if it's not 1D or convertible to 1D.
        """
        array = np.asarray(array)
        shape = array.shape

        if len(shape) == 1:
            return array
        elif len(shape) == 2 and shape[1] == 1:
            if warn:
                warnings.warn("Input is 2D but will be converted to 1D.", UserWarning)
            return array.ravel()
        else:
            raise ValueError(f"Input must be 1D. Found shape {shape}.")

    def check_samples(self, array: Union[np.ndarray, list]) -> int:
        """
        Returns the number of samples in the array.
        """
        array = np.asarray(array)
        if hasattr(array, 'shape') and len(array.shape) > 0:
            return array.shape[0]
        else:
            raise TypeError("Input must be an array-like object with at least one dimension.")

    def check_consistent_length(self, *arrays: Union[np.ndarray, list]):
        """
        Ensures all input arrays have the same length.
        """
        lengths = [self.check_samples(arr) for arr in arrays]
        if len(set(lengths)) > 1:
            raise ValueError(f"Inconsistent lengths: {lengths}")

    def validate_regression_targets(self, y_true, y_pred, dtype=np.float64):
        """
        Ensures regression target values are consistent and converted to the specified dtype.
        """
        y_true = np.asarray(y_true, dtype=dtype)
        y_pred = np.asarray(y_pred, dtype=dtype)

        if y_true.shape != y_pred.shape:
            raise ValueError(f"Shapes of y_true {y_true.shape} and y_pred {y_pred.shape} do not match.")

        return y_true, y_pred

    def check_array(self, array, ensure_2d: bool = True, dtype=np.float64, allow_nan: bool = False):
        """
        Validates input array and converts it to specified dtype.
        """
        array = np.asarray(array, dtype=dtype)

        if ensure_2d and array.ndim == 1:
            array = array.reshape(-1, 1)

        if not allow_nan and np.isnan(array).any():
            raise ValueError("Input contains NaN values, which are not allowed.")

        return array

    def check_sparse(self, array, accept_sparse: Tuple[str] = ('csr', 'csc')):
        """
        Validates sparse matrices and converts to an acceptable format.
        """
        if sparse.issparse(array):
            if array.format not in accept_sparse:
                return array.asformat(accept_sparse[0])
            return array
        else:
            raise ValueError("Input is not a sparse matrix.")

    def validate_r2_score_inputs(self, y_true, y_pred, sample_weight=None):
        """
        Ensures inputs for R2 score computation are valid.
        """
        y_true, y_pred = self.validate_regression_targets(y_true, y_pred)
        if sample_weight is not None:
            sample_weight = self.is_1d_array(sample_weight)
        return y_true, y_pred, sample_weight

    def validate_mae_mse_inputs(self, y_true, y_pred, library=None):
        """
        Ensures inputs for MAE and MSE computation are valid.
        """
        y_true, y_pred = self.validate_regression_targets(y_true, y_pred)
        if library not in {None, 'sklearn', 'torch', 'tensorflow', 'Moral88'}:
            raise ValueError(f"Invalid library: {library}. Choose from {{'Moral88', 'sklearn', 'torch', 'tensorflow'}}.")
        return y_true, y_pred


class metrics:
    def __init__(self):
        pass
    def mean_bias_deviation(self, y_true, y_pred, library=None, flatten=True):
        """
        Computes Mean Bias Deviation (MBD).
        """
        y_true, y_pred = self.validator.validate_mae_mse_inputs(y_true, y_pred, library)

        if flatten and y_true.ndim > 1:
            y_true = y_true.flatten()
            y_pred = y_pred.flatten()

        if library == 'sklearn':
            # Sklearn does not have a direct implementation for MBD
            raise NotImplementedError("Mean Bias Deviation is not implemented in sklearn.")

        if library == 'torch':
            import torch
            y_true_tensor = torch.tensor(y_true, dtype=torch.float32)
            y_pred_tensor = torch.tensor(y_pred, dtype=torch.float32)
            bias = torch.mean(y_pred_tensor - y_true_tensor).item()
            return bias

        if library == 'tensorflow':
            import tensorflow as tf
            y_true_tensor = tf.convert_to_tensor(y_true, dtype=tf.float32)
            y_pred_tensor = tf.convert_to_tensor(y_pred, dtype=tf.float32)
            bias = tf.reduce_mean(y_pred_tensor - y_true_tensor).numpy()
            return bias

        # Default implementation
        return np.mean(y_pred - y_true)
    def __init__(self):
        self.validator = DataValidator()

    def r2_score(self, y_true, y_pred, sample_weight=None, library=None, flatten=True):
        """
        Computes R2 score.
        """
        y_true, y_pred, sample_weight = self.validator.validate_r2_score_inputs(y_true, y_pred, sample_weight)

        if flatten and y_true.ndim > 1:
            y_true = y_true.flatten()
            y_pred = y_pred.flatten()

        if library == 'sklearn':
            from sklearn.metrics import r2_score as sklearn_r2
            return sklearn_r2(y_true, y_pred, sample_weight=sample_weight)

        if library == 'statsmodels':
            import statsmodels.api as sm
            model = sm.OLS(y_true, sm.add_constant(y_pred)).fit()
            return model.rsquared

        numerator = np.sum((y_true - y_pred) ** 2)
        denominator = np.sum((y_true - np.mean(y_true)) ** 2)

        if denominator == 0:
            return 0.0
        return 1 - (numerator / denominator)

    def mean_absolute_error(self, y_true, y_pred, normalize=True, threshold=None, method='mean', library='Moral88', flatten=True):
        """
        Computes Mean Absolute Error (MAE).
        """
        y_true, y_pred = self.validator.validate_mae_mse_inputs(y_true, y_pred, library)

        if flatten:
            y_true = y_true.ravel()
            y_pred = y_pred.ravel()

        if library == 'Moral88':
            if threshold is not None:
                y_pred = np.clip(y_pred, threshold[0], threshold[1])

            if y_true.ndim > 1 and flatten:
                y_true = y_true.flatten()
                y_pred = y_pred.flatten()
            absolute_errors = np.abs(y_true - y_pred)

            if method == 'mean':
                result = np.mean(absolute_errors)
            elif method == 'sum':
                result = np.sum(absolute_errors)
            elif method == 'none':
                result = absolute_errors
            else:
                raise ValueError("Invalid method. Choose from {'mean', 'sum', 'none'}.")

            # if normalize and method != 'none':
            #     range_y = np.ptp(y_true)
            #     result = result / max(abs(range_y), 1)

            return result

        elif library == 'sklearn':
            from sklearn.metrics import mean_absolute_error as sklearn_mae
            return sklearn_mae(y_true, y_pred)

        elif library == 'torch':
            import torch
            y_true_tensor = torch.tensor(y_true, dtype=torch.float32)
            y_pred_tensor = torch.tensor(y_pred, dtype=torch.float32)
            return torch.mean(torch.abs(y_true_tensor - y_pred_tensor)).item()

        elif library == 'tensorflow':
            import tensorflow as tf
            y_true_tensor = tf.convert_to_tensor(y_true, dtype=tf.float32)
            y_pred_tensor = tf.convert_to_tensor(y_pred, dtype=tf.float32)
            return tf.reduce_mean(tf.abs(y_true_tensor - y_pred_tensor)).numpy()

    def mean_squared_error(self, y_true, y_pred, normalize=True, threshold=None, method='mean', library='Moral88', flatten=True):
        """
        Computes Mean Squared Error (MSE).
        """
        y_true, y_pred = self.validator.validate_mae_mse_inputs(y_true, y_pred, library)

        if flatten:
            y_true = y_true.ravel()
            y_pred = y_pred.ravel()

        if library == 'Moral88':
            if threshold is not None:
                y_pred = np.clip(y_pred, threshold[0], threshold[1])

            if y_true.ndim > 1 and flatten:
                y_true = y_true.flatten()
                y_pred = y_pred.flatten()
            squared_errors = (y_true - y_pred) ** 2

            if method == 'mean':
                result = np.mean(squared_errors)
            elif method == 'sum':
                result = np.sum(squared_errors)
            elif method == 'none':
                result = squared_errors
            else:
                raise ValueError("Invalid method. Choose from {'mean', 'sum', 'none'}.")

            # if normalize and method != 'none':
            #     range_y = np.ptp(y_true)
            #     result = result / max(abs(range_y), 1)

            return result

        elif library == 'sklearn':
            from sklearn.metrics import mean_squared_error as sklearn_mse
            return sklearn_mse(y_true, y_pred)

        elif library == 'torch':
            import torch
            y_true_tensor = torch.tensor(y_true, dtype=torch.float32)
            y_pred_tensor = torch.tensor(y_pred, dtype=torch.float32)
            return torch.mean((y_true_tensor - y_pred_tensor) ** 2).item()

        elif library == 'tensorflow':
            import tensorflow as tf
            y_true_tensor = tf.convert_to_tensor(y_true, dtype=tf.float32)
            y_pred_tensor = tf.convert_to_tensor(y_pred, dtype=tf.float32)
            return tf.reduce_mean(tf.square(y_true_tensor - y_pred_tensor)).numpy()

    def root_mean_squared_error(self, y_true, y_pred, library=None):
        """
        Computes Root Mean Squared Error (RMSE).
        """
        y_true, y_pred = self.validator.validate_mae_mse_inputs(y_true, y_pred, library)

        if library == 'sklearn':
            from sklearn.metrics import mean_squared_error as sklearn_mse
            return np.sqrt(sklearn_mse(y_true, y_pred))

        if library == 'torch':
            import torch
            y_true_tensor = torch.tensor(y_true, dtype=torch.float32)
            y_pred_tensor = torch.tensor(y_pred, dtype=torch.float32)
            return torch.sqrt(torch.mean((y_true_tensor - y_pred_tensor) ** 2)).item()

        if library == 'tensorflow':
            import tensorflow as tf
            y_true_tensor = tf.convert_to_tensor(y_true, dtype=tf.float32)
            y_pred_tensor = tf.convert_to_tensor(y_pred, dtype=tf.float32)
            return tf.sqrt(tf.reduce_mean(tf.square(y_true_tensor - y_pred_tensor))).numpy()

        mse = self.mean_squared_error(y_true, y_pred)
        return np.sqrt(mse)

    def mean_absolute_percentage_error(self, y_true, y_pred, library=None):
        """
        Computes Mean Absolute Percentage Error (MAPE).
        """
        y_true, y_pred = self.validator.validate_regression_targets(y_true, y_pred)
        y_true, y_pred = self.validator.validate_mae_mse_inputs(y_true, y_pred, library)
        y_true = np.clip(y_true, 1e-8, None) 

        if library == 'sklearn':
            from sklearn.metrics import mean_absolute_percentage_error as sklearn_mape
            return sklearn_mape(y_true, y_pred) * 100

        if library == 'torch':
            import torch
            y_true_tensor = torch.tensor(y_true, dtype=torch.float32)
            y_pred_tensor = torch.tensor(y_pred, dtype=torch.float32)
            return torch.mean(torch.abs((y_true_tensor - y_pred_tensor) / torch.clamp(y_true_tensor, min=1e-8))).item() * 100

        if library == 'tensorflow':
            import tensorflow as tf
            y_true_tensor = tf.convert_to_tensor(y_true, dtype=tf.float32)
            y_pred_tensor = tf.convert_to_tensor(y_pred, dtype=tf.float32)
            return tf.reduce_mean(tf.abs((y_true_tensor - y_pred_tensor) / tf.clip_by_value(y_true_tensor, 1e-8, tf.float32.max))).numpy() * 100

        return np.mean(np.abs((y_true - y_pred) / np.clip(np.abs(y_true), 1e-8, None))) * 100

    def explained_variance_score(self, y_true, y_pred, library=None, flatten=True):
        """
        Computes Explained Variance Score.
        """
        y_true, y_pred = self.validator.validate_mae_mse_inputs(y_true, y_pred, library)

        if library == 'sklearn':
            from sklearn.metrics import explained_variance_score as sklearn_evs
            return sklearn_evs(y_true, y_pred)

        if library == 'torch':
            import torch
            y_true_tensor = torch.tensor(y_true, dtype=torch.float32)
            y_pred_tensor = torch.tensor(y_pred, dtype=torch.float32)
            variance_residual = torch.var(y_true_tensor - y_pred_tensor)
            variance_y = torch.var(y_true_tensor)
            return 1 - variance_residual / variance_y if variance_y != 0 else 0

        if library == 'tensorflow':
            import tensorflow as tf
            y_true_tensor = tf.convert_to_tensor(y_true, dtype=tf.float32)
            y_pred_tensor = tf.convert_to_tensor(y_pred, dtype=tf.float32)
            variance_residual = tf.math.reduce_variance(y_true_tensor - y_pred_tensor)
            variance_y = tf.math.reduce_variance(y_true_tensor)
            return 1 - variance_residual / variance_y if variance_y != 0 else 0

        numerator = np.var(y_true - y_pred)
        denominator = np.var(y_true)
        return 1 - numerator / denominator if denominator != 0 else 0

    def adjusted_r2_score(self, y_true, y_pred, n_features, library=None, flatten=True):
        """
        Computes Adjusted R-Squared Score.
        
        Parameters:
        y_true: array-like of shape (n_samples,)
            Ground truth (correct) target values.
        
        y_pred: array-like of shape (n_samples,)
            Estimated target values.
        
        n_features: int
            Number of independent features in the model.
        
        library: str, optional (default=None)
            Library to use for computation. Supports {'sklearn', 'statsmodels', None}.
        
        flatten: bool, optional (default=True)
            If True, flattens multidimensional arrays before computation.
        """
        # Validate inputs
        y_true, y_pred, _ = self.validator.validate_r2_score_inputs(y_true, y_pred)

        # Ensure inputs are 1D arrays
        if y_true.ndim == 0 or y_pred.ndim == 0:
            y_true = np.array([y_true])
            y_pred = np.array([y_pred])

        if flatten and y_true.ndim > 1:
            y_true = y_true.flatten()
            y_pred = y_pred.flatten()

        if library == 'sklearn':
            from sklearn.metrics import r2_score
            r2 = r2_score(y_true, y_pred)
        elif library == 'statsmodels':
            import statsmodels.api as sm
            X = sm.add_constant(y_pred)
            model = sm.OLS(y_true, X).fit()
            r2 = model.rsquared
        else:
            numerator = np.sum((y_true - y_pred) ** 2)
            denominator = np.sum((y_true - np.mean(y_true)) ** 2)
            r2 = 1 - (numerator / denominator) if denominator != 0 else 0.0

        n_samples = len(y_true)
        if n_samples <= n_features + 1:
            raise ValueError("Number of samples must be greater than number of features plus one for adjusted R-squared computation.")

        adjusted_r2 = 1 - (1 - r2) * (n_samples - 1) / (n_samples - n_features - 1)
        return adjusted_r2

if __name__ == '__main__':
    # Example usage
    validator = DataValidator()
    metrics = Metrics()

    # Test validation
    arr = [[1], [2], [3]]
    print("1D array:", validator.is_1d_array(arr))
    print("Samples:", validator.check_samples(arr))

    # Test MAE, MSE, R2, MBD, EV, MAPE, RMSE
    y_true = [3, -0.5, 2, 7]
    y_pred = [2.5, 0.0, 2, 8]

    print("Mean Absolute Error:", metrics.mean_absolute_error(y_true, y_pred))
    print("Mean Squared Error:", metrics.mean_squared_error(y_true, y_pred))
    print("R2 Score:", metrics.r2_score(y_true, y_pred))
    print("Mean Bias Deviation: ", metrics.mean_bias_deviation(y_true, y_pred))
    print("Explained Variance Score: ", metrics.explained_variance_score(y_true, y_pred))
    print("Mean Absolute Percentage Error: ", metrics.mean_absolute_percentage_error(y_true, y_pred))
    print("Root Mean Squared Error: ", metrics.root_mean_squared_error(y_true, y_pred))
    print("adjusted_r2_score: ", metrics.adjusted_r2_score(y_true, y_pred, 2))

