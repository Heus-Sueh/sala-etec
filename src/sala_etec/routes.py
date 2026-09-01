from flask import Blueprint, render_template, request, redirect, url_for
from sala_etec.database import db
from sala_etec.models import Curso, Modulo, Disciplina, Material, Usuario


# Criar o modulo principal das rotas
main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/login", methods=["POST"])
def login():
    name = request.form.get("name", "").strip()
    password = request.form.get("password", "").strip()

    if not name:
        return render_template(
            "index.html",
            error="O nome de usuário é obrigatório.",
        )

    if not password:
        return render_template(
            "index.html",
            error="A senha é obrigatória.",
        )

    return redirect(url_for("main.home", user=name))


@main_bp.route("/home")
def home():
    user = request.args.get("user", "Usuário")

    materiais = Material.query.all()
    disciplinas = Disciplina.query.all()

    total_materiais = len(materiais)
    total_disciplinas = len(disciplinas)

    return render_template(
        "home.html",
        user=user,
        total_materiais=total_materiais,
        total_disciplinas=total_disciplinas,
        materiais=materiais,
    )


@main_bp.route("/materiais")
def listar_materiais():
    busca = request.args.get("busca", "").strip()

    if busca:
        materiais = Material.query.filter(
            Material.titulo.ilike(f"%{busca}%")
        ).all()
    else:
        materiais = Material.query.all()

    return render_template(
        "materiais.html",
        materiais=materiais,
        busca=busca,
    )


@main_bp.route("/material/<int:id>/status", methods=["POST"])
def mudar_status(id):
    material = db.session.get(Material, id)

    if not material:
        return "Material não encontrado", 404

    if material.status == "Publicado":
        material.status = "Arquivado"
    else:
        material.status = "Publicado"

    db.session.commit()

    return redirect(url_for("main.listar_materiais"))

@main_bp.route("/adicionar/", methods=["GET", "POST"])
def adicionar_material():

    disciplinas = Disciplina.query.all()

    professores = Usuario.query.filter_by(tipo="PROFESSOR").all()

    if request.method == "GET":
        return render_template(
            "adicionar.html",
            disciplinas=disciplinas,
            professores=professores
        )

    # POST
    titulo = request.form.get("titulo", "").strip()
    desc = request.form.get("desc", "").strip()
    disciplina_id = request.form.get("disciplina_id")
    professor_id = request.form.get("professor_id")

    if not titulo:
        return render_template(
            "adicionar.html",
            disciplinas=disciplinas,
            professores=professores,
            error="O título do material é obrigatório."
        )

    if not desc:
        return render_template(
            "adicionar.html",
            disciplinas=disciplinas,
            professores=professores,
            error="A descrição é obrigatória."
        )

    if not disciplina_id:
        return render_template(
            "adicionar.html",
            disciplinas=disciplinas,
            professores=professores,
            error="A disciplina é obrigatória."
        )

    if not professor_id:
        return render_template(
            "adicionar.html",
            disciplinas=disciplinas,
            professores=professores,
            error="O professor é obrigatório."
        )

    disciplina = db.session.get(Disciplina, disciplina_id)
    professor = db.session.get(Usuario, professor_id)

    if not disciplina:
        return render_template(
            "adicionar.html",
            disciplinas=disciplinas,
            professores=professores,
            error="Disciplina inválida."
        )

    if not professor or professor.tipo != "PROFESSOR":
        return render_template(
            "adicionar.html",
            disciplinas=disciplinas,
            professores=professores,
            error="Professor inválido."
        )

    novo_material = Material(
        titulo=titulo,
        desc=desc,
        disciplina=disciplina,
        professor=professor,
        arquivo="",
    )

    db.session.add(novo_material)
    db.session.commit()

    return redirect(url_for("main.listar_materiais"))

@main_bp.route("/material/<int:id>/excluir", methods=["POST"])
def excluir_material(id):
    material = Material.query.get(id)

    if not material:
        return "Material não encontrado", 404

    db.session.delete(material)
    db.session.commit()

    return redirect(url_for("main.listar_materiais"))
