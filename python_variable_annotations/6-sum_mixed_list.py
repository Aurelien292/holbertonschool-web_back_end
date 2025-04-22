#!/usr/bin/env python3
"""
    Calcule la somme des éléments d'une liste contenant des entiers
    et des flottants.
    """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calcule la somme des éléments d'une liste contenant des entiers
    et des flottants.

    Args:
        mxd_lst (List[Union[int, float]]): Liste d'entiers et
        de flottants à additionner.

    Returns:
        float: La somme des éléments de la liste, sous forme de flottant.
    """
    return float(sum(mxd_lst))
