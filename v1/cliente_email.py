from flask import Blueprint, jsonify
from models import Cliente_email

cliente_email_v1_bp = Blueprint('cliente_email_v1', __name__, url_prefix='/v1/cliente_email')

@ cliente_email_v1_bp.route('/', methods=['GET'])
def obtener_cliente_emails():
    cliente_emails = Cliente_email.query.all()
    resultado = [{
        'id_cliente_email': cliente_email.id_cliente_email,
        'id_tipo_email': cliente_email.id_tipo_email,
        'email': cliente_email.email,      
    } for  cliente_email in cliente_emails
    ]
    return jsonify(resultado)


@ cliente_email_v1_bp.route('/<id_cliente_email>', methods=['GET'])
def obtener_cliente_email(id_cliente_email):
    cliente_email = Cliente_email.query.get(id_cliente_email)
    if not cliente_email:
        return jsonify({'mensaje': 'Ciudad no encontrado'}), 404

    resultado = {
        'id_cliente_email': cliente_email.id_cliente_email,
        'id_tipo_email': cliente_email.id_tipo_email,
        'email': cliente_email.email,  
                
    }
    return jsonify(resultado)