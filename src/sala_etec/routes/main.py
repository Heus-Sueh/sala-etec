# sala_etec/routes/main.py
from flask import Blueprint, redirect, render_template, url_for

from sala_etec.decorators import login_required

# Criar o modulo principal das rotas
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def root():
    return redirect(url_for("auth.login"))


@main_bp.route("/home")
@login_required
def home():
    return render_template(
        "main/home.html",
    )


@main_bp.route("/disciplinas")
@login_required
def disciplinas():
    return render_template("main/disciplinas.html")


@main_bp.route("/atividades")
@login_required
def atividades():
    return render_template("main/atividades.html")


@main_bp.route("/favoritos")
@login_required
def favoritos():
    return render_template("main/favoritos.html")
