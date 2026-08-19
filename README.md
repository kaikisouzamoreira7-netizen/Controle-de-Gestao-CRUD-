# 📊 Controle de Gestão

Sistema web desenvolvido em Python para auxiliar no gerenciamento e organização de informações administrativas.

Este projeto foi criado com o objetivo de colocar em prática conhecimentos de **Python, desenvolvimento web, banco de dados, HTML e CSS**, além de aprender na prática a organizar e versionar um projeto utilizando **Git e GitHub**.

## 📌 Sobre o projeto

O **Controle de Gestão** é uma aplicação web desenvolvida em Python que utiliza um banco de dados SQLite para armazenar as informações do sistema.

A aplicação possui uma estrutura baseada em:

* **Python** para a lógica da aplicação;
* **HTML** para a estrutura das páginas;
* **CSS** para a interface;
* **SQLite** para armazenamento dos dados;
* **Git e GitHub** para controle de versão.

## 🚀 Funcionalidades

Entre as principais funcionalidades e componentes do projeto estão:

* 📋 Gerenciamento de informações administrativas;
* 🗄️ Armazenamento de dados em banco SQLite;
* 🌐 Interface web;
* 🎨 Arquivos estáticos para estilização e recursos visuais;
* 📄 Páginas HTML organizadas em templates;
* 🔍 Ferramenta auxiliar para verificação do banco de dados.

## 🛠️ Tecnologias utilizadas

### Backend

* **Python**

### Banco de dados

* **SQLite**

### Frontend

* **HTML**
* **CSS**
* **JavaScript**, quando necessário

### Ferramentas

* **Git**
* **GitHub**
* **Visual Studio Code**

## 📂 Estrutura do projeto

```text
Controle de gestao/
│
├── static/
│   └── Arquivos estáticos do projeto
│
├── Templates/
│   └── Páginas HTML da aplicação
│
├── app.py
│   └── Arquivo principal da aplicação
│
├── banco.db
│   └── Banco de dados SQLite utilizado pelo sistema
│
├── banco_corrompido_backup.db
│   └── Cópia de segurança do banco de dados
│
├── verificar_banco.py
│   └── Script auxiliar para verificar o banco de dados
│
└── .gitignore
    └── Arquivos e pastas que não devem ser enviados ao Git
```

## ▶️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço do repositório no GitHub.

### 2. Entre na pasta do projeto

```bash
cd "Controle de gestao"
```

### 3. Verifique se o Python está instalado

```bash
python --version
```

### 4. Instale as dependências

Caso o projeto possua um arquivo `requirements.txt`, execute:

```bash
pip install -r requirements.txt
```

Caso ainda não exista esse arquivo, instale manualmente as bibliotecas utilizadas pelo `app.py`.

### 5. Execute a aplicação

```bash
python app.py
```

Depois, abra no navegador o endereço informado pelo programa.

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para armazenamento dos dados.

O arquivo principal é:

```text
banco.db
```

Também existe um arquivo de backup:

```text
banco_corrompido_backup.db
```

O script:

```text
verificar_banco.py
```

pode ser utilizado para auxiliar na verificação do banco de dados durante o desenvolvimento.

## 🎨 Interface

A interface do projeto é organizada utilizando:

* páginas HTML;
* templates;
* arquivos estáticos;
* CSS para estilização;
* componentes voltados para facilitar a utilização do sistema.

Os arquivos HTML ficam na pasta:

```text
Templates/
```

Enquanto os arquivos estáticos ficam em:

```text
static/
```

## 🔐 Controle de versão

Este projeto utiliza **Git** para controle de versão e **GitHub** para hospedagem do código.

Comandos básicos utilizados no desenvolvimento:

```bash
git status
git add .
git commit -m "Descrição da alteração"
git push
```

## 🎯 Objetivos do projeto

Este projeto tem como principais objetivos:

* Desenvolver aplicações utilizando Python;
* Aprender conceitos de desenvolvimento web;
* Trabalhar com bancos de dados SQLite;
* Melhorar a organização de projetos;
* Praticar Git e GitHub;
* Desenvolver uma aplicação útil para gerenciamento administrativo.

## 📚 O que estou aprendendo com este projeto

Durante o desenvolvimento deste projeto, estou colocando em prática conhecimentos relacionados a:

* Programação em Python;
* Desenvolvimento de aplicações web;
* Estruturação de páginas HTML;
* Estilização com CSS;
* Manipulação de bancos de dados;
* Organização de projetos;
* Git e GitHub;
* Depuração e correção de erros;
* Desenvolvimento de funcionalidades de forma incremental.

## 🔄 Próximas melhorias

Algumas melhorias que podem ser adicionadas ao projeto futuramente:

* [ ] Melhorar a interface;
* [ ] Adicionar novas funcionalidades de gerenciamento;
* [ ] Melhorar a validação dos dados;
* [ ] Criar um sistema de login e controle de acesso;
* [ ] Adicionar filtros e pesquisas mais avançadas;
* [ ] Melhorar os relatórios;
* [ ] Criar uma documentação mais detalhada;
* [ ] Criar um arquivo `requirements.txt`;
* [ ] Adicionar testes automatizados.

## 👨‍💻 Autor

**Kaiki Souza**

Projeto desenvolvido como parte do meu aprendizado e evolução na programação.

---

⭐ Este projeto representa parte da minha evolução no desenvolvimento de software e continuará sendo aprimorado conforme novos conhecimentos forem adquiridos.
