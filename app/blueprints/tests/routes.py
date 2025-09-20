from flask import Blueprint, flash, redirect, render_template, url_for

# FORMS
from .forms import CreateUserForm

# SERVICES
from .services import create_user_test_service

tests_bp = Blueprint("tests", __name__)


# == HOME ==
@tests_bp.route("/")
def home():
    form = CreateUserForm()
    return render_template("tests/home.html", form=form)


# == REGISTRAR USUARIO ==
@tests_bp.route("/new/user", methods=["POST"])
def new_user():
    form = CreateUserForm()

    if form.validate_on_submit():
        name = form.name.data

        success, message, _ = create_user_test_service(name)

        if success:
            flash(message, "success_tests_home")
        else:
            flash(message, "error_tests_home")

    return redirect(url_for("tests.home"))
