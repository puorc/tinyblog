from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash


def list_pages():
    cur = g.db.execute('select cid, title from contents where type = "page" order by cid desc ')
    return cur.fetchall()


def list_categories():
    cur = g.db.execute('select cid, name from metas where type = "category" order by cid desc ')
    return cur.fetchall()


def list_tags():
    cur = g.db.execute('select cid, name from metas where type = "tag" order by cid desc ')
    return cur.fetchall()


def list_posts():
    cur = g.db.execute('select cid, title, date, category, tag from contents where type = "post" order by cid desc ')
    a = cur.fetchall()
    tmp = []
    for item in a:
        cur = g.db.execute('select name from metas where cid={cid}'.format(cid=item[3]))
        cur1 = g.db.execute('select name from metas where cid={cid}'.format(cid=item[4]))
        tmp_item = list(item)
        tmp_item[3] = cur.fetchall()[0][0]
        tmp_item[4] = cur1.fetchall()[0][0]
        tmp_item = tuple(tmp_item)
        tmp.append(tmp_item)
    return tmp


def show_post(cid):
    cur = g.db.execute('select title, text, date, category, tag from contents where cid={cid}'.format(cid=cid))
    a = cur.fetchall()
    tmp = []
    for item in a:
        cur = g.db.execute('select name from metas where cid={cid}'.format(cid=item[3]))
        cur1 = g.db.execute('select name from metas where cid={cid}'.format(cid=item[4]))
        tmp_item = list(item)
        tmp_item[3] = cur.fetchall()[0][0]
        tmp_item[4] = cur1.fetchall()[0][0]
        tmp_item = tuple(tmp_item)
        tmp.append(tmp_item)
    return tmp


def show_page(cid):
    cur = g.db.execute('select title, text from contents where cid={cid}'.format(cid=cid))
    return cur.fetchall()


def show_category(cid):
    cur = g.db.execute('select cid, title from contents where category={cid}'.format(cid=cid))
    return cur.fetchall()


def show_tag(cid):
    cur = g.db.execute('select cid, title from contents where tag={cid}'.format(cid=cid))
    return cur.fetchall()
