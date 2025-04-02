![alt text](<backend.jpg>)

# holbertonschool web back end

## Introduction 

Utiliser ES6 (ECMAScript 2015) pour le développement Back-End. ES6 est une version moderne de JavaScript. Grâce à des nouveautés comme les classes, les modules, les fonctions fléchées, ou encore les promesses. 
Comment utiliser ces fonctionnalités pour mieux organiser le code, manipuler des données, et interagir avec des bases de données, tout en profitant de la puissance de ES6.


### Redirection
[ES6 Basics](https://github.com/Aurelien292/holbertonschool-web_back_end/tree/main/ES6_basic), qui contient beaucoup d'informations nécessaires pour bien démarrer avec ES6.


## Linter et correction automatique du code 

### C'est quoi un linter ?

Un linter est un outil qui analyse le code source pour détecter des erreurs, des incohérences ou des problèmes de style, sans exécuter réellement le programme.

### Commande pour exécuter le linter et appliquer des corrections automatiques :

```
npm run lint -- --fix
```

#### Ce que fait cette commande :

    npm run lint -- : Exécute le linter défini dans le fichier package.json pour vérifier le code et produit une sortie dans le terminal.

    --fix : Applique automatiquement des corrections pour les erreurs détectées, comme des espaces manquants, des points-virgules ou des noms de variables mal formatés.

#### Exemple : 

Erreur dans un fichier 1-block-scoped.js : 

__Commande dans le terminal__ : 

```
npm run lint -- --fix 1-block-scoped.js
```
__Il manque un ; au return__ 
```
export default function taskBlock() {
  const task = false;
  const task2 = true;
  return [task, task2]
}
```
Sortie de la commande : 
```
1-block-scoped.js
  4:23  error  Missing semicolon  semi

✖ 1 problem (1 error, 0 warnings)
  1 error and 0 warnings potentially fixable with the `--fix` option.
```
