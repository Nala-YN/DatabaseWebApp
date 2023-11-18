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
