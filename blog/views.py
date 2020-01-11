from django.shortcuts import  render, get_object_or_404

from  django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models  import User, Post, Comments, Share 
from .serializer import Userserializer, Postserializer, Commentserializer, Shareserializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
# Create your views here.

def Home(request):
    pass
#####################################################################################
## create  a post function
#####################################################################################
@api_view (["POST", "GET"])
def Create_post(request):
    if request.method == "POST":
        blog_post = Postserializer(data = request.data)
        #print("this is post:", blog_post)
        if blog_post.is_valid():
            blog_post.save()
            print("this is post 2:", blog_post)
           
            return Response(blog_post.data, status=status.HTTP_200_OK)
        return Response(blog_post.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(blog_post.data, status=status.HTTP_200_OK)   
 #####################################################################################
## sign up function function
#####################################################################################       
@api_view(["POST", "GET"])
def Sign_up(request):
    if request.method == "POST":
        create_user = Userserializer(data= request.data)
        if create_user.is_valid():
            create_user.save()
            return Response(create_user.data, status = status.HTTP_200_OK)
        return Response(create_user.errors, status.HTTP_400_BAD_REQUEST)
    return Response(create_user.data, status.HTTP_200_OK)
#####################################################################################
## login function
#####################################################################################
@api_view(["POST","GET"])
def Login(request):
    if request.method == "POST":
       
        data =  Userserializer(data= request.data)
        email = (data.initial_data["email"])
        password = (data.initial_data["password"])
        user = User.objects.get(email=email)
        if user is not None:
            print("this is password:",user.password)
            if user.password ==  password:
                user_data ={
                    "email" : user.email,
                    "first_name" : user.first_name,
                    "last_name" : user.last_name
                }
                return Response(user_data ,status = status.HTTP_200_OK)
                
        return Response({"error":"wrong password or email" },status=status.HTTP_401_UNAUTHORIZED)

#####################################################################################
## create  a post function
#####################################################################################
@api_view (["POST", "GET"])
def Create_post(request):
    if request.method == "POST":
        blog_post = Postserializer(data = request.data)
        #print("this is post:", blog_post)
        if blog_post.is_valid():
            blog_post.save()
            print("this is post 2:", blog_post)
           
            return Response(blog_post.data, status=status.HTTP_200_OK)
        return Response(blog_post.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(blog_post.data, status=status.HTTP_200_OK)

  #####################################################################################
##  function that display a single post and all the comments link to it (one to many comments) 
#####################################################################################       
@api_view(["POST", "GET"])
def Display_post(request):
    if request.method == "GET":
        qry = Post.objects.all()
        posts = Postserializer(qry, many=True)
        return Response(posts.data, status = status.HTTP_200_OK)
        return Response(posts.errors, status.HTTP_400_BAD_REQUEST)
    return Response(posts.data, status = status.HTTP_200_OK)


#####################################################################################
##  fuction to display all the registered users
#####################################################################################
@api_view(["DELETE", "GET"])
def All_users(request):
    if request.method == "DELETE":
        qry = Post.objects.all()
        qry.delete()
        posts = Commentserializer(qry, many=True)
        
        return Response(posts.data, status = status.HTTP_200_OK)
        return Response(posts.errors, status.HTTP_400_BAD_REQUEST)
    return Response(posts.data, status = status.HTTP_200_OK)





@api_view(["GET"])
def Viewpost(request, id):
    if request.method == "GET":
        try:
            post = Post.objects.get(id=id)
            posts = Postserializer(post)
            return Response(posts.data, status=200)
        except:
            return Response({"Error": "Does Not Exist" }, status=400)
#####################################################################################
## function that will create  a comment 
#####################################################################################
@api_view(["POST","GET"])
def Create_Comment(request,id):
    #obj = {}
    data ={}
    new_comment = None
    post = Post.objects.get(id=id)
    create_comment = Commentserializer(data= request.data)
    comment =Comments.objects.filter(post_id=id)
    if request.method == "POST":
        create_comment = Commentserializer(data= request.data)
        comment= create_comment.initial_data["comment"]
        comment_by = create_comment.initial_data["comment_by"]
        posts = post.post_id.create(comment= comment, comment_by=comment_by)
        related_post = post.post_id.all()
        return Response(related_post.values(),  status = status.HTTP_200_OK)
    elif request.method=="GET":
        related_post = post.post_id.all()
        return Response(related_post.values(),  status = status.HTTP_200_OK)
    return Response(new_comment.errors, statu= status.HTTP_400_BAD_REQUEST)
        

#####################################################################################
## class that will display all the post with page number
#####################################################################################
class Forum(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    pagination_class = PageNumberPagination

#####################################################################################
## class that will display all the comments with page number
#####################################################################################
class DisplayComment(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = Commentserializer
    pagination_class = PageNumberPagination



@api_view(["GET"])
def Qoute_post(request,id):
    if request.method == "GET":
        try:
            post = Post.objects.get(id=id)
            posts = Postserializer(post)
            return Response(posts.data, status = status.HTTP_200_OK)
        except:
            return Response({"Error": "Does Not Exist" }, status=400)

    

@api_view(["DELETE"])
def Delete_post(request,id):
    if request.method == "DELETE":
        try:
            post = Post.objects.get(id=id)
            post.delete()
            posts = Postserializer(post)
            return Response(posts.data, status = status.HTTP_200_OK)
        except:
            return Response({"Error": "Does Not Exist" }, status=400)
