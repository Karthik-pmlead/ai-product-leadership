function RecommendationPanel({
  recommendations = []
}) {
  return (
    <div
      style={{
        marginTop: "30px",
        border: "1px solid #ddd",
        padding: "20px"
      }}
    >
      <h3>Recommended Actions</h3>

      <ul>
        {recommendations.map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default RecommendationPanel;
