import sqlite3, os.path, add, show, delete, change, index
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing

app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('TINYBLOGPY_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()
    cur = g.db.execute('SELECT sitename, description FROM options')
    g.info = cur.fetchall()[0]


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def root():
    contents = {}
    contents['page'] = index.list_pages()
    contents['post'] = index.list_posts()
    contents['category'] = index.list_categories()
    contents['tag'] = index.list_tags()
    return render_template('theme/index.html', contents=contents)


@app.route('/post/<cid>')
def show_post(cid):
    contents = {}
    contents['page'] = index.list_pages()
    contents['text'] = index.show_post(cid)
    contents['category'] = index.list_categories()
    contents['tag'] = index.list_tags()
    return render_template('theme/post.html', contents=contents)


@app.route('/page/<cid>')
def show_page(cid):
    contents = {}
    contents['page'] = index.list_pages()
    contents['text'] = index.show_page(cid)
    return render_template('theme/page.html', contents=contents)


@app.route('/category/<cid>')
def show_category(cid):
    contents = {}
    contents['page'] = index.list_pages()
    contents['list_of_posts'] = index.show_category(cid)
    return render_template('theme/meta.html', contents=contents)


@app.route('/tag/<cid>')
def show_tag(cid):
    contents = {}
    contents['page'] = index.list_pages()
    contents['list_of_posts'] = index.show_tag(cid)
    return render_template('theme/meta.html', contents=contents)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('overview'))
    return render_template('admin/login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/admin/add/<type>', methods=['POST', 'GET'])
def admin_add(type):
    if not session.get('logged_in'):
        abort(401)
    g.handle_url = url_for("admin_add", type=type)
    g.handle_type = type
    if type == 'category':
        return add.category()
    elif type == 'tag':
        return add.tag()
    elif type == 'post':
        return add.post()
    elif type == 'page':
        return add.page()
    else:
        abort(404)


@app.route('/admin/')
def overview():
    if not session.get('logged_in'):
        abort(401)
    return show.ovewview()


@app.route('/test')
def test():
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
    return repr(tmp)


@app.route('/admin/<type>')
def admin_show(type):
    if not session.get('logged_in'):
        abort(401)
    g.handle_type = type
    g.handle_url = url_for("admin_add", type=type)
    if type == 'category':
        return show.category()
    elif type == 'tag':
        return show.tag()
    elif type == 'post':
        return show.post()
    elif type == 'page':
        return show.page()
    elif type == 'comment':
        return 'NotImplemented'
    else:
        abort(404)


@app.route('/admin/change', methods=['POST', 'GET'])
def admin_change():
    if not session.get('logged_in'):
        abort(401)
    if not request.method == 'POST':
        admin_change.handle_name = request.args.get('key', '')
        admin_change.handle_type = request.args.get('type', '')
    if admin_change.handle_type == 'category':
        return change.category(admin_change.handle_name)
    elif admin_change.handle_type == 'tag':
        return change.tag(admin_change.handle_name)
    elif admin_change.handle_type == 'post':
        return change.post(admin_change.handle_name)
    elif admin_change.handle_type == 'page':
        return change.page(admin_change.handle_name)
    else:
        abort(404)


admin_change.handle_name = ''
admin_change.handle_type = ''


@app.route('/admin/delete')
def admin_delete():
    if not session.get('logged_in'):
        abort(401)
    type = request.args.get('type', '')
    g.handle_url = url_for("admin_add", type=type)
    if type == 'category':
        delete.category(request.args.get('key', ''))
        return show.category()
    elif type == 'tag':
        delete.tag(request.args.get('key', ''))
        return show.tag()
    elif type == 'post':
        delete.post(request.args.get('key', ''))
        return show.post()
    elif type == 'page':
        delete.page(request.args.get('key', ''))
        return show.page()
    else:
        abort(404)


@app.route('/admin/settings', methods=['POST', 'GET'])
def settings():
    if not session.get('logged_in'):
        abort(401)
    if request.method == 'POST':
        g.db.execute('delete from options')
        g.db.execute('insert into options (sitename, description, defaultpage, numberofarticle) values (?, ?, ?, ?)',
                     [request.form['sitename'],
                      request.form['description'], request.form['defaultpage'], request.form['numberofarticle']])
        g.db.commit()
        return redirect(url_for('settings'))
    else:
        info = []
        cur = g.db.execute('select sitename, description from options')
        info = cur.fetchall()
        return render_template('admin/settings.html')


if __name__ == '__main__':
    if os.path.isfile(app.config['DATABASE']):
        pass
    else:
        init_db()
    app.run(host='0.0.0.0')
