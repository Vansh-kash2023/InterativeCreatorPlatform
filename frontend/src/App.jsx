import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Dashboard from "./pages/Dashboard";
import Challenges from "./pages/Challenges";
import ChallengeDetails from "./pages/ChallengeDetails";
import UserProgress from "./pages/UserProgress";
import Leaderboard from "./pages/Leaderboard";
import NotFound from "./pages/NotFound";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const token = localStorage.getItem("token");
        if (token) {
          const response = await axios.get("/api/user", {
            headers: { Authorization: `Bearer ${token}` },
          });
          setUser(response.data);
        }
      } catch (error) {
        console.error("Error fetching user:", error);
        localStorage.removeItem("token");
      }
    };
    fetchUser();
  }, []);

  return (
    <Router>
      <Navbar user={user} />
      <div className="flex">
        <Sidebar />
        <div className="flex-1 p-4">
          <Routes>
            <Route path="/login" element={<Login setUser={setUser} />} />
            <Route path="/signup" element={<Signup />} />
            <Route
              path="/"
              element={<ProtectedRoute user={user} element={<Dashboard />} />}
            />
            <Route
              path="/challenges"
              element={<ProtectedRoute user={user} element={<Challenges />} />}
            />
            <Route
              path="/challenges/:id"
              element={<ProtectedRoute user={user} element={<ChallengeDetails />} />}
            />
            <Route
              path="/progress"
              element={<ProtectedRoute user={user} element={<UserProgress />} />}
            />
            <Route
              path="/leaderboard"
              element={<ProtectedRoute user={user} element={<Leaderboard />} />}
            />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
