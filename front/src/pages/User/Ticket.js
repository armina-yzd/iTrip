import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "./Ticket.css";
import { FaUserCircle, FaSuitcase } from "react-icons/fa";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";

const Ticket = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const tickets = location?.state?.tickets || [];

  if (!tickets.length) {
    return (
      <div className="ticket-container">
        <h2>No ticket found</h2>
        <button onClick={() => navigate("/toUserPage")}>Back to home</button>
      </div>
    );
  }

  const handleDownload = () => {
    alert("Ticket downloaded successfully!");
  };

  return (
    <div>
      <header className="search-ticket-header">
        <div className="header-left">
          <FaUserCircle size={22} />
          <span className="header-text">Your Tickets</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span className="header-text">my trips</span>
          <FaSuitcase size={18} />
        </div>
      </header>

      {tickets.map((ticket, index) => (
        <div className="ticket-container" key={index}>
          <div className="ticket-header">
            <h1>Flight Ticket</h1>
          </div>

          <div className="ticket-details">
            <div className="ticket-section">
              <p><strong>Name:</strong> {ticket.passenger_response.first_name} {ticket.passenger_response.last_name}</p>
              <p><strong>Gender:</strong> {ticket.passenger_response.gender}</p>
              <p><strong>National ID:</strong> {ticket.passenger_response.national_id}</p>
            </div>
            <div className="ticket-section">
              <p><strong>Seat:</strong> {ticket.ticket_response.seat_num}</p>
              <p><strong>Serial:</strong> {ticket.ticket_response.ticket_serial}</p>
              <p><strong>Tracking:</strong> {ticket.ticket_response.tracking_code}</p>
            </div>
          </div>

          <button className="download-btn" onClick={handleDownload}>
            Download Ticket
          </button>
        </div>
      ))}

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

export default Ticket;
