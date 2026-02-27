import React, { useEffect, useState } from "react";
import API from "../services/api";

function Home() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    API.get("/health")
      .then(res => setMessage(res.data.status))
      .catch(() => setMessage("Backend not reachable"));
  }, []);

  return (
    <div style={{ textAlign: "center" }}>
      <h3>Backend Status: {message}</h3>
    </div>
  );
}

export default Home;