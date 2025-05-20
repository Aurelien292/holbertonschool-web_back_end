const http = require('http');

const app = http.createServer((req, res) => {
	console.log ('Request received:', req.method, req.url); // En plus
	res.statusCode = 200;
	res.setHeader('Content-Type', 'text/plain');
	res.end('Hello Holberton School!\n');
});
app.listen(1245, () => {
	console.log('Server running on port 1245');
});

module.exports = app;