# address_coordinates
Получение координат по адресу, с подсказкой ввода самого адреса.

### Технологии
* Python 3.10.4
* Django 2.2

### Установка проекта
- Установите и активируйте виртуальное окружение
```
python -m venv env
```
```
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- Выполнить миграции:
```
python manage.py migrate
```
- Создать суперпользователя:
```
python manage.py createsuperuser
```
- Перейти по адресу: http://127.0.0.1:8000/admin/
После проделанных действий на главной странице админки, будет ссылка на требуемую страницу с выполненным тестовым заданием.
### Для запуска dev сервера:
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
``` 
### Авторы
Артём Жуков. 
