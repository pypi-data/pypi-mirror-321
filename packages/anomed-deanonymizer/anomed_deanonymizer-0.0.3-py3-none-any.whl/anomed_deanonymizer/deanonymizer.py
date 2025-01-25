from abc import ABC, abstractmethod
from pathlib import Path

import numpy as np


class SupervisedLearningMIA(ABC):
    """A base class for membership inference attacks (MIA) on anonymizers
    (privacy preserving machine learning models) which rely on the supervised
    learning paradigm.

    Subclasses need to define a way to ...

    * fit/train the attack they represent using only member features, member
      targets, non-member features and  array and a target
      array (i.e. without explicitly given hyperparameters)
    * use the (fitted) attack for membership inference
    * save the (trained) attack to disk
    * validate attack input feature arrays
    """

    @abstractmethod
    def fit(
        self,
        X_member: np.ndarray,
        y_member: np.ndarray,
        X_nonmember: np.ndarray,
        y_nonmember: np.ndarray,
    ) -> None:
        """Fit the attack against a target (which is assumed to be known in
        advance).

        Parameters
        ----------
        X_member : np.ndarray
            A feature array which was part of the attack target's training set.
        y_member : np.ndarray
            A target array which was part of the attack target's training set.
        X_nonmember : np.ndarray
            A feature array which was not part of the attack target's training
            set.
        y_nonmember : np.ndarray
            A target array which was not part of the attack target's training
            set.
        """
        pass

    @abstractmethod
    def infer_memberships(
        self, X: np.ndarray, y: np.ndarray, batch_size: int | None = None
    ) -> np.ndarray:
        """Infer the memberships of target values of a feature array.

        Parameters
        ----------
        (X, y) : (np.ndarray, np.ndarray)
            The features and targets (samples) to infer the memberships of.
        batch_size : int | None, optional
            The batch size to use while inferring (to limit compute resource
            consumption). By default `None`, which results in processing the
            whole arrays at once.

        Returns
        -------
        np.ndarray
            The memberships (boolean array). If `memberships[i]` is `True`,
            `(X[i], y[i])` is a member, i.e. part of the training dataset. If
            `memberships[i]` is `False`, it is not a member, i.e. part of the
            validation dataset.

        """
        pass

    @abstractmethod
    def save(self, filepath: str | Path) -> None:
        """Save the instance to disk, maintaining the current training progress.

        Parameters
        ----------
        filepath : str | Path
            Where to save the instance.
        """
        pass

    @abstractmethod
    def validate_input(self, feature_array: np.ndarray) -> None:
        """Check whether the input array is a valid feature array argument for
        `fit` and for `predict` (parameter `X`).

        If so, do nothing. Otherwise, raise a `ValueError`.

        Parameters
        ----------
        feature_array : np.ndarray
            The feature array to validate.

        Raises
        ------
        ValueError
            If `feature_array` is incompatible with this anonymizer.
        """
        pass
