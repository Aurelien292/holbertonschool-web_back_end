#!/usr/bin/env python3
"""
    Crée une fonction qui multiplie un float par un multiplicateur donné.
    """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Crée une fonction qui multiplie un float par un multiplicateur donné.

    Args:
        multiplier (float): Le multiplicateur à utiliser.

    Returns:
        Callable[[float], float]: Une fonction prenant un float en entrée
        et retournant le résultat de la multiplication.
    """
    def multiplier_func(value: float) -> float:

        return multiplier * value
    return multiplier_func
