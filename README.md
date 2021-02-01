# Async session 9

This async session has a companion video you should see to understand today's
new concepts.  <https://www.youtube.com/watch?v=Zf0EYIVV2q4>

## Intro

Today we're going to talk about connecting to databases from our Flask
applications.  The library we will use for connecting to the databases is
called [sqlalchemy](https://www.sqlalchemy.org/)

## DB Structure

For todays example we will use a simple Database structure for a blog
application.

Our DB contains two tables, `users` and `posts`.  And there's a foreign
key between posts and users.

## Exercise

After you've finished the video, please implement the proposed exercise.  You'll
need to make the server answer to requests on `/post/<index>`, and render the post
with its title, content, and author's username.