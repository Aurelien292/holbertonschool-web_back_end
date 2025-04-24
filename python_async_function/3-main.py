#!/usr/bin/env python3
"""
    Crée une tâche avec `task_wait_random` qui attend un délai aléatoire
    jusqu'à `max_delay`, puis affiche la classe de la tâche créée.
    """


import asyncio

# Importation de la fonction `task_wait_random` depuis le fichier '3-tasks.py'
task_wait_random = __import__('3-tasks').task_wait_random

async def test(max_delay: int) -> float:
    """
    Crée une tâche avec `task_wait_random` qui attend un délai aléatoire
    jusqu'à `max_delay`, puis affiche la classe de la tâche créée.

    Parameters:
    max_delay (int): Le délai maximal pour la tâche.

    Returns:
    float: Le délai final (non utilisé dans ce test, mais peut être ajouté si nécessaire).
    """
    # Crée la tâche à partir de task_wait_random
    task = task_wait_random(max_delay)

    # Attendre la fin de la tâche
    await task

    # Afficher la classe de la tâche pour vérifier son type
    print(f"Type de la tâche : {task.__class__}")

# Exécution du test avec un max_delay de 5 secondes
asyncio.run(test(5))
