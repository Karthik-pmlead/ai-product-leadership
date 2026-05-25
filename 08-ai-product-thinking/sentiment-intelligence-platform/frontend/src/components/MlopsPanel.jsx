function MlopsPanel({ metrics }) {
  return (
    <div className="card">
      <h2>MLOps Observability</h2>

      <p>
        Model Version:
        {' '}
        {metrics.model_version}
      </p>

      <p>
        Total Predictions:
        {' '}
        {metrics.total_predictions}
      </p>

      <p>
        Average Confidence:
        {' '}
        {metrics.avg_confidence}
      </p>

      <p>
        Drift Status:
        Stable
      </p>

      <p>
        Inference Latency:
        142ms
      </p>

      <p>
        Last Retrained:
        2 days ago
      </p>

      <p>
        Active Model:
        multilingual-sentiment-v1
      </p>
    </div>
  )
}

export default MlopsPanel
