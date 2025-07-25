import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {
  FaUserCircle,
  FaSuitcase,
  FaPlane,
  FaTrain,
  FaBus,
} from "react-icons/fa";
import { FiSearch } from "react-icons/fi";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import "./UserPage.css";
import { useAuth } from "../AuthContext";

export default function UserPage() {
  const navigate = useNavigate();
  const { token } = useAuth();

  const [activeTab, setActiveTab] = useState("airplane");
  const [showStartCalendar, setShowStartCalendar] = useState(false);
  const [startDate, setStartDate] = useState("");
  const [currentMonth, setCurrentMonth] = useState(new Date().getMonth());
  const [currentYear, setCurrentYear] = useState(new Date().getFullYear());
  const [selectedStartDate, setSelectedStartDate] = useState(null);

  const [userInfo, setUserInfo] = useState(null);
  const [origin, setOrigin] = useState("");
  const [destination, setDestination] = useState("");

  const navigateMyTrips = () => navigate("/toMyTrips");
  const navigateToSearch_Ticket = () => {
    navigate("/toSearch_Ticket", {
      state: {
        from: origin,
        to: destination,
        start_date: startDate,
        tab: activeTab,
      },
    });
  };
  const navigateToProfile = () => navigate("/toProfile");

  const handleTabClick = (tab) => {
    setActiveTab(tab);
    setShowStartCalendar(false);
  };

  const handleStartDateClick = () => {
    setShowStartCalendar(!showStartCalendar);
  };

  const handleDateSelect = (date) => {
    const formatted = formatDate(date);
    setStartDate(formatted);
    setSelectedStartDate(date);
    setShowStartCalendar(false);
  };

  const formatDate = (date) =>
    date.toISOString().split("T")[0]; // yyyy-mm-dd

  const renderCalendar = () => {
    const firstDay = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    const days = [];

    for (let i = 0; i < firstDay; i++) {
      days.push(<div key={`empty-${i}`} className="calendar-day empty" />);
    }

    for (let i = 1; i <= daysInMonth; i++) {
      const date = new Date(currentYear, currentMonth, i);
      const isSelected =
        selectedStartDate &&
        date.toDateString() === selectedStartDate.toDateString();

      days.push(
        <div
          key={`day-${i}`}
          className={`calendar-day ${isSelected ? "selected" : ""}`}
          onClick={() => handleDateSelect(date)}
        >
          {i}
        </div>
      );
    }

    const monthNames = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];

    return (
      <div className="calendar-container">
        <div className="calendar-header">
          <button onClick={() => handleMonthChange(-1)}>&lt;</button>
          <span>{monthNames[currentMonth]} {currentYear}</span>
          <button onClick={() => handleMonthChange(1)}>&gt;</button>
        </div>
        <div className="calendar-days-grid">{days}</div>
      </div>
    );
  };

  const handleMonthChange = (dir) => {
    let newMonth = currentMonth + dir;
    let newYear = currentYear;

    if (newMonth < 0) {
      newMonth = 11;
      newYear--;
    } else if (newMonth > 11) {
      newMonth = 0;
      newYear++;
    }

    setCurrentMonth(newMonth);
    setCurrentYear(newYear);
  };

  useEffect(() => {
    if (!token) return;

    fetch("http://iam.localhost/api/user/me", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => setUserInfo(data))
      .catch((err) => {
        console.error("User fetch failed:", err);
        navigate("/login");
      });
  }, [token]);

  return (
    <div className="Userpage-container">
      <header className="UserPage_header">
        <div className="header-left" onClick={navigateToProfile}>
          <FaUserCircle size={22} />
          <span className="header-text">{userInfo?.username || "..."}</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span onClick={navigateMyTrips} className="header-text">my trips</span>
          <FaSuitcase size={18} />
        </div>
      </header>

      <div className="nav-tabs">
        <div className="tab-div">
          {["bus", "train", "airplane", "tour"].map((t) => (
            <div
              key={t}
              className={`tab-item ${activeTab === t ? "active" : ""}`}
              onClick={() => handleTabClick(t)}
            >
              {t === "bus" && <FaBus className="tab-icon" />}
              {t === "train" && <FaTrain className="tab-icon" />}
              {t === "airplane" && <FaPlane className="tab-icon" />}
              <span>{t}</span>
            </div>
          ))}
        </div>

        <div className="search-box">
          <input
            placeholder="origin"
            value={origin}
            onChange={(e) => setOrigin(e.target.value)}
          />
          <input
            placeholder="destination"
            value={destination}
            onChange={(e) => setDestination(e.target.value)}
          />
          <div className="date-input-container">
            <input
              placeholder="start date"
              value={startDate}
              onClick={handleStartDateClick}
              readOnly
            />
            {showStartCalendar && renderCalendar()}
          </div>
          <button className="search-button" onClick={navigateToSearch_Ticket}>
            <FiSearch />
            <span>search</span>
          </button>
        </div>
      </div>

      <p className="description">
        Looking for the best time to buy tickets? We've got you covered.
      </p>

      <footer className="UserPage_footer">
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
