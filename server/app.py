from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
import datetime

from models import db, Patient, Appointment, Doctor, Comment

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class Patients(Resource):
    def get(self):
        patients = [u.to_dict(only=("id", "name")) for u in Patient.query.all()]
        return patients, 200

    def post(self):
        try:
            new_patient = Patient(
                username=request.json['username'],
                name=request.json['name'],
                dob=request.json['dob'],
                email=request.json['email'],
                password=request.json['password'],
                doctor=Doctor.query.get(request.json['doctor_id'])
            )
            db.session.add(new_patient)
            db.session.commit()
            return new_patient.to_dict(only=("id", "name")), 201
        except:
            return {"error": "400: Validation error"}, 400

class Comments(Resource):
    def post(self):
        try:
            patient_id = request.json['patient_id']
            comment_text = request.json['comment_text']

            patient = Patient.query.get(patient_id)
            if patient is None:
                return {"error": "404: Patient not found"}, 404

            comment = Comment(text=comment_text, doctor=patient.doctor, patient=patient)
            db.session.add(comment)
            db.session.commit()

            return comment.to_dict(), 201
        except:
            return {"error": "400: Validation error"}, 400

@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.json
    patient_id = data['patient_id']
    text = data['text']

    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({'error': 'Patient not found'}), 404

    comment = Comment(text=text, patient_id=patient_id, doctor_id=patient.doctor_id)
    db.session.add(comment)
    db.session.commit()

    return jsonify(comment.to_dict()), 201


api.add_resource(Patients, "/patients")
api.add_resource(Comments, "/comments")


class DoctorResource(Resource):
    def get(self):
        doctors = Doctor.query.all()
        return [doctor.to_dict() for doctor in doctors]


api.add_resource(DoctorResource, "/doctors")


@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if request.method == 'GET':
        appointments = Appointment.query.all()
        return jsonify([appointment.to_dict() for appointment in appointments])

    elif request.method == 'POST':
        data = request.json
        patient_id = data['patient_id']
        doctor_id = data['doctor_id']
        day = datetime.datetime.strptime(data['day'], '%Y-%m-%d').date()
        time = datetime.datetime.strptime(data['time'], '%H:%M').time()

        patient = Patient.query.get(patient_id)
        doctor = Doctor.query.get(doctor_id)

        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        if not doctor:
            return jsonify({'error': 'Doctor not found'}), 404

        appointment = Appointment(patient=patient, doctor=doctor, day=day, time=time)
        db.session.add(appointment)
        db.session.commit()

        return jsonify(appointment.to_dict()), 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)

