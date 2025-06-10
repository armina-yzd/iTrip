import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {
  FaUserCircle,
  FaSuitcase,
  FaPlane,
  FaUser,
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

const SearchTicket = () => {
  const navigate = useNavigate();
  const [activeSort, setActiveSort] = useState("suggestion");
  const [showInfo, setShowInfo] = useState(false);
  const [showRules, setShowRules] = useState(false);
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);

  const [passengers, setPassengers] = useState([{ id: Date.now() }]);

  const handleAddPassenger = () => {
    setPassengers([...passengers, { id: Date.now() }]);
  };
  const handleDeletePassenger = (id) => {
    setPassengers(passengers.filter((p) => p.id !== id));
  };

  const navigateToTicket = () => {
    navigate("/toTicket");
  };

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
      if (window.innerWidth < 768) {
        setShowInfo(false);
        setShowRules(false);
      }
    };

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const flightData = {
    from: "Tehran 22:45",
    to: "Mashhad 23:55",
    airline: "kish air",
    price: "200$",
    capacity: "10",
  };

  const renderFlightTimes = () => (
    <div className="flight-times">
      <div className="from">
        <em>{flightData.from}</em>
      </div>
      {!isMobile && <div className="dots">................</div>}
      <div className="to">
        <em>{flightData.to}</em>
      </div>
    </div>
  );

  return (
    <div className="search-ticket-container">
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

      <div className="flight-card">
        <div className="flight-info">
          <div className="flight-icon">
            <FaPlane size={20} />
          </div>
          {renderFlightTimes()}
          <div className="airline">{flightData.airline}</div>
        </div>

        <div className="flight-actions">
          <div className="price">{flightData.price}</div>
          <div className="capacity">capacity remain: {flightData.capacity}</div>
        </div>
      </div>
      <div className="passenger-container">
      {passengers.map((passenger, index) => (
        <div className="form-box" key={passenger.id}>
          <div className="form-header">
            <FaUser className="form-icon" />
            <span>passenger info {index + 1}</span>
            <button
              className="delete-btn"
              onClick={() => handleDeletePassenger(passenger.id)}
              title="Delete passenger"
            >
              <FaTrash />
            </button>
          </div>
          <div className="form-inputs">
            <input type="text" placeholder="name" />
            <input type="text" placeholder="last name" />
            <input type="text" placeholder="gender" />
            <input type="text" placeholder="national id" />
          </div>
        </div>
      ))}

      <div className="bottom-bar">
        <button className="add-btn" onClick={handleAddPassenger}>
          <FaUserFriends className="icon" />
          new passenger
        </button>
        <button className="done-btn" onClick={navigateToTicket}>Done</button>
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

export default SearchTicket;
