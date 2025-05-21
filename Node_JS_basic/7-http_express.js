const express = require('express');
const counStStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (request, resonse) => {
  resonse.set('Content-Type', 'text/plain');
  resonse.send('Hello Holberton School!');
});

app.get('/students', async (request, response) => {
  const path = process.argv[2];
  const header = 'This is the list of our students\n';

  try {
    const result = await counStStudents(path);
    response.set('Content-Type', 'text/plain');
    response.send(`${header}${result.join('\n')}\n`);
  } catch (error) {
    response.set('Content-Type', 'text/plain');
    response.send(`${header}Cannot load the database\n`);
  }
});
app.listen(port);
module.exports = app;
