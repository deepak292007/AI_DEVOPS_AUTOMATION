const express = require("express");
const app = express();

// Environment variables
const PORT = process.env.PORT || 3000;
const APP_VERSION = process.env.APP_VERSION || "local";

// Home route – deployment visibility
app.get("/", (req, res) => {
  res.send(`
    <h1>Hello from AI DevOps - Version 5 - Auto Deployment Test</h1>
    <hr/>
    <p><b>Version:</b> ${APP_VERSION}</p>
    <p><b>Environment:</b> ${APP_VERSION}</p>
    <p><b>Deployed At:</b> ${new Date().toISOString()}</p>
    <p><b>Status:</b> Role A Completed Version 5 ✅</p>
  `);
});

// Health check endpoint
app.get("/health", (req, res) => {
  res.json({
    status: "UP",
    version: APP_VERSION,
    timestamp: new Date().toISOString()
  });
});

// Start server
app.listen(PORT, '0.0.0.0', () => {
  console.log(`🚀 Server running on port ${PORT}`);
});
