# 📦 Sistema de Gerenciamento de Estoque

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Django](https://img.shields.io/badge/Django-Framework-green?logo=django)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-API-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)

Sistema **Full Stack de gerenciamento de estoque** desenvolvido durante o curso **Django Master da PyCodeBR**.

O projeto implementa um sistema onde **usuários possuem diferentes níveis de acesso e permissões**, permitindo controlar operações dentro do estoque de forma segura e organizada.

Além da interface web utilizando **templates do Django**, o sistema também possui uma **API REST utilizando Django REST Framework**, permitindo integração com outros sistemas.

---

# 🧰 Stack Utilizada

| Tecnologia | Descrição |
|---|---|
| 🐍 **Python** | Linguagem principal do projeto |
| 🌐 **Django** | Framework web para desenvolvimento rápido e seguro |
| 🔌 **Django REST Framework** | Criação de API REST |
| 🐳 **Docker** | Containerização da aplicação |
| 🔐 **JWT Authentication** | Autenticação segura para a API |

---

# 🐋 Executando o Projeto com Docker

* Clonar Repositório
* * ```bash
    git clone https://github.com/Luisf66/sge.git
    ```
* Ir ao diretório
* * ```bash
    cd sge
    ```
* Execute
* * ```bash
    docker compose up --build
    ```
* Após iniciar, o sistema estará disponível em
* * ```bash
    http://localhost:8000
    ```

---

  # 👤 Criando um Superusuário

  ```bash
    docker exec -it {NOME DO CONTAINER} python manage.py createsuperuser
  ```
  * Informe nome, e-mail e senha do seu super usuário


---
 
# 📚 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de praticar e demonstrar conhecimentos em:

* desenvolvimento Full Stack com Django
* criação de APIs com Django REST Framework
* implementação de autenticação com JWT
* uso de Docker para containerização
* aplicação de boas práticas de arquitetura em projetos Django
  
