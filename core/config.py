
import os

class Config:
    def __init__(self, app):
        try:
         
            app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_key')  
            app.config['UPLOAD_FOLDER'] = 'static/imagens'
            app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
            app.config['DEBUG'] = True
            
            
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
                
            print("Configurações aplicadas com sucesso!")
        except Exception as e:
            print(f"Erro ao aplicar configurações: {str(e)}")
