# sala_etec/create_database.py
from sala_etec.app import app
from sala_etec.database import db


def main():
    with app.app_context():
        db.create_all()
        print("Tabelas criadas com sucesso!")


if __name__ == "__main__":
    main()
