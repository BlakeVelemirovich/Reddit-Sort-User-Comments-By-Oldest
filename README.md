# Reddit Comment Fetcher

## Description
This Python script retrieves a Reddit user's comments and the corresponding posts they commented on, sorted from oldest to newest. It uses the PRAW (Python Reddit API Wrapper) library to interact with the Reddit API. Since Reddit does not provide an option to sort user comments by oldest first, this script fetches all available comments and manually sorts them.

## Why Docker?
The script is containerized using Docker to ensure it can run on any system without requiring Python or additional dependencies. By using Docker, the script can be executed in a consistent environment across different devices, making it portable and easy to deploy without manual setup.

## Usage
1. Build the Docker image:
   ```sh
   docker build -t reddit-comment-fetcher .
   ```
2. Run the container with a Reddit username:
   ```sh
   docker run --rm reddit-comment-fetcher target_username
   ```

## Environment Variables
To avoid hardcoding credentials, the script reads Reddit API credentials from environment variables. These can be set when running the container:
```sh
docker run --rm \
    -e REDDIT_CLIENT_ID="your_client_id" \
    -e REDDIT_CLIENT_SECRET="your_client_secret" \
    -e REDDIT_USER_AGENT="your_script_name" \
    -e REDDIT_USERNAME="your_reddit_username" \
    -e REDDIT_PASSWORD="your_reddit_password" \
    reddit-comment-fetcher target_username
```

## Requirements
- A Reddit API account with credentials from https://www.reddit.com/prefs/apps
- Docker installed on your system

## Notes
Ensure that your Reddit API credentials are correct and that your app is registered as a **script** type application in the Reddit developer portal. The script requires a valid username and password to authenticate and fetch user comments.

