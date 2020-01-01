from django.db import models
class User(models.Model):
    id = models.AutoField(primary_key=True,serialize=True )
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField("email", unique=True)
    password = models.CharField( "password", max_length=100)
    phone = models.CharField("phone number", null=True,  max_length=15)
    date_joined = models.DateTimeField("date join", auto_now_add=True)

    def __str__(self):
        return self.email + self.password

class Post(models.Model):
    id = models.AutoField(primary_key=True,serialize=True )
    tittle = models.CharField("tittle of post", blank=True, max_length=255)
    post_body = models.CharField("post",  blank=True, max_length=25555)
    post_by = models.CharField("author name",  blank=True, max_length=255 )
    post_date = models.DateTimeField("time posted", auto_now_add=True)
    user = models.ForeignKey(User, null=True, related_name="user_post", on_delete=models.CASCADE)




class Comments(models.Model):
    id = models.AutoField(primary_key=True,serialize=True )
    comment = models.CharField("comment", null=True, max_length=2555)
    comment_by = models.CharField("Last name",null=True, max_length=255)
    post_date = models.DateTimeField("time commented", null=True, auto_now_add=True)
    user = models.ForeignKey(User, null=True, related_name="user_comment", on_delete=models.CASCADE)


class Share(models.Model):
    likes = models.IntegerField("number of likes", null=True, default=0)
    shares = models.IntegerField("number of shares", null=True, default=0)
    quote = models.IntegerField("number of quote", null=True, default=0)
    user = models.ForeignKey(User, null=True, related_name="user_share", on_delete=models.CASCADE)
   


