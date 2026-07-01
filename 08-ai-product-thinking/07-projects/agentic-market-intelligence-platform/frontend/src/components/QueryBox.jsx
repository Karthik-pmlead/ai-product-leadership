function QueryBox({
  company,
  setCompany,
  onAnalyze,
  loading
}) {
  return (
    <div
      style={{
        display: "flex",
        gap: "10px",
        marginTop: "20px"
      }}
    >
      <input
        value={company}
        onChange={(e) => setCompany(e.target.value)}
        placeholder="Enter company name"
        style={{
          flex: 1,
          padding: "12px"
        }}
      />

      <button
        onClick={onAnalyze}
        disabled={loading}
        style={{
          padding: "12px 20px"
        }}
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}

export default QueryBox;
