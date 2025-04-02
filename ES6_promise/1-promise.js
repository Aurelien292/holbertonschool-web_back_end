export default function getFullResponseFromAPI(success) {
  const attente = new Promise((resolve, reject) => (success
    ? resolve({ status: 200, body: 'Success' }) // Si
    : reject(new Error('The fake API is not working currently')))); // Alors
  return attente;
}
