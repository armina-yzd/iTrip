import React, { useState, useEffect } from "react";
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
import { useAuth } from "../AuthContext";

const options = [
  { name: "bus", icon: <FaBus /> },
  { name: "train", icon: <FaTrain /> },
  { name: "airplane", icon: <FaPlane /> },
];

const CompanyPage = () => {
  const [selectedFlight, setSelectedFlight] = useState(null);
  const [selected, setSelected] = useState("airplane");
  const [company, setCompany] = useState(null);
  const [services, setServices] = useState([]);
  const { token } = useAuth();
  const navigate = useNavigate();

  const navigateToCompanyProfile = () => navigate("/toCompanyProfile");
  const navigateToAddService = () => navigate("/toAddService");

  const endpointMap = {
    airplane: "AirplaneServiceCompany",
    train: "TrainServiceCompany",
    bus: "BusServiceCompany",
    tour: "TourServiceCompany", // if needed later
  };

  useEffect(() => {
    if (!token) return;

    // get company info
    fetch("http://iam.localhost/api/company/me", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then(setCompany)
      .catch((err) => console.error("Company fetch failed", err));
  }, [token]);

  useEffect(() => {
    if (!token || !selected) return;

    const endpoint = endpointMap[selected];
    fetch(`http://manage_services.localhost/api/getServices/${endpoint}/`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then(setServices)
      .catch((err) => console.error("Service fetch failed", err));
  }, [token, selected]);

  return (
    <div className="cpcompany-page-container">
      <header className="search-ticket-header">
        <div className="header-left">
          <TbCircleLetterC size={27} />
          <span onClick={navigateToCompanyProfile} className="header-text">
            {company?.name || "Loading..."}
          </span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span onClick={navigateToAddService} className="header-text">
            Add service
          </span>
          <LuCircleFadingPlus size={25} />
        </div>
      </header>

      <div className="cptransport-container">
        <div className="cpsearch-bar">
          <input type="text" placeholder="Search..." />
          <FaSearch className="cpsearch-icon" />
        </div>

        <div className="cptransport-options">
          {options.map((opt) => (
            <div
              key={opt.name}
              className={`cptransport-option ${selected === opt.name ? "active" : ""}`}
              onClick={() => setSelected(opt.name)}
            >
              <div className="cpicon">{opt.icon}</div>
              <div className="cplabel">{opt.name}</div>
            </div>
          ))}
        </div>
      </div>

      <div className="cpcompany-page-content">
        {services.map((service) => (
          <div
            key={service.id}
            className="cpflight-summary-card"
            onClick={() =>
              setSelectedFlight(selectedFlight?.id === service.id ? null : service)
            }
          >
            <div className="cpflight-overview">
              <FaPlane />
              <em>{service.from_location} {service.takeoff_time}</em> →
              <em>{service.to_location} {service.landing_time}</em>
              <span>{service.airplane_model || service.company_name}</span>
              <span>{service.price}$</span>
            </div>
            {selectedFlight?.id === service.id && (
              <div className="cpflight-detail-frame">
                <p>Flight Number: {service.flight_num}</p>
                <p>Airplane: {service.airplane_model}</p>
                <p>Remaining Capacity: {service.capacity}</p>
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
