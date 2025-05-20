const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });

    // Séparer le contenu en lignes
    const content = data.split('\n').filter((line) => line.trim() !== ''); // Enlève les lignes vides

    if (content.length < 2) {
      throw new Error('Cannot load the database');
    }

    // Créer un objet pour stocker les étudiants par domaine
    const fields = {};

    // Traiter les lignes suivantes qui contiennent les données des étudiants
    for (let i = 1; i < content.length; i += 1) {
      const student = content[i].split(',');

      // Si le domaine n'est pas défini, on l'initialise
      if (!fields[student[3]]) {
        fields[student[3]] = [];
      }

      // Ajouter le prénom de l'étudiant à la liste de ce domaine
      fields[student[3]].push(student[0]);
    }

    // Affichage du nombre total d'étudiants
    const totalStudents = content.length - 1; // On exclut la première ligne (en-tête)
    const response = [`Number of students: ${totalStudents}`];
    console.log(response[0]);

    // Affichage du nombre d'étudiants par domaine
    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        const studentList = fields[field];
        const message = `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`;
        console.log(message);
        response.push(message);
      }
    }

    return response;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
