# sala_etec/routes/materiais.py
from flask import Blueprint, redirect, render_template, request, url_for, session

from sala_etec.database import db
from sala_etec.decorators import login_required
from sala_etec.models import Disciplina, Material, Usuario

# Criar o modulo principal das rotas
materiais_bp = Blueprint("materiais", __name__, url_prefix="/materiais")


@materiais_bp.route("/")
@login_required
def listar():
    busca = request.args.get("busca", "").strip()

    if busca:
        materiais = Material.query.filter(Material.titulo.ilike(f"%{busca}%")).all()
    else:
        materiais = Material.query.all()

    return render_template(
        "materiais/lista.html",
        materiais=materiais,
        busca=busca,
    )


@materiais_bp.route("/material/<int:material_id>/status", methods=["POST"])
@login_required
def alterarstatus(material_id):
    material = db.session.get(Material, material_id)

    if not material:
        return "Material não encontrado", 404

    if material.status == "Publicado":
        material.status = "Arquivado"
    else:
        material.status = "Publicado"

    db.session.commit()

    return redirect(url_for("materiais.listar"))


@materiais_bp.route("/adicionar", methods=["GET", "POST"])
@login_required
def adicionar():

    disciplinas = Disciplina.query.all()

    professores = Usuario.query.filter_by(tipo="PROFESSOR").all()

    if request.method == "GET":
        return render_template(
            url_for("materiais.formulario"),
            disciplinas=disciplinas,
            professores=professores,
        )

    # POST
    titulo = request.form.get("titulo", "").strip()
    desc = request.form.get("desc", "").strip()
    disciplina_id = request.form.get("disciplina_id")
    professor_id = request.form.get("professor_id")

    if not titulo:
        return render_template(
            "materiais/formulario.html",
            disciplinas=disciplinas,
            professores=professores,
            error="O título do material é obrigatório.",
        )

    if not desc:
        return render_template(
            "materiais/formulario.html",
            disciplinas=disciplinas,
            professores=professores,
            error="A descrição é obrigatória.",
        )

    if not disciplina_id:
        return render_template(
            "materiais/formulario.html",
            disciplinas=disciplinas,
            professores=professores,
            error="A disciplina é obrigatória.",
        )

    if not professor_id:
        return render_template(
            "adicionar.html",
            disciplinas=disciplinas,
            professores=professores,
            error="O professor é obrigatório.",
        )

    disciplina = db.session.get(Disciplina, disciplina_id)
    professor = db.session.get(Usuario, professor_id)

    if not disciplina:
        return render_template(
            "materiais/formulario.html",
            disciplinas=disciplinas,
            professores=professores,
            error="Disciplina inválida.",
        )

    if not professor or professor.tipo != "PROFESSOR":
        return render_template(
            "materiais/formulario.html",
            disciplinas=disciplinas,
            professores=professores,
            error="Professor inválido.",
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

    return redirect(url_for("materiais.listar"))


@materiais_bp.route("/material/<int:material_id>/excluir", methods=["POST"])
@login_required
def excluir(material_id):
    material = Material.query.get(material_id)

    if not material:
        return "Material não encontrado", 404

    db.session.delete(material)
    db.session.commit()

    return redirect(url_for("materiais.listar"))
