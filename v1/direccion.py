from flask import Blueprint, jsonify
from models import Direccion

direccion_v1_bp = Blueprint('direccion_v1', __name__, url_prefix='/v1/direccion')

@ direccion_v1_bp.route('/', methods=['GET'])
def obtener_direcciones():
    direcciones = Direccion.query.all()
    resultado = [{
        'id_direccion': direccion.id_direccion,
        'nombre': direccion.nombre,
                
    } for  direccion in direcciones
    ]
    return jsonify(resultado)


@direccion_v1_bp.route('/<id_direccion>', methods=['GET'])
def obtener_direccion(id_direccion):
    direccion = direccion.query.get(id_direccion)
    if not direccion:
        return jsonify({'mensaje': 'Ciudad no encontrado'}), 404

    resultado = {
        'id_direccion': direccion.id_direccion,
        'nombre': direccion.nombre,
                
    }
    return jsonify(resultado)