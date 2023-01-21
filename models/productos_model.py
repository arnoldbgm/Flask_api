from app import db
from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from sqlalchemy.orm import relationship

class ProductosModel(db.Model):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45),nullable=False)
    precio = Column(Float, nullable=False)
    imagen = Column(Text, nullable=False)
    estado = Column(Boolean, default=True)

    categoria_producto = relationship('CategoriasProductosModel')

    def __init__(self, nombre, precio, imagen, estado=None) -> None:
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
        self.estado = estado

    def convertirJson(self):
        cat_prod_array=[]
        for cat_prod in self.categoria_producto:
            cat_prod_array.append(cat_prod.convertirJson())
        return{
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen,
            'estado': self.estado,
            'categoria': ''
        }