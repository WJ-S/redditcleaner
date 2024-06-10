# v1.0

import praw
import time

# Replace these with your Reddit app's credentials
client_id = '<clientid>'
client_secret = '<secret>'
username = '<username>'
password = r'<password>'
user_agent = 'Some generic string here'

# Authenticate with Reddit
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)

def delete_items(items, item_type):
    count = 0
    for item in items:
        if item_type == 'post':
            print(f'  Deleting post: {item.title} (ID: {item.id})')
        elif item_type == 'comment':
            print(f'  Deleting comment: {item.body[:30]}... (ID: {item.id})')

        item.delete()
        count += 1

    print(f'  Deleted {count} {item_type}s in this batch.')
    return count

# Fetch the authenticated user's submissions and comments
user = reddit.redditor(username)

total_deleted_posts = 0
total_deleted_comments = 0

# Delete posts in batches
while True:
    posts = list(user.submissions.new(limit=25))
    if not posts:
        print('    No more posts to delete.')
        break
    total_deleted_posts += delete_items(posts, 'post')
    time.sleep(3)  # Adjust the sleep time as necessary, just to avoid rate limiting

# Delete comments in batches
while True:
    comments = list(user.comments.new(limit=25))
    if not comments:
        print('     No more comments to delete.')
        break
    total_deleted_comments += delete_items(comments, 'comment')
    time.sleep(3)  # Adjust the sleep time as necessary, just to avoid rate limiting

print(f'Total deleted posts: {total_deleted_posts}')
print(f'Total deleted comments: {total_deleted_comments}')
