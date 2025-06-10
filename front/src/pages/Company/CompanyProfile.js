import React, { useState } from "react";
import {
  FaFacebook,
  FaInstagram,
  FaXTwitter,
  FaWhatsapp,
} from "react-icons/fa6";
import { LuCircleFadingPlus } from "react-icons/lu";
import { TbCircleLetterC } from "react-icons/tb";
import "./CompanyProfile.css";
const CompanyProfile = () => {
  const [tab, setTab] = useState("profile");
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
              <span className="label">name :</span> Kish Air
            </p>
            <p>
              <span className="label">email :</span> KishAir@..
            </p>

            <button className="logout-btn">log out</button>
          </div>
        ) : (
          <div className="notification-box">
            <div className="warning">
              <p>
                your have many objector for your last service if we recive more
                bad comment about your company we have to ban your company from
                our website.
              </p>
            </div>
          </div>
        )}
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
