def generate_summary(
    insights,
    actions
):

    summary = (
        "The AI analyst detected operational "
        "and customer experience concerns "
        "impacting business performance."
    )

    # -----------------------------------
    # ENHANCE SUMMARY
    # -----------------------------------
    if len(insights) > 2:

        summary += (
            " Multiple negative business "
            "signals were identified."
        )

    if len(actions) > 0:

        summary += (
            " Immediate investigation "
            "and mitigation actions are recommended."
        )

    return summary
