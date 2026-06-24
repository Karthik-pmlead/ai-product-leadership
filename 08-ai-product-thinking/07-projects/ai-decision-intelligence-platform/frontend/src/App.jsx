import { useEffect, useState } from "react";

import { analyzeQuery } from "./services/api";
import { createWebSocket } from "./services/api";

import QueryBox from "./components/QueryBox";
import AIInsightsPanel from "./components/AIInsightsPanel";
import RecommendationPanel from "./components/RecommendationPanel";
import ExplainabilityPanel from "./components/ExplainabilityPanel";
import WorkflowTimeline from "./components/WorkflowTimeline";
import MetricsDashboard from "./components/MetricsDashboard";
import TrendChart from "./components/TrendChart";
import AgentActivityPanel from "./components/AgentActivityPanel";

function App() {

  const [response, setResponse] = useState(null);

  useEffect(() => {

    const ws = createWebSocket((data) => {

      setResponse(data);
    });

    return () => ws.close();

  }, []);

  const handleAnalyze = async (query) => {

    const result = await analyzeQuery(query);

    setResponse(result);
  };

  return (
    <div className="app-container">

      <h1>
        AI Decision Intelligence Platform
      </h1>

      <QueryBox onAnalyze={handleAnalyze} />

      {response && (
        <>
          <AIInsightsPanel
            summary={response.summary}
            insights={response.insights}
          />

          <RecommendationPanel
            recommendations={response.recommendations}
          />

          <ExplainabilityPanel
            explanations={response.explanations}
            reasoning={response.reasoning}
          />

          <MetricsDashboard
            metrics={response.metrics}
          />

          <TrendChart
            sales={response.sales_trends.sales_data}
          />

          <WorkflowTimeline
            workflow={response.workflow}
          />

          <AgentActivityPanel
            anomalies={response.anomalies}
          />
        </>
      )}

    </div>
  );
}

export default App;
