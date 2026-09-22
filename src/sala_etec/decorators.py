# sala_etec/decorators.py
from functools import wraps

from flask import g, redirect, session, url_for

from sala_etec.database import db
from sala_etec.models import Usuario


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        usuario_id = session.get("usuario_id")

        if not usuario_id:
            return redirect(url_for("auth.login"))

        usuario = db.session.get(Usuario, usuario_id)

        if not usuario:
            session.clear()
            return redirect(url_for("auth.login"))

        g.usuario = usuario

        return func(*args, **kwargs)

    return wrapper



def role_required(*tipos):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if g.usuario.tipo not in tipos:
                return "Acesso não autorizado", 403

            return func(*args, **kwargs)

        return wrapper

    return decorator
