const express = require("express");
const path = require("path");
require("dotenv").config();

const logger = require("./middleware/logger");
const userRoutes = require("./routes/userRoutes");

const app = express();

app.use(express.json());
app.use(logger);
app.use("/api", userRoutes);

// Serve React build
app.use(express.static(path.join(__dirname, "../client/build")));

app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "../client/build/index.html"));
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});