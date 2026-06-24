from data.sample_sales import sales_data


def analyze_sales_trends():

    declining_regions = []

    for region, value in sales_data.items():

        if value < 0:
            declining_regions.append(region)

    return {
        "declining_regions": declining_regions,
        "sales_data": sales_data
    }
