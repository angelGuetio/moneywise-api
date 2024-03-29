from flask import Blueprint, jsonify
from models import Depto

depto_v1_bp = Blueprint('depto_v1', __name__, url_prefix='/v1/depto')

@depto_v1_bp.route('/', methods=['GET'])
def obtener_deptos():
    deptos = Depto.query.all()
    resultado = [{
        'id_departamento': depto.id_departamento,
        'id_pais': depto.id_pais,
        'nombre': depto.nombre,
        'indicativo': depto.indicativo,
        'estado': int(depto.estado),
        'fecha_registro': depto.fecha_registro.isoformat(),
        'fecha_actualizacion': depto.fecha_actualizacion.isoformat(),
        
    } for depto in deptos]
    return jsonify(resultado)

@depto_v1_bp.route('/<id_depto>', methods=['GET'])
def obtener_depto(id_depto):
    depto = Depto.query.get(id_depto)
    if not depto:
        return jsonify({'mensaje': 'Ciudad no encontrado'}), 404

    resultado = {
        'id_departamento': depto.id_departamento,
        'id_pais': depto.id_pais,
        'nombre': depto.nombre,
        'indicativo': depto.indicativo,
        'estado': int(depto.estado),
        'fecha_registro': depto.fecha_registro.isoformat(),
        'fecha_actualizacion': depto.fecha_actualizacion.isoformat(),
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar países si es necesario.
