from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Definir a pasta onde as imagens enviadas serão salvas
app.config['UPLOAD_FOLDER'] = 'static/imagens'  # Caminho onde as imagens serão salvas
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # Tipos de arquivos permitidos

# Verifica se a pasta "imagens" existe, se não, cria
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Função para verificar a extensão do arquivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Rota para o login
@app.route('/')
def login():
    return render_template('login.html')

# Rota para processar o login
@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    senha = request.form['password']
    
    # Verifica se as credenciais são válidas (sem verificação de senha complexa)
    if username == 'admin' and senha == 'admin':  # Valores fixos
        return redirect(url_for('upload'))
    
    return "Login falhou, tente novamente."

# Rota para upload de imagem
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return render_template('upload.html', filename=file.filename)
    return render_template('upload.html', filename=None)

if __name__ == '__main__':
    app.run(debug=True)
