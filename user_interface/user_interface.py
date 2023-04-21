from flask import Blueprint, session, render_template, url_for, redirect, \
        flash
from .forms import UserForm
from .login_user import login_user, logout_user

user = Blueprint('user', __name__,
        template_folder='templates/user_interface')

@user.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@user.route('/login', methods=['POST', 'GET'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        res = login_user(form.username.data, form.email.data,
                form.password.data, form.repeat_password.data)
        if res:
            flash(f"You've logged in as {form.username.data}", 'success')
            session['username'] = form.username.data
            return redirect(url_for('.index'))
        flash('Try again', 'error')
    return render_template('login.html', form=form)

@user.route('/logout')
def logout():
    if logout_user(session): flash("You've logged out", "success")
    return redirect(url_for('.index'))
