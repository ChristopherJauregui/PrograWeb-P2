#Paso 1
'''from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():

    return 'Bienvenido' '''
#Paso 2
'''from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/')

def hello():

    return 'Bienvenido' '''
#paso 3
'''from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/<name>')

def hello(name):

    return 'Bienvenido '+name '''
#paso 4
'''from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/<int:ncontrol>')

def hello(ncontrol):
    return 'Bienvenido '+str(ncontrol)'''
#paso 5
'''from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/<int:ncontrol>')

def hello(ncontrol):
    return f'Numero recibido es: {ncontrol}' '''
#Paso 6
'''from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/<name>/<int:ncontrol>') 

def hello(name,ncontrol):

    return f'Bienvenido {name} con numero de control: {ncontrol}'  '''
#paso 7
from flask import Flask

app = Flask(__name__)
@app.route('/wellcome/')

@app.route('/wellcome/<name>')

@app.route('/wellcome/<int:ncontrol>')

@app.route('/wellcome/<name>/<int:ncontrol>')

def bienvenido(name=None,ncontrol=None):

    if name== None and ncontrol==None:

        return 'Bienvenido '

    if name!= None and ncontrol == None:

        return f'Bienvenido {name}'

    if name == None and ncontrol != None:

        return f'El número recibido es: {ncontrol}'

    else:

        return f'Bienvenido {name} tu numero de control es: {ncontrol}' 