from flask import Flask
from models import db 
from v1.pais import pais_v1_bp
from v1.ciudad import ciudad_v1_bp
from v1.depto import depto_v1_bp
from v1.usuario import usuario_v1_bp
from v1.tipo_usuario import tipo_usuario_v1_bp
from v1.usuario_emails import usuario_emails_v1_bp
from v1.usuario_roles import usuario_roles_v1_bp
from v1.roles_usuario import roles_usuario_v1_bp

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Inicialización de la base de datos
    db.init_app(app)

    # Registro del blueprint para la versión 1 de la API
    app.register_blueprint(pais_v1_bp, url_prefix='/v1/pais')
    app.register_blueprint(ciudad_v1_bp, url_prefix='/v1/ciudad')
    app.register_blueprint(depto_v1_bp, url_prefix='/v1/depto')
    app.register_blueprint(usuario_v1_bp, url_prefix='/v1/usuario')
    app.register_blueprint(tipo_usuario_v1_bp, url_prefix='/v1/tipo_usuario')
    app.register_blueprint(usuario_emails_v1_bp, url_prefix='/v1/usuario_emails')
    app.register_blueprint(usuario_roles_v1_bp, url_prefix='/v1/usuario_roles')
    app.register_blueprint(roles_usuario_v1_bp, url_prefix='/v1/roles_usuario')
    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


