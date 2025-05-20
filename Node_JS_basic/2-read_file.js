const fs = require('fs');

function countStudents(database) {
  try {
    // Lire le fichier CSV de manière synchrone
    const data = fs.readFileSync(database, 'utf-8');

    // Séparer les lignes du fichier et filtrer les lignes vides
    const lines = data.split('\n').filter((line) => line.trim().length > 0);

    // Si le fichier contient trop peu de lignes (en-tête + données), on lève une erreur
    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    // Créer un objet pour stocker les étudiants par domaine
    const fields = {};

    // Lire l'en-tête du CSV pour déterminer les noms de colonnes
    const header = lines[0].split(',');

    // Traiter les lignes des étudiants
    for (let i = 1; i < lines.length; i += 1) {
      const student = lines[i].split(',');

      // Vérifier que la ligne a le bon nombre de colonnes
      if (student.length === header.length) {
        const firstname = student[0].trim();
        const field = student[3].trim();

        // Si le domaine n'est pas défini, on l'initialise
        if (!fields[field]) {
          fields[field] = [];
        }

        // Ajouter l'étudiant à la liste du domaine
        fields[field].push(firstname);
      }
    }

    // Calculer le nombre total d'étudiants
    const totalStudents = Object.values(fields).reduce((acc, curr) => acc + curr.length, 0);

    // Afficher le nombre total d'étudiants
    console.log(`Number of students: ${totalStudents}`);

    // Afficher le nombre d'étudiants par domaine et la liste des prénoms
    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        const count = fields[field].length;
        const list = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${count}. List: ${list}`);
      }
    }
  } catch (error) {
    // En cas d'erreur (fichier introuvable, erreur de format, etc.), afficher le message d'erreur
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
