import {
  PieChart,
  Pie,
  Tooltip,
  ResponsiveContainer,
  Legend,
  Cell
} from 'recharts'

function LanguageChart({ metrics }) {
  const distribution =
    metrics.language_distribution || {}

  const data = Object.entries(distribution).map(
    ([key, value]) => ({
      name: key,
      value
    })
  )

  const COLORS = [
    '#22c55e',
    '#3b82f6',
    '#f59e0b',
    '#ef4444',
    '#a855f7'
  ]

  return (
    <div className="card">
      <h2>Language Distribution</h2>

      <ResponsiveContainer width="100%" height={300}>
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            outerRadius={100}
            label={({ name }) => name}
          >
            {data.map((entry, index) => (
              <Cell
                key={`cell-${index}`}
                fill={
                  COLORS[
                    index % COLORS.length
                  ]
                }
              />
            ))}
          </Pie>

          <Tooltip />

          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  )
}

export default LanguageChart
