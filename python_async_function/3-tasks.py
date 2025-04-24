#!/usr/bin/env python3
"""
    Crée une tâche asyncio qui exécute `wait_random(max_delay)`
    de manière asynchrone.
    """
import asyncio
import importlib.util
import sys

# Définir le nom du module et le chemin du fichier contenant wait_random
module_name = "wait_random"
file_path = "0-basic_async_syntax.py"

# Charger dynamiquement le module
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
