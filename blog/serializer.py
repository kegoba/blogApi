from rest_framework import serializers
from .models import User, Post, Comments, Share



class Userserializer (serializers.ModelSerializer):
   
    class Meta:
        model= User
        fields = ["id", "first_name", "last_name", "password", "email" ]
       

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
         
        fields=["id","tittle", "post_body", "post_by", "post_date"]



class Commentserializer(serializers.ModelSerializer):

    #post_id = serializers.PrimaryKeyRelatedField(many=True, read_only =True)

    class Meta:
        model = Comments
      
        fields=["id","comment", "comment_by","post_id"]

class Shareserializer(serializers.ModelSerializer):
    class Meta:
        model = Share
   
        fields=["likes", "shares", "quote"]


