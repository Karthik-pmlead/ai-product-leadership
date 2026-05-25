import { useEffect, useState } from 'react'

import RecommendationList from './components/RecommendationList'
import MetricsPanel from './components/MetricsPanel'
import EventSimulator from './components/EventSimulator'
import EngagementChart from './components/EngagementChart'

function App() {
  const [recommendations, setRecommendations] = useState([])
  const [metrics, setMetrics] = useState({})
  const [profile, setProfile] = useState({})
  const [latestEvent, setLatestEvent] = useState(null)
  const [variant, setVariant] = useState("")

  useEffect(() => {
    fetchRecommendations()

    const ws = new WebSocket('ws://localhost:8000/ws')

    ws.onopen = () => {
      ws.send('connected')
    }

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data)

      setRecommendations(data.recommendations)
      setMetrics(data.metrics)
      setProfile(data.profile)
      setLatestEvent(data.latest_event)
      setVariant(data.variant)
    }

    return () => ws.close()
  }, [])

  const fetchRecommendations = async () => {
    const res = await fetch(
      'http://localhost:8000/recommendations?user_id=u1'
    )

    const data = await res.json()

    setRecommendations(data.recommendations)
    setMetrics(data.metrics)
    setProfile(data.profile)
    setVariant(data.variant)
  }

  return (
    <div className="app">
      <h1>Real-Time Retail Recommendation System</h1>

      {variant && (
        <div className="card">
          <h3>A/B Test Variant</h3>
          <p>User bucket: {variant}</p>
        </div>
      )}

      <div className="grid">
        <MetricsPanel metrics={metrics} />
        <EventSimulator />
      </div>

      <div className="grid">
        <RecommendationList recommendations={recommendations} />
        <EngagementChart profile={profile} />
      </div>

      {latestEvent && (
        <div className="card">
          <h3>Latest Event</h3>
          <p>
            {latestEvent.event_type} → {latestEvent.category}
          </p>
        </div>
      )}
    </div>
  )
}

export default App
