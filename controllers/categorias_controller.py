from models.categorias_model import CategoriasModel
from app import db

class CategoriasController:

    def __init__(self) -> None:
        self.model = CategoriasModel

    def crearCategoria(self, data):
        try:
            categoria = self.model(data['nombre'], data['estado'])
            db.session.add(categoria)
            db.session.commit()
            return{
                'data': categoria.convertirJson()
            },201
        except Exception as e:
            return{
                'message': 'Internal server error',
                'error': str(e)
            },500

    def listarCategorias(self):
        try:
            categorias = self.model.query.all()
            response = []
            for categoria in categorias:
                response.append(categoria.convertirJson())
            return{
                'data': response
            }
        except Exception as e:
            return{
                'message': 'Internal server error',
                'error': str(e)
            },500