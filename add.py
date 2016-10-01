# -*- coding:utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
import datetime


def category():
    if request.method == 'POST':
        g.db.execute('insert into metas (name, type, nickname, count) values (?, ?, ?, ?)',
                     [request.form['metas_name'], 'category', request.form['metas_nickname'], 0])
        g.db.commit()
        return redirect(url_for("admin_show", type="category"))
    return render_template('admin/add-metas.html')


def tag():
    if request.method == 'POST':
        g.db.execute('insert into metas (name, type, nickname, count) values (?, ?, ?, ?)',
                     [request.form['metas_name'], 'tag', request.form['metas_nickname'], 0])
        g.db.commit()
        return redirect(url_for("admin_show", type="tag"))
    return render_template('admin/add-metas.html')


def post():
    if request.method == 'POST':
        post_date = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(
            datetime.datetime.now().day)
        g.db.execute(
            'insert into contents (title, text, date, category, tag, status, type, commentnum) values (?, ?, ?, ?, ?, ?, ?, ?)',
            [request.form['title'], request.form['text'], post_date, request.form['category'], request.form['tag'],
             'posted', 'post', 0])
        g.db.commit()
        return redirect(url_for("admin_show", type="post"))
    else:
        metas = {}
        cur = g.db.execute('select cid, name from metas where type = "category"')
        metas['category'] = cur.fetchall()
        cur = g.db.execute('select cid, name from metas where type = "tag"')
        metas['tag'] = cur.fetchall()
        return render_template('admin/add-contents.html', metas=metas)


def page():
    if request.method == 'POST':
        post_date = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(
            datetime.datetime.now().day)
        g.db.execute(
            'insert into contents (title, text, date, category, tag, status, type, commentnum) values (?, ?, ?, ?, ?, ?, ?, ?)',
            [request.form['title'], request.form['text'], post_date, 'no', 'no',
             'posted', 'page', 0])
        g.db.commit()
        return redirect(url_for("admin_show", type="page"))
    else:
        metas = None
        return render_template('admin/add-contents.html', metas=metas)


def comment():
    NotImplemented
