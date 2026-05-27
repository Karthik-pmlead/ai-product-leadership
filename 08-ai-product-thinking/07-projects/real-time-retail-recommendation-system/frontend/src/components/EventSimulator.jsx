function EventSimulator() {
  const categories = ['Electronics', 'Sports', 'Fitness', 'Home']
  const events = ['view', 'click', 'cart', 'purchase']

  const sendEvent = async () => {
    const payload = {
      user_id: "u1",
      category:
        categories[Math.floor(Math.random() * categories.length)],
      event_type:
        events[Math.floor(Math.random() * events.length)],
    }

    await fetch('http://localhost:8000/event', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    })
  }

  return (
    <div className="card">
      <h2>User Event Simulation</h2>
      <p>Simulate real-time user behavior</p>

      <button onClick={sendEvent}>
        Simulate Event
      </button>
    </div>
  )
}

export default EventSimulator
