from flask import Blueprint, jsonify
from models import Tipo_usuario

tipo_usuario_v1_bp = Blueprint('tipo_usuario_v1', __name__, url_prefix='/v1/tipo_usuario')

@tipo_usuario_v1_bp.route('/', methods=['GET'])
def obtener_tipo_usuarios():
    tipo_usuarios = Tipo_usuario.query.all()
    resultado = [{
        'id_tipo_usuario': tipo_usuario.id_tipo_usuario,
        'nombre_tipo_usuario': tipo_usuario.nombre_tipo_usuario,
        'descripcion_usuario': tipo_usuario.id_tipo_usuario,
        
        
    } for tipo_usuario in tipo_usuarios]
    return jsonify(resultado)

@tipo_usuario_v1_bp.route('/<id_tipo_usuario>', methods=['GET'])
def obtener_tipo_usuario(id_tipo_usuario):
    tipo_usuario = Tipo_usuario.query.get(id_tipo_usuario)
    if not tipo_usuario:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    resultado = {
        'id_tipo_usuario': tipo_usuario.id_tipo_usuario,
        'nombre_tipo_usuario': tipo_usuario.nombre_tipo_usuario,
        'descripcion_tipo_usuario': tipo_usuario.descripcion_usuario,
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar usuarios si es necesario.
