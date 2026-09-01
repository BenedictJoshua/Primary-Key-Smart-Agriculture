const express = require("express");
const mysql = require("mysql2/promise");
const cors = require("cors");
const { spawn } = require("child_process");

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
    const {
      soil_type,
      ph_level,
      nitrogen,
      phosphorus,
      potassium,
    } = req.body;

    const [crops] = await db.query("SELECT * FROM crops");

    const scoredCrops = crops.map((crop) => {
      let score = 0;

      // Soil compatibility
      if (
        crop.suitable_soil &&
        crop.suitable_soil.toLowerCase() === soil_type.toLowerCase()
      ) {
        score += 40;
      }

      // pH compatibility
      if (
        ph_level >= Number(crop.min_ph) &&
        ph_level <= Number(crop.max_ph)
      ) {
        score += 30;
      }

      // Basic NPK suitability scoring
      if (Number(nitrogen) >= 40) score += 10;
      if (Number(phosphorus) >= 20) score += 10;
      if (Number(potassium) >= 20) score += 10;

      return {
        ...crop,
        score,
      };
    });

    scoredCrops.sort((a, b) => b.score - a.score);

    const recommendation = scoredCrops[0];

    res.json({
      success: true,
      recommendation,
      input: {
        soil_type,
        ph_level,
        nitrogen,
        phosphorus,
        potassium,
      },
    });
  } catch (error) {
    console.error(error);

    res.status(500).json({
      success: false,
      error: "Recommendation failed",
    });
  }
});
app.post("/api/ai-recommend", async (req, res) => {
  try {
    const { soil_type, ph, nitrogen, phosphorus, potassium } = req.body;

    const python = spawn("python3", [
      require("path").join(__dirname, "../ai/predict.py"),
    ]);
    python.on("error", (err) => {
      console.error(err);
      return res
        .status(500)
        .json({ success: false, error: "AI process failed to start" });
    });

    let output = "";
    let errorOutput = "";
    python.stdout.on("data", (data) => {
      output += data.toString();
    });

    python.stderr.on("data", (data) => {
      errorOutput += data.toString();
    });

    python.on("close", (code) => {
      if (code !== 0) {
        console.error(errorOutput);

        return res.status(500).json({
          success: false,
          error: "AI prediction failed",
        });
      }

      res.json({
        success: true,
        prediction: output.trim(),
      });
    });

    python.stdin.write(
      JSON.stringify({
        soil_type,
        ph,
        nitrogen,
        phosphorus,
        potassium,
      })
    );

    python.stdin.end();
  } catch (error) {
    console.error(error);

    res.status(500).json({
      success: false,
      error: "AI service failed",
    });
  }
});

const PORT = 5001;

app.listen(PORT, () => {
  console.log(`Smart Agriculture API running on port ${PORT}`);
});