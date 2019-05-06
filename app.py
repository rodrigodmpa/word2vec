#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, flash, redirect,url_for
from flask_bootstrap import Bootstrap
from my_word2vec import *
from form import *

def create_app():
  app = Flask(__name__)
  app.secret_key = "!@a1'f57jF2!2$d4#"
  return app

app = create_app()
@app.route('/', methods=['GET', 'POST'])
def index():
	gera = { "similarity":0,"lista":0,'operar':0,'keyerror':0 }
	if request.method == 'POST':
		if request.form['action'] == 'comparar':
			return redirect(url_for('.compara'))
		elif request.form['action'] == 'lista':
			return redirect(url_for('.lista'))
		elif request.form['action'] == 'operar':
			return redirect(url_for('.operar'))
		elif request.form['action'] == 'similar_entre':
			return redirect(url_for('.similar_entre'))
	return render_template('index.html')
	
@app.route('/compara', methods=['GET', 'POST'])
def compara():
	gera = { "similarity":0,"lista":0,'operar':0,'keyerror':0 }
	if request.method == 'POST':
		default_model = gensim.models.Word2Vec.load('modelos/saved_models')
		gera = { "similarity":1,"lista":0,'operar':0,'keyerror':0 }
		try:
			arg1 = request.form.get('arg1')
			arg2 = request.form.get('arg2')
			comparacao = default_model.wv.similarity(arg1,arg2)
		except KeyError as e:
			gera = { "similarity":1,"lista":0,'operar':0,'keyerror':1 }
			return render_template('compara.html', gera=gera, e=e)
		comparacao = round(comparacao,4)
		flash('Done! ')
		return render_template('compara.html', gera=gera, comparacao=comparacao, arg1=arg1, arg2=arg2)
	return render_template('compara.html', gera=gera)


@app.route('/lista', methods=['GET', 'POST'])
def lista():
	gera = { "similarity":0,"lista":0,'operar':0,'keyerror':0 }
	if request.method == 'POST':
		print(request.form.get('arg1',type=str))
		default_model = gensim.models.Word2Vec.load('modelos/saved_models')
		gera = { "similarity":1,"lista":1,'operar':0,'keyerror':0 }
		
		try:
			arg1 = request.form.get('arg1',type=str)
			arg2 = request.form.get('arg2',type=int)
			lista = default_model.wv.similar_by_word(arg1,topn=arg2)
		except KeyError:
			lista = []
			e = 'The word '+arg1+' don''t isn''t in the model.'
			gera = { "similarity":1,"lista":0,'operar':0,'keyerror':1 }
			return render_template('lista.html', gera=gera, lista=lista, e=e)
		flash('Done! ')
		return render_template('lista.html', gera=gera, lista=lista, arg1=arg1,arg2=arg2)
	return render_template('lista.html', gera=gera)

@app.route('/operar', methods=['GET', 'POST'])
def operar():
	gera = { "similarity":0,"lista":0,'operar':0,'keyerror':0 }
	if request.method == 'POST':
		default_model = gensim.models.Word2Vec.load('modelos/saved_models')
		gera = { "similarity":0,"lista":0,'operar':1,'keyerror':0 }
		
		try:
			arg1 = request.form.get('arg1',type=str)
			arg2 = request.form.get('arg2',type=str)
			positive = arg1.split()
			negative = arg2.split()
			lista = default_model.wv.most_similar(positive=positive, negative=negative, topn=1)
		except KeyError as e:
			lista = []
			gera = { "similarity":0,"lista":0,'operar':0,'keyerror':1 }
			return render_template('operar.html', gera=gera, lista=lista, e=e)
		flash('Done! ')
		return render_template('operar.html', gera=gera, lista=lista, positive=positive,negative=negative)
	return render_template('operar.html', gera=gera)

@app.route('/similar_entre', methods=['GET', 'POST'])
def similar_entre():
	gera = { "similarity":0,"lista":0,'operar':0,'operar':0,'keyerror':0 }
	if request.method == 'POST':
		default_model = gensim.models.Word2Vec.load('modelos/saved_models')
		gera['similar_entre'] = 1
		try:
			arg1 = request.form.get('arg1',type=str)
			arg2 = request.form.get('arg2',type=str).split()
			item = default_model.wv.most_similar_to_given(arg1, arg2)
		except KeyError as e:
			item = ''
			gera['keyerror'] = 1
			return render_template('similar_entre.html', gera=gera, item=item, e=e)
		flash('Done! ')
		return render_template('similar_entre.html', gera=gera, item=item, arg1=arg1,arg2=arg2)
	return render_template('similar_entre.html', gera=gera)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')