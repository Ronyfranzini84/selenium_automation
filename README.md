# Selenium Automation

Projeto de estudos para aprender **Selenium WebDriver** com Python, utilizando o site [Books to Scrape](https://books.toscrape.com/) como ambiente de prática. O repositório reúne scripts independentes, cada um focado em um conceito específico de automação de navegador: navegação paginada, extração de dados, logging e manipulação de múltiplas abas.

## 📂 Estrutura do projeto

```
selenium_automation/
├── main.py            # Script principal: extrai os livros de todas as páginas e salva em Excel
├── scraper.py          # Funções reutilizáveis de extração, navegação e exportação
├── logging_test.py     # Exemplo isolado de configuração de logging com logging.basicConfig
├── tabs_test.py        # Exemplo de abertura/alternância entre múltiplas abas do navegador
├── requirements.txt    # Dependências do projeto
├── logs/               # Arquivos de log gerados em tempo de execução
└── .gitignore
```

## ⚙️ Funcionalidades

### `main.py` + `scraper.py` — Scraper principal
- Abre o site [books.toscrape.com](https://books.toscrape.com/) com o Chrome via Selenium.
- Percorre **todas as páginas** do catálogo clicando no botão "next", aguardando o carregamento (`WebDriverWait`) a cada transição.
- Para cada livro extrai: **nome**, **preço**, **disponibilidade** e **avaliação (rating)**, convertendo a classificação textual (`One` a `Five`) em número (1 a 5).
- Trata erros pontuais de elementos ausentes/inválidos sem interromper a coleta (`NoSuchElementException`, `ValueError`, `KeyError`), relançando apenas falhas de elemento obsoleto (`StaleElementReferenceException`).
- Consolida os resultados em um `DataFrame` do pandas e exporta para **Excel** (`books_selenium.xlsx`) na pasta `Downloads/books_selenium`.
- Registra todo o processo em log (arquivo + console), incluindo o total de livros coletados por página e ao final da execução.

### `tabs_test.py` — Manipulação de abas
- Demonstra como abrir uma nova aba (`driver.switch_to.new_window("tab")`), navegar nela, listar as abas abertas (`window_handles`), fechar uma aba e voltar para a aba original (`switch_to.window`).

### `logging_test.py` — Configuração de logging
- Exemplo simples e isolado de configuração do módulo `logging` (`logging.basicConfig`), gerando mensagens de nível `INFO`, `WARNING` e `ERROR` em um arquivo dentro da pasta `logs/`.

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Selenium](https://www.selenium.dev/) — automação do navegador
- [pandas](https://pandas.pydata.org/) — manipulação dos dados extraídos
- [openpyxl](https://openpyxl.readthedocs.io/) — exportação para `.xlsx`
- Módulo `logging` da biblioteca padrão

## ✅ Pré-requisitos

- Python 3.10+ instalado
- Google Chrome instalado (o Selenium Manager cuida do download do driver automaticamente)

## 🚀 Instalação

```powershell
# Clonar o repositório
git clone https://github.com/Ronyfranzini84/selenium_automation.git
cd selenium_automation

# Criar e ativar um ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

# Instalar as dependências
pip install -r requirements.txt
```

## ▶️ Como executar

Extrair todos os livros do site e gerar a planilha Excel:

```powershell
python main.py
```

O resultado será salvo em `~/Downloads/books_selenium/books_selenium.xlsx` e o log da execução em `logs/selenium.log`.

Executar os exemplos isolados de aprendizado:

```powershell
python tabs_test.py
python logging_test.py
```

## 📝 Observações

- Este é um projeto de **estudo**, criado para praticar conceitos de Selenium como esperas explícitas (`WebDriverWait`/`expected_conditions`), localização de elementos (`By.XPATH`), tratamento de exceções, logging e manipulação de janelas/abas.
- A pasta `logs/` e os arquivos gerados (`.xlsx`, `.log`) são ignorados pelo Git conforme definido em [.gitignore](.gitignore).
