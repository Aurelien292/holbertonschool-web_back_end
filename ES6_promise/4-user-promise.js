export default function signUpUser(firstName, lastName) {
  const promesse = new Promise((resolve) => {
    resolve({ firstName, lastName });
  });
  return promesse;
}
