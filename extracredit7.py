from typing import Text
import praw
import random
import datetime
import time
from textblob import TextBlob

reddit = praw.Reddit('charbot')

submission_url = 'https://old.reddit.com/r/BotTown2/comments/r49opt/is_it_too_late_to_join_a_bachelorette_league/'
submission = reddit.submission(url=submission_url)

while True:
    submission.comments.replace_more(limit=None)
    all_comments = []
    all_comments = submission.comments.list()

    if 'chodosh' in submission.title.lower():
            submission.upvote()
            print('upvoted submission')
    if 'trump' in submission.title.lower():
            submission.downvote()
            print('downvoted submission')
    for comment in all_comments:
        if 'chodosh' in comment.body.lower():
            comment.upvote()
            print('upvoted comment')
    for comment in all_comments:
        if 'trump' in comment.body.lower():
            comment.downvote()
            print('downvoted comment')
    for comment in all_comments:
        commentbody = TextBlob(str(comment.body))
        polarity = commentbody.sentiment.polarity
        subjectivity = commentbody.sentiment.subjectivity
        if 'chodosh' in comment.body.lower() and polarity > 0:
            comment.upvote()
            print('upvoted chodosh comment')
        if 'chodosh' in comment.body.lower() and polarity < 0:
            comment.downvote()
            print('downvoted chodosh comment')
    
    submission = random.choice(list(reddit.subreddit('BotTown2').hot(limit=None)))
