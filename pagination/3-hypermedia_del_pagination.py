#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
from typing import Dict, List
import csv


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Renvoie une page du dataset avec pagination résiliente à
        la suppression.

        Args:
            index (int): Index de départ dans le dataset.
            page_size (int): Nombre d'éléments à retourner.

        Returns:
            dict: Dictionnaire contenant :
                  - index : l’index de départ,
                  - next_index : le prochain index à utiliser,
                  - page_size : la taille de la page retournée,
                  - data : les données de la page.
        """
        assert isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        assert index < len(self.dataset())

        data = []
        current_index = index
        count = 0

        while count < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                count += 1
            current_index += 1
            next_index = (
                current_index
                if current_index < len(self.dataset())
                else None)

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
