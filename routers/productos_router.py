from app import app
from controllers.productos_controller import ProductosController
from flask import request

@app.route("/productos/listar", methods=['GET'])
def productosListar():
    controller = ProductosController()
    return controller.listarProductos()

@app.route("/productos/crear", methods=['POST'])
def productosCrear():
    controller = ProductosController()
    return controller.crearProducto(request.json)