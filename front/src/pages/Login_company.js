import { useState } from "react";
import { Link } from "react-router-dom";
import styles from "./Login_company.module.css";
import { useNavigate } from "react-router-dom";

function Login_company() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle login logic here
    console.log({ email, password });
  };
  
  const navigate = useNavigate();

  const handleAuthNavigation = () => {
    navigate("/touser");
  };

  return (
    <div className={styles.Login_company_container}>
      <div className={styles.login_company_cardd}>
      <div className={styles.Login_company_card_up}>
        <div>
          <button onClick={handleAuthNavigation} type="submit" className={styles.Login_company_user_button}>
            user
          </button>
        </div>
        <div>
          <button onClick={handleAuthNavigation} type="submit" className={styles.Login_company_company_button}>
            company
          </button>
        </div>
      </div>
      <div className={styles.Login_company_card}>

        <h2 className={styles.Login_company_loginTitle}>Login</h2>
        <p className={styles.Login_company_lineTitle}>_______________________________</p>

        <form onSubmit={handleSubmit} className={styles.Login_company_form}>
          <div className={styles.Login_company_inputGroup}>
            <label className={styles.Login_company_label}>enter your email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className={styles.Login_company_input}
              placeholder="......"
              required
            />
          </div>

          <div className={styles.Login_company_inputGroup}>
            <label className={styles.Login_company_label}>enter your password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
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

export default Login_company;
