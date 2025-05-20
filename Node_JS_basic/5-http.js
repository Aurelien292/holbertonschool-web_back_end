const http = require('http');
const fs = require('fs');
const countStudents = require('./3-read_file_async');


const app = http.createServer((req, res) => {
	
	res.statusCode = 200;
	res.setHeader('Content-Type', 'text/plain');
	
	if (req.url === '/'){
		res.end('Hello Holberton School!\n');
	}
	else if (req.url === '/students') {
		
		const database = process.argv[2];
		if (!database) {
			res.statusCode = 500;
			res.end('Database is missing\n');
			return;
		}
	res.write('This is the list of our students\n');
	countStudents(database)
	.then ((message)=> {
		
		res.end(message.join('\n'));
	})
	.catch ((err) => {
		res.statusCode = 500;
		res.end('Cannot load the database\n');
});
	}
	else {
		res.statuscode = 404;
		res.end('Not found\n');
	}
});
app.listen(1245, () => {
	console.log('Server running on port 1245');
});

module.exports = app;