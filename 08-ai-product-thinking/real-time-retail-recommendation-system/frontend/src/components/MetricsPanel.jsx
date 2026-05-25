function MetricsPanel({ metrics }) {
  return (
    <div className="card">
      <h2>Recommendation Metrics</h2>

      <div className="metric">
        Events Processed:{' '}
        {metrics.events_processed}
      </div>

      <div className="metric">
        Recommendation Updates:{' '}
        {metrics.recommendation_updates}
      </div>

      <div className="metric">
        CTR: {metrics.ctr}
      </div>

      <div className="metric">
        Conversion Rate:{' '}
        {metrics.conversion_rate}
      </div>
    </div>
  )
}

export default MetricsPanel
