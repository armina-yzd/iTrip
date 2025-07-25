import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Profile.css";
import { FaUserCircle, FaSuitcase, FaPlus } from "react-icons/fa";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import { useAuth } from "../AuthContext"; // ✅ Import context

const Profile = () => {
  const navigate = useNavigate();
  const { token, setToken } = useAuth(); // ✅ Get token and logout handler
  const [wallet, setWallet] = useState(0);
  const [userInfo, setUserInfo] = useState(null);
  const [showInput, setShowInput] = useState(false);
  const [customAmount, setCustomAmount] = useState("");

  const handleAddCustomAmount = () => {
    const amount = parseInt(customAmount);
    if (!isNaN(amount) && amount > 0) {
      setWallet(wallet + amount);
    }
    setCustomAmount("");
    setShowInput(false);
  };

  const logout = () => {
    setToken(null); // ✅ Clear token from memory
    navigate("/toSignup");
  };

  useEffect(() => {
    if (!token) return;

    fetch("http://iam.localhost/api/user/me", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        if (!res.ok) throw new Error("Unauthorized");
        return res.json();
      })
      .then((data) => {
        setUserInfo(data);
        setWallet(data.wallet || 0); // use wallet from backend if available
      })
      .catch((err) => {
        console.error("Failed to fetch user data:", err);
        logout();
      });
  }, [token]);

  return (
    <div>
      {/* Header */}
      <header className="UserPage_header">
        <div className="header-left" style={{ cursor: "pointer" }}>
          <FaUserCircle size={22} />
          <span className="header-text">
            {userInfo?.username || "Loading..."}
          </span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span className="header-text">my trips</span>
          <FaSuitcase size={18} />
        </div>
      </header>

      {/* Profile Content */}
      <div className="container">
        <div className="profile-info">
          <p>
            <span className="label">name :</span> {userInfo?.username || "—"}
          </p>
          <p>
            <span className="label">email :</span> {userInfo?.email || "—"}
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

          <button onClick={logout} className="logout-btn">
            log out
          </button>
        </div>
      </div>

      {/* Footer */}
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
