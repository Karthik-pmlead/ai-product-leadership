import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell
} from 'recharts'

function SentimentChart({ reviews }) {
  const positive = reviews.filter(
    r => r.sentiment === 'POSITIVE'
  ).length

  const negative = reviews.filter(
    r => r.sentiment === 'NEGATIVE'
  ).length

  const neutral = reviews.filter(
    r => r.sentiment === 'NEUTRAL'
  ).length

  const data = [
    {
      name: 'Positive',
      value: positive,
      color: '#22c55e'
    },

    {
      name: 'Negative',
      value: negative,
      color: '#ef4444'
    },

    {
      name: 'Neutral',
      value: neutral,
      color: '#facc15'
    }
  ]

  return (
    <div className="card">
      <h2>Sentiment Distribution</h2>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis
            dataKey="name"
            stroke="#cbd5e1"
          />

          <YAxis stroke="#cbd5e1" />

          <Tooltip />

          <Bar dataKey="value">
            {data.map((entry, index) => (
              <Cell
                key={`cell-${index}`}
                fill={entry.color}
              />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default SentimentChart
