import praw
import sys

# Reddit API Credentials (Replace with your own)
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USER_AGENT = "your_script_name"

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# Get username as input
username = sys.argv[1] if len(sys.argv) > 1 else input("Enter Reddit username: ")

# Fetch user comments
user = reddit.redditor(username)
comments = []

# Fetch all comments (PRAW can only fetch up to ~1000 comments per call)
for comment in user.comments.new(limit=None):  # Fetch all available comments
    comments.append({
        "created_utc": comment.created_utc,  # Timestamp for sorting
        "body": comment.body,
        "post_title": comment.submission.title,  # Get the title of the post
        "post_url": comment.submission.url,  # Link to the original post
        "comment_permalink": f"https://www.reddit.com{comment.permalink}"
    })

# Sort comments by oldest
sorted_comments = sorted(comments, key=lambda x: x["created_utc"])

# Print results
for c in sorted_comments[:10]:  # Display the first 10 oldest comments
    print(f"Post: {c['post_title']} ({c['post_url']})")
    print(f"Comment: {c['body']}")
    print(f"Link to comment: {c['comment_permalink']}")
    print("-" * 80)
