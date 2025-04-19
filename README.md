# test-api

## Локальный запуск

---

### Требования

- Python **3.12** (рекомендуемая версия)
- Redis
- PostgreSQL

---

## Установка

1. **Клонировать репозиторий**
    ```shell
    git clone https://github.com/fSultan13/test-api.git
    cd test-api
    ```

2. **Создать виртуальное окружение**  
    Рекомендуем использовать Python 3.12:
   ```shell
    python -m venv venv
   ```
    ```shell
    source venv/bin/activate    # Linux/MacOS
     ```
     ```shell
   venv\Scripts\activate       # Windows
    ```

3. **Создать файл окружения**  
   Скопируйте пример и заполните все необходимые переменные:
    ```shell
    cp .env.example .env
    ```

4. **Убедиться, что Redis и PostgreSQL установлены и запущены**  
   - Запустить сервер Redis:
     ```shell
     redis-server
     ```
   - Запустить PostgreSQL (если сервис не запущен автоматически).

5. **Установить зависимости**
    ```shell
    pip install -r requirements.txt
    ```

---

### Настройка базы данных

1. **Применить миграции**
    ```shell
    python manage.py migrate
    ```

2. **Создать суперпользователя**
    ```shell
    python manage.py createsuperuser
    ```

---

### Запуск сервера

```shell
python manage.py runserver
```

Запуск celery:
```shell
celery -A project_test worker -l info --pool=threads
```
После запуска локальный сервер будет доступен по адресу:

Админ-панель:
http://127.0.0.1:8000/admin/

Swagger UI (API-документация):
http://127.0.0.1:8000/api/schema/swagger-ui/