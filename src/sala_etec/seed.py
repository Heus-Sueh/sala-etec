from datetime import datetime

from sala_etec.app import app
from sala_etec.database import db
from sala_etec.models import (
    Curso,
    Modulo,
    Disciplina,
    Usuario,
    Material,
)


def criar_dados():
    with app.app_context():

        # Evita duplicar os dados
        if Curso.query.first():
            print("Banco já possui dados.")
            return

        # -------------------------
        # CURSOS
        # -------------------------

        ds = Curso(
            nome="Desenvolvimento de Sistemas",
            desc="Curso técnico de Desenvolvimento de Sistemas."
        )

        adm = Curso(
            nome="Administração",
            desc="Curso técnico de Administração."
        )

        comercio = Curso(
            nome="Comércio Exterior",
            desc="Curso técnico de Comércio Exterior."
        )

        contabilidade = Curso(
            nome="Contabilidade",
            desc="Curso técnico de Contabilidade."
        )

        db.session.add_all([
            ds,
            adm,
            comercio,
            contabilidade
        ])

        db.session.flush()

        # -------------------------
        # MÓDULOS
        # -------------------------

        ds_modulo_1 = Modulo(
            nome="Módulo I",
            desc="Primeiro módulo de Desenvolvimento de Sistemas.",
            curso=ds
        )

        ds_modulo_2 = Modulo(
            nome="Módulo II",
            desc="Segundo módulo de Desenvolvimento de Sistemas.",
            curso=ds
        )

        ds_modulo_3 = Modulo(
            nome="Módulo III",
            desc="Terceiro módulo de Desenvolvimento de Sistemas.",
            curso=ds
        )

        db.session.add_all([
            ds_modulo_1,
            ds_modulo_2,
            ds_modulo_3
        ])

        db.session.flush()

        # -------------------------
        # USUÁRIOS / PROFESSORES
        # -------------------------

        joao = Usuario(
            nome="João Silva",
            email="joao@salatec.local",
            senha_hash="senha-ficticia",
            tipo="PROFESSOR"
        )

        maria = Usuario(
            nome="Maria Santos",
            email="maria@salatec.local",
            senha_hash="senha-ficticia",
            tipo="PROFESSOR"
        )

        carlos = Usuario(
            nome="Carlos Oliveira",
            email="carlos@salatec.local",
            senha_hash="senha-ficticia",
            tipo="PROFESSOR"
        )

        # -------------------------
        # ALUNOS
        # -------------------------

        aluno1 = Usuario(
            nome="Matheus Silva",
            email="matheus@salatec.local",
            senha_hash="senha-ficticia",
            tipo="ALUNO"
        )

        aluno2 = Usuario(
            nome="Ana Souza",
            email="ana@salatec.local",
            senha_hash="senha-ficticia",
            tipo="ALUNO"
        )

        # -------------------------
        # ADMINISTRADOR
        # -------------------------

        admin = Usuario(
            nome="Administrador",
            email="admin@salatec.local",
            senha_hash="senha-ficticia",
            tipo="ADMIN"
        )

        db.session.add_all([
            joao,
            maria,
            carlos,
            aluno1,
            aluno2,
            admin
        ])

        db.session.flush()

        # -------------------------
        # DISCIPLINAS
        # -------------------------

        banco = Disciplina(
            nome="Banco de Dados II",
            desc="Banco de dados relacionais e SQL.",
            modulo=ds_modulo_2
        )

        web = Disciplina(
            nome="Programação Web II",
            desc="Desenvolvimento de aplicações web.",
            modulo=ds_modulo_2
        )

        sistemas = Disciplina(
            nome="Análise e Projeto de Sistemas",
            desc="Análise e modelagem de sistemas.",
            modulo=ds_modulo_1
        )

        desenvolvimento = Disciplina(
            nome="Desenvolvimento de Sistemas I",
            desc="Fundamentos do desenvolvimento de sistemas.",
            modulo=ds_modulo_1
        )

        ptcc = Disciplina(
            nome="PTCC",
            desc="Planejamento e desenvolvimento do trabalho de conclusão.",
            modulo=ds_modulo_3
        )

        mobile = Disciplina(
            nome="Programação de Aplicativos Mobile I",
            desc="Desenvolvimento de aplicações mobile.",
            modulo=ds_modulo_3
        )

        projetos = Disciplina(
            nome="Projetos de Desenvolvimento de Sistemas",
            desc="Desenvolvimento de projetos de sistemas.",
            modulo=ds_modulo_3
        )

        db.session.add_all([
            banco,
            web,
            sistemas,
            desenvolvimento,
            ptcc,
            mobile,
            projetos
        ])

        db.session.flush()

        # -------------------------
        # MATERIAIS
        # -------------------------

        material1 = Material(
            titulo="Introdução ao SQL",
            desc="Material introdutório sobre SQL.",
            disciplina=banco,
            professor=joao,
            arquivo="introducao_sql.pdf",
            criado_em=datetime.now()
        )

        material2 = Material(
            titulo="Modelo Entidade-Relacionamento",
            desc="Introdução aos modelos entidade-relacionamento.",
            disciplina=banco,
            professor=joao,
            arquivo="modelo_er.pdf",
            criado_em=datetime.now()
        )

        material3 = Material(
            titulo="Introdução ao Flask",
            desc="Primeiros passos com Flask.",
            disciplina=web,
            professor=maria,
            arquivo="introducao_flask.pdf",
            criado_em=datetime.now()
        )

        material4 = Material(
            titulo="Documentação de Sistemas",
            desc="Conceitos de documentação de sistemas.",
            disciplina=sistemas,
            professor=carlos,
            arquivo="documentacao.pdf",
            criado_em=datetime.now()
        )

        db.session.add_all([
            material1,
            material2,
            material3,
            material4
        ])

        db.session.commit()

        print("Dados fictícios criados com sucesso!")


if __name__ == "__main__":
    criar_dados()
