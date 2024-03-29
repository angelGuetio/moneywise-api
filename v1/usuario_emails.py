from flask import Blueprint, jsonify
from models import Usuario_emails

usuario_emails_v1_bp = Blueprint('usuario_emails_v1', __name__, url_prefix='/v1/usuario_emails')

@usuario_emails_v1_bp.route('/', methods=['GET'])
def obtener_usuarios_emails():
    usuarios_emails = Usuario_emails.query.all()
    resultado = [{
        'id_usuario_email': usuario_email.id_usuario_email,
        'id_usuario': usuario_email.id_usuario,
        'email_usuario':usuario_email.email_usuario,
        
    } for usuario_email in usuarios_emails]
    return jsonify(resultado)

@usuario_emails_v1_bp.route('/<id_usuario_email>', methods=['GET'])
def obtener_usuario_email(id_usuario_email):
    usuario_email = Usuario_emails.query.get(id_usuario_email)
    if not usuario_email:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    resultado = {
        'id_usuario_email': usuario_email.id_usuario_email,
        'id_usuario': usuario_email.id_usuario,
        'email_usuario':usuario_email.email_usuario,
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar usuarios si es necesario.
