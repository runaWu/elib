import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db
# buku ==================================================

class Buku(db.Model):
    __tablename__ = 'buku'

    buku_id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String())
    tahun_terbit = db.Column(db.String())
    pengarang = db.Column(db.String())

    def __init__(self, judul, tahun_terbit, pengarang):
        self.judul=judul
        self.tahun_terbit = tahun_terbit
        self.pengarang= pengarang


    def __repr__(self):
        return '<buku id {}>'.format(self.buku_id)

    def serialize(self):
        return{
            'buku_id': self.buku_id,
            'judul': self.judul,
            'tahun_terbit': self.tahun_terbit,
            'pengarang': self.pengarang
            # 'contract_status': [{'id_': item.id_, 'vendor_name': item.vendor_name, 'contract_start_date': item.contract_start_date, 'contract_end_date': item.contract_end_date} for item in self.contract_status]
       }
# person =========================================================
class Person(db.Model):
    __tablename__ = 'person'

    person_id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String())

    def __init__(self, nama):
        self.nama=nama


    def __repr__(self):
        return '<person id {}>'.format(self.person_id)

    def serialize(self):
        return{
            'person_id': self.person_id,
            'nama': self.nama

       }
# peminjaman ==================================================

class Peminjaman(db.Model):
    __tablename__ = 'peminjaman'

    peminjaman_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    buku_id = db.Column(db.Integer)
    nama = db.Column(db.String())
    judul = db.Column(db.String())
    tanggal_peminjaman =  db.Column(db.DateTime)
    tanggal_pengembalian =  db.Column(db.DateTime)


    def __init__(self, person_id, buku_id, nama, judul, tanggal_peminjaman, tanggal_pengembalian):
        self.person_id=person_id
        self.buku_id = buku_id
        self.nama= nama
        self.judul =judul
        self.tanggal_peminjaman=tanggal_peminjaman
        self.tanggal_pengembalian=tanggal_pengembalian


    def __repr__(self):
        return '<peminjaman id {}>'.format(self.peminjaman_id)

    def serialize(self):
        return{
            'peminjaman_id': self.peminjaman_id,
            'person_id':self.person_id,
            'buku_id':self.buku_id,
            'nama':self.nama,
            'judul':self.judul,
            'tanggal_peminjaman':self.tanggal_peminjaman,
            'tanggal_pengembalian':self.tanggal_pengembalian
            
            
       }