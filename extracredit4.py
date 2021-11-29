import praw
import time

reddit = praw.Reddit('charbot')

count = 0
for submission in reddit.subreddit("TheEricAndreShow").hot(limit=300):
    a = submission.title
    b = submission.url
    try:
        reddit.subreddit('BotTown').submit(a, url=b)
    except praw.exceptions.RedditAPIException:
        pass
    count += 1
    print('reposted comments = ', count)
    time.sleep(1)
