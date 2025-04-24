#!/usr/bin/env python3
"""
    Mesure le temps moyen d'exécution de wait_n(n, max_delay).
    """


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n  # adapte le nom du fichier

def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps moyen d'exécution de wait_n(n, max_delay).

    Args:
        n (int): Nombre de fois que wait_random sera lancé.
        max_delay (int): Délai maximum pour chaque appel.

    Returns:
        float: Temps moyen d'exécution par appel (en secondes).
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    return total_time / n
