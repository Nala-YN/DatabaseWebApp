import json
import sys

sys.path.append('../')
import pymysql.cursors
from django.views.decorators.csrf import csrf_exempt
from server.settings import DATABASES as db_conf
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse


# Create your views here.
# 与数据库连接
def create_connection():
    return pymysql.connect(host=db_conf["default"]["HOST"],
                           user=db_conf["default"]["USER"],
                           password=db_conf["default"]["PASSWORD"],
                           database=db_conf["default"]["NAME"],
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)


# 仅为测试能否连接数据库时所写，无用
"""
@csrf_exempt
def register_info(request):
    if request.method == "GET":
        return render(request, "login.html")
    # request_dict = json.loads(request.body.decode('utf-8'))

    # user_name = request_dict["userName"]
    # telephone = request_dict["telephone"]
    # password = request_dict["password"]

    user_name = request.POST.get("userName")
    telephone = request.POST.get("telephone")
    password = request.POST.get("password")

    connection = create_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('insert into user(user_name,telephone,password) values(%s,%s,%s)', [user_name, telephone, password])
            connection.commit()

    return HttpResponse(None)
"""


# 注册
@csrf_exempt
def register(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_name = request_dict["username"]
    email = request_dict["email"]
    password = request_dict["password"]
    phone = request_dict["phone"]
    campus = request_dict["campus"]
    address = request_dict["address"]

    connection = create_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('insert into user_info(user_name,user_email,user_password,user_phonenum,user_campus,user_address)'
                           ' values(%s,%s,%s,%s,%s,%s)',[user_name, email, password, phone, campus, address])
            connection.commit()

    return HttpResponse(None)


# 登录
@csrf_exempt
def login(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))
    user_name = request_dict["username"]
    password = request_dict["password"]

    connection = create_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("select * from user_info where user_name = %s and user_password = %s", [user_name, password])
            is_success = cursor.fetchall()
            connection.commit()
            if len(is_success) == 1:
                response = {"isSuccess": True}
                return JsonResponse(response)
            else:
                response = {"isSuccess": False}
                return JsonResponse(response)



