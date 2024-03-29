from flask import Blueprint, jsonify
from models import Usuario_roles

usuario_roles_v1_bp = Blueprint('usuario_roles_v1', __name__, url_prefix='/v1/usuario_roles')

@usuario_roles_v1_bp.route('/', methods=['GET'])
def obtener_usuario_roles():
    usuario_roles = Usuario_roles.query.all()
    resultado = [{
        'id_usuario_roles': usuario_role.id_usuario_roles,
        'id_roles_usuario': usuario_role.id_roles_usuario,
        'id_usuario': usuario_role.id_usuario,
        
    } for usuario_role in usuario_roles]
    return jsonify(resultado)


@usuario_roles_v1_bp.route('/<id_usuario_roles>', methods=['GET'])
def obtener_usuario_rol(id_usuario_roles):
    usuario_role = usuario_role.query.get(id_usuario_roles)
    if not usuario_role:
        return jsonify({'mensaje': 'Ciudad no encontrado'}), 404

    resultado = {
        'id_usuario_roles': usuario_role.id_usuario_roles,
        'id_roles_usuario': usuario_role.id_roles_usuario,
        'id_usuario': usuario_role.id_usuario,
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar países si es necesario.
