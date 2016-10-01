# -*- coding:utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
import datetime


def category(name):
    if request.method == 'POST':
        g.db.execute('update metas set name="{new_name}", nickname="{new_nickname}" where name="{oldname}"'.format(
            new_name=request.form['metas_name'], new_nickname=request.form['metas_nickname'], oldname=name))
        g.db.commit()
        return redirect(url_for("admin_show", type="category"))
    else:
        sql = 'select * from metas where name=' + "\"" + name + "\""
        cur = g.db.execute(sql)
        contents = cur.fetchall()
        metas = {}
        metas['name'] = contents[0][1]
        metas['nickname'] = contents[0][3]
        return render_template('admin/change-metas.html', metas=metas)


def tag(name):
    if request.method == 'POST':
        g.db.execute('update metas set name="{new_name}", nickname="{new_nickname}" where name="{oldname}"'.format(
            new_name=request.form['metas_name'], new_nickname=request.form['metas_nickname'], oldname=name))
        g.db.commit()
        return redirect(url_for("admin_show", type="tag"))
    else:
        sql = 'select * from metas where name=' + "\"" + name + "\""
        cur = g.db.execute(sql)
        contents = cur.fetchall()
        metas = {}
        metas['name'] = contents[0][1]
        metas['nickname'] = contents[0][3]
        return render_template('admin/change-metas.html', metas=metas)


def post(title):
    if request.method == 'POST':
        post_date = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(
            datetime.datetime.now().day)
        g.db.execute(
            'update contents set title="{new_title}", text="{new_text}", date="{new_date}", textmd="{new_textmd}" where title="{oldtitle}"'.format(
                new_title=request.form['title'], new_text=request.form['test-editormd-html-code'], new_date=post_date,
                oldtitle=title, new_textmd=request.form['test-editormd-markdown-doc']))
        g.db.commit()
        return redirect(url_for("admin_show", type="post"))
    else:
        sql = 'select * from contents where title=' + "\"" + title + "\""
        cur = g.db.execute(sql)
        contents = cur.fetchall()
        content = {}
        content['title'] = contents[0][1]
        content['text'] = contents[0][2]
        content['textmd'] = contents[0][8]
        return render_template('admin/change-contents.html', content=content)


def page(title):
    if request.method == 'POST':
        post_date = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(
            datetime.datetime.now().day)
        g.db.execute(
            'update contents set title="{new_title}", text="{new_text}", date="{new_date}" where title="{oldtitle}"'.format(
                new_title=request.form['title'], new_text=request.form['text'], new_date=post_date,
                oldtitle=title))
        g.db.commit()
        return redirect(url_for("admin_show", type="page"))
    else:
        sql = 'select * from contents where title=' + "\"" + title + "\""
        cur = g.db.execute(sql)
        contents = cur.fetchall()
        content = {}
        content['title'] = contents[0][1]
        content['text'] = contents[0][2]
        return render_template('admin/change-contents.html', content=content)


def comment():
    NotImplemented
