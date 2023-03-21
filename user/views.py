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
            return get_response(data=data, status=204)
    return get_response(status=405)
