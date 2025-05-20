// 0-console.test.js
const displayMessage = require('../0-console');

describe('displayMessage', () => {
  // Simuler le comportement de console.log
  beforeAll(() => {
    console.log = jest.fn();
  });

  // Tester si le message est bien affiché
  it('should print the message to the console', () => {
    const message = 'Hello NodeJS!';

    displayMessage(message); // Appel de la fonction

    // Vérifier si console.log a été appelé avec le bon message
    expect(console.log).toHaveBeenCalledWith(message);
  });
});
