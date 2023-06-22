from flask import Flask
from faker import Faker
from datetime import datetime
from app import app, db, Patient, Appointment, Doctor

fake = Faker()

with app.app_context():
    doctor = Doctor(id=1, name="Dr. Farley", email="drfarley@example.com", password="password")
    db.session.add(doctor)
    db.session.commit()

    for i in range(5):
        username = fake.user_name()
        name = fake.name()
        dob = fake.date_of_birth()
        password = fake.password()
        email = fake.email()

        patient = Patient(username=username, name=name, dob=dob, password=password, email=email, doctor=doctor)
        db.session.add(patient)
        db.session.commit()

        for j in range(3):
            day = fake.date_between(start_date='today', end_date='+30d')
            day_str = day.strftime('%Y-%m-%d')
            appointment_time = fake.time(pattern='%H:%M')
            appointment_datetime = datetime.strptime(f"{day_str} {appointment_time}", '%Y-%m-%d %H:%M')

            details = fake.paragraph()

            appointment = Appointment(patient=patient, doctor=doctor, day=appointment_datetime.date(), time=appointment_datetime.time(), details=details)
            db.session.add(appointment)
            db.session.commit()
