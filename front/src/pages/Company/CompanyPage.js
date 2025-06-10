import React, { useState } from "react";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import { FaBus, FaTrain, FaPlane, FaSearch } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import { LuCircleFadingPlus } from "react-icons/lu";
import { TbCircleLetterC } from "react-icons/tb";
import "./CompanyPage.css";

const options = [
  { name: "bus", icon: <FaBus /> },
  { name: "train", icon: <FaTrain /> },
  { name: "airplane", icon: <FaPlane /> },
];

const CompanyPage = () => {
  const [selectedFlight, setSelectedFlight] = useState(null);
  const navigate = useNavigate();
  const navigateToCompanyProfile = () => {
    navigate("/toCompanyProfile");
  };
  const navigateToAddService = () => {
    navigate("/toAddService");
  };

  const flights = [
    {
      id: 1,
      from: "Tehran 06:00",
      to: "Shiraz 07:15",
      airline: "Kish Air",
      price: "180$",
      capacity: 5,
      flightNum: "IR101",
      airplane: "Airbus A320",
      details: "Gate A4, Terminal 1. Meals included.",
    },
    {
      id: 2,
      from: "Isfahan 08:45",
      to: "Tabriz 10:10",
      airline: "Kish Air",
      price: "190$",
      capacity: 3,
      flightNum: "MA202",
      airplane: "Boeing 737",
      details: "Gate B1, Terminal 2. No meals.",
    },
  ];

  const [selected, setSelected] = useState("airplane");
  return (
    <div className="cpcompany-page-container">
      <header className="search-ticket-header">
        <div className="header-left">
          <TbCircleLetterC size={27} />
          <span onClick={navigateToCompanyProfile} className="header-text">Kish Air</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span onClick={navigateToAddService} className="header-text">Add service</span>
          <LuCircleFadingPlus size={25} />
        </div>
      </header>
      <div>
        <div className="cptransport-container">
          <div className="cpsearch-bar">
            <input type="text" placeholder="......." />
            <FaSearch className="cpsearch-icon" />
          </div>

          <div className="cptransport-options">
            {options.map((opt) => (
              <div
                key={opt.name}
                className={`cptransport-option ${
                  selected === opt.name ? "active" : ""
                }`}
                onClick={() => setSelected(opt.name)}
              >
                <div className="cpicon">{opt.icon}</div>
                <div className="cplabel">{opt.name}</div>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="cpcompany-page-content">
        {flights.map((flight) => (
          <div
            key={flight.id}
            className="cpflight-summary-card"
            onClick={() =>
              setSelectedFlight(
                selectedFlight?.id === flight.id ? null : flight
              )
            }
          >
            <div className="cpflight-overview">
              <FaPlane />
              <em>{flight.from}</em> → <em>{flight.to}</em>
              <span>{flight.airline}</span>
              <span>{flight.price}</span>
            </div>
            {selectedFlight?.id === flight.id && (
              <div className="cpflight-detail-frame">
                <p>Flight Number: {flight.flightNum}</p>
                <p>Airplane: {flight.airplane}</p>
                <p>Remaining Capacity: {flight.capacity}</p>
                <p>Details: {flight.details}</p>
                <button>cancle</button>
              </div>
            )}
          </div>
        ))}
      </div>

      <footer className="cpCompanyPage-footer">
        <p>You dream it, We'll ticket it</p>
        <div className="cpsocial-icons">
          <FaFacebook size={20} />
          <FaInstagram size={20} />
          <FaXTwitter size={20} />
          <FaWhatsapp size={20} />
        </div>
      </footer>
    </div>
  );
};

export default CompanyPage;
