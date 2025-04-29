#!/usr/bin/env python3
import csv
from typing import List


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


class Server:
    """Classe Server pour paginer un dataset des prénoms populaires de bébés.

    Cette classe permet de charger les données d'un fichier CSV, de paginer
    ces données, et de retourner les pages demandées en fonction des paramètres
    `page` et `page_size`.

    Attributs:
        DATA_FILE (str): Le chemin vers le fichier CSV contenant les données.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialise un objet Server.
        Par défaut, le dataset est non chargé et sera chargé à la demande.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Charge et met en cache les données du fichier CSV.

        Lit le fichier CSV contenant les prénoms de bébés populaires
        et retourne le dataset sous forme de liste de listes,
        en ignorant la première ligne (en-tête).

        Returns:
            List[List]: Liste des enregistrements (chaque ligne du CSV)
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retourne les lignes correspondant à la page demandée.

        Cette méthode utilise la fonction `index_range` pour
        déterminer les indices de début et de fin pour
        extraire les éléments du dataset correspondant à la
        page demandée, et retourne une sous-liste avec ces éléments.

        Args:
            page (int): Le numéro de la page demandée (par défaut 1).
            page_size (int): Le nombre d'éléments par page (par défaut 10).

        Returns:
            List[List]: Liste des lignes du dataset correspondant à
            la page demandée.Si la page est hors limites, retourne
            une liste vide.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []
        return dataset[start:end]
