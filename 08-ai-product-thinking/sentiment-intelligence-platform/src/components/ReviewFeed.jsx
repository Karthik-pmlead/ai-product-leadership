function ReviewFeed({ reviews }) {
  return (
    <div>
      <h2>Live Review Feed</h2>

      {reviews.map(review => (
        <div
          className="review-card"
          key={review.id}
        >
          <h3>{review.language}</h3>

          <p>{review.text}</p>

          <div>
            <span
              className={`chip chip-${review.sentiment.toLowerCase()}`}
            >
              {review.sentiment}
            </span>

            <span className="chip">
              {review.topic}
            </span>
          </div>

          <p>
            Confidence: {review.confidence}
          </p>
        </div>
      ))}
    </div>
  )
}

export default ReviewFeed
