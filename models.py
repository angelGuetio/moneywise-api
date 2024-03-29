
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Pais(db.Model):
    __tablename__ = 'pais'
    __table_args__ = {'schema': 'public'}

    id_pais = db.Column(db.String(3), primary_key=True)  # Cambiado a minúsculas
    nombre = db.Column(db.String(40), nullable=False)  # Cambiado a minúsculas
    indicativo_telefonico = db.Column(db.Numeric(4), nullable=False)  # Cambiado a minúsculas
    estado = db.Column(db.Numeric(1), nullable=False)  # Cambiado a minúsculas
    fecha_resgistro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)  # Cambiado a minúsculas
    fecha_actualizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Cambiado a minúsculas
    id_usuario = db.Column(db.String(10), nullable=True)  # Cambiado a minúsculas
    id_address = db.Column(db.String(15), nullable=True)  # Cambiado a minúsculas

    def __repr__(self):
        return f"<Pais(id_pais='{self.id}', nombre='{self.nombre}', indicativo_telefonico={self.indicativo_telefonico}, estado={self.estado}, fecha_resgistro='{self.fecha_resgistro}', fecha_actualizacion='{self.fecha_actualizacion}', id_usuario='{self.id_usuario}', id_address='{self.id_address}')>"

class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    __table_args__ = {'schema': 'public'}

    id_ciudad = db.Column(db.String(3), primary_key=True)  # Cambiado a minúsculas
    id_departamento = db.Column(db.String(3), nullable=True) 
    nombre = db.Column(db.String(10), nullable=False)  # Cambiado a minúsculas
    indicativo = db.Column(db.Numeric(4), nullable=False)  # Cambiado a minúsculas
    estado = db.Column(db.Boolean, nullable=False)
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)  # Cambiado a minúsculas
    fecha_actulizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Cambiado a minúsculas
    
    def __repr__(self):
        return f"<Ciudad(id_ciudad='{self.id}', id_departamento='{self.id_departamento}',nombre='{self.nombre}', indicativo={self.indicativo}, estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actulizacion='{self.fecha_actulizacion}')>"

class Depto(db.Model):
    __tablename__ = 'depto'
    __table_args__ = {'schema': 'public'}

    id_departamento = db.Column(db.String(3), primary_key=True)  # Cambiado a minúsculas
    id_pais = db.Column(db.String(3), nullable=True) 
    nombre = db.Column(db.String(30), nullable=False)  # Cambiado a minúsculas
    indicativo = db.Column(db.Integer, nullable=False)  # Cambiado a minúsculas
    estado = db.Column(db.Integer, nullable=False)  # Cambiado a minúsculas
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)  # Cambiado a minúsculas
    fecha_actualizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Cambiado a minúsculas
    
    def __repr__(self):
        return f"<Depto(id_departamento='{self.id}', id_pais='{self.id_pais}',nombre='{self.nombre}', indicativo={self.indicativo}, estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}')>"

class Usuario(db.Model):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': 'public'}

    id_usuario = db.Column(db.Integer, primary_key=True)
    id_ciudad = db.Column(db.Integer, nullable=False)
    id_tipo_usuario = db.Column(db.Integer, nullable=False)
    id_cliente_email = db.Column(db.Integer, nullable=False)
    usuario_email = db.Column(db.String(100), nullable=False)
    nombre_usuario = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.Numeric(1), nullable=False)
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    indicativo = db.Column(db.Numeric(4), nullable=False)  # Cambiado a minúsculas
    def __repr__(self):
        return f"<Usuario(id_usuario={self.id_usuario}, id_ciudad={self.id_ciudad}, id_tipo_usuario={self.id_tipo_usuario}, id_cliente_email={self.id_cliente_email}, usuario_email='{self.usuario_email}', nombre_usuario='{self.nombre_usuario}', nombre='{self.nombre}', apellido='{self.apellido}', estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}'indicativo='{self.indicativo}')>"

class Tipo_usuario(db.Model):
    __tablename__ = 'tipo_usuario'
    __table_args__ = {'schema': 'public'}

    id_tipo_usuario = db.Column(db.Integer, primary_key=True)
    nombre_tipo_usuario = db.Column(db.String(50), nullable=False)
    descripcion_tipo_usuario = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"<Tipo_usuario(id_tipo_usuario={self.id_tipo_usuario}, nombre_tipo_usuario={self.nombre_tipo_usuario}, descripcion_tipo_usuario={self.descripcion_tipo_usuario})>"

class Usuario_emails(db.Model):
    __tablename__ = 'usuario_emails'
    __table_args__ = {'schema': 'public'}

    id_usuario_email = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.String(50), nullable=False)
    email_usuario = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"<Usuario_emails(id_usuario_email={self.id_usuario_email}, id_usuario={self.id_usuario}, email_usuario={self.email_usuario})>"


class Usuario_roles(db.Model):
    __tablename__ = 'usuario_roles'
    __table_args__ = {'schema': 'public'}

    id_usuario_roles = db.Column(db.Integer, primary_key=True)
    id_roles_usuario = db.Column(db.String(50), nullable=False)
    id_usuario = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"<Usuario_roles(id_usuario_roles={self.id_usuario_roles},  id_roles_usuario={self.id_roles_usuario},  id_usuario={self.id_usuario})>"

class Roles_usuario(db.Model):
    __tablename__ = 'roles_usuario'
    __table_args__ = {'schema': 'public'}

    id_roles_usuario = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"<Roles_usuario(id_roles_usuario={self.id_roles_usuario},  nombre_rol={self.nombre_rol},  descripcion={self.descripcion})>"
