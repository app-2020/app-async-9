# -*- coding: utf-8 -*-

from flask import Flask, render_template
from sqlalchemy import create_engine

app = Flask("Example 2")

engine = create_engine("sqlite:///blog.db")

@app.route("/")
def index():
    
    users_query = """
      SELECT *
      FROM users
    """
    
    posts_query = """
      SELECT id, title
      FROM posts
    """
    
    with engine.connect() as connection:
        
        user_results = connection.execute(users_query)
        post_results = connection.execute(posts_query)
    
        return render_template("index.html",
                               users = user_results,
                               posts = post_results)

app.run()