import { useEffect, useState } from "react"
import axios from "axios"

import GraphView from "./components/GraphView"
import RiskPanel from "./components/RiskPanel"
import AlertPanel from "./components/AlertPanel"
import MetricsDashboard from "./components/MetricsDashboard"
import EventSimulator from "./components/EventSimulator"
import ExplainabilityPanel from "./components/ExplainabilityPanel"

const API = "http://localhost:8000"

function App() {

  const [graphData, setGraphData] = useState(null)
  const [alerts, setAlerts] = useState([])
  const [anomalies, setAnomalies] = useState([])
  const [metrics, setMetrics] = useState({})
  const [latestEvent, setLatestEvent] = useState(null)

  useEffect(() => {
    loadGraph()

    const ws = new WebSocket("ws://localhost:8000/ws")

    ws.onmessage = (event) => {

      const data = JSON.parse(event.data)

      setGraphData(data.graph)
      setAlerts(data.alerts || [])
      setAnomalies(data.anomalies || [])
      setMetrics(data.metrics || {})
      setLatestEvent(data.latest_event || data.news)
    }

    return () => ws.close()
  }, [])

  const loadGraph = async () => {

    const res = await axios.get(`${API}/graph`)

    setGraphData(res.data.graph)
    setAlerts(res.data.alerts)
    setAnomalies(res.data.anomalies)
    setMetrics(res.data.metrics)
  }

  return (
    <div className="container">

      <h1>Financial Risk Graph Intelligence Platform</h1>

      <EventSimulator />

      <div className="grid">

        <div>

          <GraphView graph={graphData} />

          <ExplainabilityPanel
            alerts={alerts}
            anomalies={anomalies}
          />

        </div>

        <div>

          <MetricsDashboard metrics={metrics} />

          <RiskPanel alerts={alerts} />

          <AlertPanel anomalies={anomalies} />

          {latestEvent && (
            <div className="card">
              <h3>Latest Event</h3>

              <pre>
                {JSON.stringify(latestEvent, null, 2)}
              </pre>
            </div>
          )}

        </div>

      </div>

    </div>
  )
}

export default App
