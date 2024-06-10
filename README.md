Reddit Post and Comment Deletion Script
This Python script allows you to delete all posts and comments from a specified Reddit account in batches using the praw (Python Reddit API Wrapper) library.

Requirements
  Python 3.x
  praw library

You can install the praw library using pip:
  pip install praw

Setup
  Create a Reddit app to obtain the necessary credentials:

    Go to https://www.reddit.com/prefs/apps
    Click "Create App" or "Create Another App"
    Fill out the form with the required details. Set the "Redirect URI" to http://localhost:8000 or any other URL.
    Note down the client_id, client_secret, and user_agent.
    Replace the placeholder values in the script with your Reddit app's credentials and Reddit account details:

      client_id = '<clientid>'
      client_secret = '<secret>'
      username = '<username>'
      password = r'<password>'

Script Explanation
  Authentication: The script authenticates with Reddit using the provided credentials.
  Delete Items Function: A function delete_items is defined to delete a batch of posts or comments. It prints the details of each deleted item.
  Delete Posts: The script fetches the authenticated user's submissions (posts) in batches of 25 and deletes them.
  Delete Comments: The script fetches the authenticated user's comments in batches of 25 and deletes them.
  Rate Limiting: The script includes a sleep time (time.sleep(3)) between each batch deletion to avoid hitting Reddit's rate limits. Adjust this time if necessary.

Output
  The script will output the details of each deleted post and comment, and finally, it will print the total number of deleted posts and comments.

Important Notes
  Irreversible Action: Deleting posts and comments is irreversible. Ensure you have backups or are sure you want to delete the content permanently.
