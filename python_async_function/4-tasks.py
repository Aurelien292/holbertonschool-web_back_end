#!/usr/bin/env python3
"""
    Crée une tâche asyncio qui exécute `wait_random(max_delay)`
    de manière asynchrone.
    """
import asyncio
import importlib.util
import sys
import random
from typing import List

# Définir le nom du module et le chemin du fichier contenant wait_random
module_name = "wait_random"
file_path = "0-basic_async_syntax.py"

# Charger dynamiquement le module contenant wait_random
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sys.modules[module_name] = module  # Ajouter le module dans sys.modules

# Accéder à la fonction wait_random depuis le module chargé
wait_random = module.wait_random  # Fonction disponible via le module


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
    Coroutine qui exécute `task_wait_random` n fois de manière
    asynchrone et retourne
    la liste des délais obtenus, triée dans l'ordre croissant
    grâce à la concurrence.

    Parameters:
    n (int): Le nombre de tâches à exécuter.
    max_delay (int): La valeur maximale du délai pour chaque tâche.

    Returns:
    List[float]: Liste triée des délais retournés par chaque appel de
    `task_wait_random`.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Crée n tâches

    for task in asyncio.as_completed(tasks):
        delay = await task  # Attend la fin de chaque tâche
        delays.append(delay)

    return delays  # Liste des délais obtenus, sans tri supplémentaire


async def main():
    n = 5
    max_delay = 5
    result = await task_wait_n(n, max_delay)
    print(result)  # Affiche les résultats

# Exécuter la fonction main pour tester
asyncio.run(main())
