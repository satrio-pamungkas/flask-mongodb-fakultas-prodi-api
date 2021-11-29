from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from controller import *
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/fakultas-prodi', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type','application/json'])
def all():
    data = get_all()
    response = {'data': data}
    return jsonify(response), 200


@app.route('/fakultas', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type','application/json'])
def list_fakultas():
    data = get_list_fakultas()
    response = {'data': data}
    return jsonify(response), 200


@app.route('/fakultas/<nama_fakultas>/prodi', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type','application/json'])
def list_prodi_fakultas(nama_fakultas):
    data = get_list_prodi_fakultas(nama_fakultas)
    
    if data is None:
        message = []
        desc = {
            "status": "404",
            "title": "Tidak ditemukan",
            "detail": "Prodi dari fakultas bersangkutan tidak ditemukan"
        }
        message.append(desc)
        response = {'errors': message}
        return jsonify(response), 404
    
    response = {'data': data}
    return jsonify(response), 200


@app.route('/prodi', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type','application/json'])
def list_prodi():
    data = get_list_prodi()
    response = {'data': data}
    return jsonify(response), 200


@app.route('/prodi/<kode_prodi>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type','application/json'])
def prodi(kode_prodi):
    data = get_prodi(kode_prodi)
    
    if data is None:
        message = []
        desc = {
            "status": "404",
            "title": "Tidak ditemukan",
            "detail": "Kode prodi tidak ditemukan"
        }
        message.append(desc)
        response = {'errors': message}
        return jsonify(response), 404
    
    response = {'data': data}
    return jsonify(response), 200
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)

