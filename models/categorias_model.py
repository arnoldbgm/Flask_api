from app import db
from sqlalchemy import Column, Integer, String, Boolean

class CategoriasModel(db.Model):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    estado = Column(Boolean, default=True)

    def __init__(self, nombre, estado=None) -> None:
        self.nombre = nombre
        self.estado = estado

    def convertirJson(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'estado': self.estado
        }