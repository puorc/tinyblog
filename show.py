# -*- coding:utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash


def post():
    cur = g.db.execute('select title from contents where type = "post" order by cid desc')
    contents = cur.fetchall()
    g.handle_type = 'post'
    return render_template('admin/metas.html', contents=contents)


def page():
    cur = g.db.execute('select title from contents where type = "page" order by cid desc ')
    contents = cur.fetchall()
    g.handle_type = 'page'
    return render_template('admin/metas.html', contents=contents)


def category():
    cur = g.db.execute('select name from metas where type = "category" order by cid desc')
    contents = cur.fetchall()
    g.handle_type = 'category'
    return render_template('admin/metas.html', contents=contents)


def tag():
    cur = g.db.execute('select name from metas where type = "tag" order by cid desc ')
    contents = cur.fetchall()
    g.handle_type = 'tag'
    return render_template('admin/metas.html', contents=contents)


def comment():
    NotImplemented


def ovewview():
    num = {}
    cur = g.db.execute('select count(name) from metas where type = "category"')
    contents = cur.fetchall()
    num['category'] = contents[0][0]
    cur = g.db.execute('select count(name) from metas where type = "tag"')
    contents = cur.fetchall()
    num['tag'] = contents[0][0]
    cur = g.db.execute('select count(title) from contents where type = "post"')
    contents = cur.fetchall()
    num['post'] = contents[0][0]
    cur = g.db.execute('select count(title) from contents where type = "page"')
    contents = cur.fetchall()
    num['page'] = contents[0][0]
    return render_template('admin/overview.html', num=num)
