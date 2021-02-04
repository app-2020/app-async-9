#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:01:10 2021

@author: pepe
"""
#%%  Executing this cell will create the database with the two tables.

from sqlalchemy import create_engine, Column, Integer, Text, MetaData, Table, ForeignKey

engine = create_engine('sqlite:///blog.db')
 
metadata = MetaData()
posts = Table(
    'posts', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', Text),
    Column('content', Text),
    Column('author', Integer, ForeignKey("users.id"), nullable=False),
)

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', Text),
)

users.create(bind=engine)
posts.create(bind=engine)

insert_user1 = users.insert().values(username="pepegar")
insert_user2 = users.insert().values(username="otheruser")
engine.execute(insert_user1)
engine.execute(insert_user2)

insert_post = posts.insert().values(
    title = "This is my first post",
    content = "In this post I want to... yadda yadda yadda...",
    author = 1)
engine.execute(insert_post)

#%% accessing the data in the database

with engine.connect() as connection:
    
    users_query = """
        SELECT id, username
        FROM users
    """
    
    results = connection.execute(users_query)

    for user in results:
        print(user)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





























