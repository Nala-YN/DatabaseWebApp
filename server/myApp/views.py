import base64
import decimal
import json
import sys

sys.path.append('../')
from myApp.models import user_info
from myApp.models import sell_book
from myApp.models import post
from myApp.models import message
from myApp.models import cart
from myApp.models import order
from myApp.models import comment
from django.db.models import Max
from django.http import JsonResponse

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
    base64_str = request_dict.get('book_image')
    ori_str = base64_str
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
    book_image = request_dict.get('book_image')
    image_data = base64.b64decode(book_image)
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

    user_post = post.objects.filter(user_id=user_id). \
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

    response = {'userinfo': userinfo}
    return JsonResponse(response)


# 修改用户信息
def modifyinfo(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']
    modify_which = request_dict['modify_which']
    modify_content = request_dict['modify_content']

    modify_info = user_info.objects.get(user_id=user_id)

    if modify_which == "phonenum":
        modify_info.user_phonenum = modify_content
    elif modify_which == "email":
        modify_info.user_email = modify_content
    elif modify_which == "campus":
        modify_info.user_campus = modify_content
    elif modify_which == "address":
        modify_info.user_address = modify_content
    elif modify_which == "money":
        modify_info.user_money = modify_content

    modify_info.save()
    response = {'success': True}
    return JsonResponse(response)


# 修改用户密码
def modifypassword(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']
    old_pw = request_dict['old_pw']
    new_pw = request_dict['new_pw']

    response = {'success': False}

    modify_user = user_info.objects.get(user_id=user_id)
    user_password = user_info.objects.filter(user_id=user_id).values('user_password')
    user_password = user_password[0]['user_password']
    if old_pw == user_password:
        modify_user.user_password = new_pw
        modify_user.save()
        response['success'] = True

    return JsonResponse(response)


# 获取消息
def getMsgs(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    messages = message.objects.filter(receive_id=user_id).order_by('message_id'). \
        values('message_id', 'from_solder', 'send_id', 'message_time', 'message_content')

    buyerMsgs = []
    sellerMsgs = []
    for i in messages:
        i['msg_id'] = int(i.pop('message_id'))
        i['year'] = int(str(i['message_time']).split('-')[0])
        i['month'] = int(str(i['message_time']).split('-')[1])
        i['day'] = int(str(i['message_time']).split('-')[2])
        i.pop('message_time')
        i['content'] = i.pop('message_content')
        send_info = user_info.objects.filter(user_id=user_id).values('user_name', 'user_phonenum')
        send_name = send_info[0]['user_name']
        send_phone = send_info[0]['user_phonenum']
        i['phoneNum'] = send_phone
        if i['from_solder'] == 0:
            i['buyerName'] = send_name
            i.pop('from_solder')
            buyerMsgs.append(i)
        elif i['from_solder'] == 1:
            i['sellerName'] = send_name
            i.pop('from_solder')
            sellerMsgs.append(i)
    response = {'buyerMsgs': buyerMsgs,
                'sellerMsgs': sellerMsgs}
    return JsonResponse(response)


# 删除一条消息
def rmMsg(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    msg_id = request_dict['msg_id']

    message.objects.get(message_id=msg_id).delete()

    response = {'success': True}
    return JsonResponse(response)


# 删除用户的所有消息
def rmUserMsg(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    message.objects.filter(receive_id=user_id).delete()

    response = {'success': True}
    return JsonResponse(response)


# 加入购物车
def addtocart(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']
    item_id = request_dict['item_id']
    response = {'success': False}

    query_result = cart.objects.filter(cart_item_id=item_id, cart_custom_id=user_id)
    if len(query_result) >= 1:
        return JsonResponse(response)

    max_id = cart.objects.all().aggregate(Max('cart_id'))  # 查询当前最大的id
    if max_id['cart_id__max'] is not None:
        new_id = int(max_id['cart_id__max']) + 1  # 若不为空，新id为最大id加1
    else:
        new_id = 1  # 若为空，id为1

    cart.objects.create(cart_id=new_id, cart_item_id=item_id, cart_custom_id=user_id)
    response['success'] = True
    return JsonResponse(response)


# 购买书籍
def buybook(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']
    item_id = request_dict['item_id']
    response = {'success': False}

    balance = user_info.objects.filter(user_id=user_id).values('user_money')
    balance = balance[0]['user_money']

    price = sell_book.objects.filter(sell_id=item_id).values('sell_book_price')
    price = price[0]['sell_book_price']

    if balance < price:
        return JsonResponse(response)

    book_info = sell_book.objects.filter(sell_id=item_id).values('sell_merchant_id', 'sell_book_intro',
                                                                 'sell_book_name',
                                                                 'sell_book_photo', 'sell_book_price')


    sell_id = book_info[0]['sell_merchant_id']
    intro = book_info[0]['sell_book_intro']
    name = book_info[0]['sell_book_name']
    photo = book_info[0]['sell_book_photo']
    sell_book.objects.get(sell_id=item_id).delete()

    max_id = order.objects.all().aggregate(Max('order_id'))  # 查询当前最大的id
    if max_id['order_id__max'] is not None:
        order_id = int(max_id['order_id__max']) + 1  # 若不为空，新id为最大id加1
    else:
        order_id = 1  # 若为空，id为1
    order.objects.create(order_id=order_id, order_book_intro=intro, order_book_name=name, order_book_price=price,
                         order_book_photo=photo, order_customer_id=user_id, order_merchant_id=sell_id,
                         order_status="未完成")

    max_id = message.objects.all().aggregate(Max('message_id'))  # 查询当前最大的id
    if max_id['message_id__max'] is not None:
        message_id = int(max_id['message_id__max']) + 1  # 若不为空，新id为最大id加1
    else:
        message_id = 1  # 若为空，id为1

    message.objects.create(message_id=message_id, from_solder=0, send_id=user_id, receive_id=sell_id,
                           message_content="您的书籍" + name + "已有人购买，请您与其联系")

    response['success'] = True
    return JsonResponse(response)


# 获取在售书籍
def getbooks(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    book_list = sell_book.objects.exclude(sell_merchant_id=user_id).values('sell_id', 'sell_book_intro',
                                                                           'sell_book_name', 'sell_book_price',
                                                                           'sell_book_photo').order_by('sell_id')[:20]

    books = []
    for i in book_list:
        i['id'] = i.pop('sell_id')
        i['name'] = i.pop('sell_book_name')
        i['intro'] = i.pop('sell_book_intro')
        i['image'] = str(base64.b64encode(i.pop('sell_book_photo')))
        i['image'] = tobase64(i['image'])
        i['price'] = i.pop('sell_book_price')
        books.append(i)

    response = {'books': books}
    return JsonResponse(response)


# 搜索在售书籍
def searchbooks(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']
    content = request_dict['content']

    book_list = sell_book.objects.exclude(sell_merchant_id=user_id).filter(sell_book_name__icontains=content). \
                    values('sell_id', 'sell_book_intro', 'sell_book_name', 'sell_book_price',
                           'sell_book_photo').order_by('sell_id')[:20]

    books = []
    for i in book_list:
        i['id'] = i.pop('sell_id')
        i['name'] = i.pop('sell_book_name')
        i['intro'] = i.pop('sell_book_intro')
        i['image'] = str(base64.b64encode(i.pop('sell_book_photo')))
        i['image'] = tobase64(i['image'])
        i['price'] = i.pop('sell_book_price')
        books.append(i)

    response = {'books': books}
    return JsonResponse(response)


# 获取在售书籍详细信息
def getdetail(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    book_id = request_dict['book_id']

    book_info = sell_book.objects.filter(sell_id=book_id).values('sell_merchant_id', 'sell_book_intro',
                                                                 'sell_book_name',
                                                                 'sell_book_photo', 'sell_book_price')

    seller_id = book_info[0]['sell_merchant_id']

    book = {'id': book_id,
            'name': book_info[0]['sell_book_name'],
            'intro': book_info[0]['sell_book_intro'],
            'image': tobase64(str(base64.b64encode(book_info[0]['sell_book_photo']))),
            'price': book_info[0]['sell_book_price']}

    seller_info = user_info.objects.filter(user_id=seller_id).values('user_name', 'user_address', 'user_campus',
                                                                     'user_phonenum')

    seller = {'name': seller_info[0]['user_name'],
              'phonenum': seller_info[0]['user_phonenum'],
              'campus': seller_info[0]['user_campus'],
              'address': seller_info[0]['user_address']}

    seller_comment = comment.objects.filter(commented_user_id=seller_id).values('comment_user_id', 'comment_date',
                                                                                'comment_content')

    comments = []

    for i in seller_comment:
        i['content'] = i.pop('comment_content')
        i['date'] = str(i.pop('comment_date'))
        name = user_info.objects.filter(user_id=i['comment_user_id']).values('user_name')
        i['name'] = name[0]['user_name']
        i.pop('comment_user_id')
        comments.append(i)

    response = {'seller': seller,
                'book': book,
                'comments': comments}
    return JsonResponse(response)


# 获取买家的订单信息
def getbought(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    order_info = order.objects.filter(order_customer_id=user_id, order_status="未完成"). \
        values('order_id', 'order_book_name', 'order_book_intro', 'order_book_price', 'order_book_photo',
               'order_merchant_id')

    items = []

    for i in order_info:
        i['id'] = i.pop('order_id')
        i['name'] = i.pop('order_book_name')
        i['intro'] = i.pop('order_book_intro')
        i['price'] = i.pop('order_book_price')
        i['image'] = str(base64.b64encode(i.pop('order_book_photo')))
        i['image'] = tobase64(i['image'])
        seller_info = user_info.objects.filter(user_id=i['order_merchant_id']).values('user_name', 'user_phonenum')
        i['sellerName'] = seller_info[0]['user_name']
        i['phoneNum'] = seller_info[0]['user_phonenum']
        i.pop('order_merchant_id')
        items.append(i)

    response = {'items': items}
    return JsonResponse(response)


# 买家确认收货和添加评论
def confirm(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    item_id = request_dict['item_id']

    order_info = order.objects.get(order_id=item_id)
    order_info.order_status = "已完成"
    order_info.save()

    order_info = order.objects.filter(order_id=item_id).values('order_customer_id', 'order_merchant_id',
                                                               'order_book_price', 'order_book_name')

    send_id = order_info[0]['order_customer_id']
    receive_id = order_info[0]['order_merchant_id']
    price = order_info[0]['order_book_price']
    name = order_info[0]['order_book_name']

    max_id = message.objects.all().aggregate(Max('message_id'))  # 查询当前最大的id
    if max_id['message_id__max'] is not None:
        message_id = int(max_id['message_id__max']) + 1  # 若不为空，新id为最大id加1
    else:
        message_id = 1  # 若为空，id为1

    message.objects.create(message_id=message_id, from_solder=0, send_id=send_id, receive_id=receive_id,
                           message_content="您的书籍" + name + "的买家已确认收到书籍")

    seller = user_info.objects.get(user_id=receive_id)
    seller.user_money = float(seller.user_money) + float(price)
    seller.save()

    buyer = user_info.objects.get(user_id=send_id)
    buyer.user_money = float(buyer.user_money) - float(price)
    buyer.save()

    if 'content' in request_dict:
        max_id = comment.objects.all().aggregate(Max('comment_id'))  # 查询当前最大的id
        if max_id['comment_id__max'] is not None:
            comment_id = int(max_id['comment_id__max']) + 1  # 若不为空，新id为最大id加1
        else:
            comment_id = 1  # 若为空，id为1

        comment.objects.create(comment_id=comment_id, comment_user_id=send_id, commented_user_id=receive_id,
                               comment_content=request_dict['content'])

    response = {'success': True}
    return JsonResponse(response)


# 发送消息
def sendMsg(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    item_id = request_dict['item_id']
    content = request_dict['content']
    from_which = request_dict['from_which']

    order_info = order.objects.filter(order_id=item_id).values('order_customer_id', 'order_merchant_id')

    send_id = order_info[0]['order_customer_id']
    receive_id = order_info[0]['order_merchant_id']

    if from_which == 1:
        send_id = order_info[0]['order_merchant_id']
        receive_id = order_info[0]['order_customer_id']

    max_id = message.objects.all().aggregate(Max('message_id'))  # 查询当前最大的id
    if max_id['message_id__max'] is not None:
        message_id = int(max_id['message_id__max']) + 1  # 若不为空，新id为最大id加1
    else:
        message_id = 1  # 若为空，id为1

    message.objects.create(message_id=message_id, from_solder=from_which, send_id=send_id, receive_id=receive_id,
                           message_content=content)

    response = {'success': True}
    return JsonResponse(response)


# 获取历史购买消息
def getboughtHistory(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    order_info = order.objects.filter(order_customer_id=user_id, order_status="已完成"). \
        values('order_id', 'order_book_name', 'order_book_intro', 'order_book_price', 'order_book_photo',
               'order_merchant_id')

    items = []

    for i in order_info:
        i['id'] = i.pop('order_id')
        i['name'] = i.pop('order_book_name')
        i['intro'] = i.pop('order_book_intro')
        i['price'] = i.pop('order_book_price')
        i['image'] = str(base64.b64encode(i.pop('order_book_photo')))
        i['image'] = tobase64(i['image'])
        seller_info = user_info.objects.filter(user_id=i['order_merchant_id']).values('user_name', 'user_phonenum')
        i['sellerName'] = seller_info[0]['user_name']
        i['phoneNum'] = seller_info[0]['user_phonenum']
        i.pop('order_merchant_id')
        items.append(i)

    response = {'items': items}
    return JsonResponse(response)


# 获取购物车信息
def getcart(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    cart_info = cart.objects.filter(cart_custom_id=user_id).values('cart_item_id')

    books = []

    for i in cart_info:
        i['id'] = i.pop('cart_item_id')
        book_info = sell_book.objects.filter(sell_id=i['id']).values('sell_book_intro', 'sell_book_name',
                                                                     'sell_book_photo', 'sell_book_price')
        i['name'] = book_info[0]['sell_book_name']
        i['intro'] = book_info[0]['sell_book_intro']
        i['price'] = book_info[0]['sell_book_price']
        i['image'] = str(base64.b64encode(book_info[0]['sell_book_photo']))
        i['image'] = tobase64(i['image'])
        books.append(i)

    response = {'books': books}
    return JsonResponse(response)


# 从购物车中移除
def rmFromCart(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']
    item_id = request_dict['item_id']

    cart_id = cart.objects.filter(cart_item_id=item_id, cart_custom_id=user_id).values('cart_id')
    if len(cart_id) >= 1:
        cart.objects.get(cart_item_id=item_id, cart_custom_id=user_id).delete()

    response = {'success': True}
    return JsonResponse(response)


# 结算购物车中所有书籍
def buyAll(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    cart_info = cart.objects.filter(cart_custom_id=user_id).values('cart_item_id')

    response = {'success': False}

    total_price = decimal.Decimal(0.00)
    for i in cart_info:
        book_price = sell_book.objects.filter(sell_id=i['cart_item_id']).values('sell_book_price')
        total_price = total_price + book_price[0]['sell_book_price']

    balance = user_info.objects.filter(user_id=user_id).values('user_money')
    balance = balance[0]['user_money']
    if balance < total_price:
        return JsonResponse(response)

    for i in cart_info:
        book_info = sell_book.objects.filter(sell_id=i['cart_item_id']).values('sell_merchant_id', 'sell_book_intro',
                                                                               'sell_book_name',
                                                                               'sell_book_photo', 'sell_book_price')

        sell_id = book_info[0]['sell_merchant_id']
        intro = book_info[0]['sell_book_intro']
        name = book_info[0]['sell_book_name']
        photo = book_info[0]['sell_book_photo']
        price = book_info[0]['sell_book_price']
        sell_book.objects.get(sell_id=i['cart_item_id']).delete()

        max_id = order.objects.all().aggregate(Max('order_id'))  # 查询当前最大的id
        if max_id['order_id__max'] is not None:
            order_id = int(max_id['order_id__max']) + 1  # 若不为空，新id为最大id加1
        else:
            order_id = 1  # 若为空，id为1

        order.objects.create(order_id=order_id, order_book_intro=intro, order_book_name=name, order_book_price=price,
                             order_book_photo=photo, order_customer_id=user_id, order_merchant_id=sell_id,
                             order_status="未完成")

        max_id = message.objects.all().aggregate(Max('message_id'))  # 查询当前最大的id
        if max_id['message_id__max'] is not None:
            message_id = int(max_id['message_id__max']) + 1  # 若不为空，新id为最大id加1
        else:
            message_id = 1  # 若为空，id为1

        message.objects.create(message_id=message_id, from_solder=0, send_id=user_id, receive_id=sell_id,
                               message_content="您的书籍《" + name + "》已有人购买，请您与其联系")

    response['success'] = True
    return JsonResponse(response)


# 获取卖家的订单信息
def getsold(request):
    assert request.method == "POST"
    request_dict = json.loads(request.body.decode('utf-8'))

    user_id = request_dict['user_id']

    order_info = order.objects.filter(order_merchant_id=user_id, order_status="未完成").\
        values('order_id', 'order_book_name', 'order_book_intro', 'order_book_price', 'order_book_photo',
               'order_customer_id')

    items = []

    for i in order_info:
        i['id'] = i.pop('order_id')
        i['name'] = i.pop('order_book_name')
        i['intro'] = i.pop('order_book_intro')
        i['price'] = i.pop('order_book_price')
        i['image'] = str(base64.b64encode(i.pop('order_book_photo')))
        i['image'] = tobase64(i['image'])
        buyer_info = user_info.objects.filter(user_id=i['order_customer_id']).values('user_name', 'user_phonenum')
        i['buyerName'] = buyer_info[0]['user_name']
        i['phoneNum'] = buyer_info[0]['user_phonenum']
        i.pop('order_customer_id')
        items.append(i)

    response = {'items': items}
    return JsonResponse(response)


def tobase64(half_base64):
    half_base64 = half_base64.replace("'", "", 2)
    half_base64 = half_base64[1:]
    half_base64 = half_base64.replace("data", "data:")
    half_base64 = half_base64.replace("base64", ";base64,")
    return half_base64
