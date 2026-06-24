import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function TrendChart({ sales }) {

  const data = Object.entries(sales).map(
    ([region, value]) => ({
      region,
      value
    })
  );

  return (
    <div className="card">

      <h2>Regional Sales Trends</h2>

      <BarChart
        width={500}
        height={300}
        data={data}
      >
        <CartesianGrid strokeDasharray="3 3" />

        <XAxis dataKey="region" />

        <YAxis />

        <Tooltip />

        <Bar dataKey="value" />
      </BarChart>

    </div>
  );
}

export default TrendChart;
