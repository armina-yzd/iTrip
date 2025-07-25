import React, { useState } from "react";
import "./AddService.css";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import { FaBus, FaTrain, FaPlane } from "react-icons/fa";
import { LuCircleFadingPlus } from "react-icons/lu";
import { TbCircleLetterC } from "react-icons/tb";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../AuthContext";

const AddService = () => {
  const { token } = useAuth();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    transportType: "airplane",
    from_location: "",
    to_location: "",
    start_date: "",
    start_time: "",
    vehicle_num: "",
    vehicle_type: "",
    detail: "",
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

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      from_location: formData.from_location,
      to_location: formData.to_location,
      start_date: formData.start_date,
      start_time: formData.start_time,
      price: Number(formData.price),
      capacity: Number(formData.capacity),
      vehicle_num: formData.vehicle_num || undefined,
      vehicle_type: formData.vehicle_type || undefined,
      detail: formData.detail || undefined,
    };

    const endpointMap = {
      airplane: "addAirplaneService",
      train: "addTrainService",
      bus: "addBusService",
      tour: "addTourService",
    };

    const selectedEndpoint = endpointMap[formData.transportType];

    try {
      const response = await fetch(`http://manage_services.localhost/api/addServices/${selectedEndpoint}/`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) throw new Error("Failed to add service");

      await response.json();
      alert("Service added successfully!");
      navigate("/toCompanyPage"); // ✅ return to dashboard
    } catch (err) {
      console.error("Error adding service:", err);
      alert("Error while adding service");
    }
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

          <div className="flight-input-row">
            <label className="flight-label">From:</label>
            <input
              type="text"
              name="from_location"
              value={formData.from_location}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">To:</label>
            <input
              type="text"
              name="to_location"
              value={formData.to_location}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">Date:</label>
            <input
              type="date"
              name="start_date"
              value={formData.start_date}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

        

          <div className="flight-input-row">
            <label className="flight-label">Landing Time:</label>
            <input
              type="time"
              name="start_time"
              value={formData.start_time}
              onChange={handleChange}
              className="flight-input-box"
              required
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">Flight Number:</label>
            <input
              type="text"
              name="vehicle_num"
              value={formData.vehicle_num}
              onChange={handleChange}
              className="flight-input-box"
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">Airplane Model:</label>
            <input
              type="text"
              name="vehicle_type"
              value={formData.vehicle_type}
              onChange={handleChange}
              className="flight-input-box"
            />
          </div>

          <div className="flight-input-row">
            <label className="flight-label">detail:</label>
            <input
              type="text"
              name="detail"
              value={formData.detail}
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
