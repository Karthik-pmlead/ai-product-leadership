import CytoscapeComponent from "react-cytoscapejs"

function GraphView({ graph }) {

  if (!graph) return null

  const elements = [
    ...graph.nodes.map((n) => ({
      data: {
        id: n.id,
        label: `${n.label} (${n.risk})`,
      }
    })),

    ...graph.edges.map((e) => ({
      data: {
        source: e.source,
        target: e.target,
      }
    }))
  ]

  return (
    <div className="card">

      <h2>Risk Network Graph</h2>

      <CytoscapeComponent
        elements={elements}
        style={{
          width: "100%",
          height: "500px",
          background: "#0f172a"
        }}
        layout={{
          name: "cose"
        }}
        stylesheet={[
          {
            selector: "node",
            style: {
              label: "data(label)",
              "background-color": "#ef4444",
              color: "white",
              "text-valign": "center",
              "text-halign": "center",
              "font-size": "10px",
            }
          },
          {
            selector: "edge",
            style: {
              width: 2,
              "line-color": "#64748b",
            }
          }
        ]}
      />

    </div>
  )
}

export default GraphView
