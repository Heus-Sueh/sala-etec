# sala_etec/routes/app.py
import os
from flask import Flask

from sala_etec.database import db
from sala_etec.routes import register_blueprints

app = Flask(__name__)

app.config["SECRET_KEY"] = "chave-dev-sala-etec"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sala_etec.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração para receber os uploads
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')

# Configuração para limitar o tamanho máximo do arquivo de upload (5 MB)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

db.init_app(app)
register_blueprints(app)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
