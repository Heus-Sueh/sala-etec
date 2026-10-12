# sala_etec/create_database.py
import os
from sala_etec.app import app
from sala_etec.database import db


def main():
    with app.app_context():
        # Cria a pasta de upload caso não exista
        print("URI configurada:", app.config["SQLALCHEMY_DATABASE_URI"])
        print("Banco utilizado:", db.engine.url.database)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

        db.create_all()
        print("Tabelas criadas com sucesso!")


if __name__ == "__main__":
    main()
