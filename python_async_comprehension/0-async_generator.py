#!/usr/bin/env python3
"""
    Cette coroutine génère une séquence de 10 nombres aléatoires compris
    entre 0 et 10
    """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Cette coroutine génère une séquence de 10 nombres aléatoires
    compris entre 0 et 10, un nombre toutes les secondes. Chaque nombre
    est généré de manière asynchrone, ce qui permet de ne pas bloquer
    l'exécution du programme principal.

    Yield:
        _type_ : Un nombre flottant aléatoire compris entre 0 et 10
        à chaque itération.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        # Génère un nombre aléatoire entre 0 et 10
        yield random.uniform(0, 10)
