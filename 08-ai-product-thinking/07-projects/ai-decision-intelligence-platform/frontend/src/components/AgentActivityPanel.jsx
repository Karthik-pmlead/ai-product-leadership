function AgentActivityPanel({
  anomalies
}) {

  return (
    <div className="card">

      <h2>Agent Activity</h2>

      <ul>
        {anomalies.map((item, idx) => (
          <li key={idx}>
            {item}
          </li>
        ))}
      </ul>

    </div>
  );
}

export default AgentActivityPanel;
