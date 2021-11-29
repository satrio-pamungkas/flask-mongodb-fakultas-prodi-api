from config import *
import pymongo
import json

client = pymongo.MongoClient(f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@cluster0.od9px.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")
db = client[DB_NAME]
collection = db[DB_COLLECTION]

def get_all():
    base = {"universitas": "Universitas Pendidikan Indonesia"}
    cursor = collection.distinct('fakultas', {})

    list_fakultas = []
    for fakultas in cursor:
        data = {'namaFakultas': fakultas, 'listProdi': get_all_list(fakultas)}
        list_fakultas.append(data)
        
    base['listFakultas'] = list_fakultas
    return base
    
    
def get_all_list(nama_fakultas):
    cursor = collection.find({'fakultas': nama_fakultas}, {'kode':1, 'prodi':1, '_id':0})

    if cursor.count() == 0:
        return None

    list_prodi = []
    for prodi in cursor:
        data = {'kodeProdi': prodi['kode'], 'namaProdi': prodi['prodi']}
        list_prodi.append(data)
        
    return list_prodi


def get_list_fakultas():
    cursor = collection.distinct('fakultas', {})
    
    if cursor is None:
        return None

    list_fakultas = []
    for fakultas in cursor:
        data = {'namaFakultas': fakultas}
        list_fakultas.append(data)
        
    return list_fakultas
    

def get_list_prodi_fakultas(nama_fakultas):
    base = {"namaFakultas": nama_fakultas}
    cursor = collection.find({'fakultas': nama_fakultas}, {'kode':1, 'prodi':1, '_id':0})

    if cursor.count() == 0:
        return None

    list_prodi = []
    for prodi in cursor:
        data = {'kodeProdi': prodi['kode'], 'namaProdi': prodi['prodi']}
        list_prodi.append(data)
        
    base['listProdi'] = list_prodi
    return base


def get_list_prodi():
    cursor = collection.find({}, {'kode':1, 'prodi':1, '_id':0})
    
    if cursor is None:
        return None
    
    list_prodi = list(cursor)
    return list_prodi


def get_prodi(kode_prodi):
    cursor = collection.find_one({'kode': kode_prodi}, {'_id':0})
        
    if cursor is None:
        return None
    
    return cursor
    
    


