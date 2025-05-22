import chai from 'chai';
import chaiHttp from 'chai-http';
import app from '../full_server/server'; // Ton fichier où Express est lancé

process.argv[2] = 'database.csv'; // chemin vers ta base locale

chai.use(chaiHttp);
const { expect } = chai;

describe('StudentsController', () => {
  describe('GET /students/SWE', () => {
  it('devrait retourner la liste des étudiants SWE', (done) => {
    chai.request(app)
      .get('/students/SWE')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.text).to.include('List:');
        done();
      });
  });
});
  describe('GET /students', () => {
    it('devrait retourner une liste de tous les étudiants', (done) => {
      chai.request(app)
        .get('/students')
        .end((err, res) => {
          expect(res).to.have.status(200);
          expect(res.text).to.include('This is the list of our students');
          expect(res.text).to.include('Number of students in CS');
          expect(res.text).to.include('Number of students in SWE');
          done();
        });
    });
  });

  describe('GET /students/CS', () => {
    it('devrait retourner la liste des étudiants CS', (done) => {
      chai.request(app)
        .get('/students/CS')
        .end((err, res) => {
          expect(res).to.have.status(200);
          expect(res.text).to.include('List:');
          done();
        });
    });
  });

  describe('GET /students/French', () => {
    it('devrait retourner une erreur 500 pour un major invalide', (done) => {
      chai.request(app)
        .get('/students/French')
        .end((err, res) => {
          expect(res).to.have.status(500);
          expect(res.text).to.equal('Major parameter must be CS or SWE');
          done();
        });
    });
  });
});

describe('GET /students avec fichier invalide', () => {
  it('devrait retourner une erreur 500 si la base est introuvable', (done) => {
    // Simule un mauvais chemin de base
    process.argv[2] = 'invalid.csv';

    chai.request(app)
      .get('/students')
      .end((err, res) => {
        expect(res).to.have.status(500);
        expect(res.text).to.equal('Cannot load the database');
        // Remettre un chemin correct après le test
        process.argv[2] = 'database.csv';
        done();
      });
  });
});

