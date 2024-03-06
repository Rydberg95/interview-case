from flask import Blueprint, render_template

blueprint = Blueprint("base", __name__)


@blueprint.route("/")
def index():
    return render_template("index.html")


@blueprint.route("/contact")
def contact():
    return render_template("contact.html")
