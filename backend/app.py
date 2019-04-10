from flask import Flask, jsonify, request, json, make_response
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from models import *
from random import randint
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)

POSTGRES = {
    'user': 'postgres',
    'pw': 'adittampan',
    'db': 'elibrary',
    'host': 'localhost',
    'port': '5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# postgresql://username:password@localhost:5432/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
# addbuku ============ 
@app.route('/addBuku', methods=["POST"])
def add_buku():

    body = request.json

    judul = body['judul']
    tahun_terbit = body['tahun_terbit']
    pengarang = body['pengarang']

    try:
        buku = Buku(
            judul=judul,
            tahun_terbit=tahun_terbit,
            pengarang=pengarang

        )

        db.session.add(buku)
        db.session.commit()
        return "add buku. buku id={}".format(buku.buku_id), 200

    except Exception as e:
        return(str(e)), 400

# GET ALL buku ===========
@app.route('/getAllBuku', methods=["GET"])
def get_all_buku():
        try:
                buku = Buku.query.order_by(Buku.buku_id).all()
                return jsonify([book.serialize()
                for book in buku])
        except Exception as e:
                return (str(e))

# GET buku BY ==============
@app.route('/getBukuBy/<bukuId_>', methods=["GET"])
def get_buku_by(bukuId_):
        try:
                buku = Buku.query.filter_by(buku_id=bukuId_).first()
                return jsonify(buku.serialize())
        except Exception as e:  
                return (str(e))
# addperson ============ 
@app.route('/addPerson', methods=["POST"])
def add_person():

    body = request.json

    nama = body['nama']


    try:
        person = Person(
            nama=nama

        )

        db.session.add(person)
        db.session.commit()
        return "add person. person id={}".format(person.person_id), 200

    except Exception as e:
        return(str(e)), 400
# addpeminjaman ============ 
@app.route('/addPeminjaman', methods=["POST"])
def add_peminjaman():

    body = request.json

    person_id = body['person_id']
    buku_id = body['buku_id']
    nama = body['nama']
    judul = body['judul']
    tanggal_peminjaman = body['tanggal_peminjaman']
    tanggal_pengembalian = body['tanggal_pengembalian']


    try:
        peminjaman = Peminjaman(
            person_id=person_id,
            buku_id=buku_id,
            nama=nama,
            judul=judul,
            tanggal_peminjaman=tanggal_peminjaman,
            tanggal_pengembalian=tanggal_pengembalian

        )

        db.session.add(peminjaman)
        db.session.commit()
        return "add peminjaman. peminjaman id={}".format(peminjaman.peminjaman_id), 200

    except Exception as e:
        return(str(e)), 400
