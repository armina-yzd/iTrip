import { useState } from "react";
import { Link } from "react-router-dom";
import styles from "./Login_user.module.css";
import { useNavigate } from "react-router-dom";

function Login_user() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle login logic here
    console.log({ email, password });
  };

  const navigate = useNavigate();

  const handleAuthNavigation = () => {
    navigate("/tocompany");
  };

  return (
    <div className={styles.Login_user_container}>
      <div className={styles.login_user_cardd}>
      <div className={styles.Login_user_card_up}>
        <div>
          <button onClick={handleAuthNavigation} type="submit" className={styles.Login_user_user_button}>
            user
          </button>
        </div>
        <div>
          <button onClick={handleAuthNavigation} type="submit" className={styles.Login_user_company_button}>
            company
          </button>
        </div>
      </div>
      <div className={styles.Login_user_card}>

        <h2 className={styles.Login_user_loginTitle}>Login</h2>
        <p className={styles.Login_user_lineTitle}>_______________________________</p>

        <form onSubmit={handleSubmit} className={styles.Login_user_form}>
          <div className={styles.Login_user_inputGroup}>
            <label className={styles.Login_user_label}>enter your email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className={styles.Login_user_input}
              placeholder="......"
              required
            />
          </div>

          <div className={styles.Login_user_inputGroup}>
            <label className={styles.Login_user_label}>enter your password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
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

export default Login_user;
