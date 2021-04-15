from flask import Flask, jsonify, request
from paquete import paquetesl

paquetes = Flask(__name__)

@paquetes.route('/paquetes',methods = ['POST'])
def newpaquete():
  newp = {
            "id":request.json['id'],
            "nombre":request.json['nombre'],
            "precio":request.json['precio'],
            "trayectoria":request.json['trayectoria'],
        }
  paquetesl.append(newp)
  return jsonify({"message": "Paquete agregado correctamente", "Paquete": paquetesl})

@paquetes.route('/paquetes/<int:id>',methods = ['GET'])
def buscapaquete(id):
  PFound = [bpaquete for bpaquete in paquetesl if bpaquete['id'] == id]
  if(len(PFound)>0):
    return jsonify({"message": "Paquete Encontrado", "Cliente": PFound[0]})
  return jsonify({"message": "Error"})

@paquetes.route('/paquetes/<int:id>',methods = ['PUT'])
def uppaquete(id):
  PFound = [bpaquete for bpaquete in paquetesl if bpaquete['id'] == id]
  if(len(PFound)>0):
    PFound[0]["nombre"] = request.json['nombre']
    PFound[0]["precio"]=request.json['precio']
    PFound[0]["trayectoria"]=request.json['trayectoria']
    return jsonify({"message": "Paquete Actualizado", "Cliente": PFound[0]})
  return jsonify({"message": "Error"})


if __name__ == '__main__':
    paquetes.run(debug=True, port=4000)