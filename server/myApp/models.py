from django.db import models


# Create your models here.
class user_info(models.Model):
    user_id = models.CharField(max_length=64, primary_key=True)
    user_password = models.CharField(max_length=64)
    user_name = models.CharField(max_length=64)
    user_phonenum = models.CharField(max_length=11)
    user_email = models.CharField(max_length=64)
    user_campus = models.CharField(max_length=32)
    user_address = models.CharField(max_length=64)
    user_money = models.DecimalField(max_digits=32, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'user_info'  # 移除前缀


class sell_book(models.Model):
    sell_id = models.IntegerField(primary_key=True)
    sell_merchant = models.ForeignKey(user_info, on_delete=models.CASCADE)
    sell_book_intro = models.CharField(max_length=256)
    sell_book_name = models.CharField(max_length=256)
    sell_book_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_book_photo = models.BinaryField()

    class Meta:
        db_table = 'sell_book'


class post(models.Model):
    post_id = models.CharField(max_length=64, primary_key=True)
    user = models.ForeignKey(user_info, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    post_date = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'post'


class message(models.Model):
    message_id = models.CharField(max_length=64, primary_key=True)
    from_solder = models.IntegerField()
    send = models.ForeignKey(user_info, related_name='+', on_delete=models.CASCADE)
    receive = models.ForeignKey(user_info, related_name='+', on_delete=models.CASCADE)
    message_time = models.DateField(auto_now=True)
    message_content = models.CharField(max_length=256)

    class Meta:
        db_table = 'message'


class cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    cart_item = models.ForeignKey(sell_book, on_delete=models.CASCADE)
    cart_custom = models.ForeignKey(user_info, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'


class order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_time = models.DateField(auto_now=True)
    order_book_intro = models.CharField(max_length=256)
    order_book_name = models.CharField(max_length=256)
    order_book_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_book_photo = models.BinaryField()
    order_customer = models.ForeignKey(user_info, related_name="+", on_delete=models.CASCADE)
    order_merchant = models.ForeignKey(user_info, related_name="+", on_delete=models.CASCADE)
    order_status = models.CharField(max_length=10)

    class Meta:
        db_table = 'order'


class comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    commented_user = models.ForeignKey(user_info, related_name="+", on_delete=models.CASCADE)
    comment_user = models.ForeignKey(user_info, related_name="+", on_delete=models.CASCADE)
    comment_date = models.DateField(auto_now=True)
    comment_content = models.CharField(max_length=256)

    class Meta:
        db_table = 'comment'


