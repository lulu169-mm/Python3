from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)


"""
CREATE TABLE app01_userinfo (
    id bigint AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32),
    password VARCHAR(32),
    age INT
);

"""

# class Department(models.Model):
#     title=models.CharField(max_length=16)
#
# class Role(models.Model):
#     caption=models.CharField(max_length=16)