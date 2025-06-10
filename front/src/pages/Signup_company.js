import { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Signup_company.module.css";
import { FiArrowLeft } from "react-icons/fi";

function SignupCompany() {
  const [formData, setFormData] = useState({
    email: "",
    username: "",
    password: "",
  });
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    // Add your signup logic here
  };
  const navigateTosignup = () => navigate("/tosignup");
  const navigateback = () => navigate("/toHomePage");

  return (
    <div className={styles.Signup_company_container}>
      <button
        onClick={navigateback}
        style={{
          padding: "8px 12px",
          backgroundColor: "#dbdfea",
          color: "white",
          borderRadius: "6px",
          cursor: "pointer",
          display: "flex",
          alignItems: "center",
          border: 0,
        }}
      >
        <FiArrowLeft size={16} />
      </button>

      <div className={styles.Signup_company_cardd}>
        <div className={styles.Signup_company_card_up}>
          <button
            onClick={navigateTosignup}
            className={styles.Signup_company_user_button}
          >
            user
          </button>
          <button className={styles.Signup_company_company_button}>
            company
          </button>
        </div>

        <div className={styles.Signup_company_card}>
          <h2 className={styles.Signup_company_loginTitle}>Sign Up</h2>
          <p className={styles.Signup_company_lineTitle}>
            _______________________________
          </p>

          <form onSubmit={handleSubmit} className={styles.Signup_company_form}>
            <div className={styles.Signup_company_inputGroup}>
              <label className={styles.Signup_company_label}>
                enter your email
              </label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className={styles.Signup_company_input}
                placeholder="......"
                required
              />
            </div>

            <div className={styles.Signup_company_inputGroup}>
              <label className={styles.Signup_company_label}>
                enter your username
              </label>
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
                className={styles.Signup_company_input}
                placeholder="......"
                required
              />
            </div>

            <div className={styles.Signup_company_inputGroup}>
              <label className={styles.Signup_company_label}>
                make your own password
              </label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                className={styles.Signup_company_input}
                placeholder="......"
                required
              />
            </div>

            <p
              onClick={() => navigate("/tologin")}
              className={styles.Signup_company_loginPrompt}
            >
              already have an account?
            </p>

            <button type="submit" className={styles.Signup_company_button}>
              send verification code
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default SignupCompany;
