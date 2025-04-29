#!/usr/bin/env python3

"""
    Calcule les indices de début et de fin pour la pagination d'une liste.
    """


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calcule les indices de début et de fin pour la pagination d'une liste.

    Args:
        page (int): Le numéro de la page (1-indexé, c'est-à-dire que
        la première page est 1).
        page_size (int): Le nombre d'éléments à afficher par page.

    Returns:
        tuple[int, int]: Un tuple contenant l'indice de début (inclus)
        et l'indice de fin (exclu)
                         correspondant aux éléments à extraire pour cette page.
                         Peut être utilisé pour faire une découpe de liste
                         comme my_list[start:end].
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
