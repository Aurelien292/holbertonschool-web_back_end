#!/usr/bin/env python3
"""
    Crée une tâche asyncio qui exécute `wait_random(max_delay)`
    de manière asynchrone.
    """

import asyncio
import random
from typing import List

# Charger dynamiquement le module contenant wait_random avec __import__
wait_random = __import__('0-basic_async_syntax').wait_random  # Chargement de la fonction wait_random depuis 0-basic_async_syntax


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


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine qui exécute `task_wait_random` n fois de manière asynchrone
    et retourne la liste des délais obtenus, triée dans l'ordre croissant
    grâce à la concurrence.

    Parameters:
    n (int): Le nombre de tâches à exécuter.
    max_delay (int): La valeur maximale du délai pour chaque tâche.

    Returns:
    List[float]: Liste triée des délais retournés par chaque appel de `task_wait_random`.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Crée n tâches

    # Attente de chaque tâche au fur et à mesure qu'elles se terminent
    for task in asyncio.as_completed(tasks):
        delay = await task  # Attend la fin de chaque tâche
        delays.append(delay)

    return delays  # Liste des délais obtenus, triée grâce à la concurrence


async def main():
    """
    Fonction principale pour tester la création de tâches et l'exécution.
    """
    n = 5  # Nombre de tâches à exécuter
    max_delay = 5  # Délai maximal pour chaque tâche
    result = await task_wait_n(n, max_delay)  # Appeler task_wait_n avec les paramètres
    print(result)  # Afficher les résultats (les délais obtenus)

# Exécuter la fonction principale pour tester
asyncio.run(main())
