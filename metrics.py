from typing import Union
import pandas as pd


def accuracy(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the accuracy
    """
from typing import Union
import pandas as pd

def accuracy(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the accuracy
    """

    # Check if input series are not empty
    assert not y_hat.empty, "Input series y_hat is empty"
    assert not y.empty, "Input series y is empty"

    # Check if input series have the same data type
    assert y_hat.dtype == y.dtype, "Input series y_hat and y have different data types"

    # Check if input series have the same index
    assert y_hat.index.equals(y.index), "Input series y_hat and y have different indices"

    # Check if input series values are not NaN
    assert not y_hat.isna().any(), "Input series y_hat contains NaN values"
    assert not y.isna().any(), "Input series y contains NaN values"

    # Check if sizes of y_hat and y are equal
    assert y_hat.size == y.size, "Input series y_hat and y have different sizes"

    # TODO: Add your accuracy calculation logic here
    pass

# Example usage:
# y_hat = pd.Series([1, 0, 1, 1, 0])
# y = pd.Series([1, 1, 0, 1, 0])
# accuracy_score = accuracy(y_hat, y)
# print("Accuracy:", accuracy_score)

    """
    The following assert checks if sizes of y_hat and y are equal.
    Students are required to add appropriate assert checks at places to
    ensure that the function does not fail in corner cases.
    """
    assert y_hat.size == y.size
    # TODO: Write here
    pass


def precision(y_hat: pd.Series, y: pd.Series, cls: Union[int, str]) -> float:
    """
    Function to calculate the precision
    """
    pass


def recall(y_hat: pd.Series, y: pd.Series, cls: Union[int, str]) -> float:
    """
    Function to calculate the recall
    """
    pass


def rmse(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the root-mean-squared-error(rmse)
    """

    pass


def mae(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the mean-absolute-error(mae)
    """
    pass
