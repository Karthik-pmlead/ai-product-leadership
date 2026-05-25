function AlertsPanel({ alerts }) {
  return (
    <div className="card">
      <h2>Risk Alerts</h2>

      {alerts.map(alert => (
        <div
          key={alert.id}
          style={{
            padding: '16px',
            marginBottom: '12px',
            border: '1px solid #334155',
            borderRadius: '8px'
          }}
        >
          <h3 className={`alert-${alert.risk_level.toLowerCase()}`}>
            {alert.risk_level} RISK
          </h3>

          <p>
            Transaction #{alert.transaction_id} flagged because:
          </p>

          <ul>
            {alert.reasons.map((reason, index) => (
              <li key={index}>{reason}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  )
}

export default AlertsPanel
