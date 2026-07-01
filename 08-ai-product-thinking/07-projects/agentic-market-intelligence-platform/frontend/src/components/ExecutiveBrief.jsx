function ExecutiveBrief({ summary }) {
  return (
    <div
      style={{
        marginTop: "30px",
        border: "1px solid #ddd",
        padding: "20px"
      }}
    >
      <h2>Executive Brief</h2>

      <p>{summary}</p>
    </div>
  );
}

export default ExecutiveBrief;
