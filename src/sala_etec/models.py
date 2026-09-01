# Importar a instancia do banco 'db' criada no arquivo database.py
from sqlalchemy.orm import backref
from sala_etec.database import db
from datetime import datetime

# Definir a classe que ira realizar todo o mapeamento da minha tabela
class Curso(db.Model):

    # Define o nome da minha tabela
    __tablename__ = 'curso'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)

    # relação dos objetos
    modulos = db.relationship("Modulo", back_populates="curso")
    matriculas = db.relationship(
        "Matricula",
        back_populates="curso"
    )

class Modulo(db.Model):

    # Define o nome da minha tabela
    __tablename__ = 'modulo'

    id = db.Column(db.Integer, primary_key=True)
    curso_id = db.Column(db.Integer, db.ForeignKey("curso.id"), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)

    # relação dos objetos
    curso = db.relationship("Curso", back_populates="modulos")
    disciplinas = db.relationship("Disciplina", back_populates="modulo")

class Disciplina(db.Model):

    # Define o nome da minha tabela
    __tablename__ = 'disciplina'

    id = db.Column(db.Integer, primary_key=True)
    modulo_id = db.Column(db.Integer, db.ForeignKey("modulo.id"), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)


    # relação dos objetos
    modulo = db.relationship("Modulo", back_populates="disciplinas")
    materiais = db.relationship(
        "Material",
        back_populates="disciplina"
    )

    atividades = db.relationship(
        "Atividade",
        back_populates="disciplina"
    )

class Material(db.Model):

    # Define o nome da minha tabela
    __tablename__ = 'material'

    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey("disciplina.id"), nullable=False) # FK (Foreign Key)
    professor_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False) # FK (Foreign Key)
    titulo = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    arquivo = db.Column(db.String(200), nullable=False)
    status = db.Column(
        db.String(20),
        nullable=False,
        default="Publicado"
    )
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.now)

    disciplina = db.relationship(
        "Disciplina",
        back_populates="materiais"
    )

    professor = db.relationship(
        "Usuario",
        back_populates="materiais"
    )


class Atividade(db.Model):

    # Define o nome da minha tabela
    __tablename__ = 'atividade'

    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey("disciplina.id"), nullable=False) # FK (Foreign Key)
    professor_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False) # FK (Foreign Key)
    titulo = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    arquivo = db.Column(db.String(200), nullable=False)
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.now)


    disciplina = db.relationship(
        "Disciplina",
        back_populates="atividades"
    )

    professor = db.relationship(
        "Usuario",
        back_populates="atividades"
    )


class Usuario(db.Model):

    # Define o nome da minha tabela
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.now)

    matriculas = db.relationship(
        "Matricula",
        back_populates="usuario"
    )

    materiais = db.relationship(
        "Material",
        back_populates="professor"
    )

    atividades = db.relationship(
        "Atividade",
        back_populates="professor"
    )

class Matricula(db.Model):

    # Define o nome da minha tabela
    __tablename__ = 'matricula'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False) # FK (Foreign Key)
    curso_id = db.Column(db.Integer, db.ForeignKey("curso.id"), nullable=False) # FK (Foreign Key)
    data_matricula = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now
    )

    usuario = db.relationship(
        "Usuario",
        back_populates="matriculas"
    )

    curso = db.relationship(
        "Curso",
        back_populates="matriculas"
    )


# db.session.add(obj) # - adds an object to the session, to be inserted. Modifying an object’s attributes updates the object.
# db.session.delete(obj) # - deletes an object.
# Remember to call db.session.commit() after modifying, adding, or deleting any data.
