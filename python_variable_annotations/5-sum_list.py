#!/usr/bin/env python3
from typing import List
"""
    Calcule la somme des éléments d'une liste de flottants.
    """


def sum_list(input_list: List[float]) -> float:
    """
    Calcule la somme des éléments d'une liste de flottants.

    Args:
        input_list (List[float]): Une liste de nombres flottants à additionner.

    Returns:
        float: La somme des éléments de la liste.
    """
    return sum(input_list)
