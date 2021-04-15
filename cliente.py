from flask import Flask, jsonify, request
from clientes import clientel
from init import app

@app.route('/clientes',methods = ['POST'])
def aggcliente():
  newc = {
            "id":request.json['id'],
            "nombre":request.json['nombre'],
            "apellidos":request.json['apellidos'],
            "direccion":request.json['direccion'],
            "cod_postal":request.json['cod_postal']
        }
  clientel.append(newc)
  return jsonify({"message": "Cliente agregado correctamente", "Clientes": clientel})

@app.route('/clientes/<int:id>',methods = ['GET'])
def buscliente(id):
  CFound = [bcliente for bcliente in clientel if bcliente['id'] == id]
  if(len(CFound)>0):
    return jsonify({"message": "Cliente Encontrado", "Cliente": CFound[0]})
  return jsonify({"message": "Error"})

@app.route('/clientes/<int:id>', methods = ['PUT'])
def actualizarCliente(id):
  c = [bcliente for bcliente in clientel if bcliente['id'] == id]
  if  (len(c)>0):
    c[0]['nombre'] =  request.json['nombre']
    c[0]['apellidos'] = request.json['apellidos']
    c[0]['direccion'] = request.json['direccion']
    c[0]['cod_postal'] = request.json['cod_postal']
    return jsonify({"message": "Cliente Actualizado", "Cliente": c[0]})
  return jsonify({"message": "Error"})

