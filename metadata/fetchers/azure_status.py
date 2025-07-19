import feedparser
from datetime import datetime

def fetch_azure_status():
    try:
        url = "https://status.azure.com/en-us/status/feed/"
        feed = feedparser.parse(url)

        status_summary = []
        for entry in feed.entries[:5]:  # Limit to recent 5 events
            status_summary.append({
                "title": entry.title,
                "published": entry.published,
                "summary": entry.summary
            })

        return {
            "fetched_at": datetime.utcnow().isoformat() + "Z",
            "status_updates": status_summary
        }

    except Exception as e:
        return {"error": str(e)}
