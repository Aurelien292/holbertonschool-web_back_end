Coming soon


## Qu'est-ce qu'une Promise ?

Une Promise (promesse) est un objet qui représente l'éventuelle réussite ou l'échec d'une opération asynchrone. En d'autres termes, cela permet de gérer le résultat de tâches qui prennent du temps (comme des appels réseau ou des traitements longs) sans bloquer l'exécution du programme.

Lorsqu'une Promise est utilisée, elle peut avoir trois états :

    Pending : La promesse est en cours (en attente).

    Resolved : La promesse a été réalisée avec succès.

    Rejected : La promesse a échoué (par exemple, en cas d'erreur).

	Cela permet d'écrire un code non-bloquant, où les autres tâches peuvent continuer pendant qu'une opération longue (comme une requête HTTP) est en cours.


## Chainage ternaires : 

Exemple de chaînage d'opérateurs ternaires :

let age = 25;
let statut = age < 18 ? 'Mineur' : age < 30 ? 'Jeune adulte' : 'Adulte';
console.log(statut);  // Affichera "Jeune adulte"

Explication :

    age < 18 ? 'Mineur' : age < 30 ? 'Jeune adulte' : 'Adulte' :

        Première condition : Si age < 18, le résultat est 'Mineur'.

        Deuxième condition (si la première est fausse) : Si age < 30, le résultat est 'Jeune adulte'.

        Troisième condition (si les deux premières sont fausses) : Si l'âge est supérieur ou égal à 30, le résultat est 'Adulte'.


## Promise.race