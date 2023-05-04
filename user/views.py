import json
from django.db import connection
from .utils import get_response


def register_user(request):
    data = json.loads(request.body)
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    username = data.get("username")
    password = data.get('password')
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user_user(first_name, last_name, username, password) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, username, password))
            cursor.execute("select * from user_user WHERE first_name=%s", [first_name])
            atr_list = ['id', 'username', 'password', 'first_name', 'last_name']
            data = {atr_list[i]: row for i, row in enumerate(cursor.fetchone())}
            return get_response(data=data, status=202)
    return get_response(status=405)


def retrieve_users(request):
    if request.method == "GET":
        cursor = connection.cursor()
        cursor.execute("select * from user_user")
        data = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
        return get_response(data=data, status=200)
    return get_response(status=405)


def update_user(request):
    data = json.loads(request.body)
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    username = data.get("username")
    password = data.get('password')
    user_id = data.get('id')
    if request.method == "PUT":
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE user_user SET first_name=%s, last_name=%s, username=%s, password=%s where id=%s",
                [first_name, last_name, username, password, user_id])
            cursor.execute("select * from user_user WHERE first_name=%s", [first_name])
            atr_list = ['id', 'username', 'password', 'first_name', 'last_name']
            data = {atr_list[i]: row for i, row in enumerate(cursor.fetchone())}
            return get_response(data=data, status=201)
    return get_response(status=405)


def delete_user(request):
    data = json.loads(request.body)
    user_id = data.get("user_id")
    if request.method == "DELETE":
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM user_user WHERE id=%s", [user_id])
            return get_response(status=204)
    return get_response(status=405)


def add_city(request):
    data = json.loads(request.body)
    city_name = data.get("city_name")
    user = data.get('user')
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user_city(city_name, user_id) VALUES (%s, %s)", (city_name, user))
            cursor.execute("select * from user_city WHERE city_name=%s", [city_name])
            atr_list = ['id', 'city_name', 'user_id']
            data = {atr_list[i]: row for i, row in enumerate(cursor.fetchone())}
            return get_response(data=data, status=202)
    return get_response(status=405)


def delete_city(request):
    data = json.loads(request.body)
    city_id = data.get("city_id")
    if request.method == "DELETE":
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM user_city WHERE id=%s", [city_id])
            return get_response(status=204)
    return get_response(status=405)


def retrieve(request):
    if request.method == "GET":
        cursor = connection.cursor()
        # cursor.execute("select * from user_user ORDER BY first_name")
        # cursor.execute("select * from user_user LIMIT 2")
        # cursor.execute("select * from user_user OFFSET 3 LIMIT 2")
        # cursor.execute("select * from user_user WHERE first_name LIKE '%A%'")
        # cursor.execute("select * from user_user WHERE id BETWEEN  '3' and '6'")
        # cursor.execute("select first_name from user_user WHERE first_name LIKE 'A%'")
        # cursor.execute("select COUNT(id), username from user_user GROUP BY username")
        # cursor.execute("select COUNT(id), first_name last_name from user_user GROUP BY first_name HAVING COUNT(id) = 1")
        # cursor.execute("select first_name AS Name from user_user")
        # cursor.execute("select * from user_user WHERE  id IN (2, 7)")
        # cursor.execute("select COUNT(id) from user_user")
        # cursor.execute("select COUNT(id) from user_user")
        # cursor.execute("select MIN(id) from user_user")
        # cursor.execute("select MAX(id) from user_user")
        # cursor.execute("select first_name, city_name from user_city JOIN user_user ON user_city.user_id = user_user.id")
        # cursor.execute("select * from user_city JOIN user_user ON user_city.user_id = user_user.id")
        # cursor.execute("select * from user_city INNER JOIN user_user ON user_city.user_id = user_user.id")
        # cursor.execute("select * from user_city LEFT JOIN user_user ON user_city.user_id = user_user.id")
        # cursor.execute("select first_name, city_name from user_city CROSS JOIN user_user")
        # cursor.execute("select * from user_city LEFT OUTER JOIN user_user ON user_city.user_id=user_user.id")
        # cursor.execute("select * from user_city RIGHT OUTER JOIN user_user ON user_city.user_id=user_user.id")
        cursor.execute("select first_name, city_name from user_city FULL OUTER JOIN user_user ON user_city.user_id=user_user.id")
        data = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
        return get_response(data=data, status=200)
    return get_response(status=405)
