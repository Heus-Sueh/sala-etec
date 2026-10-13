# sala_etec/routes/materiais.py
import os
from werkzeug.utils import secure_filename
from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

from sala_etec.database import db
from sala_etec.decorators import login_required
from sala_etec.models import Disciplina, Material, Usuario

# Criar o modulo principal das rotas
materiais_bp = Blueprint("materiais", __name__, url_prefix="/materiais")


# definir as extensões que permitimos receber
EXTENSOES_PERMITIDAS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def arquivo_permitido(filename):
    """Verifica se a extensão do arquivo é permitida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXTENSOES_PERMITIDAS


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


@materiais_bp.route("/<int:material_id>/status", methods=["POST"])
@login_required
def alterar_status(material_id):
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
            "materiais/formulario.html",
            disciplinas=disciplinas,
            professores=professores,
        )

    # POST
    titulo = request.form.get("titulo", "").strip()
    desc = request.form.get("desc", "").strip()
    disciplina_id = request.form.get("disciplina_id")
    professor_id = request.form.get("professor_id")

    imagefile = request.files.get("imagem_id")
    new_image = "padrao.png"

    if not titulo or not desc or not disciplina_id or not professor_id:
        flash("Todos os campos são obrigatórios", "danger")
        return redirect(url_for("materiais.adicionar"))


    disciplina = db.session.get(Disciplina, disciplina_id)
    professor = db.session.get(Usuario, professor_id)

    if not disciplina:
        flash("Disciplina inválida", "danger")
        return redirect(url_for("materiais.adicionar"))

    if not professor or professor.tipo != "PROFESSOR":
        flash("Professor inválido", "danger")
        return redirect(url_for("materiais.adicionar"))


    if imagefile and imagefile.filename:
        if not arquivo_permitido(imagefile.filename):
            flash("Extensão de arquivo não permitida. Use PNG, JPG, ou webp.", "danger")
            return redirect(url_for("materiais.adicionar"))

        # Remove caracteres inválidos do nome do arquivo.
        safename = secure_filename(imagefile.filename)

        if not safename:
            flash("Nome de arquivo inválido", "danger")
            return redirect(url_for("materiais.adicionar"))

        # Usa o mesmo nome no banco e no arquivo físico.
        new_image = f"imagem_{safename}"

        fullpath = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            new_image,
        )

        imagefile.save(fullpath)

    novo_material = Material(
        titulo=titulo,
        desc=desc,
        disciplina=disciplina,
        professor=professor,
        imagem=new_image,
        arquivo="",
    )

    db.session.add(novo_material)
    db.session.commit()

    return redirect(url_for("materiais.listar"))


@materiais_bp.route("/<int:material_id>/excluir", methods=["POST"])
@login_required
def excluir(material_id):
    material = db.session.get(Material, material_id)

    if not material:
        return "Material não encontrado", 404

    # Guarda o nome da imagem antes de excluir o registro.
    nome_imagem = material.imagem

    try:
        db.session.delete(material)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

    # Exclui a imagem física, exceto a imagem padrão.
    if nome_imagem and nome_imagem != "padrao.png":
        caminho_imagem = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            nome_imagem,
        )

        if os.path.isfile(caminho_imagem):
            try:
                os.remove(caminho_imagem)
            except OSError:
                current_app.logger.exception(
                    "Não foi possível excluir a imagem %s",
                    nome_imagem,
                )
                flash(
                    "Material excluído, mas não foi possível remover sua imagem.",
                    "warning",
                )
                return redirect(url_for("materiais.listar"))

    flash("Material excluído com sucesso.", "success")

    return redirect(url_for("materiais.listar"))
