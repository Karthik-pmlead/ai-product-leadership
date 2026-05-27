import axios from "axios"

const API = "http://localhost:8000"

function EventSimulator() {

  const simulateRisk = async () => {

    await axios.post(`${API}/simulate-risk`, {
      entity_id: "fund_x",
      risk_delta: 30,
      reason: "Liquidity stress detected"
    })
  }

  const simulateNews = async () => {

    await axios.post(`${API}/simulate-news`)
  }

  return (
    <div className="card">

      <h2>Event Simulator</h2>

      <button onClick={simulateRisk}>
        Simulate Risk Event
      </button>

      <button onClick={simulateNews}>
        Simulate News Event
      </button>

    </div>
  )
}

export default EventSimulator
