import React, { useState } from "react";
import "./AddService.css";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import { FaBus, FaTrain, FaPlane } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import { LuCircleFadingPlus } from "react-icons/lu";
import { TbCircleLetterC } from "react-icons/tb";

const AddService = () => {
  const [formData, setFormData] = useState({
    transportType: "airplane",
    from: "",
    to: "",
    date: "",
    landingTime: "",
    endTime: "",
    flightNum: "",
    airplaneModel: "",
    bar: "",
    price: "",
    capacity: 100,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === "capacity" ? parseInt(value) : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Transport Info Submitted:\n" + JSON.stringify(formData, null, 2));
  };

  return (
    <div>
      <header className="search-ticket-header">
        <div className="header-left">
          <TbCircleLetterC size={27} />
          <span className="header-text">Kish Air</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span className="header-text">Add service</span>
          <LuCircleFadingPlus size={25} />
        </div>
      </header>

      <div className="flight-form-wrapper">
        <h2 className="flight-title">Transportation Information</h2>
        <form className="flight-form-body" onSubmit={handleSubmit}>
          {/* Transport Type Selection */}
          <div className="flight-input-row">
            <label className="flight-label">Transport Type:</label>
            <select
              name="transportType"
              value={formData.transportType}
              onChange={handleChange}
              className="flight-input-box"
            >
              <option value="airplane">✈️ Airplane</option>
              <option value="bus">🚌 Bus</option>
              <option value="train">🚆 Train</option>
            </select>
          </div>

          {/* From / To / Date / Time / Details */}
          <div className="flight-input-row">
            <label className="flight-label">From:</label>
            <input
              type="text"
              name="from"
              value={formData.from}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">To:</label>
            <input
              type="text"
              name="to"
              value={formData.to}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">Date:</label>
            <input
              type="date"
              name="date"
              value={formData.date}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">Landing Time:</label>
            <input
              type="time"
              name="landingTime"
              value={formData.landingTime}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">End Time:</label>
            <input
              type="time"
              name="endTime"
              value={formData.endTime}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">Flight Number:</label>
            <input
              type="text"
              name="flightNum"
              value={formData.flightNum}
              onChange={handleChange}
              className="flight-input-box"
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">Airplane Model:</label>
            <input
              type="text"
              name="airplaneModel"
              value={formData.airplaneModel}
              onChange={handleChange}
              className="flight-input-box"
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">Bar:</label>
            <input
              type="text"
              name="bar"
              value={formData.bar}
              onChange={handleChange}
              className="flight-input-box"
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">Price:</label>
            <input
              type="number"
              name="price"
              value={formData.price}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">
              Capacity: {formData.capacity} seats
            </label>
            <input
              type="range"
              name="capacity"
              min="10"
              max="300"
              step="10"
              value={formData.capacity}
              onChange={handleChange}
              className="flight-range-slider"
            />
          </div>

          <button type="submit" className="flight-submit-btn">
            Done
          </button>
        </form>
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

export default AddService;
