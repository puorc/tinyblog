# -*- coding:utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash


def post(title):
    sql = 'delete from contents where title=' + "\"" + title + "\""
    g.db.execute(sql)
    g.db.commit()


def page(title):
    sql = 'delete from contents where title=' + "\"" + title + "\""
    g.db.execute(sql)
    g.db.commit()


def category(name):
    sql = 'delete from metas where name=' + "\"" + name + "\""
    g.db.execute(sql)
    g.db.commit()


def tag(name):
    sql = 'delete from metas where name=' + "\"" + name + "\""
    g.db.execute(sql)
    g.db.commit()


def comment():
    NotImplemented
