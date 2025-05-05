import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import Login_user from "./pages/Login_user";
import Login_company from "./pages/Login_company";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/auth" element={<Login_user />} />
      </Routes>
      <Routes>
        <Route path="/" element={<Login_user />} />
        <Route path="/tocompany" element={<Login_company />} />
      </Routes>
      <Routes>
        <Route path="/" element={<Login_company />} />
        <Route path="/touser" element={<Login_user />} />
      </Routes>
    </Router>
  );
}

export default App;
