from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Doctor(db.Model, SerializerMixin):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    patients = db.relationship('Patient', backref='doctor', foreign_keys='Patient.doctor_id')
    comments = db.relationship('Comment', backref='doctor', foreign_keys='Comment.doctor_id')

class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    name = db.Column(db.String)
    dob = db.Column(db.DateTime)
    email = db.Column(db.String)
    password = db.Column(db.String)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    comments = db.relationship('Comment', backref='patient', lazy=True)

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    day = db.Column(db.Date)
    time = db.Column(db.Time)

    patient = db.relationship('Patient', backref='appointments', lazy=True)
    doctor = db.relationship('Doctor', backref='appointments', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'day': self.day.strftime('%Y-%m-%d'),
            'time': self.time.strftime('%H:%M')
        }
