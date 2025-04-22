#!/usr/bin/env python3
"""
    Retourne un tuple contenant :
    - Le premier élément est la chaîne `k`.
    - Le deuxième élément est le carré de `v`, converti en float.
    """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Retourne un tuple contenant :
    - Le premier élément est la chaîne `k`.
    - Le deuxième élément est le carré de `v`, converti en float.

    Args:
        k (str): La chaîne de caractères.
        v (Union[int, float]): Le nombre dont le carré est calculé.

    Returns:
        tuple: Un tuple contenant la chaîne `k` et le carré de `v`
        sous forme de float.
    """
    return(k, float(v**2))
