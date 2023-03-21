import json
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


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
            atr_list = ['id', 'first_name', 'last_name', 'username', 'password']
            rows = cursor.fetchone()
            response_dict = {}
            [response_dict.update({atr_list[i]: row}) for i, row in enumerate(rows)]
            return JsonResponse({"message": "Registered Successfully", "data": response_dict, "status": 202},
                                status=202)
    return JsonResponse({"Message": "Method not allowed", "status": 405}, status=405)


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
            atr_list = ['id', 'first_name', 'last_name', 'username', 'password']
            rows = cursor.fetchone()
            data = {}
            [data.update({atr_list[i]: row}) for i, row in enumerate(rows)]
        return JsonResponse({"message": "Updated Successfully", "data": data, "status": 201}, status=201)
    return JsonResponse({"Message": "Method not allowed", "status": 405}, status=405)


def retrieve_users(request):
    if request.method == "GET":
        cursor = connection.cursor()
        cursor.execute("select * from user_user")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return JsonResponse({"message": "Data Retrieved", "data": data, "status": 200})


def delete_user(request):
    data = json.loads(request.body)
    user_id = data.get("id")
    if request.method == "DELETE":
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM user_user WHERE id=%s", [user_id])
    return JsonResponse({"message": "Deleted Successfully", "status": 204})
