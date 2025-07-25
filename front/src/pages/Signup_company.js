import { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Signup_company.module.css";
import { FiArrowLeft } from "react-icons/fi";
import { useAuth } from "./AuthContext";

function SignupCompany() {
  const [formData, setFormData] = useState({
    email: "",
    name: "",
    password: "",
  });
  const [otp, setOtp] = useState("");
  const [showOtpInput, setShowOtpInput] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { setToken } = useAuth();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSendOtp = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://iam.localhost/api/company/sendOtp/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      if (!response.ok) throw new Error("Failed to send OTP");
      await response.json();
      setShowOtpInput(true);
    } catch (err) {
      console.error(err);
      alert("Error sending OTP.");
    } finally {
      setLoading(false);
    }
  };

  const handleVerifyOtp = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://iam.localhost/api/company/creatCompany/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...formData, otp }),
      });

      if (!response.ok) throw new Error("Invalid OTP");
      const data = await response.json();
      setToken(data.access_token); // ✅ token saved
      navigate("/toCompanyPage");
    } catch (err) {
      console.error(err);
      alert("Verification failed.");
    } finally {
      setLoading(false);
    }
  };

  const navigateToUser = () => navigate("/tosignup");
  const navigateback = () => navigate("/toHomePage");

  return (
    <div className={styles.Signup_company_container}>
      <button onClick={navigateback} className={styles.back_button}>
        <FiArrowLeft size={16} />
      </button>

      <div className={styles.Signup_company_cardd}>
        <div className={styles.Signup_company_card_up}>
          <button onClick={navigateToUser} className={styles.Signup_company_user_button}>
            user
          </button>
          <button className={styles.Signup_company_company_button}>company</button>
        </div>

        <div className={styles.Signup_company_card}>
          <h2 className={styles.Signup_company_loginTitle}>Sign Up</h2>
          <p className={styles.Signup_company_lineTitle}>_______________________________</p>

          <form onSubmit={showOtpInput ? handleVerifyOtp : handleSendOtp} className={styles.Signup_company_form}>
            {!showOtpInput && (
              <>
                <div className={styles.Signup_company_inputGroup}>
                  <label className={styles.Signup_company_label}>enter your email</label>
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
                  <label className={styles.Signup_company_label}>enter company name</label>
                  <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className={styles.Signup_company_input}
                    placeholder="......"
                    required
                  />
                </div>

                <div className={styles.Signup_company_inputGroup}>
                  <label className={styles.Signup_company_label}>make your own password</label>
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
              </>
            )}

            {showOtpInput && (
              <div className={styles.Signup_company_inputGroup}>
                <label className={styles.Signup_company_label}>enter verification code</label>
                <input
                  type="text"
                  value={otp}
                  onChange={(e) => setOtp(e.target.value)}
                  className={styles.Signup_company_input}
                  placeholder="6-digit code"
                  required
                />
              </div>
            )}

            <p onClick={() => navigate("/tologin")} className={styles.Signup_company_loginPrompt}>
              already have an account?
            </p>

            <button type="submit" className={styles.Signup_company_button} disabled={loading}>
              {loading ? "Please wait..." : showOtpInput ? "Done" : "Send verification code"}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default SignupCompany;
