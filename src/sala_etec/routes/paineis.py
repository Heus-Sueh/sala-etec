# sala_etec/routes/paineis.py

from flask import Blueprint, render_template

from sala_etec.decorators import login_required, role_required


paineis_bp = Blueprint(
    "paineis",
    __name__,
)


@paineis_bp.route("/aluno")
@login_required
@role_required("ALUNO")
def aluno():
    return render_template("paineis/aluno.html")


@paineis_bp.route("/professor")
@login_required
@role_required("PROFESSOR")
def professor():
    return render_template("paineis/professor.html")


@paineis_bp.route("/admin")
@login_required
@role_required("ADMIN")
def admin():
    return render_template("paineis/admin.html")
