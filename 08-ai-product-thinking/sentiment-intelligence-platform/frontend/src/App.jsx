import { useEffect, useState } from 'react'

import API from './api'

import MetricCard from './components/MetricCard'
import ReviewFeed from './components/ReviewFeed'
import SentimentChart from './components/SentimentChart'
import LanguageChart from './components/LanguageChart'
import MlopsPanel from './components/MlopsPanel'

import AlertBanner from './components/AlertBanner'
import TopicAnalytics from './components/TopicAnalytics'

function App() {
  const [reviews, setReviews] = useState([])
  const [metrics, setMetrics] = useState({})

  const fetchData = async () => {
    try {
      const reviewsRes = await API.get('/reviews')

      const metricsRes = await API.get('/metrics')

      setReviews(reviewsRes.data || [])

      setMetrics(metricsRes.data || {})
    } catch (err) {
      console.error(err)
    }
  }

  const simulateSpike = async () => {
    for (let i = 0; i < 5; i++) {
      await API.post('/simulate')
    }

    fetchData()
  }

  useEffect(() => {
    fetchData()

    const socket = new WebSocket(
      'ws://localhost:8000/ws'
    )

    socket.onmessage = event => {
      const review = JSON.parse(event.data)

      setReviews(prev => [review, ...prev])
    }

    return () => socket.close()
  }, [])

  const positive = reviews.filter(
    r => r.sentiment === 'POSITIVE'
  ).length

  const negative = reviews.filter(
    r => r.sentiment === 'NEGATIVE'
  ).length

  const neutral = reviews.filter(
    r => r.sentiment === 'NEUTRAL'
  ).length

  return (
    <div className="container">
      <h1>
        Multilingual Sentiment Intelligence Platform
      </h1>

      <p className="subtitle">
         Real-time AI-powered review analytics and operational intelligence
      </p>

      <AlertBanner reviews={reviews} />

      <button onClick={simulateSpike}>
        Simulate Review Spike
      </button>

      <div
        className="grid"
        style={{ marginTop: '24px' }}
      >
        <MetricCard
          title="Reviews Processed"
          value={reviews.length}
        />

        <MetricCard
          title="Positive"
          value={positive}
        />

        <MetricCard
          title="Negative"
          value={negative}
        />

        <MetricCard
          title="Avg Confidence"
          value={metrics.avg_confidence || 0}
        />
      </div>

      <div style={{ marginTop: '32px' }}>
        <SentimentChart reviews={reviews} />
      </div>

      <div style={{ marginTop: '32px' }}>
        <LanguageChart metrics={metrics} />
      </div>

      <div style={{ marginTop: '32px' }}>
        <MlopsPanel metrics={metrics} />
      </div>

      <div style={{ marginTop: '32px' }}>
        <TopicAnalytics reviews={reviews} />
      </div>

      <div style={{ marginTop: '32px' }}>
        <ReviewFeed reviews={reviews} />
      </div>
    </div>
  )
}

export default App
