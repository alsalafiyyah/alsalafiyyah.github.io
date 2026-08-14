import json
import os
from pathlib import Path
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

PROPERTY_ID = os.getenv("GA_PROPERTY_ID")
CREDENTIALS_JSON = os.getenv("GA_SERVICE_ACCOUNT_KEY")
OUTPUT_PATH = Path("_data/popular_posts.json")


def fetch_popular_posts():
    if not PROPERTY_ID or not CREDENTIALS_JSON:
        raise ValueError("Missing GA_PROPERTY_ID or GA_SERVICE_ACCOUNT_KEY environment variables.")

    # Temporarily write credentials JSON for Google Authentication
    cred_file = Path("ga_credentials.json")
    cred_file.write_text(CREDENTIALS_JSON, encoding="utf-8")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(cred_file)

    try:
        client = BetaAnalyticsDataClient()

        request = RunReportRequest(
            property=f"properties/{PROPERTY_ID}",
            dimensions=[Dimension(name="pagePath")],
            metrics=[Metric(name="screenPageViews")],
            date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
            limit=30,  # Fetch extra to filter out non-post URLs
        )

        response = client.run_report(request)

        popular_posts = []
        for row in response.rows:
            path = row.dimension_values[0].value

            # Ignore homepage, tag pages, feeds, or asset paths
            if path in ["/", "/index.html", "/about/", "/search/"] or path.startswith("/assets/"):
                continue

            popular_posts.append({"url": path})

            # Stop once we collect top 10 valid post paths
            if len(popular_posts) >= 10:
                break

        # Ensure _data directory exists
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

        # Write output to Jekyll data directory
        OUTPUT_PATH.write_text(json.dumps(popular_posts, indent=2), encoding="utf-8")
        print(f"Successfully wrote {len(popular_posts)} popular posts to {OUTPUT_PATH}")

    finally:
        # Clean up temporary credentials file
        if cred_file.exists():
            cred_file.unlink()


if __name__ == "__main__":
    fetch_popular_posts()