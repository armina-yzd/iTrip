import { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Login_company.module.css";
import { FiArrowLeft } from "react-icons/fi";
import { useAuth } from "./AuthContext";

function LoginCompany() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const navigate = useNavigate();
  const { setToken } = useAuth(); // ✅ store token

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://iam.localhost/api/company/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          username: formData.email,
          password: formData.password,
        }),
      });

      if (!response.ok) throw new Error("Login failed");
      const data = await response.json();
      setToken(data.access_token); // ✅ token in context
      navigate("/toCompanyPage");
    } catch (err) {
      console.error(err);
      alert("Invalid email or password.");
    }
  };

  const navigateToUser = () => navigate("/touser");
  const navigateback = () => navigate("/tosignup");

  return (
    <div className={styles.Login_company_container}>
      <button onClick={navigateback} className={styles.back_button}>
        <FiArrowLeft size={16} />
      </button>

      <div className={styles.login_company_cardd}>
        <div className={styles.Login_company_card_up}>
          <button onClick={navigateToUser} className={styles.Login_company_user_button}>
            user
          </button>
          <button className={styles.Login_company_company_button}>company</button>
        </div>

        <div className={styles.Login_company_card}>
          <h2 className={styles.Login_company_loginTitle}>Login</h2>
          <p className={styles.Login_company_lineTitle}>_______________________________</p>

          <form onSubmit={handleSubmit} className={styles.Login_company_form}>
            <div className={styles.Login_company_inputGroup}>
              <label className={styles.Login_company_label}>enter your email</label>
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
              <label className={styles.Login_company_label}>enter your password</label>
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

            <button type="submit" className={styles.Login_company_button}>
              done
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default LoginCompany;
