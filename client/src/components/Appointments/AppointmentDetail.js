import React, { useState, useEffect } from 'react';

const AppointmentDetail = ({ appointmentId }) => {
  const [appointment, setAppointment] = useState(null);
  const [day, setDay] = useState('');
  const [time, setTime] = useState('');
  const [details, setDetails] = useState('');
  const [doctorId, setDoctorId] = useState('');

  useEffect(() => {
    fetchAppointment();
  }, []);

  const fetchAppointment = async () => {
    try {
      const response = await fetch(`http://localhost:5555/appointments/${appointmentId}`);
      if (!response.ok) {
        throw new Error('Error fetching appointment');
      }
      const data = await response.json();
      setAppointment(data);
      setDay(data.day);
      setTime(data.time);
      setDetails(data.details);
      setDoctorId(data.doctor_id);
    } catch (error) {
      console.error('Error fetching appointment:', error);
    }
  };

  const updateAppointment = async () => {
    try {
      const response = await fetch(`http://localhost:5555/appointments/${appointmentId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          day,
          time,
          details,
          doctor_id: doctorId
        })
      });
      if (!response.ok) {
        throw new Error('Error updating appointment');
      }
      alert('Appointment updated successfully!');
    } catch (error) {
      console.error('Error updating appointment:', error);
    }
  };

  const deleteAppointment = async () => {
    try {
      const response = await fetch(`http://localhost:5555/appointments/${appointmentId}`, {
        method: 'DELETE'
      });
      if (!response.ok) {
        throw new Error('Error deleting appointment');
      }
      alert('Appointment deleted successfully!');
    } catch (error) {
      console.error('Error deleting appointment:', error);
    }
  };

  if (!appointment) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Appointment Details</h2>
      <div>
        <label>Date:</label>
        <input type="date" value={day} onChange={e => setDay(e.target.value)} />
      </div>
      <div>
        <label>Time:</label>
        <input type="time" value={time} onChange={e => setTime(e.target.value)} />
      </div>
      <div>
        <label>Details:</label>
        <textarea value={details} onChange={e => setDetails(e.target.value)} />
      </div>
      <div>
        <label>Doctor ID:</label>
        <input type="number" value={doctorId} onChange={e => setDoctorId(e.target.value)} />
      </div>
      <button onClick={updateAppointment}>Update</button>
      <button onClick={deleteAppointment}>Delete</button>
    </div>
  );
};

export default AppointmentDetail;
