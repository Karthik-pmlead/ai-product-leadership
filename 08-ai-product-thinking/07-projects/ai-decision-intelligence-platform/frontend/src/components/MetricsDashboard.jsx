function MetricsDashboard({ metrics }) {

  return (
    <div className="card">

      <h2>Operational Metrics</h2>

      <ul>
        <li>
          Conversion Change:
          {metrics.conversion_change}%
        </li>

        <li>
          Bounce Rate Change:
          {metrics.bounce_rate_change}%
        </li>

        <li>
          Checkout Failure Rate:
          {metrics.checkout_failure_rate}%
        </li>

        <li>
          Mobile Latency:
          {metrics.mobile_latency} ms
        </li>
      </ul>

    </div>
  );
}

export default MetricsDashboard;
