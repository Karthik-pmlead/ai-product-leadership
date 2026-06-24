function RecommendationPanel({
  recommendations
}) {

  return (
    <div className="card">

      <h2>Recommendations</h2>

      <ul>
        {recommendations.map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>

    </div>
  );
}

export default RecommendationPanel;
