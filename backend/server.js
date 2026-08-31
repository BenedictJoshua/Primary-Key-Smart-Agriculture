const express = require("express");
const mysql = require("mysql2/promise");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

const db = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "root",
  database: "smart_agriculture",
  port: 3306,
});

app.get("/", (req, res) => {
  res.json({
    message: "Smart Agriculture API is running",
  });
});

app.get("/api/crops", async (req, res) => {
  try {
    const [rows] = await db.query("SELECT * FROM crops");
    res.json(rows);
  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: "Failed to fetch crops",
    });
  }
});

app.get("/api/soil/:farmId", async (req, res) => {
  try {
    const [rows] = await db.query(
      "SELECT * FROM soil_data WHERE farm_id = ?",
      [req.params.farmId]
    );

    res.json(rows);
  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: "Failed to fetch soil data",
    });
  }
});

app.post("/api/recommend", async (req, res) => {
  try {
    const { soil_type, ph_level } = req.body;

    const [rows] = await db.query(
      `SELECT * FROM crops
       WHERE LOWER(suitable_soil) = LOWER(?)
       AND ? BETWEEN min_ph AND max_ph`,
      [soil_type, ph_level]
    );

    if (rows.length === 0) {
      return res.json({
        success: true,
        recommendation: null,
        message: "No suitable crop found for the given conditions."
      });
    }

    res.json({
      success: true,
      recommendation: rows[0]
    });

  } catch (error) {
    console.error(error);

    res.status(500).json({
      success: false,
      error: "Recommendation failed"
    });
  }
});

const PORT = 5001;

app.listen(PORT, () => {
  console.log(`Smart Agriculture API running on port ${PORT}`);
});