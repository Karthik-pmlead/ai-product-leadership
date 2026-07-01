function AgentWorkflow() {
  const agents = [
    "Planner Agent",
    "Market Analyst Agent",
    "Executive Brief Agent"
  ];

  return (
    <div
      style={{
        marginTop: "30px",
        border: "1px solid #ddd",
        padding: "20px"
      }}
    >
      <h2>Agent Workflow</h2>

      {agents.map((agent) => (
        <div
          key={agent}
          style={{
            marginBottom: "10px"
          }}
        >
          ✓ {agent}
        </div>
      ))}
    </div>
  );
}

export default AgentWorkflow;
