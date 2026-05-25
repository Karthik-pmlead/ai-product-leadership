import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell,
} from 'recharts'

function EngagementChart({ profile }) {
  const data = Object.entries(profile).map(
    ([category, value]) => ({
      category,
      value,
    })
  )

  return (
    <div className="card">
      <h2>User Interest Profile</h2>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="category" />
          <YAxis />
          <Tooltip />

          <Bar dataKey="value">
            {data.map((_, index) => (
              <Cell key={index} fill="#3b82f6" />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default EngagementChart
