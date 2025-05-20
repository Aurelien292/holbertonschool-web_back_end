// 1-stdin.test.js
const { exec } = require('child_process');

describe('Test 1-stdin.js', () => {
  it('should handle user input and output correctly', (done) => {
    // Exécuter le fichier 1-stdin.js dans un processus enfant
    const process = exec('node 1-stdin.js');

    let output = '';

    // Capturer la sortie du processus
    process.stdout.on('data', (data) => {
      output += data;
    });

    // Simuler l'entrée stdin après que le message de bienvenue soit affiché
    process.stdin.write('Bob\n');
    process.stdin.end(); // Terminer l'entrée

    // Vérifier les résultats
    process.on('close', (code) => {
      expect(output).toContain('Welcome to Holberton School, what is your name?');
      expect(output).toContain('Your name is: Bob');
      expect(output).toContain('This important software is now closing');
      done();
    });
  });
});
