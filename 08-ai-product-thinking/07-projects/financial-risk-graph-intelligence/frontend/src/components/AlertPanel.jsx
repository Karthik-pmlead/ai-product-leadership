function AlertPanel({ anomalies }) {

  return (
    <div className="card">

      <h2>Anomaly Detection</h2>

      {anomalies.length === 0 && (
        <p>No anomalies detected</p>
      )}

      {anomalies.map((a, idx) => (
        <div className="alert" key={idx}>

          <strong>{a.entity}</strong>

          <div>{a.reason}</div>

          <div>
            Connections: {a.connections}
          </div>

        </div>
      ))}

    </div>
  )
}

export default AlertPanel
