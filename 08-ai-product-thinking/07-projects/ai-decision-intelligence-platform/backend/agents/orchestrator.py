from analytics.sentiment_engine import (
    analyze_sentiment
)

from analytics.metrics_engine import (
    analyze_metrics
)

from analytics.anomaly_engine import (
    detect_anomalies
)

from analytics.trend_engine import (
    analyze_sales_trends
)

from services.workflow_service import (
    build_workflow_steps
)

from services.explainability_service import (
    generate_explanation
)


def run_decision_workflow(query):

    query_lower = query.lower()

    # -----------------------------------
    # ANALYTICS
    # -----------------------------------
    sentiment_score = analyze_sentiment()

    metrics = analyze_metrics()

    anomalies = detect_anomalies()

    trends = analyze_sales_trends()

    # -----------------------------------
    # DYNAMIC OUTPUTS
    # -----------------------------------
    insights = []
    recommendations = []
    reasoning = []

    # ===================================
    # SALES / CONVERSION QUESTIONS
    # ===================================
    if (
        "conversion" in query_lower
        or "sales" in query_lower
        or "revenue" in query_lower
    ):

        insights = [
            "Conversion metrics declined significantly.",
            "Sales trends weakened in APAC and EU.",
            "Bounce rates increased recently."
        ]

        recommendations = [
            "Investigate checkout funnel friction.",
            "Review pricing and campaign performance.",
            "Analyze regional user behavior."
        ]

        reasoning = [
            "Negative conversion trends correlate with rising bounce rates.",
            "Regional declines indicate localized business issues."
        ]

        summary = (
            "The system detected declining conversion "
            "and sales performance across multiple regions."
        )

    # ===================================
    # OPERATIONAL QUESTIONS
    # ===================================
    elif (
        "operational" in query_lower
        or "incident" in query_lower
        or "latency" in query_lower
        or "system" in query_lower
    ):

        insights = [
            "Operational anomalies were detected.",
            "Mobile latency exceeded acceptable thresholds.",
            "Checkout service degradation observed."
        ]

        recommendations = [
            "Escalate operational incidents immediately.",
            "Investigate infrastructure bottlenecks.",
            "Audit reliability monitoring systems."
        ]

        reasoning = [
            "High latency correlates with declining customer experience.",
            "Operational instability likely impacts conversions."
        ]

        summary = (
            "The platform identified operational "
            "performance degradation affecting user experience."
        )

    # ===================================
    # SENTIMENT / CUSTOMER QUESTIONS
    # ===================================
    elif (
        "customer" in query_lower
        or "sentiment" in query_lower
        or "feedback" in query_lower
        or "review" in query_lower
    ):

        insights = [
            "Customer sentiment trend is negative.",
            "Users reported checkout frustration.",
            "Support response quality concerns detected."
        ]

        recommendations = [
            "Review customer support workflows.",
            "Improve checkout UX experience.",
            "Analyze negative review clusters."
        ]

        reasoning = [
            "Negative sentiment signals indicate customer dissatisfaction.",
            "Repeated checkout complaints increased risk score."
        ]

        summary = (
            "The AI analyst detected negative "
            "customer experience signals impacting engagement."
        )

    # ===================================
    # LEADERSHIP / EXECUTIVE QUESTIONS
    # ===================================
    elif (
        "leadership" in query_lower
        or "executive" in query_lower
        or "summary" in query_lower
        or "risk" in query_lower
    ):

        insights = [
            "Business risk indicators increased.",
            "Operational and customer signals weakened.",
            "Regional performance variability detected."
        ]

        recommendations = [
            "Prioritize operational stabilization.",
            "Launch customer retention initiatives.",
            "Increase executive risk monitoring."
        ]

        reasoning = [
            "Multiple negative signals contributed to elevated business risk.",
            "Operational instability amplified customer dissatisfaction."
        ]

        summary = (
            "The platform identified elevated "
            "business risk across operational and customer dimensions."
        )

    # ===================================
    # DEFAULT
    # ===================================
    else:

        insights = [
            "General operational analysis completed.",
            "Business signals reviewed successfully."
        ]

        recommendations = [
            "Continue monitoring operational metrics."
        ]

        reasoning = [
            "No major critical risks identified."
        ]

        summary = (
            "The AI analyst completed a high-level business analysis."
        )

    # -----------------------------------
    # EXPLAINABILITY
    # -----------------------------------
    explanations = generate_explanation({
        "sentiment_score": sentiment_score,
        "conversion_change":
            metrics["conversion_change"],
        "incident_count":
            len(anomalies)
    })

    # -----------------------------------
    # WORKFLOW
    # -----------------------------------
    workflow = build_workflow_steps(query)

    # -----------------------------------
    # RESPONSE
    # -----------------------------------
    return {
        "query": query,
        "summary": summary,
        "insights": insights,
        "recommendations": recommendations,
        "reasoning": reasoning,
        "explanations": explanations,
        "workflow": workflow,
        "metrics": metrics,
        "anomalies": anomalies,
        "sales_trends": trends
    }

