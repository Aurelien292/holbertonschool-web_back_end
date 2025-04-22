#!/usr/bin/env python3
from typing import List, Tuple, Iterable, Sequence
"""
    Prend une liste d'objets itérables et retourne une liste de
    tuples (élément, longueur).
    """


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Prend une liste d'objets itérables et retourne une liste de
    tuples (élément, longueur).

    Args:
        lst (List[Iterable]): Une liste d'objets ayant une longueur
        (comme des str, list, tuple).

    Returns:
        List[Tuple[Iterable, int]]: Une liste de tuples contenant l'objet
        original et sa longueur.
    """
    return [(i, len(i)) for i in lst]
