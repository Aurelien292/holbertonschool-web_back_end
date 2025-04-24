#!/usr/bin/env python3
"""
    Lancement de n coroutines wait_random avec le délai max donné.
    Retourne les délais dans l'ordre d'achèvement
    """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random  # Remplace par ton nom de fichier

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lancement de n coroutines wait_random avec le délai max donné.
    Retourne les délais dans l'ordre d'achèvement (pas dans l’ordre de lancement).

    Args:
        n (int): Nombre de fois qu'on appelle wait_random.
        max_delay (int): Délai maximum (en secondes).

    Returns:
        List[float]: Liste des délais dans l’ordre croissant de fin.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    
    return delays
