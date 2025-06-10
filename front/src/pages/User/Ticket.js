import React from "react";
import "./Ticket.css";
import { FaUserCircle, FaSuitcase } from "react-icons/fa";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";

const Ticket = () => {
  const handleDownload = () => {
    alert("Ticket downloaded successfully!");
  };

  const tickets = [
    {
      from: "Tehran",
      to: "Mashhad",
      date: "2/1/2025",
      time: "22:45",
      name: "Narjes Gorji",
      flyNum: "1234",
      price: "200$",
      exporter: "Itrip",
      bookDate: "12/12/2024",
      tax: "2$",
      seat: "22",
      bookTime: "8:30",
    },
  ];

  return (
    <div>
      <header className="search-ticket-header">
        <div className="header-left">
          <FaUserCircle size={22} />
          <span className="header-text">Narjes Gorji</span>
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
              <div className="detail-row">
                <span className="detail-label">from:</span>
                <span className="detail-value">{ticket.from}</span>
              </div>
              <div className="detail-row">
                <span className="detail-label">date:</span>
                <span className="detail-value">{ticket.date}</span>
              </div>
              <div className="detail-row">
                <span className="detail-label">passenger name:</span>
                <span className="detail-value">{ticket.name}</span>
              </div>
            </div>

            <div className="ticket-section">
              <div className="detail-row">
                <span className="detail-label">to:</span>
                <span className="detail-value">{ticket.to}</span>
              </div>
              <div className="detail-row">
                <span className="detail-label">time:</span>
                <span className="detail-value">{ticket.time}</span>
              </div>
              <div className="detail-row">
                <span className="detail-label">fly num:</span>
                <span className="detail-value">{ticket.flyNum}</span>
              </div>
            </div>

            <div className="ticket-section">
              <div className="detail-row">
                <span className="detail-label">price:</span>
                <span className="detail-value">{ticket.price}</span>
              </div>
              <div className="detail-row">
                <span className="detail-label">exporter:</span>
                <span className="detail-value">{ticket.exporter}</span>
              </div>
              <div className="detail-row">
                <span className="detail-label">book date:</span>
                <span className="detail-value">{ticket.bookDate}</span>
              </div>
            </div>

            <div className="ticket-section">
              <div className="detail-row">
                <span className="detail-label">tax:</span>
                <span className="detail-value">{ticket.tax}</span>
              </div>
              <div className="detail-row">
                <span className="detail-label">sit number:</span>
                <span className="detail-value">{ticket.seat}</span>
              </div>
              <div className="detail-row">
                <span className="detail-label">book time:</span>
                <span className="detail-value">{ticket.bookTime}</span>
              </div>
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
