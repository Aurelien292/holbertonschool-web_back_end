export default class Currency {
	constructor(code, name) {
	  // Initialisation des variables privées
	  this._code = code;
	  this._name = name;
	}
  
	// Getter pour l'attribut _code
	get code() {
	  return this._code;
	}
  
	// Setter pour l'attribut _code
	set code(value) {
	  this._code = value;
	}
  
	// Getter pour l'attribut _name
	get name() {
	  return this._name;
	}
  
	// Setter pour l'attribut _name
	set name(value) {
	  this._name = value;
	}
  
	// Méthode pour afficher la devise sous le format name (code)
	displayFullCurrency() {
	  return `${this._name} (${this._code})`;
	}
  }