import praw
from datetime import datetime

reddit = praw.Reddit('thabot')

subreddit = reddit.subreddit("superstonk")

#Get last 5 comments of author
def comment_five(a):
    print("Last 5 comments:")
    print("_____________")
    for comment in reddit.redditor(a).comments.new(limit=5):
        print("Sub:",comment.subreddit)
        print("Submission title:",comment.submission.title)
        print("Comment:",comment.body.split("\n", 1)[0][:79])
        
        
        print("---------------")


#Get top submission of author		
def top_submission(a):
    for submission in reddit.redditor(a).submissions.top('all',limit=1):
        print("Top Submission:",submission.title)

#Get submission count of author
def submission_count(a):
    counter = 0
    submissions = reddit.redditor(a).submissions.new(limit=None)

    for submission in submissions:
        counter += 1
    if counter ==1000:
        counter = "Over 1k"

    print("Total Submissions:",counter)


#Get comment count of author
def comment_count(a):
    counter = 0
    comments = reddit.redditor(a).comments.new(limit=None)

    for comment in comments:
        counter += 1
    
    if counter ==1000:
        counter = "Over 1k"

    print("Total Comments:",counter)


#Run the script. Limiting to 5 for testing. But should be run constantly. Have to test more and add posting functionality.
for post in subreddit.new(limit=5):

    print("*********")
    print("Hi! I'm Thabot. I was created to give you a bit of info on OP. Here's the deets:")
    print()
    
    print("Username:",post.author)
    
    print("Karma:",post.author.comment_karma)
    
    print("Account created on:",str(datetime.fromtimestamp(post.author.created_utc)))
   
    submission_count(str(post.author))
    
    comment_count(str(post.author))
    
    top_submission(str(post.author))
    
    comment_five(str(post.author))
