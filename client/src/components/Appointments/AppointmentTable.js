import React, { useEffect, useState } from 'react';
import "./AppointmentStyles.css";
import AppointmentDetail from './AppointmentDetail';

function AppointmentsTable() {
  const [appointments, setAppointments] = useState([]);
  const [selectedAppointment, setSelectedAppointment] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/appointments')
      .then(response => response.json())
      .then(data => setAppointments(data))
      .catch(error => console.error(error));
  }, []);

  const showAppointmentDetails = (appointmentId) => {
    setSelectedAppointment(appointmentId);
  };

  return (
    <div className="table-container">
      <table className="appointments-table">
        <thead>
          <tr>
            <th>Patient Name</th>
            <th>Doctor Name</th>
            <th>Date</th>
            <th>Time</th>
            <th>Comments</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {appointments.map(appointment => (
            <tr key={appointment.id}>
              <td>{appointment.patient_name}</td>
              <td>{appointment.doctor_name}</td>
              <td>{appointment.day}</td>
              <td>{appointment.time}</td>
              <td>{appointment.details}</td>
              <td>
                <button onClick={() => showAppointmentDetails(appointment.id)}>Edit</button>
                {/* Add a delete button here as well if needed */}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selectedAppointment && <AppointmentDetail appointmentId={selectedAppointment} />}
    </div>
  );
}

export default AppointmentsTable;
