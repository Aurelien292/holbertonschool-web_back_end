const fs = require('fs').promises;

async function readDatabase(path) {
	try {
		const data = await fs.readFile(path, {encoding: 'utf-8'});
		const content = data.split('\n').filter(line => line.trim() !== '');

		if (content.length < 2) {
			throw new Error('Cannot load the database');
		}

		const fields = {};

		for (let i = 1; i <content.length; i += 1 ){
			const student = content[i].split(',');

			if (!fields[student[3]]) {
				fields[student[3]] = [];
			}
			fields[student[3]].push(student[0]);
		}
		return fields;
	}
	catch (err) {
		throw new Error('Cannot load the database');
	}
}
export default readDatabase;
