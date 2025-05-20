process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.setEncoding('utf8');
process.stdin.on('readable', () => {
  const UserName = process.stdin.read();
  if (UserName) process.stdout.write(`Your name is: ${UserName}`);
});
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
