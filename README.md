# QA Automation Challenge

Automação de testes cobrindo API REST e fluxo E2E web, com pipeline de CI/CD integrada.

## Tecnologias utilizadas

| Camada | Ferramenta |
|--------|------------|
| Linguagem | Python 3.11 |
| Testes de API | pytest + requests |
| Testes Web | pytest + Selenium 4 |
| Relatórios | pytest-html |
| CI/CD | GitHub Actions |

## Estrutura do projeto

qa-automation-challenge/
+-- .github/workflows/ci.yml
+-- api-tests/
¦   +-- tests/
¦   ¦   +-- test_pet.py
¦   ¦   +-- test_store.py
¦   ¦   +-- test_user.py
¦   +-- utils/api_client.py
¦   +-- conftest.py
+-- web-tests/
¦   +-- pages/
¦   ¦   +-- login_page.py
¦   ¦   +-- inventory_page.py
¦   ¦   +-- checkout_page.py
¦   +-- tests/test_e2e.py
¦   +-- conftest.py
+-- requirements.txt

## Como executar localmente

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Rodar testes de API
```bash
cd api-tests
python -m pytest tests/ -v
```

### Rodar testes Web E2E
```bash
cd web-tests
python -m pytest tests/ -v
```

## Escopo dos testes

### API — Petstore
- Pet: criar, buscar, atualizar, listar por status, deletar
- Store: inventário, criar pedido, buscar, deletar
- User: criar, buscar, atualizar, login, logout, deletar

### Web E2E — SauceDemo
- Login com credencial inválida
- Login válido, adicionar produto, finalizar compra

## Design Patterns
- Page Object Model (POM)
- Fixture Pattern (pytest)
- Arrange-Act-Assert (AAA)
