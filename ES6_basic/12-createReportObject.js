export default function createReportObject(employeesList) {
  return {
	  // Utilisation de l'opérateur de propagation pour assigner les départements directement
	  allEmployees: { ...employeesList },

	  // Méthode pour compter le nombre de départements
	  getNumberOfDepartments() {
      // On utilise Object.keys pour obtenir les clés de l'objet (les départements) et on renvoie la longueur de ce tableau
      return Object.keys(employeesList).length;
	  },
  };
}
