import requests
import datetime
import os

API_KEY = os.getenv("BLOGGER_API_KEY")
BLOG_ID = os.getenv("BLOGGER_BLOG_ID")

post_data = {
    "kind": "blogger#post",
    "title": f"Automated Post {datetime.datetime.now()}",
    "content": "hi"
}

response = requests.post(
    f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts?key={API_KEY}",
    json=post_data
)

print(response.json())
