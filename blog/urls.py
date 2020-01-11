from django.urls import path
from . import views



urlpatterns =[
    path("", views.Home, name="Home"),
    path("user/", views.All_users, name="all_users"),
    path("create_post/", views.Create_post, name="Create_post"),
    path("signup/", views.Sign_up, name="Sign_up"),
    path("login/", views.Login, name="Login"),
    path("viewpost/<int:id>/", views.Viewpost, name="getpost"),
    path("comment/<int:id>/", views.Create_Comment, name="Create_Comment"),
    path("deletepost/<int:id>/", views.Delete_post, name="Delete_post"),
    path("forum/", views.Forum.as_view(), name="Forum"),
    path("quotepost/<int:id>/", views.Qoute_post, name="Qoute_post"),
    path("displaycomment/", views.DisplayComment.as_view(), name="DisplayComment"),
   
      

        
]
