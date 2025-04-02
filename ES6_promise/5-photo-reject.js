export default function uploadPhoto(filename) {
  const Promesse = new Promise((resolve, reject) => {
    reject(Error(`${filename} cannot be processed`));
  });

  return Promesse;
}
