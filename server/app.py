from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
import datetime

from models import db, Patient, Appointment, Doctor, BlogPost

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
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
                username=request.json["username"],
                name=request.json["name"],
                dob=request.json["dob"],
                email=request.json["email"],
                password=request.json["password"],
                doctor=Doctor.query.get(request.json["doctor"]),
            )
            db.session.add(new_patient)
            db.session.commit()
            return new_patient.to_dict(only=("id", "name")), 201
        except:
            return {"error": "400: Validation error"}, 400


api.add_resource(Patients, "/patients")


class DoctorResource(Resource):
    def get(self):
        doctors = Doctor.query.all()
        return [doctor.to_dict() for doctor in doctors]


api.add_resource(DoctorResource, "/doctors")


class Appointments(Resource):
    def get(
        self, appointment_id=None
    ):  # Add appointment_id parameter with a default value of None
        if appointment_id is None:
            appointments = Appointment.query.all()
            return [appointment.to_dict() for appointment in appointments]
        else:
            appointment = Appointment.query.get(appointment_id)
            if not appointment:
                return {"error": "Appointment not found"}, 404
            return appointment.to_dict()

    def post(self):
        data = request.json
        patient_id = data["patient_id"]
        doctor_id = data["doctor_id"]
        day = datetime.datetime.strptime(data["day"], "%Y-%m-%d").date()
        time = datetime.datetime.strptime(data["time"], "%H:%M").time()
        details = data["details"]

        patient = Patient.query.get(patient_id)
        doctor = Doctor.query.get(doctor_id)

        if not patient:
            return {"error": "Patient not found"}, 404
        if not doctor:
            return {"error": "Doctor not found"}, 404

        appointment = Appointment(
            patient=patient, doctor=doctor, day=day, time=time, details=details, doctor_id=doctor.id
        )
        db.session.add(appointment)
        db.session.commit()

        return appointment.to_dict(), 201

    def put(self, appointment_id):
        data = request.json
        appointment = Appointment.query.get(appointment_id)

        if not appointment:
            return {"error": "Appointment not found"}, 404

        appointment.day = datetime.datetime.strptime(data["day"], "%Y-%m-%d").date()
        appointment.time = datetime.datetime.strptime(data["time"], "%H:%M").time()
        appointment.doctor_id = data["doctor_id"]
        appointment.details = data["details"]

        db.session.commit()

        return appointment.to_dict(), 200

    def delete(self, appointment_id):
        appointment = Appointment.query.get(appointment_id)

        if not appointment:
            return {"error": "Appointment not found"}, 404

        db.session.delete(appointment)
        db.session.commit()

        return {"message": "Appointment deleted"}, 200


api.add_resource(Appointments, "/appointments", "/appointments/<int:appointment_id>")

class BlogPosts(Resource):
    def get(self):
        posts = BlogPost.query.all()
        return [post.to_dict() for post in posts]

    def post(self):
        data = request.json
        author = data['name']
        title = data['title']
        content = data['content']

        doctor_id = data['doctor_id']
        doctor = Doctor.query.get(doctor_id)
        if not doctor:
            return {'error': 'Doctor not found'}, 404

        post = BlogPost(doctor=doctor.posts, author_doctor=author, title=title, content=content, doctor_id=doctor_id)
        db.session.add(post)
        db.session.commit()

        return post.to_dict(), 201

    def put(self, post_id):
        data = request.json
        post = BlogPost.query.get(post_id)

        if not post:
            return {'error': 'Blog post not found'}, 404

        post.author_doctor = data['name']
        post.title = data['title']
        post.content = data['content']
        db.session.commit()

        return post.to_dict(), 200

    def delete(self, post_id):
        post = BlogPost.query.get(post_id)

        if not post:
            return {'error': 'Blog post not found'}, 404

        db.session.delete(post)
        db.session.commit()

        return {'message': 'Blog post deleted'}, 200


api.add_resource(BlogPosts, "/blog/posts", "/blog/posts/<int:post_id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
