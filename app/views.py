from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/indexdb')
def indexdb():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('indexdb.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/logindb', methods=['GET', 'POST'])
def logindb():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/indexdb')
    return render_template('logindb.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/')
def index():
    
    user = current_user.get_id() or 'Guess'
    return render_template ('index.html', user = user)


@app.route('/login')
def login():
    
    return render_template('login.html' )


@app.route('/login/check', methods=['post'])
def login_check():
    # validate username and password
    user = User.get(request.form['username'])
    if (user and user.password == request.form['password']):
        login_user(user)
    else:
        flash('Username or password incorrect')

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

