import React, { useState } from "react";
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
import "./HomePage.css";

export default function HomePage() {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState("airplane");
  const [showStartCalendar, setShowStartCalendar] = useState(false);
  const [showEndCalendar, setShowEndCalendar] = useState(false);
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [currentMonth, setCurrentMonth] = useState(new Date().getMonth());
  const [currentYear, setCurrentYear] = useState(new Date().getFullYear());
  const [selectedStartDate, setSelectedStartDate] = useState(null);
  const [selectedEndDate, setSelectedEndDate] = useState(null);

  const navigateToSignup = () => {
    navigate("/tosignup");
  };


  const handleTabClick = (tab) => {
    setActiveTab(tab);
    setShowStartCalendar(false);
    setShowEndCalendar(false);
  };

  const handleStartDateClick = () => {
    setShowStartCalendar(!showStartCalendar);
    setShowEndCalendar(false);
  };

  const handleDateSelect = (date, isStartDate) => {
    const formattedDate = formatDate(date);

    if (isStartDate) {
      setStartDate(formattedDate);
      setSelectedStartDate(date);
      setShowStartCalendar(false);

      if (selectedEndDate && date > selectedEndDate) {
        setEndDate("");
        setSelectedEndDate(null);
      }
    } else {
      setEndDate(formattedDate);
      setSelectedEndDate(date);
      setShowEndCalendar(false);
    }
  };

  const formatDate = (date) => {
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
    });
  };

  const renderCalendar = (isStart) => {
    const firstDay = new Date(currentYear, currentMonth, 1);
    const lastDay = new Date(currentYear, currentMonth + 1, 0);
    const daysInMonth = lastDay.getDate();
    const startingDay = firstDay.getDay();

    const days = [];
    let day = 1;

    for (let i = 0; i < startingDay; i++) {
      days.push(<div key={`empty-${i}`} className="calendar-day empty"></div>);
    }

    for (let i = 1; i <= daysInMonth; i++) {
      const date = new Date(currentYear, currentMonth, i);
      const isSelected =
        (isStart &&
          selectedStartDate &&
          date.toDateString() === selectedStartDate.toDateString()) ||
        (!isStart &&
          selectedEndDate &&
          date.toDateString() === selectedEndDate.toDateString());
      const isDisabled =
        (isStart && selectedEndDate && date > selectedEndDate) ||
        (!isStart && selectedStartDate && date < selectedStartDate);

      days.push(
        <div
          key={`day-${i}`}
          className={`calendar-day ${isSelected ? "selected" : ""} ${
            isDisabled ? "disabled" : ""
          }`}
          onClick={
            !isDisabled ? () => handleDateSelect(date, isStart) : undefined
          }
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
          <button
            onClick={() => handleMonthChange(-1)}
            className="calendar-nav-button"
          >
            &lt;
          </button>
          <span>
            {monthNames[currentMonth]} {currentYear}
          </span>
          <button
            onClick={() => handleMonthChange(1)}
            className="calendar-nav-button"
          >
            &gt;
          </button>
        </div>
        <div className="calendar-weekdays">
          {["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].map((day) => (
            <div key={day}>{day}</div>
          ))}
        </div>
        <div className="calendar-days-grid">{days}</div>
      </div>
    );
  };

  const handleMonthChange = (direction) => {
    let newMonth = currentMonth + direction;
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

  return (
    <div className="homepage-container">
      {/* Header */}
      <header className="HomePage_header">
        <div
          className="header-left"
          onClick={navigateToSignup}
          style={{ cursor: "pointer" }}
        >
          <FaUserCircle size={22} />
          <span className="header-text">login-signup</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span className="header-text">my trips</span>
          <FaSuitcase size={18} />
        </div>
      </header>

      {/* Navigation Tabs */}
      <div className="nav-tabs">
        <div className="tab-div">
          <div
            className={`tab-item ${activeTab === "bus" ? "active" : ""}`}
            onClick={() => handleTabClick("bus")}
          >
            <FaBus className="tab-icon" />
            <span>bus</span>
          </div>
          <div
            className={`tab-item ${activeTab === "train" ? "active" : ""}`}
            onClick={() => handleTabClick("train")}
          >
            <FaTrain className="tab-icon" />
            <span>train</span>
          </div>
          <div
            className={`tab-item ${activeTab === "airplane" ? "active" : ""}`}
            onClick={() => handleTabClick("airplane")}
          >
            <FaPlane className="tab-icon" />
            <span>airplane</span>
          </div>
        </div>

        {/* Search Fields */}
        <div className="search-box">
         
          <input placeholder="origin" />
          <input placeholder="destination" />

          <div className="date-input-container">
            <input
              placeholder="start"
              value={startDate}
              onClick={handleStartDateClick}
              readOnly
            />
            {showStartCalendar && renderCalendar(true)}
          </div>


          {/* <input placeholder="p count" /> */}
          <button className="search-button" onClick={navigateToSignup}>
            <FiSearch />
            <span>search</span>
          </button>
        </div>
      </div>

      {/* Description */}
      <p className="description">
        Looking for the best time to buy airline tickets to get a cheap flight
        to everywhere? We've got you covered anytime anywhere. <br /> Here's how
        to find the best deal for flight booking no matter where you want to go
        in the world.
      </p>

      {/* Travel Blog CTA */}
      {/* <div className="blog-button-container">
        <button className="blog-button">
          <span>travel blog</span>
          <p>share your experience</p>
        </button>
      </div> */}

      {/* Footer */}
      <footer className="HomePage_footer">
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
