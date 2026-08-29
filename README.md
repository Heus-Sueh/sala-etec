# sala-etec

# Projeto 

**Sala ETEC**

## Nome da Empresa

**LogosTech Soluções**

## Integrantes

- **Douglas Almeida da Cruz**
-	**Kelly dos Santos Lima**
-	**Leonardo Araujo de Andrade**
-	**Maria Clara Silva Nunes de Lima**
-	**Matheus Silva de Moura**
-	**Michael Kyle da Silva**

## Nome do Sistema

**Sala Etec**

## Descrição

O **Sala Etec** é uma plataforma web voltada para alunos e professores da ETEC. Seu objetivo é centralizar materiais didáticos, atividades e informações das disciplinas em um único ambiente, facilitando o acesso aos conteúdos e a comunicação acadêmica.

---

# Objetivo

Disponibilizar uma plataforma online para organização e compartilhamento de conteúdos acadêmicos, permitindo que alunos acessem materiais de estudo e que professores publiquem conteúdos de forma simples e organizada.

---

# Público-alvo

* Alunos
* Professores
* Administradores

---

# Requisitos Funcionais

* Cadastro e login de usuários.
* Recuperação de senha.
* Gerenciamento de perfil do usuário.
* Cadastro de cursos, módulos e disciplinas.
* Publicação de materiais didáticos pelos professores.
* Visualização e download de materiais pelos alunos.
* Pesquisa de materiais por disciplina ou nome.
* Organização dos conteúdos por curso e módulo.
* Controle de permissões (Administrador, Professor e Aluno).

---

# Requisitos Não Funcionais

* Interface responsiva para computadores e dispositivos móveis.
* Senhas armazenadas utilizando criptografia (hash).
* Controle de acesso conforme o tipo de usuário.
* Banco de dados relacional.
* Tempo de resposta adequado para navegação.
* Disponibilidade do sistema via navegador.
* Código organizado e documentado para facilitar manutenção.

---

# Tecnologias

**Backend**

* Python
* FastAPI
* SQLAlchemy
* Alembic

**Frontend**

* HTML
* CSS
* Bulma
* JavaScript

**Banco de Dados**

* MySQL

![DER](/docs/DER.png)

---

# Módulos do Sistema

### Aluno

* Login
* Visualizar disciplinas
* Acessar materiais
* Download de arquivos
* Editar perfil

### Professor

* Login
* Publicar materiais
* Editar materiais
* Excluir materiais

### Administrador

* Gerenciar usuários
* Gerenciar cursos
* Gerenciar disciplinas
* Gerenciar permissões

---

# Diferenciais

* Organização dos conteúdos por curso, módulo e disciplina.
* Ambiente único para professores e alunos.
* Interface simples e intuitiva.
* Estrutura preparada para futuras funcionalidades, como atividades online, fóruns e notificações

# Horarios de Pico

* Segunda a Sexta das 18:00 às 22:00

# Padrão de Arquitetura Escolhido:

Justificativa Técnica:
A equipe escolheu a arquitetura monolítica porque o sistema Sala Etec possui uma complexidade moderada e será desenvolvido por uma equipe pequena, não havendo inicialmente uma grande necessidade de escala. Nesse modelo, as principais funcionalidades do sistema ficam integradas em uma única aplicação, facilitando o desenvolvimento, os testes, a manutenção e a implantação. Além disso, a arquitetura monolítica é mais adequada para o projeto neste momento, pois permite que a equipe trabalhe com uma estrutura mais simples e tenha maior facilidade para gerenciar o sistema e seu banco de dados. Caso o sistema cresça futuramente e passe a exigir maior escalabilidade, partes específicas poderão ser separadas em serviços independentes.

# Mapeamento de Evento - Arquitetura Orientada a Eventos

Nome do Evento:
“Quando o professor publica um novo material”
Reações Automatizadas do Sistema:
    1. Salvar o material no banco de dados, associando-o à disciplina, módulo e professor responsável.
    2. Disponibilizar automaticamente o material para os alunos que possuem acesso àquela disciplina.
    3. Atualizar a listagem de materiais da disciplina, permitindo que o novo conteúdo seja encontrado pela pesquisa.
    4. Registrar a publicação, armazenando informações como data, professor e material publicado.
Esse evento é adequado porque a publicação de materiais é uma das principais funções do Sala Etec e desencadeia várias ações dentro do sistema.

![usuario-cliente](/docs/usuario-cliente.png)
![fluxo-dados]](/docs/fluxo-dados.png)
![modulo-servicos]](/docs/modulo-servicos.png)
