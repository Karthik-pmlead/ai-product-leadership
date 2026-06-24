def generate_summary(
    insights,
    actions
):

    summary = (
        "The platform detected declining operational "
        "and customer experience signals."
    )

    if len(actions) > 0:
        summary += (
            " Immediate investigation is recommended."
        )

    return summary
