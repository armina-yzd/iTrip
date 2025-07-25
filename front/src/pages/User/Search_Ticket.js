import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import {
  FaUserCircle,
  FaSuitcase,
  FaPlane,
  FaTrain,
  FaBus,
} from "react-icons/fa";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import "./Search_Ticket.css";
import { useAuth } from "../AuthContext";

export default function SearchTicket() {
  const { token } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();

  const [userInfo, setUserInfo] = useState(null);
  const [services, setServices] = useState([]);
  const [selectedservice_type, setselectedservice_type] = useState('bus');

  const { from, to, start_date, tab } = location.state || {};

  const navigateMyTrips = () => navigate("/toMyTrips");
  const navigateToProfile = () => navigate("/toProfile");

  

  useEffect(() => {
    const service_type = {
      bus: "bus",
      train: "train",
      airplane: "airplane",
    };
  
    setselectedservice_type(service_type[tab]);
  }, [tab]);

  useEffect(() => {
    if (!token) return;

    // Fetch user info
    fetch("http://iam.localhost/api/user/me", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => setUserInfo(data))
      .catch(() => navigate("/login"));
  }, [token]);

  useEffect(() => {
    if (!token || !from || !to || !start_date || !tab) return;

    const endpointMap = {
      bus: "FilterBusService",
      train: "FilterTrainService",
      airplane: "FilterAirplaneService",
    };

    const selectedEndpoint = endpointMap[tab];

    fetch(
      `http://manage_services.localhost/api/filterServices/${selectedEndpoint}/?from_location=${from}&to_location=${to}&start_date=${start_date}`,
      {
        method: "GET",
        headers: { Authorization: `Bearer ${token}` },
      }
    )
      .then((res) => res.json())
      .then((data) => setServices(data))
      .catch((err) => console.error("Fetch error:", err));
  }, [token, from, to, start_date, tab]);

  return (
    <div className="search-ticket-container">
      <header className="search-ticket-header">
        <div className="header-left" onClick={navigateToProfile}>
          <FaUserCircle size={22} />
          <span className="header-text">{userInfo?.username || "..."}</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span className="header-text" onClick={navigateMyTrips}>
            my trips
          </span>
          <FaSuitcase size={18} />
        </div>
      </header>

      <div className="services-list">
        {services.length === 0 ? (
          <p style={{ padding: "1rem", textAlign: "center" }}>
            No results found for your search.
          </p>
        ) : (
          services.map((service) => (
            <div key={service.id} className="flight-card">
              <div className="flight-info">
                <FaPlane size={20} />
                <div>
                  <strong>{service.from_location}</strong> →{" "}
                  <strong>{service.to_location}</strong>
                </div>
                <div>{service.start_time}</div>
                <div>{service.vehicle_type}</div>
              </div>

              <div className="flight-actions">
                <div className="price">${service.price}</div>

                <button
                  className="choose-button"
                  onClick={() =>
                    navigate("/toPathInfo", {
                      state: {
                        serviceId: service.id,
                        serviceType: selectedservice_type.toLowerCase(),
                        price: service.price,
                      },
                    })
                  }
                >
                  Choose
                </button>

                <div className="capacity">Remain: {service.remain}</div>
              </div>
            </div>
          ))
        )}
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
}
