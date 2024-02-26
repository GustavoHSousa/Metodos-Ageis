from flask import Flask, render_template, request

app = Flask(__name__)

class Autenticacao:
    def __init__(self):
        self.usuarios = {'usuario1': 'senha123', 'usuario2': 'senha456'}

    def autenticar(self, usuario, senha):
        return usuario in self.usuarios and self.usuarios[usuario] == senha

autenticacao = Autenticacao()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usuario_inserido = request.form['usuario']
        senha_inserida = request.form['senha']

        if autenticacao.autenticar(usuario_inserido, senha_inserida):
            return render_template('sucesso.html', usuario=usuario_inserido)
        else:
            return render_template('falha.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
