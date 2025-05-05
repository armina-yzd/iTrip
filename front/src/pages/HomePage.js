import { useNavigate } from "react-router-dom";
import backgroundImage from "../assets/bg.jpg";

function HomePage() {
  const navigate = useNavigate();

  const handleAuthNavigation = () => {
    navigate("/auth");
  };

  return (
    <div
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
      }}
    >
      <h1
        style={{ color: "white", textShadow: "2px 2px 4px rgba(0, 0, 0, 0.5)" }}
      >
        Welcome to itrip
      </h1>
      <button
        onClick={handleAuthNavigation}
        style={{
          padding: "12px 24px",
          fontSize: "18px",
          backgroundColor: "rgba(0, 123, 255, 0.8)",
          color: "white",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
          marginTop: "20px",
          boxShadow: "0 4px 8px rgba(0, 0, 0, 0.2)",
        }}
      >
        Login / Sign Up
      </button>
    </div>
  );
}

export default HomePage;
