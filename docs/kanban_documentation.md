# Documentação Ágil: Kanban e Commits Semânticos

Este documento serve como suporte metodológico do projeto **TaskFlow Ágil**, descrevendo como a metodologia ágil Kanban foi aplicada, sugerindo cards para simular o fluxo de trabalho acadêmico e fornecendo 10 sugestões de commits estruturados utilizando a convenção de **Commits Semânticos**.

---

## 📋 1. Metodologia Ágil Utilizada (Kanban)

O Kanban é uma metodologia visual de gestão de projetos que tem como objetivo gerenciar e otimizar o fluxo de trabalho de ponta a ponta. 

### Princípios do Kanban aplicados no projeto:
1. **Visualização do Trabalho:** O quadro Kanban divide o trabalho em colunas físicas (*A Fazer*, *Em Progresso*, *Concluído*) facilitando a percepção visual do gargalo da equipe.
2. **Limite de Trabalho em Progresso (WIP):** Sugere-se limitar o número máximo de itens simultâneos na coluna *Em Progresso* (WIP limit de 3 a 5 itens) para incentivar a equipe a concluir tarefas antes de iniciar novas.
3. **Gestão de Fluxo:** A adição da **Prioridade das Tarefas** (Mudança de Escopo) ajuda a equipe a priorizar o que puxar da coluna *A Fazer* para a coluna *Em Progresso*.

---

## 📇 2. Sugestão de Cards para Simulação do Kanban

Abaixo estão sugestões de cards de tarefas reais para simular o fluxo de desenvolvimento deste sistema:

### Coluna: A Fazer (Backlog Priorizado)
*   **Card 1 - Modelagem de Banco de Dados**
    *   *Prioridade:* Alta
    *   *Descrição:* Estruturar tabela SQLite `tasks` contemplando id, title, description, status, priority e created_at.
*   **Card 2 - Documentação Técnica do Projeto**
    *   *Prioridade:* Média
    *   *Descrição:* Criar diagramas UML de Classe e Casos de Uso detalhando a estrutura modular da aplicação.
*   **Card 3 - Layout Responsivo Mobile**
    *   *Prioridade:* Baixa
    *   *Descrição:* Implementar CSS Media Queries para otimizar a visualização das 3 colunas Kanban em dispositivos móveis.

### Coluna: Em Progresso (Desenvolvimento Ativo)
*   **Card 4 - Desenvolvimento dos Testes do Pytest**
    *   *Prioridade:* Alta
    *   *Descrição:* Implementar suíte de testes unitários para cobrir validação de criação, edição e exclusão de tarefas.
*   **Card 5 - Criação do Pipeline de CI**
    *   *Prioridade:* Média
    *   *Descrição:* Escrever arquivo ci.yml do GitHub Actions para validar e testar a aplicação a cada alteração.

### Coluna: Concluído (Entregue e Validado)
*   **Card 6 - Protótipo da Interface HTML**
    *   *Prioridade:* Média
    *   *Descrição:* Desenvolver templates HTML iniciais com a estrutura das 3 colunas e formulário de cadastro básico.

---

## 💬 3. Sugestão de 10 Commits Semânticos

Utilizar commits semânticos ajuda na legibilidade do histórico do projeto Git, um ponto altamente valorizado em trabalhos de Engenharia de Software. Segue a lista cronológica recomendada:

1.  `feat: estrutura inicial de pastas e dependências base do projeto`
    *   *Explicação:* Configura o diretório, o `.gitignore` e o arquivo `requirements.txt`.
2.  `feat: criar conexão e lógica de inicialização de banco SQLite`
    *   *Explicação:* Cria o arquivo `database.py` e configura a criação automática de tabelas.
3.  `feat: criar modelo Task e operações CRUD com validações de campos`
    *   *Explicação:* Codifica as operações essenciais de criação, leitura, atualização e exclusão na camada Model.
4.  `feat: implementar rotas Flask principais para controle de tarefas`
    *   *Explicação:* Desenvolve as rotas HTTP GET/POST da aplicação em `app.py`.
5.  `feat: criar layouts e templates HTML para renderizar quadro Kanban`
    *   *Explicação:* Adiciona os arquivos `base.html`, `index.html` e `edit.html`.
6.  `feat: estilizar interface com design escuro premium e responsividade`
    *   *Explicação:* Codifica as variáveis CSS e regras de layout do quadro Kanban e cards de prioridades.
7.  `test: adicionar fixtures de banco isolado e suíte de testes em Pytest`
    *   *Explicação:* Cria arquivos de testes unitários e de integração validando rotas e models.
8.  `ci: configurar workflow no GitHub Actions para execução de testes`
    *   *Explicação:* Adiciona o pipeline automático no arquivo `.github/workflows/ci.yml`.
9.  `docs: documentar arquitetura com diagramas de classe e caso de uso`
    *   *Explicação:* Adiciona arquivo markdown detalhando diagramas UML.
10. `docs: atualizar README com orientações de execução e mudança de escopo`
    *   *Explicação:* Finaliza a documentação principal para entrega.
