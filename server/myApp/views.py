import base64
import json
import sys

sys.path.append('../')
import pymysql.cursors
from myApp.models import user_info
from myApp.models import sell_book
from myApp.models import post
from django.db.models import Max
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse


# Create your views here.


# 注册
def register(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    name = request_dict['username']
    email = request_dict['email']
    password = request_dict['password']
    phone = request_dict['phoneNum']
    campus = request_dict['campus']
    address = request_dict['address']
    response = {
        'success': False,
        'message': '',
        'user_id': '',
        'user_name': ''
    }

    exit_email = user_info.objects.filter(user_email=email)  # 查询邮箱是否存在
    if len(exit_email) >= 1:
        response['message'] = "邮箱账户已存在"
        return JsonResponse(response)

    exit_name = user_info.objects.filter(user_name=name)  # 查询用户昵称是否存在
    if len(exit_name) >= 1:
        response['message'] = "用户昵称已存在"
        return JsonResponse(response)

    max_id = user_info.objects.all().aggregate(Max('user_id'))  # 查询当前最大的id
    if max_id['user_id__max'] is not None:
        new_id = int(max_id['user_id__max']) + 1  # 若不为空，新id为最大id加1
    else:
        new_id = 1  # 若为空，id为1
    response['success'] = True
    response['user_id'] = new_id
    response['user_name'] = name
    user_info.objects.create(user_id=new_id, user_name=name, user_email=email, user_password=password,
                             user_phonenum=phone, user_campus=campus, user_address=address)
    return JsonResponse(response)


# 登录
def login(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    name = request_dict['username']
    password = request_dict['password']

    query_result = user_info.objects.filter(user_name=name, user_password=password).values('user_id')
    if len(query_result) == 1:
        response = {'isSuccess': True,
                    'userid': query_result[0]['user_id']}
    else:
        response = {'isSuccess': False}
    return JsonResponse(response)


def upload(request):
    request_dict = json.loads(request.body.decode('utf-8'))
    base64_str = request_dict.get('image')
    ori_str = base64_str  # 把这个上传到数据库，代表图片，可能要用blob类型
    base64_str = base64_str.split(',')[1]
    image_data = base64.b64decode(base64_str)
    with open('image.jpg', 'wb') as f:
        f.write(image_data)
    response = {'image_data': ori_str}
    return JsonResponse(response)


# 上传书籍信息
def uploadsell(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    merchant_id = request_dict['user_id']
    book_name = request_dict['book_name']
    book_intro = request_dict['book_intro']
    book_price = request_dict['book_price']
    book_image = request_dict['book_image']

    base64_str = book_image.split(',')[1]
    image_data = base64.b64decode(base64_str)

    response = {
        'success': False,
        'message': '',
    }

    if len(book_name) > 256:
        response['message'] = "书籍名称过长，最多为256字"
        return JsonResponse(response)
    if len(book_intro) > 256:
        response['message'] = "书籍介绍过长，最多为256字"
        return JsonResponse(response)
    if book_price >= 10000000000:
        response['message'] = "书籍价格过高"
        return JsonResponse(response)
    if '.' in str(book_price) and len(str(book_price).split('.')[1]) > 2:
        response['message'] = "价格最多两位小数"
        return JsonResponse(response)

    max_id = sell_book.objects.all().aggregate(Max('sell_id'))  # 查询当前最大的id
    if max_id['sell_id__max'] is not None:
        new_id = int(max_id['sell_id__max']) + 1  # 若不为空，新id为最大id加1
    else:
        new_id = 1

    sell_book.objects.create(sell_id=new_id, sell_merchant_id=merchant_id, sell_book_intro=book_intro,
                             sell_book_name=book_name, sell_book_price=book_price, sell_book_photo=image_data)
    response['success'] = True
    return JsonResponse(response)


# 上传帖子
def uploadpost(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']
    title = request_dict['title']
    content = request_dict['content']

    response = {
        'success': False,
        'message': '',
    }

    if len(title) > 256:
        response['message'] = "帖子标题过长，最多为256字"
        return JsonResponse(response)
    if len(content) > 256:
        response['message'] = "帖子内容过长，最多为256字"
        return JsonResponse(response)

    max_id = post.objects.all().aggregate(Max('post_id'))  # 查询当前最大的id
    if max_id['post_id__max'] is not None:
        new_id = int(max_id['post_id__max']) + 1  # 若不为空，新id为最大id加1
    else:
        new_id = 1

    post.objects.create(post_id=new_id, user_id=user_id, title=title, content=content)
    response['success'] = True
    return JsonResponse(response)


# 获取所有帖子
def getallpost(request):
    assert request.method == "POST"
    all_post = post.objects.all().order_by('post_id').values('post_id', 'title', 'user_id', 'content', 'post_date')
    posts = []
    for i in all_post:
        i['id'] = int(i.pop('post_id'))
        user_name = user_info.objects.filter(user_id=i['user_id']).values('user_name')
        user_name = user_name[0]['user_name']
        i.pop('user_id')
        i['username'] = user_name
        i['year'] = int(str(i['post_date']).split('-')[0])
        i['month'] = int(str(i['post_date']).split('-')[1])
        i['day'] = int(str(i['post_date']).split('-')[2])
        i.pop('post_date')
        posts.append(i)
    response = {'posts': posts}
    return JsonResponse(response)


# 获取用户的帖子
def getuserpost(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    user_post = post.objects.filter(user_id=user_id).\
        order_by('post_id').values('post_id', 'title', 'content', 'post_date')
    userposts = []
    for i in user_post:
        i['id'] = int(i.pop('post_id'))
        user_name = user_info.objects.filter(user_id=user_id).values('user_name')
        user_name = user_name[0]['user_name']
        i['username'] = user_name
        i['year'] = int(str(i['post_date']).split('-')[0])
        i['month'] = int(str(i['post_date']).split('-')[1])
        i['day'] = int(str(i['post_date']).split('-')[2])
        i.pop('post_date')
        userposts.append(i)
    response = {'userposts': userposts}
    return JsonResponse(response)


# 撤回帖子
def deletepost(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    post_id = request_dict['post_id']

    response = {'success': False}

    post.objects.get(post_id=post_id).delete()

    response['success'] = True
    return JsonResponse(response)


# 获取用户信息
def getuserinfo(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    get_info = user_info.objects.filter(user_id=user_id).values('user_name', 'user_phonenum', 'user_email',
                                                                'user_campus', 'user_address', 'user_money')
    userinfo = {'username': get_info[0]['user_name'],
                'phonenum': get_info[0]['user_phonenum'],
                'email': get_info[0]['user_email'],
                'campus': get_info[0]['user_campus'],
                'address': get_info[0]['user_address'],
                'money': get_info[0]['user_money']}
    print(userinfo)
    response = {'userinfo': userinfo}
    return JsonResponse(response)




