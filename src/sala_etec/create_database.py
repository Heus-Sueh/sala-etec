from sala_etec.app import app
from sala_etec.database import db


with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")
