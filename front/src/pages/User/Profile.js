import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Profile.css";
import {
  FaUserCircle,
  FaSuitcase,
  FaPlane,
  FaPlus,
} from "react-icons/fa";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";

const Profile = () => {
  const navigate = useNavigate();
  const [tab, setTab] = useState("profile");
  const [wallet, setWallet] = useState(2000);
  const [showInput, setShowInput] = useState(false);
  const [customAmount, setCustomAmount] = useState("");
  const navigateToSignup = () => {
    navigate("/toSignup");
  };

  const handleAddCustomAmount = () => {
    const amount = parseInt(customAmount);
    if (!isNaN(amount) && amount > 0) {
      setWallet(wallet + amount);
    }
    setCustomAmount("");
    setShowInput(false);
  };
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
      {<div className="dots">................</div>}
      <div className="to">
        <em>{flightData.to}</em>
      </div>
    </div>
  );

  return (
    <div>
      <header className="UserPage_header">
        <div className="header-left" style={{ cursor: "pointer" }}>
          <FaUserCircle size={22} />
          <span className="header-text">Narjes Gorji</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span className="header-text">my trips</span>
          <FaSuitcase size={18} />
        </div>
      </header>

      <div className="container">
        <div className="tabs">
          <span
            className={tab === "profile" ? "tab active" : "tab"}
            onClick={() => setTab("profile")}
          >
            profile
          </span>
          <span
            className={tab === "notification" ? "tab active" : "tab"}
            onClick={() => setTab("notification")}
          >
            notification
          </span>
        </div>

        {tab === "profile" ? (
          <div className="profile-info">
            <p>
              <span className="label">name :</span> Narjes Gorji
            </p>
            <p>
              <span className="label">number :</span> 0902098....
            </p>
            <p>
              <span className="label">wallet :</span> {wallet}$
            </p>

            {!showInput ? (
              <button className="wallet-btn" onClick={() => setShowInput(true)}>
                <FaPlus /> increase wallet
              </button>
            ) : (
              <div className="wallet-input-wrapper">
                <input
                  type="number"
                  value={customAmount}
                  onChange={(e) => setCustomAmount(e.target.value)}
                  placeholder="Amount"
                  className="wallet-input"
                />
                <button className="done-btn" onClick={handleAddCustomAmount}>
                  Done
                </button>
              </div>
            )}

            <button onClick={navigateToSignup} className="logout-btn">
              log out
            </button>
          </div>
        ) : (
          <div className="notification-box">
            <div className="flight-card">
              <div className="flight-info">
                <div className="flight-icon">
                  <FaPlane size={20} />
                </div>
                {renderFlightTimes()}
                <div className="airline">{flightData.airline}</div>
              </div>

              <div className="flight-actions">
                <button className="choose-button">cancelled</button>
              </div>
            </div>
          </div>
        )}
      </div>

      <footer className="Profile_footer">
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

export default Profile;
