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
  const [otp, setOtp] = useState("");
  const [showOtpInput, setShowOtpInput] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSendOtp = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://iam.localhost/api/user/sendOtp/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error("Failed to send OTP");
      const data = await response.json();
      console.log("OTP Sent:", data);
      setShowOtpInput(true);
    } catch (err) {
      console.error(err);
      alert("Error sending verification code.");
    } finally {
      setLoading(false);
    }
  };

  const handleVerifyOtp = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://iam.localhost/api/user/creatUser/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: formData.username,
          email: formData.email,
          password: formData.password,
          otp: otp,
        }),
      });

      if (!response.ok) throw new Error("Invalid OTP");
      const data = await response.json();
      console.log("Account verified:", data);

      alert("Account successfully created!");
      navigate("/toUserPage"); 
    } catch (err) {
      console.error(err);
      alert("Verification failed.");
    } finally {
      setLoading(false);
    }
  };

  const navigateTosuCompany = () => navigate("/tosucompany");
  const navigateback = () => navigate("/toHomePage");

  return (
    <div className={styles.Signup_user_container}>
      <button onClick={navigateback} className={styles.back_button}>
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

          <form
            onSubmit={showOtpInput ? handleVerifyOtp : handleSendOtp}
            className={styles.Signup_user_form}
          >
            {!showOtpInput && (
              <>
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
              </>
            )}

            {showOtpInput && (
              <div className={styles.Signup_user_inputGroup}>
                <label className={styles.Signup_user_label}>
                  enter verification code
                </label>
                <input
                  type="text"
                  name="otp"
                  value={otp}
                  onChange={(e) => setOtp(e.target.value)}
                  className={styles.Signup_user_input}
                  placeholder="6-digit code"
                  required
                />
              </div>
            )}

            <p
              onClick={() => navigate("/tologin")}
              className={styles.Signup_user_loginPrompt}
            >
              already have an account?
            </p>

            <button
              type="submit"
              className={styles.Signup_user_button}
              disabled={loading}
            >
              {loading
                ? "Please wait..."
                : showOtpInput
                ? "Done"
                : "Send verification code"}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default SignupUser;
