import React, { useState, useEffect } from "react";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import { LuCircleFadingPlus } from "react-icons/lu";
import { TbCircleLetterC } from "react-icons/tb";
import "./CompanyProfile.css";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../AuthContext";

const CompanyProfile = () => {
  const { token, logout } = useAuth();
  const [company, setCompany] = useState(null);
  const navigate = useNavigate();

  // ✅ Fetch company data using token
  useEffect(() => {
    if (!token) return;

    fetch("http://iam.localhost/api/company/me", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        if (!res.ok) throw new Error("Unauthorized");
        return res.json();
      })
      .then((data) => setCompany(data))
      .catch((err) => {
        console.error("Error fetching company data:", err);
        logout(); // optional: log out if invalid token
        navigate("/tologin");
      });
  }, [token, logout, navigate]);

  return (
    <div>
      <header className="search-ticket-header">
        <div className="header-left">
          <TbCircleLetterC size={27} />
          <span className="header-text">{company?.name || "Loading..."}</span>
        </div>
        <h1 className="header-title">ITRIP</h1>
        <div className="header-right">
          <span className="header-text">Add service</span>
          <LuCircleFadingPlus size={25} />
        </div>
      </header>

      <div className="container">
        <div className="tabs">
          <span className="tab active">profile</span>
        </div>

        <div className="profile-info">
          <p>
            <span className="label">name :</span> {company?.name || "Loading..."}
          </p>
          <p>
            <span className="label">email :</span> {company?.email || "Loading..."}
          </p>

          <button className="logout-btn" onClick={logout}>
            log out
          </button>
        </div>
      </div>

      <footer className="CompanyPage-footer">
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

export default CompanyProfile;
