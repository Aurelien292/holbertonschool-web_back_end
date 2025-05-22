import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    const databasePath = process.argv[2]; // Récupérer le chemin de la base de données depuis les arguments de la ligne de commande
    try {
      const studentsData = await readDatabase(databasePath);

      // Tri des domaines (field) par ordre alphabétique, insensible à la casse
      const sortedFields = Object.keys(studentsData).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      // Construire la réponse
      let response = 'This is the list of our students\n';

      sortedFields.forEach((field) => {
        const studentList = studentsData[field];
        response += `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}\n`;
      });

      return res.status(200).send(response);
    } catch (error) {
      // Si une erreur survient (par exemple, impossible de lire le fichier)
      return res.status(500).send('Cannot load the database');
    }
  }

  // Méthode pour récupérer les étudiants d'un domaine spécifique (CS ou SWE)
  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params; // Récupérer le paramètre major de l'URL

    // Vérifier si le domaine est valide (CS ou SWE)
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }
    const databasePath = process.argv[2];

    try {
      const studentsData = await readDatabase(databasePath);

      // Vérifier si le domaine (major) existe dans la base de données
      if (!studentsData[major]) {
        return res.status(500).send('Cannot load the database');
      }

      // Récupérer la liste des étudiants pour ce domaine
      const studentList = studentsData[major];

      // Retourner la réponse avec la liste des prénoms des étudiants du domaine demandé
      return res.status(200).send(`List: ${studentList.join(', ')}`);
    } catch (error) {
      return res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
