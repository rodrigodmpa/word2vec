# word2vec

Web Interface for w2v model

Needs a w2v trained model from gensim on a `model/` folder.

Needs Docker to run.

To run:

* Build:</br>
`docker build -t flask-app:latest .`
* Run:</br>
`docker run -p 5000:5000 -v [path to the app]:/app flask-app`
* If wants to use the container bash:</br>
`docker exec -i -t name-container bash`

## Functions

1) Compare: Show a graph of the similariry of two words;

2) Top 10: Returns a list with the 10 most similiar words;

3) Operate: Operate words separated with a space. Can sum and subtract;

4) Similar among: Returns the most similar word among a list of words;
