from flask import Blueprint, jsonify
from models import Tipo_direccion

tipo_direccion_v1_bp = Blueprint('tipo_direccion_v1', __name__, url_prefix='/v1/tipo_direccion')

@ tipo_direccion_v1_bp.route('/', methods=['GET'])
def obtener_tipo_direcciones():
    tipo_direcciones = Tipo_direccion.query.all()
    resultado = [{
        'id_tipo_direccion': tipo_direccion.id_tipo_direccion,
        'nombre': tipo_direccion.nombre,
                
    } for  tipo_direccion in tipo_direcciones
    ]
    return jsonify(resultado)


@ tipo_direccion_v1_bp.route('/<id_tipo_direccion>', methods=['GET'])
def obtener_tipo_direccion(id_tipo_direccion):
    tipo_direccion = tipo_direccion.query.get(id_tipo_direccion)
    if not tipo_direccion:
        return jsonify({'mensaje': 'Ciudad no encontrado'}), 404

    resultado = {
         'id_tipo_direccion': tipo_direccion.id_tipo_direccion,
        'nombre': tipo_direccion.nombre,
                
    }
    return jsonify(resultado)