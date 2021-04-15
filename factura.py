from flask import Flask, jsonify, request
from clientes import clientel
from datetime import datetime
from facturas import factural
from paquete import paquetesl

factura = Flask(__name__)

@factura.route('/facturas',methods = ['POST'])
def aggfactura():
  items = []
  total = 0.0
  nc = {
    "id":request.json['cliente']['id'],
    "nombre":request.json['cliente']['nombre'],
    "apellidos":request.json['cliente']['apellidos'],
    "direccion":request.json['cliente']['direccion'],
    "cod_postal":request.json['cliente']['cod_postal']
  }
  items = request.json['items']
  for i in items:
    total=total+i['trayectoria']['costo']+i['precio']
  
  newf = {
    "id":request.json['id'],
    "total":total,
    "fecha":datetime.now(),
    "cliente":nc,
    "items":items
  }
  factural.append(newf)
  return jsonify({"message": "Factura generada correctamente", "Factura": newf})

@factura.route('/facturas/<int:id>',methods = ['GET'])
def buscfact(id):
  FFound = [bfactura for bfactura in factural if bfactura['id'] == id]
  if(len(FFound)>0):
    return jsonify({"message": "Factura Encontrada", "Factura": FFound[0]})
  return jsonify({"message": "Error"})

@factura.route('/facturas/<int:id>',methods = ['DELETE'])
def delfact(id):
  FFound = [bfactura for bfactura in factural if bfactura['id'] == id]
  if(len(FFound)>0):
    factural.remove(FFound[0])
    return jsonify({"message": "Factura Eliminada", "Lista de Facturas": factural})
  return jsonify({"message": "Error"})

@factura.route('/facturas/<int:id>', methods = ['PUT'])
def actualizarCliente(id):
  FFound = [bfactura for bfactura in factural if bfactura['id'] == id]
  if  (len(FFound)>0):  
    nc = {
      "id":request.json['cliente']['id'],
      "nombre":request.json['cliente']['nombre'],
      "apellidos":request.json['cliente']['apellidos'],
      "direccion":request.json['cliente']['direccion'],
      "cod_postal":request.json['cliente']['cod_postal']
    }
    items = []
    tempitems = request.json['items']
    for i in tempitems:
      if (i['Del']!=True):
        items.append(i)
    for i in items:
      total=total+i['trayectoria']['costo']+i['precio']
    FFound[0]['fecha']:datetime.now()
    FFound[0]['cliente']:nc
    FFound[0]['items']:items
    FFound[0]['total']:total
    return jsonify({"message": "Factura Actualizada", "Factura": FFound[0]})
  return jsonify({"message": "Error"})



if __name__ == '__main__':
    factura.run(debug=True, port=4000)