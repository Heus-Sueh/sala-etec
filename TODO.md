# TODO — Refatoração da Estrutura do Sala ETEC

## 1. Organizar rotas em Blueprints

- [x] Criar diretório `sala_etec/routes/`
- [x] Criar `sala_etec/routes/__init__.py`
- [x] Criar Blueprint `auth` em `routes/auth.py`
- [x] Criar Blueprint `main` em `routes/main.py`
- [x] Criar Blueprint `materiais` em `routes/materiais.py`
- [x] Registrar os novos Blueprints na aplicação
- [x] Remover o arquivo antigo de rotas após concluir a migração

Estrutura esperada:

    sala_etec/
    ├── routes/
    │   ├── __init__.py
    │   ├── auth.py
    │   ├── main.py
    │   └── materiais.py
    ├── database.py
    ├── decorators.py
    └── models.py


## 2. Refatorar autenticação

- [x] Mover `login()` para `routes/auth.py`
- [x] Permitir `GET` e `POST` em `/login`
- [x] Fazer `GET /login` exibir o formulário
- [x] Fazer `POST /login` autenticar o usuário
- [x] Remover os `print()` usados para debug
- [x] Não aplicar `.strip()` na senha
- [x] Criar rota de logout
- [x] Fazer logout limpar a sessão com `session.clear()`
- [x] Redirecionar logout para a página de login

Rotas esperadas:

    GET  /login
    POST /login
    POST /logout


## 3. Melhorar `login_required`

- [ ] Centralizar a verificação de `usuario_id` no decorator
- [ ] Verificar se o usuário da sessão ainda existe
- [ ] Limpar a sessão caso o usuário não exista
- [ ] Redirecionar usuários não autenticados para `/login`
- [x] Aplicar `@login_required` nas páginas protegidas
- [ ] Remover verificações de autenticação duplicadas das rotas

Exemplo desejado:

    @main_bp.route("/home")
    @login_required
    def home():
        return render_template("main/home.html")


## 4. Refatorar rotas principais

- [x] Manter as rotas gerais em `routes/main.py`
- [-] Fazer `/` redirecionar para login ou home
- [-] Manter `/home` como página inicial do usuário
- [ ] Remover lógica de autenticação duplicada de `home()`

Rotas esperadas:

    GET /
    GET /home


## 5. Refatorar rotas de materiais

- [x] Mover rotas de materiais para `routes/materiais.py`
- [x] Criar Blueprint `materiais`
- [x] Adicionar `url_prefix="/materiais"`
- [x] Renomear `listar_materiais()` para `listar()`
- [x] Renomear `adicionar_material()` para `adicionar()`
- [x] Renomear `mudar_status()` para `alterar_status()`
- [x] Renomear `excluir_material()` para `excluir()`
- [x] Aplicar `@login_required` às rotas

Rotas esperadas:

    GET      /materiais/
    GET      /materiais/adicionar
    POST     /materiais/adicionar
    POST     /materiais/<material_id>/status
    POST     /materiais/<material_id>/excluir


## 6. Padronizar parâmetros e nomes

- [ ] Substituir parâmetros genéricos `id` por nomes específicos
- [x] Usar `material_id`
- [ ] Usar `disciplina_id`
- [ ] Usar `usuario_id`
- [ ] Usar `atividade_id`
- [ ] Renomear `desc` para `descricao`
- [ ] Padronizar nomes de funções em português
- [ ] Evitar repetir o domínio no nome quando o Blueprint já fornece contexto

Exemplo:

    materiais.listar
    materiais.adicionar
    materiais.alterar_status
    materiais.excluir

Em vez de:

    main.listar_materiais
    main.adicionar_material
    main.mudar_status
    main.excluir_material


## 7. Padronizar acesso ao banco

- [ ] Substituir `Model.query.get(id)` por `db.session.get(Model, id)`
- [ ] Usar `db.session.get()` consistentemente
- [ ] Remover imports de models que não são utilizados em cada arquivo

Exemplo:

    material = db.session.get(Material, material_id)


## 8. Organizar templates

- [x] Criar diretório `templates/auth/`
- [x] Criar diretório `templates/main/`
- [x] Criar diretório `templates/materiais/`
- [x] Renomear `index.html` para `auth/login.html`
- [x] Mover `home.html` para `main/home.html`
- [x] Renomear `materiais.html` para `materiais/lista.html`
- [x] Renomear `adicionar.html` para `materiais/formulario.html`
- [x] Atualizar chamadas de `render_template()`

Estrutura esperada:

    templates/
    ├── base.html
    ├── auth/
    │   └── login.html
    ├── main/
    │   └── home.html
    └── materiais/
        ├── lista.html
        └── formulario.html


## 9. Padronizar navegação

- [x] Substituir URLs escritas manualmente por `url_for()`
- [x] Atualizar links da sidebar
- [x] Atualizar formulários
- [x] Atualizar redirects
- [x] Atualizar links após a separação dos Blueprints

Exemplo:

    url_for("main.home")
    url_for("materiais.listar")
    url_for("materiais.adicionar")


## 10. Implementar botão Voltar

- [x] Adicionar bloco `back_button` ao `base.html`
- [x] Não mostrar botão Voltar na Home
- [ ] Permitir que páginas sobrescrevam o destino
- [ ] Fazer páginas de materiais voltarem para `materiais.listar`
- [ ] Fazer páginas de disciplinas voltarem para `disciplinas.listar`
- [ ] Fazer páginas de atividades voltarem para `atividades.listar`


## 11. Preparar estrutura para novas funcionalidades

Após finalizar a refatoração:

- [x] Criar `routes/disciplinas.py`
- [x] Criar `routes/atividades.py`
- [x] Criar `routes/favoritos.py`

Estrutura:

    routes/
    ├── __init__.py
    ├── auth.py
    ├── main.py
    ├── materiais.py
    ├── disciplinas.py
    ├── atividades.py
    └── favoritos.py


## 12. Organizar novos templates

- [ ] Criar `templates/disciplinas/`
- [ ] Criar `templates/atividades/`
- [ ] Criar `templates/favoritos/`

Estrutura:

    templates/
    ├── base.html
    ├── auth/
    ├── main/
    ├── materiais/
    ├── disciplinas/
    ├── atividades/
    └── favoritos/


## 13. Preparar controle de permissões

- [ ] Diferenciar permissões de `ALUNO`
- [ ] Diferenciar permissões de `PROFESSOR`
- [ ] Diferenciar permissões de `ADMIN`
- [ ] Impedir alunos de publicar materiais/atividades
- [ ] Permitir professores criarem e gerenciarem conteúdo
- [ ] Definir permissões administrativas
- [ ] Evitar criar rotas duplicadas para aluno e professor
- [ ] Centralizar autorização em decorators ou funções auxiliares


## 14. Revisão final

- [ ] Verificar se todas as páginas exigidas usam `@login_required`
- [ ] Verificar se todos os `url_for()` apontam para os novos endpoints
- [ ] Verificar se nenhum template referencia caminhos antigos
- [ ] Remover imports não utilizados
- [ ] Remover código de debug
- [ ] Testar login
- [ ] Testar logout
- [ ] Testar listagem de materiais
- [ ] Testar busca de materiais
- [ ] Testar criação de material
- [ ] Testar alteração de status
- [ ] Testar exclusão de material
- [ ] Testar navegação e botão Voltar
- [ ] Testar acesso sem autenticação
- [ ] Testar permissões de aluno
- [ ] Testar permissões de professor
- [ ] Atualizar documentação do projeto
