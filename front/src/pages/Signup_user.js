import { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Signup_user.module.css";
import { FiArrowLeft } from "react-icons/fi";

function SignupUser() {
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
  };
  const navigateTosuCompany = () => navigate("/tosucompany");
  const navigateback = () => navigate("/toHomePage");

  return (
    <div className={styles.Signup_user_container}>

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

      <div className={styles.Signup_user_cardd}>
        <div className={styles.Signup_user_card_up}>
          <button className={styles.Signup_user_user_button}>user</button>
          <button
            onClick={navigateTosuCompany}
            className={styles.Signup_user_company_button}
          >
            company
          </button>
        </div>

        <div className={styles.Signup_user_card}>
          <h2 className={styles.Signup_user_loginTitle}>Sign Up</h2>
          <p className={styles.Signup_user_lineTitle}>
            _______________________________
          </p>

          <form onSubmit={handleSubmit} className={styles.Signup_user_form}>
            <div className={styles.Signup_user_inputGroup}>
              <label className={styles.Signup_user_label}>
                enter your email
              </label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className={styles.Signup_user_input}
                placeholder="......"
                required
              />
            </div>

            <div className={styles.Signup_user_inputGroup}>
              <label className={styles.Signup_user_label}>
                enter your username
              </label>
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
                className={styles.Signup_user_input}
                placeholder="......"
                required
              />
            </div>

            <div className={styles.Signup_user_inputGroup}>
              <label className={styles.Signup_user_label}>
                make your own password
              </label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                className={styles.Signup_user_input}
                placeholder="......"
                required
              />
            </div>

            <p
              onClick={() => navigate("/tologin")}
              className={styles.Signup_user_loginPrompt}
            >
              already have an account?
            </p>

            <button type="submit" className={styles.Signup_user_button}>
              send verification code
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default SignupUser;
