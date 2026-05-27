function TransactionTable({ transactions }) {
  return (
    <div className="card">
      <h2>Transactions</h2>

      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Amount</th>
            <th>Country</th>
            <th>Risk Score</th>
          </tr>
        </thead>

        <tbody>
          {transactions.map(tx => (
            <tr key={tx.id}>
              <td>{tx.id}</td>
              <td>{tx.user}</td>
              <td>${tx.amount}</td>
              <td>{tx.country}</td>
              <td>{tx.risk_score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default TransactionTable
