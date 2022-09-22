from flask import Flask, render_template
app = Flask(__name__)

@app.route('/Localhost:5000')
def consulta_one():
    return '¡Hola Mundo!'




@app.route('/Localhost:5000/dojo')
def consulta_two():
    return 'Dojo!'

@app.route('/Localhost:5000/say/<nombre>')
def consulta_three(nombre):
    if app (nombre,str):
        return f'Hola, {nombre} !' 
    else:
        return "<h1> Intentalo de nuevo </h1>"


    

@app.route('/Localhost:5000/repeat/<int:k>/<name>')
def consulta_for(k, name):
    return render_template('index.html',palabra=name, cantidad=k)







if __name__ =="__main__":
    app.run(debug=True)