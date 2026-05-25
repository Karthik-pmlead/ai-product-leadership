function AlertBanner({ reviews }) {
  const negative = reviews.filter(
    r => r.sentiment === 'NEGATIVE'
  ).length

  if (negative < 3) {
    return null
  }

  return (
    <div className="alert-banner">
      🚨 Negative sentiment spike detected.
      Product quality and logistics complaints
      increasing in real time.
    </div>
  )
}

export default AlertBanner
