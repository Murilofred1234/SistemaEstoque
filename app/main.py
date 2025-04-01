from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(__name__)

app.secret_key = "chave"

USERS = {
    "adm": {"password": "123", "role": "adm"},
    "func": {"password": "123", "role": "funcionario"}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    usuarioDigitado = request.form.get('usuario')
    senhaDigitada = request.form.get('senha')

    with open('usuarios.json') as usuariosTemp:
         usuarios = json.load(usuariosTemp)

         for usuario in usuarios:
             if usuario['usuario'] == usuarioDigitado and usuario['senha'] == senhaDigitada:
                 return render_template('')
    flash('Usuário INVÁLIDO')
    return redirect('/')
   
if __name__ == '__main__':
    app.run(debug=True)