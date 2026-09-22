# sala_etec/routes/auth.py
from flask import Blueprint, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash

from sala_etec.models import Usuario

# Criar o modulo principal das rotas
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "GET":
        return render_template("auth/login.html")

    else:
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")
        if not email:
            return render_template("auth/login.html", error="Informe seu e-mail.")

        if not senha:
            return render_template("auth/login.html", error="Informe sua senha.")

        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario:
            return render_template(
                "auth/login.html", error="E-mail ou senha inválidos."
            )

        if not check_password_hash(usuario.senha_hash, senha):
            return render_template(
                "auth/login.html", error="E-mail ou senha inválidos."
            )

        session["usuario_id"] = usuario.id

        return redirect(url_for("main.home"))


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
