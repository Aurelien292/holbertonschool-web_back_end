#!/usr/bin/env python3

import asyncio
import random
"""
    Cette coroutine génère une séquence de 10 nombres aléatoires compris
    entre 0 et 10
    """


async def async_generator():
    """
    Cette coroutine génère une séquence de 10 nombres aléatoires
    compris entre 0 et 10, un nombre toutes les secondes. Chaque nombre
    est généré de manière asynchrone, ce qui permet de ne pas bloquer
    l'exécution du programme principal.

    Retourne :
        float : Un nombre flottant aléatoire compris entre 0 et 10
        à chaque itération.
    """
    for _ in range(10):
        # Attend 1 sec
        await asyncio.sleep(1)
        # Génère un nombre aléatoire entre 0 et 10
        yield random.uniform(0, 10)
