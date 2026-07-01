
function OpportunityPanel({ opportunities = [] }) {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        padding: "20px"
      }}
    >
      <h3>Growth Opportunities</h3>

      <ul>
        {opportunities.map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default OpportunityPanel;
