import { useState } from "react";
import "./App.css";

function App() {
  const [soil, setSoil] = useState("");
  const [location, setLocation] = useState("");
  const [ph, setPh] = useState("");
  const [nitrogen, setNitrogen] = useState("");
  const [phosphorus, setPhosphorus] = useState("");
  const [potassium, setPotassium] = useState("");
  const [result, setResult] = useState(null);

const getRecommendation = async () => {
  if (!soil || !location || !ph || !nitrogen || !phosphorus || !potassium) return;

  try {
    const response = await fetch("http://127.0.0.1:5001/api/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        soil_type: soil,
        ph_level: Number(ph),
        nitrogen: Number(nitrogen),
        phosphorus: Number(phosphorus),
        potassium: Number(potassium),
      }),
    });

    const data = await response.json();

    if (data.recommendation) {
      setResult({
        crop: data.recommendation.crop_name,
        reason: `${data.recommendation.description} Soil: ${soil} | pH: ${ph} | N: ${nitrogen} | P: ${phosphorus} | K: ${potassium}.`,
        score: data.recommendation.score,
      });
    } else {
      setResult({
        crop: "No suitable crop found",
        reason: data.message,
      });
    }
  } catch (error) {
    console.error(error);

    setResult({
      crop: "Connection Error",
      reason: "Unable to connect to the Smart Agriculture backend.",
    });
  }
};

  return (
    <div className="app">
      <nav className="navbar">
        <div className="brand">
          <span className="logo">PK</span>
          <div>
            <h2>Primary Key</h2>
            <p>Smart Agriculture Intelligence</p>
          </div>
        </div>

        <div className="nav-links">
          <a href="#dashboard">Dashboard</a>
          <a href="#recommend">Crop Recommendation</a>
          <a href="#about">About</a>
        </div>
      </nav>

      <main>
        <section className="hero" id="dashboard">
          <div>
            <p className="tag">AI-POWERED AGRICULTURE</p>
            <h1>Smarter decisions.<br />Better farming.</h1>
            <p className="hero-text">
              An intelligent agriculture portal that combines structured
              agricultural data with AI-assisted recommendations.
            </p>
            <button
              className="primary-btn"
              onClick={() =>
                document.getElementById("recommend").scrollIntoView({
                  behavior: "smooth"
                })
              }
            >
              Get Crop Recommendation →
            </button>
          </div>

          <div className="hero-card">
            <div className="card-icon">🌱</div>
            <h3>Smart Agriculture</h3>
            <p>
              Data-driven insights to help farmers make informed crop
              decisions.
            </p>
          </div>
        </section>

        <section className="recommend-section" id="recommend">
          <div className="section-heading">
            <p className="tag">AI CROP RECOMMENDATION</p>
            <h2>Find the right crop</h2>
            <p>
              Enter basic agricultural information to receive an
              AI-assisted recommendation.
            </p>
          </div>

          <div className="recommend-card">
            <div className="form-group">
              <label>Soil Type</label>
              <select value={soil} onChange={(e) => setSoil(e.target.value)}>
                <option value="">Select soil type</option>
                <option value="Alluvial">Alluvial</option>
                <option value="Black">Black</option>
                <option value="Red">Red</option>
                <option value="Loamy">Loamy</option>
                <option value="Sandy">Sandy</option>
              </select>
            </div>

            <div className="form-group">
              <label>Location</label>
              <select
                value={location}
                onChange={(e) => setLocation(e.target.value)}
              >
                <option value="">Select location</option>
                <option value="Tamil Nadu">Tamil Nadu</option>
                <option value="Kerala">Kerala</option>
                <option value="Karnataka">Karnataka</option>
                <option value="Andhra Pradesh">Andhra Pradesh</option>
                <option value="Telangana">Telangana</option>
              </select>
            </div>

            <div className="form-group">
              <label>Soil pH</label>
              <input
                type="number"
                step="0.1"
                min="0"
                max="14"
                placeholder="Enter pH (e.g. 6.5)"
                value={ph}
                onChange={(e) => setPh(e.target.value)}
              />
            </div>

            <div className="form-group">
              <label>Nitrogen (N)</label>
              <input
                type="number"
                placeholder="e.g. 90"
                value={nitrogen}
                onChange={(e) => setNitrogen(e.target.value)}
              />
            </div>

            <div className="form-group">
              <label>Phosphorus (P)</label>
              <input
                type="number"
                placeholder="e.g. 45"
                value={phosphorus}
                onChange={(e) => setPhosphorus(e.target.value)}
              />
            </div>

            <div className="form-group">
              <label>Potassium (K)</label>
              <input
                type="number"
                placeholder="e.g. 40"
                value={potassium}
                onChange={(e) => setPotassium(e.target.value)}
              />
            </div>

            <button className="recommend-btn" onClick={getRecommendation}>
              Analyze & Recommend
            </button>
          </div>

          {result && (
            <div className="result-card">
              <p className="tag">AI RESULT</p>
              <h3>{result.crop}</h3>
              <p>{result.reason}</p>

              {result.score !== undefined && (
                <p>
                  <strong>Suitability Score:</strong> {result.score}/100
                </p>
              )}
            </div>
          )}
        </section>

        <section className="features" id="about">
          <div>
            <span>01</span>
            <h3>Structured Data</h3>
            <p>A relational database organizes agricultural information efficiently.</p>
          </div>

          <div>
            <span>02</span>
            <h3>AI Assistance</h3>
            <p>AI helps transform agricultural inputs into useful recommendations.</p>
          </div>

          <div>
            <span>03</span>
            <h3>Simple Interface</h3>
            <p>A clean portal makes agricultural information easier to access.</p>
          </div>
        </section>
      </main>

      <footer>
        <p>© 2026 Team Primary Key • Smart Agriculture Intelligence Portal</p>
      </footer>
    </div>
  );
}

export default App;