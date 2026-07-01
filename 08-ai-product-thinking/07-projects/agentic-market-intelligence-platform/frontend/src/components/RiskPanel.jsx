function RiskPanel({ risks = [] }) {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        padding: "20px"
      }}
    >
      <h3>Strategic Risks</h3>

      <ul>
        {risks.map((risk, idx) => (
          <li key={idx}>{risk}</li>
        ))}
      </ul>
    </div>
  );
}

export default RiskPanel;
