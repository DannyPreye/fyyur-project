from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate


# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

db = SQLAlchemy()


class Shows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey(
        'Venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'Artist.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"start time{self.start_time}"


class Venue(db.Model):
    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    looking_for_talent = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.String())
    genres = db.Column(db.String(120), nullable=False)
    venue = db.relationship('Venue', secondary=Shows.__tablename__,
                            backref=db.backref('Venue_shows', lazy=True))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    def __repr__(self):
        return f"Venue Name{self.name} Venue City{self.city}"


class Artist(db.Model):
    __tablename__ = 'Artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    looking_for_venue = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.String())
    artists = db.relationship('Artist', secondary=Shows.__tablename__,
                              backref=db.backref('Artist_shows', lazy=True))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    def __repr__(self):
        return f"Artist Name{self.name}"
