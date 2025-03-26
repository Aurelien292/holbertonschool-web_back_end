export default function appendToEachArrayValue(array, appendString) {
	const Tableau = [];
	
	for (const value of array) {
	  Tableau.push(appendString + value); 
	}
  
	return Tableau;
  }