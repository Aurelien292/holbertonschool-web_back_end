#!/usr/bin/env python3
import math


def floor(n: float) -> int:
    """
    Retourne le plancher (la partie entière inférieure) du nombre flottant n.

    Args:
        n (float): Le nombre flottant dont on souhaite obtenir le plancher.

    Returns:
        int: La partie entière inférieure de n.
    """
    return int(math.floor(n))
