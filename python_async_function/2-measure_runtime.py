#!/usr/bin/env python3
import time
import asyncio
import importlib.util
import sys

# Chargement dynamique du module
module_name = "wait_n"
file_path = "1-concurrent_coroutines.py"  # Le fichier contenant wait_n

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sys.modules[module_name] = module

# On récupère la fonction wait_n depuis le module importé dynamiquement
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps total pour exécuter `wait_n(n, max_delay)` et retourne le
    temps moyen par tâche.

    Parameters:
    n (int): Le nombre total de tâches asynchrones.
    max_delay (int): Le délai maximal pour chaque appel à `wait_random`.

    Returns:
    float: Le temps moyen (en secondes) pour exécuter une tâche.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
