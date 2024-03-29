from flask import Blueprint, jsonify
from models import Roles_usuario

roles_usuario_v1_bp = Blueprint('roles_usuario_v1', __name__, url_prefix='/v1/roles_usuario')

@roles_usuario_v1_bp.route('/', methods=['GET'])
def obtener_roles_usuarios():
    roles_usuarios = Roles_usuario.query.all()
    resultado = [{
        'id_roles_usuario': roles_usuario.id_roles_usuario,
        'nombre_rol': roles_usuario.nombre_rol,
        'descripcion': roles_usuario.descripcion,
        
    } for  roles_usuario in roles_usuarios
    ]
    return jsonify(resultado)


@roles_usuario_v1_bp.route('/<id_roles_usuario>', methods=['GET'])
def obtener_roles_usuario(id_roles_usuario):
    roles_usuario = roles_usuario.query.get(id_roles_usuario)
    if not roles_usuario:
        return jsonify({'mensaje': 'Ciudad no encontrado'}), 404

    resultado = {
        'id_roles_usuario': roles_usuario.id_roles_usuario,
        'nombre_rol': roles_usuario.nombre_rol,
        'descripcion': roles_usuario.descripcion,
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar países si es necesario.
