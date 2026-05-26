function ExplainabilityPanel({ alerts, anomalies }) {

  return (
    <div className="card">

      <h2>Explainability Layer</h2>

      {alerts.map((a) => (
        <div
          className="node-info"
          key={a.id}
        >

          <strong>{a.label}</strong>

          <ul>
            <li>Connected to risky entities</li>
            <li>Risk propagated through graph network</li>
            <li>Triggered threshold-based alert</li>
          </ul>

        </div>
      ))}

      {anomalies.map((a, idx) => (
        <div
          className="node-info"
          key={idx}
        >

          <strong>{a.entity}</strong>

          <ul>
            <li>High network connectivity</li>
            <li>Abnormal risk concentration</li>
            <li>Potential contagion risk</li>
          </ul>

        </div>
      ))}

    </div>
  )
}

export default ExplainabilityPanel
