from flask import Flask

from sala_etec.database import db
from sala_etec.routes import main_bp


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sala_etec.db"

db.init_app(app)

app.register_blueprint(main_bp)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
