const express = require("express");
const router = express.Router();
const { healthCheck } = require("../controllers/userController");

router.get("/health", healthCheck);

module.exports = router;