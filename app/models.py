from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from sqlalchemy_paginator import Paginator
from secrets import token_hex

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    apitoken = db.Column(db.String, default=None, nullable=True)

    def __init__(self,fname,lname,email,username,password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.apitoken = token_hex(16)
    
    def to_dict(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email,
            'username': self.username,
            'token': self.apitoken
        }

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

class Cigars(db.Model):
    cigar_id = db.Column(db.Integer, primary_key=True)
    cigar = db.Column(db.String, nullable=False)
    length = db.Column(db.String)
    ring_gauge = db.Column(db.String)
    country = db.Column(db.String)
    shape = db.Column(db.String)
    wrapper = db.Column(db.String)
    binder = db.Column(db.String)
    filler = db.Column(db.String)
    color = db.Column(db.String)
    strength = db.Column(db.String)
    start_mfg_yr = db.Column(db.String)
    end_mfg_yr = db.Column(db.String)
    img_url = db.Column(db.String)
    img_cigar = db.Column(db.String)
    mfg_website = db.Column(db.String)

    def __init__(self,cigar,length,ring_gauge,country,shape,wrapper,binder,filler,color,strength,start_mfg_yr,end_mfg_yr,img_url,img_cigar,mfg_website):
        self.cigar = cigar
        self.length = length
        self.ring_gauge = ring_gauge
        self.country = country
        self.shape = shape
        self.wrapper = wrapper
        self.binder = binder
        self.filler = filler
        self.color = color
        self.strength = strength
        self.start_mfg_yr = start_mfg_yr
        self.end_mfg_yr = end_mfg_yr
        self.img_url = img_url
        self.img_cigar = img_cigar
        self.mfg_website = mfg_website

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def saveChanges(self):
        db.session.commit()

    def updateInfo(self,cigar,length,ring_gauge,country,shape,wrapper,binder,filler,color,strength,start_mfg_yr,end_mfg_yr,img_url,img_cigar,mfg_website):
        self.cigar = cigar
        self.length = length
        self.ring_gauge = ring_gauge
        self.country = country
        self.shape = shape
        self.wrapper = wrapper
        self.binder = binder
        self.filler = filler
        self.color = color
        self.strength = strength
        self.start_mfg_yr = start_mfg_yr
        self.end_mfg_yr = end_mfg_yr
        self.img_url = img_url
        self.img_cigar = img_cigar
        self.mfg_website = mfg_website

    def to_dict(self):
        return {
            "cigar_id": self.cigar_id,
            "cigar": self.cigar,
            "length": self.length,
            "ring_gauge": self.ring_gauge,
            "country": self.country,
            "shape": self.shape,
            "wrapper": self.wrapper,
            "binder": self.binder,
            "filler": self.filler,
            "color": self.color,
            "strength": self.strength,
            "start_mfg_yr": self.start_mfg_yr,
            "end_mfg_yr": self.end_mfg_yr,
            "img_url": self.img_url,
            "img_cigar": self.img_cigar,
            "mfg_website": self.mfg_website
        }

class Cigar_smdb(db.Model):
    cigar_id = db.Column(db.Integer, primary_key=True)
    cigar = db.Column(db.String, nullable=False)
    length = db.Column(db.String)
    ring_gauge = db.Column(db.String)
    country = db.Column(db.String)
    shape = db.Column(db.String)
    wrapper = db.Column(db.String)
    binder = db.Column(db.String)
    filler = db.Column(db.String)
    color = db.Column(db.String)
    strength = db.Column(db.String)
    start_mfg_yr = db.Column(db.String)
    end_mfg_yr = db.Column(db.String)
    img_url = db.Column(db.String)
    img_cigar = db.Column(db.String)
    mfg_website = db.Column(db.String)

    def __init__(self,cigar,length,ring_gauge,country,shape,wrapper,binder,filler,color,strength,start_mfg_yr,end_mfg_yr,img_url,img_cigar,mfg_website):
        self.cigar = cigar
        self.length = length
        self.ring_gauge = ring_gauge
        self.country = country
        self.shape = shape
        self.wrapper = wrapper
        self.binder = binder
        self.filler = filler
        self.color = color
        self.strength = strength
        self.start_mfg_yr = start_mfg_yr
        self.end_mfg_yr = end_mfg_yr
        self.img_url = img_url
        self.img_cigar = img_cigar
        self.mfg_website = mfg_website

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def saveChanges(self):
        db.session.commit()

    def updateInfo(self,cigar,length,ring_gauge,country,shape,wrapper,binder,filler,color,strength,start_mfg_yr,end_mfg_yr,img_url,img_cigar,mfg_website):
        self.cigar = cigar
        self.length = length
        self.ring_gauge = ring_gauge
        self.country = country
        self.shape = shape
        self.wrapper = wrapper
        self.binder = binder
        self.filler = filler
        self.color = color
        self.strength = strength
        self.start_mfg_yr = start_mfg_yr
        self.end_mfg_yr = end_mfg_yr
        self.img_url = img_url
        self.img_cigar = img_cigar
        self.mfg_website = mfg_website

    def to_dict(self):
        return {
            "cigar_id": self.cigar_id,
            "cigar": self.cigar,
            "length": self.length,
            "ring_gauge": self.ring_gauge,
            "country": self.country,
            "shape": self.shape,
            "wrapper": self.wrapper,
            "binder": self.binder,
            "filler": self.filler,
            "color": self.color,
            "strength": self.strength,
            "start_mfg_yr": self.start_mfg_yr,
            "end_mfg_yr": self.end_mfg_yr,
            "img_url": self.img_url,
            "img_cigar": self.img_cigar,
            "mfg_website": self.mfg_website
        }