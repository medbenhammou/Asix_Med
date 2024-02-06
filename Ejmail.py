#Mohamed Ben Hammou

from flask import Flask, render_template, request


app = Flask(__name__)

# Lista de nombres y correos electrónicos
my_dectionario = {
"Mercedes":	"mcast386@xtec.cat",
"Rayane": "rayane@rayane.sa",
"Mohamed": "moha@gmail.com",
"Jad": "jad@gmail.com",
"Oriol": "joam@gmail.com",
"Elias": "hola123@gmail.com",
"Armau": "arnau@gmail.com",
"Asdrúbal": "asdrubal@gmail.com",
"Adrian": "pedrosanchez@asix2.com",
"Eric": "eric@gmail.com",
"Emma":	"pacosanz@gmail.com",
"nishwan": "nishwan@gmail.com",
"Javi":	"javi@gmail.com",
"Novel": "novelferreras49@gmail.com",
"Bruno": "elcigala@gmail.com",
"David": "david@gmail.com",
"Judit": "judit@gmail.com",
"Joao":	"joao@gmail.com",
"Laura": "laura@gmail.com",
"enrico": "123@gmail.com",
"Joel":	"joel@gmail.com",
"Aaron": "aaron@gmail.com"
}

@app.route('/getmail', methods=['GET', 'POST'])
def getmailform():
    if request.method == 'POST':
        nombre = request.form['nombre']
        if nombre in my_dectionario:
            email = my_dectionario[nombre]
            return render_template('resultgetmail.html', nombre=nombre, email=email)
        else:
            mensaje = "*Usuario no encontrado!!!"
            return render_template('formgetmail.html', mensaje=mensaje)
    return render_template('formgetmail.html')

@app.route('/addmail', methods=['GET', 'POST'])
def addmailform():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        my_dectionario[nombre] = email
        return render_template('resultaddmail.html', nombre=nombre, email=email)      
    return render_template('formaddmail.html')

if __name__ == '__main__':
    app.run(debug=True)