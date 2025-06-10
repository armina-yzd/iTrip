import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { FaUserCircle, FaSuitcase, FaPlane } from "react-icons/fa";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import "./Search_Ticket.css";

const SearchTicket = () => {
  const navigate = useNavigate();
  const [activeSort, setActiveSort] = useState("suggestion");
  const [showInfo, setShowInfo] = useState(false);
  const [showRules, setShowRules] = useState(false);
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);
  const navigateToPathInfo = () => {
    navigate("/toPathInfo");
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
    flightNum: "1234",
    airplane: "boeing MD-82",
    rules: [
      { percentage: "100%", text: "from the 12 PM before flight onwards" },
      {
        percentage: "85%",
        text: "from the 12 PM of two days before flight to the 12 PM of 1 day before the flight",
      },
      {
        percentage: "70%",
        text: "from the 12 PM of 3 days before the flight to the 12 PM of 2 days before the flight",
      },
      {
        percentage: "50%",
        text: "from issuing the ticket to the 12 PM of 3 days before the flight",
      },
    ],
  };

  const sortOptions = ["suggestion", "sooner", "cheapest", "expensivest"];

  const navigateToSignup = () => navigate("/tosignup");
  const toggleInfo = () => {
    setShowInfo(!showInfo);
    setShowRules(false);
  };
  const toggleRules = () => {
    setShowRules(!showRules);
    setShowInfo(false);
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
        <div className="header-left" onClick={navigateToSignup}>
          <FaUserCircle size={22} />
          <span className="header-text">Narjes Gorji</span>
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
          {sortOptions.map((option) => (
            <button
              key={option}
              className={activeSort === option ? "active" : ""}
              onClick={() => setActiveSort(option)}
            >
              {option}
            </button>
          ))}
        </div>
      </div>

      <div className="flight-card">
        <div className="flight-info">
          <div className="flight-icon">
            <FaPlane size={20} />
          </div>
          {renderFlightTimes()}
          <div className="airline">{flightData.airline}</div>
          <div className="extra-links">
            <button onClick={toggleInfo}>information</button>
            <button onClick={toggleRules}>rules</button>
          </div>
        </div>

        <div className="flight-actions">
          <div className="price">{flightData.price}</div>
          <button onClick={navigateToPathInfo}  className="choose-button">choose</button>
          <div className="capacity">capacity remain: {flightData.capacity}</div>
        </div>
      </div>

      {showInfo && (
        <div className="info-dropdown">
          <div className="info-content">
            <p>flight num : {flightData.flightNum}</p>
            <p>airplane : {flightData.airplane}</p>
          </div>
        </div>
      )}

      {showRules && (
        <div className="rules-dropdown">
          <div className="rules-content">
            {flightData.rules.map((rule, index) => (
              <div key={index} className="rule-item">
                <span className="percentage">{rule.percentage}</span>
                <span className="rule-text">{rule.text}</span>
              </div>
            ))}
          </div>
        </div>
      )}

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
