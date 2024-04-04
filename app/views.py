#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Time    : 2024/4/2 17:43
# @Author  : Sepine Tam
# @File    : views.py
# @IDE     : PyCharm
# app/views.py
from flask import render_template, request, redirect, url_for, flash
from . import app, db
from .models import Post
from .forms import PostForm


@app.route('/')
def index():
    posts = Post.query.order_by(Post.pub_date.desc()).all()
    return render_template('index.html', posts=posts)


@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data, user_id=1)  # 临时使用固定的user_id
        db.session.add(new_post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('post.html', title='New Post', form=form)
