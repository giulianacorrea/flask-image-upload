import logging
import os
from flask import Flask, render_template, request, redirect, url_for
from core.config import Config  
from core.erro import ErrorHandler  

app = Flask(__name__)

config = Config(app) #passando o app p  config 


logging.basicConfig(level=logging.DEBUG)  
app.logger.info('Aplicação Flask iniciada')  

# Função para verificar a extensão do arquivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def login():
    app.logger.info('Página de login acessada ')  
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    senha = request.form['password']
    
  
    if username == 'admin' and senha == 'admin':
        app.logger.info('Login bem-sucedido')  
        return redirect(url_for('upload'))
    
    app.logger.warning(f'Falha no login para o usuário: {username}')  
    return "Login falhou, tente novamente."


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            app.logger.info(f'Imagem {file.filename} salva com sucesso!')  
            return render_template('upload.html', filename=file.filename)
        else:
            app.logger.warning(f'Arquivo inválido: {file.filename}')  
    return render_template('upload.html', filename=None)
 

if __name__ == "__main__":
    app.run(debug=True)
