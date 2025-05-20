const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  const database = process.argv[2];

  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(database)
      .then((students) => {
        const response = `This is the list of our students\n${students.join('\n')}`;
        res.statusCode = 200;
        res.end(response);
      })
      .catch(() => {
        res.statusCode = 200;
        res.end('This is the list of our students\nCannot load the database');
      });
  }
});

app.listen(1245);
module.exports = app;
