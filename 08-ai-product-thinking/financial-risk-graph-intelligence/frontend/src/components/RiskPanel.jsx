function RiskPanel({ alerts }) {

  return (
    <div className="card">

      <h2>High Risk Entities</h2>

      {alerts.length === 0 && (
        <p>No critical alerts</p>
      )}

      {alerts.map((a) => (
        <div className="alert" key={a.id}>

          <strong>{a.label}</strong>

          <div>
            Risk Score: {a.risk}
          </div>

        </div>
      ))}

    </div>
  )
}

export default RiskPanel
