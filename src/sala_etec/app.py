# sala_etec/routes/app.py
from flask import Flask

from sala_etec.database import db
from sala_etec.routes import register_blueprints

app = Flask(__name__)

app.config["SECRET_KEY"] = "chave-dev-sala-etec"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sala_etec.db"

db.init_app(app)
register_blueprints(app)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
