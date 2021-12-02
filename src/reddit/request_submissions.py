import praw
from src.reddit.redditsecrets import *

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    #password=PASSWORD,
    user_agent=USER_AGENT,
    #username=USERNAME,
)

hot_posts = reddit.subreddit('AMA').hot(limit=100000)

with open("responses.txt", 'a') as f:
    for submission in hot_posts:
        submission.comments.replace_more(limit=None)
        threads = []
        for top_level_comment in submission.comments:
            this_thread = [[submission.author.name, submission.title + "\n" + submission.selftext]]
            if top_level_comment.author is not None:
                this_thread.append([top_level_comment.author.name, top_level_comment.body])
                for second_level_comment in top_level_comment.replies:
                    if second_level_comment.author is not None:
                        this_thread.append([second_level_comment.author.name, second_level_comment.body])
                        break
            threads.append(this_thread)
        f.write(str(threads))