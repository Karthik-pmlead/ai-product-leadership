import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts"

function MetricsDashboard({ metrics }) {

  const data = [
    {
      name: "Events",
      value: metrics.events_processed || 0
    },
    {
      name: "Risk",
      value: metrics.high_risk_entities || 0
    },
    {
      name: "Anomalies",
      value: metrics.anomalies_detected || 0
    },
  ]

  return (
    <div className="card">

      <h2>Metrics</h2>

      <ResponsiveContainer width="100%" height={250}>

        <BarChart data={data}>

          <XAxis dataKey="name" stroke="#fff" />

          <YAxis stroke="#fff" />

          <Tooltip />

          <Bar dataKey="value" fill="#3b82f6" />

        </BarChart>

      </ResponsiveContainer>

    </div>
  )
}

export default MetricsDashboard
