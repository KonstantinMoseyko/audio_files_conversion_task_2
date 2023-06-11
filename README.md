# Тестовое задание для _Python_-программиста. Задача 2

## "Audio files conversion task 2"
## Веб-сервис выполняет следующие функции:
  
  1. 
  2. 
  3. 
  4. 

  ### Stack
  [![Flask][Flask]][Flask-url] [![SQLAlchemy][SQLAlchemy]][SQLAlchemy-url] [![PostgreSQL][PostgreSQL]][PostgreSQL-url] [![Docker][Docker]][Docker-url]


## Инструкция по сборке и запуску сервиса
  
  1. Предполагается, что у пользователя уже установлены docker и docker-compose
  
  2. Клонируйте репозиторий
     ```sh
     git clone 
     ```
  
  3. Скопируйте и переименуйте .env.template в .env
     ```sh
     cp .env.template .env
     ```
  
  4. С помощью docker-compose билдим и апаем контейнеры
     ```sh
     docker compose build
     docker compose up
     ```

  5. Далее с помощью curl или другого инструмента делаем POST-запрос на http://127.0.0.1:5000/api/, например:
     ```sh
     
     ```
  
     



<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Flask]: https://img.shields.io/badge/flask-778876?style=for-the-badge&logo=flask&logoColor=black
[Flask-url]: https://palletsprojects.com/p/flask/
[SQLAlchemy]: https://img.shields.io/badge/sqlalchemy-778876?style=for-the-badge&logo=python&logoColor=black
[SQLAlchemy-url]: https://www.sqlalchemy.org/
[Docker]: https://img.shields.io/badge/Docker-230db7?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-233161?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/