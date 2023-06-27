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
    posts = db.relationship('BlogPost', backref='author_doctor', lazy=True, foreign_keys='BlogPost.doctor_id')

class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    name = db.Column(db.String)
    dob = db.Column(db.DateTime)
    email = db.Column(db.String)
    password = db.Column(db.String)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    day = db.Column(db.Date)
    time = db.Column(db.Time)
    details = db.Column(db.String)  # New column for comments/details

    patient = db.relationship('Patient', backref='appointments', lazy=True)
    doctor = db.relationship('Doctor', backref='appointments', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'patient_name': self.patient.name,  # Include patient name
            'doctor_id': self.doctor_id,
            'doctor_name': self.doctor.name,  # Include doctor name
            'day': self.day.strftime('%Y-%m-%d'),
            'time': self.time.strftime('%H:%M'),
            'details': self.details
        }

class BlogPost(db.Model):
    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, db.ForeignKey('doctors.name'))
    title = db.Column(db.String)
    content = db.Column(db.String)

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    doctor = db.relationship('Doctor', backref='blog_posts', lazy=True, foreign_keys='BlogPost.doctor_id')

