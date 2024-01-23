# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2024, Paul Cunningham'

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Unicode(255), nullable=False)
    description = db.Column(db.UnicodeText(), nullable=True)

    def __str__(self):
        return self.name
