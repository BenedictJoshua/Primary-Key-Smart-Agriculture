const featuredMetrics = [
  { label: 'Active farms', value: '1,284', note: 'Monitored in real time' },
  { label: 'Crop alerts', value: '42', note: 'Weather and disease updates' },
  { label: 'Yield uplift', value: '+18%', note: 'Across pilot regions' },
  { label: 'AI advice', value: '24/7', note: 'Guidance on demand' },
];

const actionCards = [
  {
    title: 'Crop recommendations',
    description: 'Suggest the right crop based on soil type, season, and location.',
    accent: 'from-emerald-400 to-lime-300',
  },
  {
    title: 'Weather-aware planning',
    description: 'Give farmers clear next steps when rain, heat, or pests are expected.',
    accent: 'from-amber-400 to-orange-300',
  },
  {
    title: 'Market insights',
    description: 'Show prices, demand trends, and the best time to sell produce.',
    accent: 'from-sky-400 to-cyan-300',
  },
];

const workflowSteps = [
  'Farmer enters location, soil, and crop interest.',
  'System compares database records, AI rules, and live signals.',
  'UI returns a recommendation card with actions and warnings.',
  'Farmer saves the plan, tracks updates, and revisits later.',
];

function App() {
  return (
    <main className="app-shell">
      <section className="hero-panel">
        <div className="hero-copy">
          <p className="eyebrow">Smart Agriculture Intelligence Portal</p>
          <h1>Clear farming guidance, built for speed in the field.</h1>
          <p className="hero-text">
            This interface is shaped for farmers and support teams who need quick,
            understandable agricultural information, not cluttered dashboards.
          </p>
          <div className="hero-actions">
            <button className="primary-button">Explore recommendations</button>
            <button className="secondary-button">View crop insights</button>
          </div>
        </div>

        <div className="hero-card">
          <div className="card-header">
            <span>Today’s field summary</span>
            <span className="status-pill">Live</span>
          </div>
          <div className="field-grid">
            <div>
              <strong>Soil</strong>
              <span>Loamy, balanced</span>
            </div>
            <div>
              <strong>Weather</strong>
              <span>Light rain expected</span>
            </div>
            <div>
              <strong>Risk</strong>
              <span>Moderate pest pressure</span>
            </div>
            <div>
              <strong>Advice</strong>
              <span>Delay watering, inspect leaves</span>
            </div>
          </div>
        </div>
      </section>

      <section className="metrics-row">
        {featuredMetrics.map((item) => (
          <article className="metric-card" key={item.label}>
            <span>{item.label}</span>
            <strong>{item.value}</strong>
            <p>{item.note}</p>
          </article>
        ))}
      </section>

      <section className="content-grid">
        <article className="panel">
          <p className="section-label">Core experience</p>
          <h2>What the UI should make easy</h2>
          <div className="card-list">
            {actionCards.map((card) => (
              <div className="feature-card" key={card.title}>
                <div className={`feature-accent ${card.accent}`} />
                <div>
                  <h3>{card.title}</h3>
                  <p>{card.description}</p>
                </div>
              </div>
            ))}
          </div>
        </article>

        <article className="panel workflow-panel">
          <p className="section-label">Recommended flow</p>
          <h2>Farmer journey</h2>
          <ol className="workflow-list">
            {workflowSteps.map((step) => (
              <li key={step}>{step}</li>
            ))}
          </ol>
        </article>
      </section>

      <section className="footer-panel">
        <div>
          <p className="section-label">UI head notes</p>
          <h2>Suggested system structure</h2>
          <p>
            Build the frontend around a dashboard layout, a recommendation detail
            page, a crop knowledge page, and a market insight page. Keep the visual
            language earthy, modern, and readable in outdoor conditions.
          </p>
        </div>
        <ul className="tag-row">
          <li>Dashboard</li>
          <li>Recommendations</li>
          <li>Crop library</li>
          <li>Market trends</li>
          <li>Alerts</li>
        </ul>
      </section>
    </main>
  );
}

export default App;
