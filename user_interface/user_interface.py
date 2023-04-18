from flask import Blueprint, render_template
from .forms import UserForm
from .login_user import login_user

user = Blueprint('user', __name__,
        template_folder='templates/user_interface')

@user.route('/login', methods=['POST', 'GET'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        res = login_user(form.username.data, form.email.data,
                form.password.data, form.repeat_password.data)
        if res: return "OK"
    return render_template('login.html', form=form)

