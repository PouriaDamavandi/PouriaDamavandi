from github import Github
import datetime
import os

# Initialize GitHub
g = Github(os.environ['GITHUB_TOKEN'])
repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])

# Get recent activity
events = repo.get_events().get_page(0)[:10]  # Last 10 events

# Generate activity log
activity_log = "# Recent Activity\n\n"
for event in events:
    if event.type in ['PushEvent', 'PullRequestEvent', 'IssuesEvent']:
        activity_log += f"- {event.type}: {event.created_at}\n"

# Update README
contents = repo.get_contents("README.md")
repo.update_file(contents.path, "Update activity log", activity_log, contents.sha)
