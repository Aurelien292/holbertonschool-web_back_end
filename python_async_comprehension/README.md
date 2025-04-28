![alt text](<asynchron.png>)
# Asynchrones Tâches - Python Project

__Introduction :__

Ce projet consiste à utiliser asyncio en Python pour exécuter des tâches asynchrones. __1)__ Il génère des nombres aléatoires de manière concurrente, __2)__ les collecte de façon asynchrone en liste , __3)__ mesure le temps d'exécution des opérations parallèles. L'objectif est de comprendre l'efficacité des tâches concurrentes en Python.


## Structure du projet

__1. *0-async_generator.py*__ : Génère 10 nombres aléatoires de manière asynchrone.

__2. *1-async_comprehension.py*__ : Utilise une compréhension de liste asynchrone pour collecter ces nombres.

__3. *2-measure_runtime.py*__ : Mesure le temps d'exécution de 4 appels simultanés à la fonction async_comprehension.

__4. *Lexique :*__

__5. *Conclusion*__

## Explications des projets


### 1. 0-async_generator.py 

__Variantes possible :__

random.uniform(0, 10)

    Retourne un nombre à virgule flottante (float), aléatoire, dans l'intervalle [0, 10] (inclusif sur les deux bornes).

random.randint(0, 10)

    Retourne un nombre entier (int), aléatoire, dans l'intervalle [0, 10] (inclusif sur les deux bornes).

### 2. 1-async_comprehension.py
Retourne 0-async_generator.py sous forme de liste 



### 3. 2-measure_runtime.py
__Variantes possible :__

Cela décompose la liste `tasks` en 4 arguments distincts
```
tasks = [async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension()]
await asyncio.gather(*tasks) 
```
OU 

Le * permet de "décomposer" un générateur ou une liste en ses éléments individuels et de les transmettre comme arguments séparés à la fonction
```
await asyncio.gather(*(async_comprehension() for _ in range(4)))
```

OU
```
await asyncio.gather(
    async_comprehension(),
    async_comprehension(),
    async_comprehension(),
    async_comprehension()
)
```
### Lexique :


__"L'asynchrone"__ fait référence à un mode d'exécution où certaines tâches peuvent être lancées et laissées se terminer sans bloquer le programme principal. __asyncio__ = tâches parallèles qui ne bloquent pas l'exécution.

__"Une coroutine"__ : est une fonction spéciale en Python qui permet d'exécuter des tâches de manière asynchrone.Elle peut être suspendue et reprise à tout moment. On utilise __async__ pour la définir et __await__ pour attendre une autre tâche sans bloquer l'exécution. __Coroutine__ = fonction qui gère des tâches asynchrones.

__" de manière non-bloquante "__ :  Lorsqu'une coroutine attend quelque chose, comme un délai de 1 seconde , elle ne bloque pas l'exécution d'autres tâches .

__"await"__ permet d'attendre la fin d'une coroutine sans bloquer l'exécution du programme.
Exemple complet await :
```
import asyncio

# Définition de coroutines qui simulent des tâches longues
async def task_1():
    print("Tâche 1 commence.")
    await asyncio.sleep(2)  # Simule un délai de 2 secondes
    print("Tâche 1 terminée.")

async def task_2():
    print("Tâche 2 commence.")
    await asyncio.sleep(1)  # Simule un délai de 1 seconde
    print("Tâche 2 terminée.")

# Coroutine principale pour exécuter les tâches
async def main():
    # Lancer les deux tâches en parallèle
    await asyncio.gather(task_1(), task_2())  # Attendre les deux tâches simultanément

# Exécution du programme
asyncio.run(main())
```

## Conclusion : 

L'asynchrone permet ainsi de maximiser l'efficacité en permettant à plusieurs tâches de s'exécuter en même temps sans que l'une n'attende que l'autre soit terminée. Cela est particulièrement utile pour des applications qui nécessitent d'attendre des opérations d'entrée-sortie (comme des requêtes réseau ou des opérations sur des fichiers), car ces opérations ne bloquent pas le programme.
