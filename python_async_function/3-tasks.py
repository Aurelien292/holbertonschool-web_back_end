#!/usr/bin/env python3
"""
    Crée une tâche asyncio qui exécute `wait_random(max_delay)`
    de manière asynchrone.
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée une tâche asyncio qui exécute `wait_random(max_delay)`
    de manière asynchrone.

    Parameters:
    max_delay (int): La valeur maximale du délai pour la tâche.

    Returns:
    asyncio.Task: La tâche associée à l'exécution de `wait_random(max_delay)`.
    """
    # Crée et retourne la tâche en utilisant la fonction wait_random
    return asyncio.create_task(wait_random(max_delay))
