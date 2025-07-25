import React, { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../AuthContext";
import {
  FaUserCircle,
  FaSuitcase,
  FaPlane,
  FaUserFriends,
  FaTrash,
} from "react-icons/fa";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import "./PathInfo.css";

const PathInfo = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { token } = useAuth();

  const [passengers, setPassengers] = useState([
    { id: Date.now(), first_name: "", last_name: "", gender: "", national_id: "" },
  ]);

  const [paymentMethod] = useState("wallet");

  const serviceId = location?.state?.serviceId;
  const serviceType = location?.state?.serviceType;
  const price = location?.state?.price;

  if (!serviceId || !serviceType || !price) {
    return (
      <div className="error-page">
        <h2>Missing booking information.</h2>
        <p>Please return to the previous page and select a ticket again.</p>
        <button onClick={() => navigate("/toUserPage")}>Back to Home</button>
      </div>
    );
  }

  const handleAddPassenger = () => {
    setPassengers([
      ...passengers,
      { id: Date.now(), first_name: "", last_name: "", gender: "", national_id: "" },
    ]);
  };

  const handleDeletePassenger = (id) => {
    setPassengers(passengers.filter((p) => p.id !== id));
  };

  const handleChange = (id, field, value) => {
    setPassengers((prev) =>
      prev.map((p) => (p.id === id ? { ...p, [field]: value } : p))
    );
  };

  const handleSubmit = async () => {
    try {
      const ticket_num = passengers.length;
      const paid = ticket_num * price;
      console.log(serviceType)
      const bodyData ={
          discount_id: 0,
          service_type: serviceType,
          paid,
          ticket_num,
          purchase_method: paymentMethod,
      };
      console.log(bodyData);
      // 1. Create Payment
      const paymentRes = await fetch(`http://user_ticket.localhost/api/Ticket/payment/${serviceId}`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          discount_id: 0,
          service_type: serviceType,
          paid,
          ticket_num,
          purchase_method: paymentMethod,
        }),
      });

      if (!paymentRes.ok) throw new Error("Payment failed");
      const paymentData = await paymentRes.json();

      // 2. Create Tickets
      const buyTicketData = passengers.map((p, i) => ({
        passenger_create: {
          gender: p.gender.toLowerCase(),
          first_name: p.first_name,
          last_name: p.last_name,
          national_id: p.national_id,
        },
        ticket_create: {
          ticket_serial: 1000 + i,
          tracking_code: 5000 + i,
          seat_num: i + 1,
        },
      }));

      const ticketRes = await fetch(
        `http://user_ticket.localhost/api/Ticket/buyTicket/${serviceId}?payment_id=${paymentData.id}`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(buyTicketData),
        }
      );

      if (!ticketRes.ok) throw new Error("Ticket purchase failed");

      const ticketResults = await ticketRes.json();
      navigate("/toTicket", { state: { tickets: ticketResults } });
    } catch (err) {
      console.error("Purchase error:", err);
      alert("An error occurred during ticket purchase.");
    }
  };

  return (
    <div className="search-ticket-container">
      <header className="search-ticket-header">
        <div className="header-left">
          <FaUserCircle size={22} />
          <span className="header-text">Passenger Info</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span className="header-text">my trips</span>
          <FaSuitcase size={18} />
        </div>
      </header>

      <div className="passenger-container">
        {passengers.map((p, i) => (
          <div className="form-box" key={p.id}>
            <div className="form-header">
              <FaPlane className="form-icon" />
              <span>Passenger {i + 1}</span>
              <button className="delete-btn" onClick={() => handleDeletePassenger(p.id)}>
                <FaTrash />
              </button>
            </div>
            <div className="form-inputs">
              <input
                type="text"
                placeholder="First Name"
                value={p.first_name}
                onChange={(e) => handleChange(p.id, "first_name", e.target.value)}
              />
              <input
                type="text"
                placeholder="Last Name"
                value={p.last_name}
                onChange={(e) => handleChange(p.id, "last_name", e.target.value)}
              />
              <input
                type="text"
                placeholder="Gender (male/female)"
                value={p.gender}
                onChange={(e) => handleChange(p.id, "gender", e.target.value)}
              />
              <input
                type="text"
                placeholder="National ID"
                value={p.national_id}
                onChange={(e) => handleChange(p.id, "national_id", e.target.value)}
              />
            </div>
          </div>
        ))}

        <div className="bottom-bar">
          <button className="add-btn" onClick={handleAddPassenger}>
            <FaUserFriends className="icon" />
            Add Passenger
          </button>
          <button className="done-btn" onClick={handleSubmit}>Done</button>
        </div>
      </div>

      <footer className="search-ticket-footer">
        <p>You dream it, We'll ticket it</p>
        <div className="social-icons">
          <FaFacebook size={20} />
          <FaInstagram size={20} />
          <FaXTwitter size={20} />
          <FaWhatsapp size={20} />
        </div>
      </footer>
    </div>
  );
};

export default PathInfo;
