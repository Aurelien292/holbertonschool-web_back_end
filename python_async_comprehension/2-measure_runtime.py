#!/usr/bin/env python3
"""
    Cette coroutine mesure le temps nécessaire pour exécuter la coroutine
    async_comprehension quatre fois en parallèle en utilisant asyncio.gather()
    """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Cette coroutine mesure le temps nécessaire pour exécuter la coroutine
    async_comprehension quatre fois en parallèle en utilisant asyncio.gather().
    Elle retourne le temps total d'exécution.

    Return :
        float : Le temps total d'exécution en secondes.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()

    return end_time - start_time
