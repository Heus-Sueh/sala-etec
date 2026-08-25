from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


disciplinas = [
    "Análise e Projeto de Sistemas",
    "Banco de Dados II",
    "Desenvolvimento de Sistemas I",
    "PTCC",
    "Programação de Aplicativos Mobile I",
    "Programação Web II",
    "Projetos de Desenvolvimento de Sistemas",
]

materiais = [
    {
        "id": 1,
        "titulo": "Introdução ao SQL",
        "disciplina": "Banco de Dados II",
        "professor": "João",
        "status": "Publicado",
    },
    {
        "id": 2,
        "titulo": "Modelo Entidade-Relacionamento",
        "disciplina": "Banco de Dados II",
        "professor": "João",
        "status": "Publicado",
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
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

    return redirect(url_for("home", user=name))


@app.route("/home")
def home():
    user = request.args.get("user", "Usuário")

    total_materiais = len(materiais)
    total_disciplinas = len(disciplinas)

    materiais_publicados = sum(
        1 for material in materiais
        if material["status"] == "Publicado"
    )

    return render_template(
        "home.html",
        user=user,
        total_materiais=total_materiais,
        total_disciplinas=total_disciplinas,
        materiais_publicados=materiais_publicados,
        materiais=materiais,
    )


@app.route("/materiais")
def listar_materiais():
    busca = request.args.get("busca", "").strip().lower()

    if busca:
        materiais_filtrados = [
            material
            for material in materiais
            if busca in material["titulo"].lower()
            or busca in material["disciplina"].lower()
        ]
    else:
        materiais_filtrados = materiais

    return render_template(
        "materiais.html",
        materiais=materiais_filtrados,
        busca=busca,
    )


@app.route("/material/<int:id>/status", methods=["POST"])
def mudar_status(id):
    for material in materiais:
        if material["id"] == id:
            if material["status"] == "Publicado":
                material["status"] = "Arquivado"
            else:
                material["status"] = "Publicado"

            return redirect(url_for("listar_materiais"))

    return "Material não encontrado", 404

@app.route("/adicionar/", methods=["POST"])
def adicionar_material():

    titulo = request.form.get("titulo", "").strip()
    disciplina = request.form.get("disciplina", "").strip()
    professor = request.form.get("professor", "").strip()

    # "titulo": "Modelo Entidade-Relacionamento",
    # "disciplina": "Banco de Dados II",
    # "professor": "João",
    # "status": "Publicado",
    if not titulo:
           return render_template(
               "adicionar.html",
               error="O título do material é obrigatório."
           )

    if not disciplina:
        return render_template(
            "adicionar.html",
            error="A disciplina é obrigatória."
        )

    if not professor:
        return render_template(
            "adicionar.html",
            error="O professor é obrigatório."
        )

    material = {
        "id": len(materiais) + 1,
        "titulo": titulo,
        "disciplina": disciplina,
        "professor": professor,
        "status": "Publicado",
    }
    materiais.append(material)

    return redirect(url_for("listar_materiais"))

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
