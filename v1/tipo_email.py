from flask import Blueprint, jsonify
from models import Tipo_email

tipo_email_v1_bp = Blueprint('tipo_email_v1', __name__, url_prefix='/v1/tipo_email')

@ tipo_email_v1_bp.route('/', methods=['GET'])
def obtener_tipo_emails():
    tipo_emails = Tipo_email.query.all()
    resultado = [{
        'id_tipo_email': tipo_email.id_tipo_email,
        'descripcion': tipo_email.descripcion,
        
    } for  tipo_email in tipo_emails
    ]
    return jsonify(resultado)


@ tipo_email_v1_bp.route('/<id_tipo_email>', methods=['GET'])
def obtener_cliente_email(id_tipo_email):
    tipo_email = Tipo_email.query.get(id_tipo_email)
    if not tipo_email:
        return jsonify({'mensaje': 'Ciudad no encontrado'}), 404

    resultado = {
         'id_tipo_email': tipo_email.id_tipo_email,
        'descripcion': tipo_email.descripcion,
    }
    return jsonify(resultado)