import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import Login_user from "./pages/Login_user";
import Login_company from "./pages/Login_company";
import Signup_user from "./pages/Signup_user";
import Signup_company from "./pages/Signup_company";
import UserPage from "./pages/User/UserPage";
import Search_Ticket from "./pages/User/Search_Ticket";
import PathInfo from "./pages/User/PathInfo";
import Ticket from "./pages/User/Ticket";
import Profile from "./pages/User/Profile";
import MyTrips from "./pages/User/MyTrips";
import CompanyPage from "./pages/Company/CompanyPage";
import CompanyProfile from "./pages/Company/CompanyProfile";
import AddService from "./pages/Company/AddService";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/tosignup" element={<Signup_user />} />
      </Routes>

      <Routes>
        <Route path="/" element={<Login_user />} />
        <Route path="/tocompany" element={<Login_company />} />
      </Routes>

      <Routes>
        <Route path="/" element={<Login_company />} />
        <Route path="/touser" element={<Login_user />} />
      </Routes>

      <Routes>
        <Route path="/" element={<Signup_user />} />
        <Route path="/tologin" element={<Login_user />} />
      </Routes>

      <Routes>
        <Route path="/" element={<Signup_user />} />
        <Route path="/tosucompany" element={<Signup_company />} />
      </Routes>
      <Routes>
        <Route path="/toHomePage" element={<HomePage />} />
      </Routes>
      <Routes>
        <Route path="/toUserPage" element={<UserPage />} />
      </Routes>
      <Routes>
        <Route path="/toSearch_Ticket" element={<Search_Ticket />} />
      </Routes>
      <Routes>
        <Route path="/toPathInfo" element={<PathInfo />} />
      </Routes>
      <Routes>
        <Route path="/toTicket" element={<Ticket />} />
      </Routes>
      <Routes>
        <Route path="/toProfile" element={<Profile />} />
      </Routes>
      <Routes>
        <Route path="/toMyTrips" element={<MyTrips />} />
      </Routes>
      <Routes>
        <Route path="/toCompanyPage" element={<CompanyPage />} />
      </Routes>
      <Routes>
        <Route path="/toCompanyProfile" element={<CompanyProfile />} />
      </Routes>
      <Routes>
        <Route path="/toAddService" element={<AddService />} />
      </Routes>

    </Router>
  );
}

export default App;
