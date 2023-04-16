from flask import Blueprint, render_template
from .forms import UserForm
user_interface = Blueprint('user_interface', __name__,
        template_folder='templates/user_interface')

@user_interface.route('/login', methods=['POST', 'GET'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        #TODO: create validation and commit to database
        pass
    return render_template('login.html', form=form)
