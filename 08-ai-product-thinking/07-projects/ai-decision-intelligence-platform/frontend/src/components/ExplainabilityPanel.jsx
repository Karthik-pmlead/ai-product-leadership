function ExplainabilityPanel({
  explanations,
  reasoning
}) {

  return (
    <div className="card">

      <h2>Explainability</h2>

      <h3>Explanations</h3>

      <ul>
        {explanations.map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>

      <h3>Reasoning</h3>

      <ul>
        {reasoning.map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>

    </div>
  );
}

export default ExplainabilityPanel;
