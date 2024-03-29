from flask import Blueprint, jsonify
from models import Usuario

usuario_v1_bp = Blueprint('usuario_v1', __name__, url_prefix='/v1/usuario')

@usuario_v1_bp.route('/', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    resultado = [{
        'id_usuario': usuario.id_usuario,
        'id_ciudad': usuario.id_ciudad,
        'id_tipo_usuario': usuario.id_tipo_usuario,
        'id_cliente_email': usuario.id_cliente_email,
        'usuario_email': usuario.usuario_email,
        'nombre_usuario': usuario.nombre_usuario,
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'estado': int(usuario.estado),
        'fecha_registro': usuario.fecha_registro.isoformat(),
        'fecha_actualizacion': usuario.fecha_actualizacion.isoformat(),
    } for usuario in usuarios]
    return jsonify(resultado)

@usuario_v1_bp.route('/<id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    if not usuario:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    resultado = {
        'id_usuario': usuario.id_usuario,
        'id_ciudad': usuario.id_ciudad,
        'id_tipo_usuario': usuario.id_tipo_usuario,
        'id_cliente_email': usuario.id_cliente_email,
        'usuario_email': usuario.usuario_email,
        'nombre_usuario': usuario.nombre_usuario,
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'estado': int(usuario.estado),
        'fecha_registro': usuario.fecha_registro.isoformat(),
        'fecha_actualizacion': usuario.fecha_actualizacion.isoformat(),
        'indicativo': usuario.indicativo,
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar usuarios si es necesario.
