from django.db import models

# Create your models here.


class UserSignup(models.Model):
    name=models.CharField(max_length=50)
    userName=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


class AddQuotes(models.Model):
    quotes=models.SlugField(max_length=1000)
    userName=models.ForeignKey(UserSignup,on_delete=models.CASCADE)


class ApproveQuotes(models.Model):
    user=models.ForeignKey(UserSignup, on_delete=models.CASCADE, default="")
    quotes=models.ForeignKey(AddQuotes, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.quotes


class Postlike(models.Model):
    user_id=models.ForeignKey(UserSignup,on_delete=models.CASCADE)

    