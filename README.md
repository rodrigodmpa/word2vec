# word2vec
Web Interface for w2v model

Needs a w2v trained model from gensim on a `model/` folder.

Needs Docker to run.

To run:

* Build 
`docker build -t flask-app:latest .`
* Run
`docker run -p 5000:5000 -v [path to the app]:/app flask-app`
* If wants to use the container bash
`docker exec -i -t name-container bash`
