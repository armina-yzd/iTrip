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
import "./UserPage.css";

export default function UserPage() {
  const navigate = useNavigate();
  const [showTripType, setShowTripType] = useState(false);
  const [tripType, setTripType] = useState("one way");
  const [activeTab, setActiveTab] = useState("airplane");
  const [showStartCalendar, setShowStartCalendar] = useState(false);
  const [showEndCalendar, setShowEndCalendar] = useState(false);
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [currentMonth, setCurrentMonth] = useState(new Date().getMonth());
  const [currentYear, setCurrentYear] = useState(new Date().getFullYear());
  const [selectedStartDate, setSelectedStartDate] = useState(null);
  const [selectedEndDate, setSelectedEndDate] = useState(null);

  const navigateMyTrips = () => {
    navigate("/toMyTrips");
  };
  const navigateToSearch_Ticket = () => {
    navigate("/toSearch_Ticket");
  };
  const navigateToProfile = () => {
    navigate("/toProfile");
  };

  const toggleTripType = () => {
    setShowTripType(!showTripType);
    setShowStartCalendar(false);
    setShowEndCalendar(false);
  };

  const selectTripType = (type) => {
    setTripType(type);
    setShowTripType(false);
    if (type === "one way") {
      setEndDate("");
      setSelectedEndDate(null);
    }
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

  const handleEndDateClick = () => {
    if (tripType === "two way") {
      setShowEndCalendar(!showEndCalendar);
      setShowStartCalendar(false);
    }
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
    <div className="Userpage-container">
      {/* Header */}
      <header className="UserPage_header">
        <div
          className="header-left"
          onClick={navigateToProfile}
          style={{ cursor: "pointer" }}
        >
          <FaUserCircle size={22} />
          <span className="header-text" >Narjes Gorji</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span onClick={navigateMyTrips} className="header-text">my trips</span>
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
          <div className="trip-type-container">
            <button className="one-way" onClick={toggleTripType}>
              {tripType}
            </button>
            {showTripType && (
              <div className="trip-type-dropdown">
                <div
                  className="trip-type-option"
                  onClick={() => selectTripType("one way")}
                >
                  one way
                </div>
                <div
                  className="trip-type-option"
                  onClick={() => selectTripType("two way")}
                >
                  two way
                </div>
              </div>
            )}
          </div>
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

          {tripType === "two way" && (
            <div className="date-input-container">
              <input
                placeholder="end"
                value={endDate}
                onClick={handleEndDateClick}
                readOnly
              />
              {showEndCalendar && renderCalendar(false)}
            </div>
          )}

          <input placeholder="p count" />
          <button className="search-button" onClick={navigateToSearch_Ticket}>
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
      <div className="blog-button-container">
        <button className="blog-button">
          <span>travel blog</span>
          <p>share your experience</p>
        </button>
      </div>

      {/* Footer */}
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
