# sala_etec/routes/main.py
from flask import Blueprint, g, redirect, render_template, url_for

from sala_etec.decorators import login_required

# Criar o modulo principal das rotas
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def root():
    return redirect(url_for("auth.login"))


@main_bp.route("/home")
@login_required
def home():
    tipo = g.usuario.tipo

    if tipo == "ALUNO":
        return redirect(url_for("paineis.aluno"))

    if tipo == "PROFESSOR":
        return redirect(url_for("paineis.professor"))

    if tipo == "ADMIN":
        return redirect(url_for("paineis.admin"))

    return "Tipo de usuário inválido", 403


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
