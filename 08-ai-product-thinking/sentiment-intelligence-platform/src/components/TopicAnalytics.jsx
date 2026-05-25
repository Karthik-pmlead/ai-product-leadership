function TopicAnalytics({ reviews }) {
  const topicCounts = {}

  reviews.forEach(review => {
    const topic = review.topic

    if (!topicCounts[topic]) {
      topicCounts[topic] = 0
    }

    topicCounts[topic] += 1
  })

  return (
    <div className="card">
      <h2>Topic Intelligence</h2>

      {Object.entries(topicCounts).map(
        ([topic, count]) => (
          <p key={topic}>
            {topic}: {count}
          </p>
        )
      )}
    </div>
  )
}

export default TopicAnalytics
