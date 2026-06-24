function AIInsightsPanel({
  summary,
  insights
}) {

  return (
    <div className="card">

      <h2>Executive Summary</h2>

      <p>{summary}</p>

      <h3>Insights</h3>

      <ul>
        {insights.map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>

    </div>
  );
}

export default AIInsightsPanel;
