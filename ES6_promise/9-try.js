export default function guardrail(mathFunction) {
  const queue = [];

  try {
    // execute fonction mathFunction et ajoute dans le tableau
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(error.toString()); // si erreur on ajoute au resultat
  }
  queue.push('Guardrail was processed'); // ajout du message final
  return queue;
}
