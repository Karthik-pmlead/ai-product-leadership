function WorkflowTimeline({
  workflow
}) {

  return (
    <div className="card">

      <h2>Agent Workflow Timeline</h2>

      <ol>
        {workflow.map((step, idx) => (
          <li key={idx}>
            {step}
          </li>
        ))}
      </ol>

    </div>
  );
}

export default WorkflowTimeline;
