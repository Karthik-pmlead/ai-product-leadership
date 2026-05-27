import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from 'recharts'

function RiskTrendChart({ alerts }) {
  const data = alerts.map((a, index) => ({
    name: index + 1,
    score: a.risk_score
  }))

  return (
    <div className="card" style={{ marginTop: '24px' }}>
      <h2>Risk Trend</h2>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="score" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}

export default RiskTrendChart
