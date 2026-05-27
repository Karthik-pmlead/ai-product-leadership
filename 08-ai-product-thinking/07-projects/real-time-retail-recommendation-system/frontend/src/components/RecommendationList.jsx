function RecommendationList({ recommendations }) {
  return (
    <div className="card">
      <h2>Personalized Recommendations</h2>

      {recommendations.map((product) => (
        <div key={product.id} className="product">

          {/* PRODUCT INFO */}
          <div>
            <strong>{product.name}</strong>
            <div>{product.category}</div>
          </div>

          {/* SCORE */}
          <div>
            Score: {Number(product.score).toFixed(2)}
          </div>

          {/* EXPLANATION LAYER */}
          <div style={{ marginTop: "10px", fontSize: "12px", color: "#94a3b8" }}>
            <strong>Why recommended:</strong>
            <ul>
              {product.reasons?.map((r, idx) => (
                <li key={idx}>{r}</li>
              ))}
            </ul>
          </div>

        </div>
      ))}
    </div>
  )
}

export default RecommendationList
