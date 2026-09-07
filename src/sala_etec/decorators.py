from functools import wraps

from flask import redirect, session, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("main.index"))

        return func(*args, **kwargs)

    return wrapper
