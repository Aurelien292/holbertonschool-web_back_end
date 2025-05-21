const express = require('express');
const counStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (request, response) => {
  response.set('Content-Type', 'text/plain');
  response.send('Hello Holberton School!');
});

app.get('/students', async (request, response) => {
  const path = process.argv[2];
  const header = 'This is the list of our students\n';

  try {
    const result = await counStudents(path);
    response.set('Content-Type', 'text/plain');
    response.send(`${header}${result.join('\n')}`);
  } catch (error) {
    response.set('Content-Type', 'text/plain');
    response.send(`${header}Cannot load the database`);
  }
});
app.listen(port);
module.exports = app;
