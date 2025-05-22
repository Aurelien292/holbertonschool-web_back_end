class AppController {
	static getHomepage (request, response) {
		response.status(200).send('Hello Holberthon School!');
	}
}
export default AppController;