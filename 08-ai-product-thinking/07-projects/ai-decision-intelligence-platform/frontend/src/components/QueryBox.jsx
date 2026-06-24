import { useState } from "react";

function QueryBox({ onAnalyze }) {

  const [query, setQuery] = useState("");

  const submit = () => {

    if (!query) return;

    onAnalyze(query);
  };

  return (
    <div className="card">

      <h2>Ask AI Analyst</h2>

      <textarea
        rows="4"
        placeholder="Why are conversions dropping?"
        value={query}
        onChange={(e) =>
          setQuery(e.target.value)
        }
      />

      <button onClick={submit}>
        Analyze
      </button>

    </div>
  );
}

export default QueryBox;
