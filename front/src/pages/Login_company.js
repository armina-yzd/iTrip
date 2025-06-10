import { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Login_company.module.css";
import { FiArrowLeft } from "react-icons/fi";

function LoginCompany() {
  const [formData, setFormData] = useState({
    email: "",
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
    // Add your login logic here
  };

  const navigateToUser = () => navigate("/touser");
  const navigateback = () => navigate("/tosignup");
  const navigateToCompanyPage = () => navigate("/toCompanyPage");
  return (
    <div className={styles.Login_company_container}>
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

      <div className={styles.login_company_cardd}>
        <div className={styles.Login_company_card_up}>
          <button
            onClick={navigateToUser}
            className={styles.Login_company_user_button}
          >
            user
          </button>
          <button

            className={styles.Login_company_company_button}
          >
            company
          </button>
        </div>

        <div className={styles.Login_company_card}>
          <h2 className={styles.Login_company_loginTitle}>Login</h2>
          <p className={styles.Login_company_lineTitle}>
            _______________________________
          </p>

          <form onSubmit={handleSubmit} className={styles.Login_company_form}>
            <div className={styles.Login_company_inputGroup}>
              <label className={styles.Login_company_label}>
                enter your email
              </label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className={styles.Login_company_input}
                placeholder="......"
                required
              />
            </div>

            <div className={styles.Login_company_inputGroup}>
              <label className={styles.Login_company_label}>
                enter your password
              </label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                className={styles.Login_company_input}
                placeholder="......"
                required
              />
            </div>

            <button type="submit" onClick={navigateToCompanyPage} className={styles.Login_company_button}>
              done
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default LoginCompany;
