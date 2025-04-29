#!/usr/bin/env python3
"""
    Cette coroutine récupère les 10 nombres générés par
    async_generator() à l'aide d'une compréhension asynchrone et les
    retourne sous forme de liste.
    """
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator
"""
    Cette coroutine récupère les 10 nombres générés par
    async_generator() à l'aide d'une compréhension asynchrone et les
    retourne sous forme de liste.
    """


async def async_comprehension() -> List[float]:
    """
    Cette coroutine récupère les 10 nombres générés par async_generator()
    à l'aide d'une compréhension asynchrone et les retourne
    sous forme de liste.

    Retourne :
        list : Une liste contenant 10 nombres aléatoires générés
        par async_generator().
    """
    return [number async for number in async_generator()]
