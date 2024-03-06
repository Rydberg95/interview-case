from flask import Blueprint, render_template, redirect, url_for
from flaskr.models import InsuranceClaim
from flaskr.helper import generate_claim_id, generate_random_claim_cost
from flaskr.extensions import db

blueprint = Blueprint("base", __name__)


@blueprint.route("/")
def index():
    return render_template("index.html")


@blueprint.route("/generate_random_claim")
def generate_random_claim():
    new_claim = InsuranceClaim(
        claim_reference=generate_claim_id(), claim_cost=generate_random_claim_cost()
    )
    db.session.add(new_claim)
    db.session.commit()
    return redirect(url_for("base.claims"))


@blueprint.route("/claims")
def claims():
    allInsuranceClaims = InsuranceClaim.query.all()
    return render_template("claims.html", all_insurance_claims=allInsuranceClaims)
