# Информация


Запуск сервера с помощью команды 
```bash
docker-compose up -d --build
```

После запуска требуется запустить миграции внутри контейнера командой
```bash
python3 manage.py migrate
```

Api описаны с помощью swagger, доступ по ссылке - http://127.0.0.1:8000/swagger/

    'api_auth/' - API для авторизации 
    'poll/<int:poll_pk>/user/<int:user_pk>/' - API для проверки ответов пользователя по определенномму опросу
    'user/<int:user_pk>/polls/' - API для просмотра пройденных опросов
    'polls/active/' - API для просмотра активных опросов
    'poll/<int:poll_pk>/' - API для просмотра конкретного опроса
    'manage/' - API для администратора