#!/usr/bin/env python3
"""
    Coroutine asynchrone qui attend un délai aléatoire entre 0 et
    max_delay secondes (inclus),puis retourne ce délai.
    """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine asynchrone qui attend un délai aléatoire entre 0 et
    max_delay secondes (inclus),puis retourne ce délai.

    Parameters:
    max_delay (int): Le délai maximal (en secondes). Doit être un
    entier positif.La valeur par défaut est 10.

    Returns:
    float: La durée du délai aléatoire attendu, en secondes
    (nombre flottant).
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
