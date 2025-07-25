import { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Login_user.module.css";
import { FiArrowLeft } from "react-icons/fi";

function LoginUser() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };


  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://iam.localhost/api/user/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          username: formData.email, // FastAPI OAuth expects 'username'
          password: formData.password,
        }),
      });
      console.log(response);
      if (!response.ok) throw new Error("Login failed");

      const data = await response.json();
      console.log("Token:", data.access_token);

      // Save token in localStorage or context:
      localStorage.setItem("access_token", data.access_token);

      navigate("/toUserPage");
    } catch (error) {
      console.error(error);
      alert("Invalid email or password.");
    }
  };

  const navigateToCompany = () => navigate("/tocompany");
  const navigateback = () => navigate("/tosignup");
  const navigatetoUserPage = () => navigate("/toUserPage");

  return (
    <div className={styles.Login_user_container}>
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

      <div className={styles.login_user_cardd}>
        <div className={styles.Login_user_card_up}>
          <button className={styles.Login_user_user_button}>user</button>
          <button
            onClick={navigateToCompany}
            className={styles.Login_user_company_button}
          >
            company
          </button>
        </div>

        <div className={styles.Login_user_card}>
          <h2 className={styles.Login_user_loginTitle}>Login</h2>
          <p className={styles.Login_user_lineTitle}>
            _______________________________
          </p>

          <form onSubmit={handleSubmit} className={styles.Login_user_form}>
            <div className={styles.Login_user_inputGroup}>
              <label className={styles.Login_user_label}>
                enter your email
              </label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className={styles.Login_user_input}
                placeholder="......"
                required
              />
            </div>

            <div className={styles.Login_user_inputGroup}>
              <label className={styles.Login_user_label}>
                enter your password
              </label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                className={styles.Login_user_input}
                placeholder="......"
                required
              />
            </div>

            <button type="submit" className={styles.Login_user_button}>
              done
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default LoginUser;
