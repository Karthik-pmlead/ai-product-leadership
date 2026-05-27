import { useEffect, useState } from 'react'
import API from './api'
import RiskCard from './components/RiskCard'
import TransactionTable from './components/TransactionTable'
import AlertsPanel from './components/AlertsPanel'
import RiskTrendChart from './components/RiskTrendChart'

function App() {
  const [transactions, setTransactions] = useState([])
  const [alerts, setAlerts] = useState([])

  const fetchData = async () => {
    try {
      const txRes = await API.get('/transactions')
      const alertRes = await API.get('/alerts')

      setTransactions(txRes.data || [])
      setAlerts(alertRes.data || [])
    } catch (err) {
      console.error('API Error:', err)
    }
  }

  const simulateAttack = async () => {
    try {
      await API.post('/simulate')
      fetchData()
    } catch (err) {
      console.error('Simulation Error:', err)
    }
  }

  useEffect(() => {
    fetchData()

    const socket = new WebSocket('ws://localhost:8000/ws')

    socket.onopen = () => {
      console.log('WebSocket Connected')
    }

    socket.onmessage = event => {
      const tx = JSON.parse(event.data)

      setTransactions(prev => [tx, ...prev])
    }

    socket.onerror = error => {
      console.error('WebSocket Error:', error)
    }

    socket.onclose = () => {
      console.log('WebSocket Closed')
    }

    return () => socket.close()
  }, [])

  const highRisk = (alerts || []).filter(
    a => a.risk_level === 'HIGH'
  ).length

  const mediumRisk = (alerts || []).filter(
    a => a.risk_level === 'MEDIUM'
  ).length

  const lowRisk = (alerts || []).filter(
    a => a.risk_level === 'LOW'
  ).length

  return (
    <div className="container">
      <h1>FinTech Risk Intelligence Platform</h1>

      <button
        onClick={simulateAttack}
        style={{
          marginBottom: '20px',
          padding: '12px 20px',
          borderRadius: '8px',
          border: 'none',
          background: '#2563eb',
          color: 'white',
          cursor: 'pointer',
          fontWeight: 'bold'
        }}
      >
        Simulate Fraud Attack
      </button>

      <div className="grid">
        <RiskCard
          title="Transactions"
          value={transactions.length}
        />

        <RiskCard
          title="High Risk Alerts"
          value={highRisk}
        />

        <RiskCard
          title="Medium Risk"
          value={mediumRisk}
        />

        <RiskCard
          title="Low Risk"
          value={lowRisk}
        />
      </div>

      <RiskTrendChart alerts={alerts} />

      <div style={{ marginTop: '24px' }}>
        <TransactionTable
          transactions={transactions}
        />
      </div>

      <div style={{ marginTop: '24px' }}>
        <AlertsPanel alerts={alerts} />
      </div>
    </div>
  )
}

export default App
