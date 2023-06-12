# Тестовое задание для _Python_-программиста. Задача 2
# Веб-сервис"Audio files conversion task 2"

## Веб-сервис выполняет следующие функции:
  
  1. Создание пользователя, POST:
     - Принимает на вход запросы с именем пользователя;
     - Создаёт в базе данных пользователя заданным именем, так же генерирует уникальный идентификатор пользователя и UUID токен доступа (в виде строки) для данного пользователя;
     - Возвращает сгенерированные идентификатор пользователя и токен.
  2. Добавление аудиозаписи, POST:
     - Принимает на вход запросы, содержащие уникальный идентификатор пользователя, токен доступа и аудиозапись в формате wav;
     - Преобразует аудиозапись в формат mp3, генерирует для неё уникальный UUID идентификатор и сохраняет их в базе данных;
     - Возвращает URL для скачивания записи вида http://host:port/api/download?id_record=id_записи&id_user=id_юзера.
  3. Доступ к аудиозаписи, GET:
     - Предоставляет возможность скачать аудиозапись по ссылке из п 2.3.

  ### Stack
  [![Flask][Flask]][Flask-url] [![SQLAlchemy][SQLAlchemy]][SQLAlchemy-url] [![PostgreSQL][PostgreSQL]][PostgreSQL-url] [![Docker][Docker]][Docker-url]


## Инструкция по сборке и запуску сервиса
  
  1. Предполагается, что у пользователя уже установлены docker и docker-compose
  
  2. Клонируйте репозиторий
     ```sh
     git clone https://github.com/KonstantinMoseyko/audio_files_conversion_task_2.git
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

  5. C помощью curl делаем POST-запрос c содержимым вида {"username": "str"} на http://127.0.0.1:5000/api/registration/, например:
     ```sh
     curl -X POST -H "Content-Type: application/json" -d '{"username": "Bob"}' http://127.0.0.1:5000/api/registration/
     ```
     Получаем ответ (в Вашем случае может получиться другой ответ):
     ```sh
     {
      "id_user": 3,
      "user_token": "21dce7ef-a03e-4f3f-8dbd-d539dd01b25a"
     }
     ```
  
  6. Воспользуемся ответом из п.5, curl-ом делаем POST-запрос c содержимым вида "user_token=UUID_юзера", "id_user=id_юзера", "file_wav=@file_path(абсолютный путь до аудиофайла)" на http://127.0.0.1:5000/api/upload_audiorecord/, например:
     ```sh
     curl -F "user_token=21dce7ef-a03e-4f3f-8dbd-d539dd01b25a" -F "id_user=3" -F "file_wav=@/home/konstantin/Music/sample-6s.wav" http://127.0.0.1:5000/api/upload_audiorecord/
     ```
     Получаем ответ (в Вашем случае может получиться другой ответ):
     ```sh
     {
      "URL for download": "http://127.0.0.1:5000/api/download?id_record=4&id_user=3"
     }
     ```
   
   7. Далее переходите по полученной ссылочке для скачивания аудиофайла в формате "mp3", загрузка начнётся автоматически.
      

     











<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Flask]: https://img.shields.io/badge/flask-778876?style=for-the-badge&logo=flask&logoColor=black
[Flask-url]: https://palletsprojects.com/p/flask/
[SQLAlchemy]: https://img.shields.io/badge/sqlalchemy-778876?style=for-the-badge&logo=python&logoColor=black
[SQLAlchemy-url]: https://www.sqlalchemy.org/
[Docker]: https://img.shields.io/badge/Docker-230db7?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-233161?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/