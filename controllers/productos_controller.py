from models.productos_model import ProductosModel
from models.categorias_productos_model import CategoriasProductosModel
from pprint import pprint
from app import db


class ProductosController:
    def __init__(self) -> None:
        self.model = ProductosModel

    def crearProducto(self, data):
        try:
            producto = self.model(data['nombre'], data['precio'], data['imagen'])
            db.session.add(producto)
            db.session.commit()
            categorias_productos = []
            for categoria in data['categorias']:
                nueva_categoria_producto = CategoriasProductosModel(categoria['categoria_id'], producto.id)
                categorias_productos.append(nueva_categoria_producto)

            db.session.add_all(categorias_productos)
            db.session.commit()

            return {
                'data': producto.convertirJson()
            }
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def listarProductos(self):
        try:
            productos = ProductosModel.query.all()
            response = []
            for producto in productos:
                response.append(producto.convertirJson())
            return {
                'data': response
            }
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500