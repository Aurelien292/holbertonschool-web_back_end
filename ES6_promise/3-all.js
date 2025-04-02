import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoResult, userResult]) => { // Déstructuration des résultats des promesses
      const { body } = photoResult; // On garde le nom original 'body'

      // Déstructuration de 'firstName' et 'lastName' de userResult
      const { firstName, lastName } = userResult;

      // Log des informations dans la console
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch((error) => {
      // Gestion des erreurs
      console.log('Signup system offline', error);
    });
}
