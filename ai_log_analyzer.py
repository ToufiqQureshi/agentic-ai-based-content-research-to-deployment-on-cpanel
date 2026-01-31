import os
import re
from collections import Counter
from datetime import datetime

def analyze_server_logs(log_file_path):
    """
    Analyzes server access logs to detect AI bot activity.
    Returns a summary of AI hits.
    """

    # Known AI User-Agents
    ai_bots = {
        "GPTBot": "OpenAI Crawler (Training)",
        "ChatGPT-User": "ChatGPT Browsing (User Query)",
        "Google-Extended": "Gemini/Bard",
        "ClaudeBot": "Claude AI",
        "PerplexityBot": "Perplexity AI",
        "Amazonbot": "Alexa/Amazon",
        "FacebookBot": "Meta AI",
        "Applebot": "Siri/Apple Intelligence"
    }

    ai_hits = Counter()
    details = []

    if not os.path.exists(log_file_path):
        return "❌ Log file not found."

    with open(log_file_path, 'r') as f:
        for line in f:
            for bot_sign, bot_name in ai_bots.items():
                if bot_sign in line:
                    ai_hits[bot_name] += 1
                    # Extract timestamp and URL if possible (Common Log Format)
                    # Example: 127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
                    details.append(f"[{bot_name}] found in line: {line[:100]}...")

    report = "🤖 **AI Bot Traffic Report**\n"
    report += "=" * 30 + "\n"

    if not ai_hits:
        report += "No AI bots detected in logs.\n"
    else:
        for bot, count in ai_hits.most_common():
            report += f"• {bot}: {count} hits\n"

    return report

# Example Usage (Commented out)
# print(analyze_server_logs("/var/log/apache2/access.log"))
