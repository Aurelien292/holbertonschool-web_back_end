const http = require('http');

const app = http.createServer((req, res) => {
  console.log('Request received:', req.method, req.url); // En plus
  res.writeHead('200', { 'Content-Type': 'text/plain' });
  res.write('Hello Holberton School!\n');
  res.end();
});
app.listen(1245);

module.exports = app;
