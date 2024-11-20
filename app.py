from flask import Flask, render_template, request, redirect, url_for, flash, abort
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Ensure the posts file exists
POSTS_FILE = 'posts.json'
if not os.path.exists(POSTS_FILE):
    with open(POSTS_FILE, 'w') as f:
        json.dump([], f)

def load_posts():
    try:
        with open(POSTS_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_posts(posts):
    with open(POSTS_FILE, 'w') as f:
        json.dump(posts, f, indent=4)

@app.route('/')
def home():
    posts = load_posts()
    posts.sort(key=lambda x: x['date'], reverse=True)  # Show newest first
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    posts = load_posts()
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        abort(404)
    return render_template('post_detail.html', post=post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True)