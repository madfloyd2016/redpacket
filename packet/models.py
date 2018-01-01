from django.db import models


CATE_NAME_CHOICES = (
    (1, "美团外卖"),
    (2, "饿了么"),
)

class RedPacket(models.Model):
    title = models.CharField(max_length=60,
                             help_text="标题")
    cate_name = models.IntegerField(max_length=20,
                                    choices=CATE_NAME_CHOICES,
                                    help_text="分类")
    url = models.CharField(max_length=120, help_text="url")
    click_count = models.IntegerField(default=0, help_text="点击次数")
    add_time = models.DateTimeField(auto_now_add=True,
                                    help_text="添加时间")
    last_click_time = models.DateField(auto_now=True,
                                       help_text="最后抢的时间")
