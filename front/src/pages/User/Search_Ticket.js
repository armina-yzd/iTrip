import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { FaUserCircle, FaSuitcase, FaPlane } from "react-icons/fa";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import { useAuth } from "../AuthContext";
import "./Search_Ticket.css";

const SearchTicket = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { token } = useAuth();

  const { from, to, start_date, tab } = location.state || {};
  const [results, setResults] = useState([]);
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);
  const [activeSort, setActiveSort] = useState("suggestion");

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  useEffect(() => {
    if (!token || !tab) return;

    const endpointMap = {
      airplane: "FilterAirplaneService",
      train: "FilterTrainService",
      bus: "FilterBusService",
      tour: "FilterTourService",
    };

    const endpoint = endpointMap[tab];

    fetch(`http://iam.localhost/api/filterServices/${endpoint}/?from_location=${from}&to_location=${to}&start_date=${start_date}`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => {
        if (!res.ok) throw new Error("Fetch failed");
        return res.json();
      })
      .then((data) => setResults(data))
      .catch((err) => {
        console.error("Failed to fetch services:", err);
      });
  }, [from, to, start_date, tab, token]);

  return (
    <div className="search-ticket-container">
      <header className="search-ticket-header">
        <div className="header-left">
          <FaUserCircle size={22} />
          <span className="header-text">Welcome</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span className="header-text">my trips</span>
          <FaSuitcase size={18} />
        </div>
      </header>

      <div className="sort-bar">
        <span>sort:</span>
        <div className="sort-options">
          {["suggestion", "sooner", "cheapest", "expensivest"].map((opt) => (
            <button
              key={opt}
              className={activeSort === opt ? "active" : ""}
              onClick={() => setActiveSort(opt)}
            >
              {opt}
            </button>
          ))}
        </div>
      </div>

      {results.map((item, index) => (
        <div className="flight-card" key={index}>
          <div className="flight-info">
            <div className="flight-icon"><FaPlane size={20} /></div>
            <div className="flight-times">
              <div className="from"><em>{item.from_location} {item.takeoff_time}</em></div>
              {!isMobile && <div className="dots">................</div>}
              <div className="to"><em>{item.to_location} {item.landing_time}</em></div>
            </div>
            <div className="airline">{item.airplane_model || item.company_name}</div>
          </div>

          <div className="flight-actions">
            <div className="price">{item.price}$</div>
            <button onClick={() => navigate("/toPathInfo")} className="choose-button">choose</button>
            <div className="capacity">capacity: {item.capacity}</div>
          </div>
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

export default SearchTicket;
