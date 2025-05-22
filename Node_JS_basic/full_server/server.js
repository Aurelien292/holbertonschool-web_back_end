import express from 'express';
import router from './routes/index.js';

const app = express();
const port = 1245;


app.use('/', router);

if ( require.main === module) {
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
}
export default app;
