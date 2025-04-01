![alt text](<ES6Bases.jpg>)

![version](https://img.shields.io/badge/version-3.9.1-red)
![shell](https://img.shields.io/badge/Inspected-green)

# Bases ES6 en JavaScript

### *Avant-propos*

#### Interactions entre les technologies pour une creation de site web .

![alt text](<bandeau.png>)                           
__*Python avec Flask*__ : Gère le côté serveur, traitant la logique métier, les requêtes HTTP, l'authentification des utilisateurs et la gestion des sessions.

__*MySQL*__ : Stocke et organise les données essentielles du site (utilisateurs, articles, commandes), et interagit avec Flask pour récupérer et manipuler ces données.

__*HTML*__ : Structure la page web en définissant les éléments essentiels comme les titres, paragraphes, formulaires et images.

__*CSS*__ : Stylise l'apparence de la page en contrôlant la mise en page, les couleurs, les polices et les animations.

__*JavaScript*__ : Ajoute de l'interactivité côté client, permettant la gestion des événements et la validation dynamique des données.
                             
![alt text](<bandeau.png>)                              

### Introduction 

ES6 (ECMAScript 6), est une version majeure de JavaScript qui a introduit de nouvelles fonctionnalités et améliorations afin de rendre le langage plus puissant. JavaScript a évolué pour inclure des fonctionnalités comme les __classes__, les __fonctions fléchées__, la __gestion des promesses__, __les modules__, et bien d'autres.

#### Quelques fonctionnalités introduites dans ES6
1.__Let et const__

2.__Arrow functions__

3.__Template literals__

4.__Modules__

5.__Rest et spread__

6.__Destructuring__

7.__Promises__

8.__Generators__

9.__Maps et Sets__

![alt text](<bandeau.png>)    
### 1.Différences entre une constante (const) et une variable (let / var).

__*var*__ : Déclare une variable, accessible dans toute la fonction ou tout le script où elle est définie. Peut être redéclarée sans erreur.

__*let*__ : Déclare une variable, accessible seulement à l'intérieur des accolades où elle est définie (par exemple, dans une boucle ou une condition). Vous pouvez changer sa valeur, mais vous ne pouvez pas la redéclarer dans le même bloc.

__*const*__ : Déclare une constante, accessible seulement à l’intérieur des accolades où elle est définie. Sa valeur ne peut pas être changée après l'initialisation.

#### Exemple :
```
class Vehicle {
  constructor(type, speed) {
    // var : Peut être redéclaré, mais attention aux comportements inattendus
    var vehicleType = type;
    var vehicleType = "Electric " + type;  // OK, var permet la redéclaration
    console.log(vehicleType);  // Affiche "Electric Car"

    // let : Ne peut pas être redéclaré dans le même bloc
    let vehicleSpeed = speed;
    // let vehicleSpeed = 100;  // Erreur : ne peut pas redéclarer dans le même bloc
    vehicleSpeed = 100;  // OK, réassignation
    console.log(vehicleSpeed);  // Affiche 100

    // const : Ne peut pas être redéclaré ni réassigné
    const vehicleModel = "Model X";
    // const vehicleModel = "Model S";  // Erreur : ne peut pas redéclarer
    // vehicleModel = "Model Y";  // Erreur : ne peut pas réassigner
    console.log(vehicleModel);  // Affiche "Model X"
  }
}

const myVehicle = new Vehicle("Car", 80);
```
![alt text](<bandeau.png>)    

### 2.Arrow functions

Les fonctions fléchées permettent d'écrire des fonctions de manière plus compacte.

#### Exemple __sans__ arrow function :
```
const sum = function(a, b) {
  return a + b;
};

console.log(sum(3, 4)); // Affiche 7
```
#### Exemple __avec__ arrow function :
```
const sum = (a, b) => a + b;  // Fonction fléchée : somme des deux arguments
console.log(sum(3, 4)); // Affiche 7
```
### 3.Template literals
Permettent de créer des __chaînes de caractères__ avec une syntaxe plus lisible. Ils utilisent les backticks ( ` ) et permettent d'inclure des variables ou des expressions à l'intérieur des chaînes grâce à ${  }.

#### Exemple :
```
const name = "Alice";
const Hello = `Bonjour, ${name}!`;  // Inclut la variable 'name' dans la chaîne
console.log(Hello); // Affiche "Bonjour, Alice!"
```

### 4.Les modules

Les modules ES6 permettent de diviser le code JavaScript en plusieurs fichiers. Grâce aux mots-clés __export__ et __import__, tu peux exporter des variables, fonctions, ou objets depuis un fichier et les importer dans un autre fichier.

#### 4.1 __export__ classique
Exporter des éléments de manière nommée (c'est-à-dire en donnant un nom explicite à l'élément exporté). Ces éléments doivent ensuite être importés avec le même nom.

#### Exemple :

Fichier module.js :
```
export const pi = 3.14;  // exporte une constante pi
export function add(a, b) {
  return a + b; // exporte une fonction add
}
```

Ensuite, dans un autre fichier, tu peux importer ces éléments :

```
import { pi, add } from './module.js';  // importe les éléments de module.js

console.log(pi);   // Affiche 3.14
console.log(add(2, 3));  // Affiche 5
```
#### 4.1 __export default__

L'export default est utilisé lorsque tu veux exporter un seul élément (fonction, objet, classe, etc.) par défaut d'un module. Tu n'as pas besoin de spécifier le nom de l'élément lors de l'importation.

#### Exemple :

Fichier module.js :

```
export default function greet(name) {
  return `Hello, ${name}!`;
}  // exporte une fonction par défaut
```
Ensuite, dans un autre fichier, tu peux importer cette fonction sans utiliser de accolades :

```
import greet from './module.js';  // importe la fonction par défaut de module.js

console.log(greet('Alice'));  // Affiche "Hello, Alice!"
```

![alt text](<bandeau.png>)    
### 5.Rest et spread 

#### 5.1 Rest : Regrouper plusieurs éléments dans un tableau ou un objet
#### Exemple :
```
function sum(...numbers) {
  return numbers.reduce((acc, num) => acc + num, 0);
}

console.log(sum(1, 2, 3, 4)); // Affiche 10
```
L'opérateur __...numbers__ permet de regrouper tous les arguments passés à la fonction dans un tableau, puis la méthode __reduce__ additionne ces éléments pour retourner leur somme.

#### 5.2 Spread : Étendre un tableau ou un objet
#### Exemple :
```
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];
console.log(arr2);  // Affiche [1, 2, 3, 4, 5]
```
L'opérateur __...arr1__ étend les éléments du tableau __*arr1*__ dans __*arr2*__, puis ajoute les éléments 4 et 5 à la fin de arr2 pour obtenir le résultat final [1, 2, 3, 4, 5].


### 6.Le destructuring

Permet d'extraire facilement des valeurs d'un objet ou d'un tableau et de les assigner directement à des variables.

#### Exemple :

```
const user = { name: "Alice", age: 25 };
const { name, age } = user;  // Extrait 'name' et 'age' de l'objet 'user'
console.log(name);  // Affiche "Alice"
console.log(age);   // Affiche 25
```
Le destructuring __const { name, age } = user;__ extrait les propriétés name et age de l'objet user et les assigne directement aux variables name et age, qui sont ensuite affichées avec console.log.

![alt text](<bandeau.png>)    
### 7.Promises
Les promesses en JavaScript sont utilisées pour gérer des opérations asynchrones (comme les requêtes réseau) de manière plus claire et structurée. Elles représentent une valeur qui sera disponible à un moment donné, soit avec succès (résolue), soit en cas d'échec (rejetée).

#### Exemple :
```
const fetchData = new Promise((resolve, reject) => {

  let data = "Données récupérées";

  if (data) {

    resolve(data);  // Si tout se passe bien, la promesse est résolue avec 'data'

  } else {

    reject("Erreur lors de la récupération des données");  
    // Sinon, la promesse est rejetée avec un message d'erreur
  }
});

fetchData
  .then(data => console.log(data))  // Si la promesse est résolue, affiche les données
  .catch(error => console.log(error));  // Si la promesse est rejetée, affiche l'erreur
  ```
#### Résumé :

* __resolve__ : Signale que l'opération est terminée avec succès (ressemble à un return).

* __reject__ : Signale qu'une erreur s'est produite (cela peut être comparé à un return avec une erreur, comme un code HTTP 404).

* __.then()__ : Permet de spécifier ce qui se passe si la promesse est réussie, en utilisant le résultat de la promesse.

* __.catch()__ : Permet de spécifier ce qui se passe si la promesse échoue, en gérant l'erreur.

### 8.Generators

*Utilisation des Generators pour un Questionnaire*

#### Gestion d'un questionnaire séquentiel : 

Gérer un questionnaire en posant chaque question une par une, en mettant l'exécution en pause après chaque question. Cela permet de contrôler l'ordre des questions et de sauvegarder les réponses au fur et à mesure.

#### Reprise à partir de n'importe quelle étape :
Puisque l'exécution d'un generator peut être mise en pause et reprise à partir du dernier __yield__, vous pourriez reprendre un questionnaire à partir de la dernière question répondue si nécessaire.

#### Exemple :
```
function* questionnaire() {
  yield "Quel est votre nom ?";
  yield "Quel est votre âge ?";
  yield "Quel est votre pays d'origine ?";
}

const survey = questionnaire();

// Simulation d'un questionnaire
console.log(survey.next().value);  // Affiche "Quel est votre nom ?"
// L'utilisateur répond à la question ici

console.log(survey.next().value);  // Affiche "Quel est votre âge ?"
// L'utilisateur répond à la question ici

console.log(survey.next().value);  // Affiche "Quel est votre pays d'origine ?"
// L'utilisateur répond à la question ici

console.log(survey.next().value);  // Affiche "undefined", car il n'y a plus de questions
```

__Une fonction generator est déclarée avec un astérisque function*.__ 

![alt text](<bandeau.png>)    
### 9.Maps et Sets

__Map__ : Collection clé-valeur, avec des clés uniques et de n'importe quel type.

### Méthodes importantes pour Map :

__set(key, value)__ : Ajoute ou met à jour une paire clé-valeur.

__get(key)__ : Récupère la valeur associée à une clé.

__has(key)__ : Vérifie si une clé existe.

__delete(key)__ : Supprime une paire clé-valeur.

__size__ : Renvoie le nombre de paires dans la Map.

__Set__ : Collection d'éléments uniques, éliminant les doublons automatiquement.

### Méthodes importantes pour Set :

__add(value)__ : Ajoute un élément au Set.

__has(value)__ : Vérifie si un élément existe.

__delete(value)__ : Supprime un élément du Set.

__size__ : Renvoie le nombre d'éléments dans le Set.

#### Exemple :
```
// Map
const map = new Map();
map.set('name', 'Alice');
map.set('age', 25);
console.log(map.get('name')); // Affiche "Alice"

// Set
const set = new Set([1, 2, 3, 4, 4, 5]);
console.log(set); // Affiche Set { 1, 2, 3, 4, 5 }
```
![alt text](<bandeau.png>)    
![alt text](<bandeau.png>)    
