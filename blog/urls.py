from django.urls import path
from . import views



urlpatterns =[
    path("", views.Home, name="Home"),
    path("user/", views.All_users, name="all_users"),
    path("create_post/", views.Create_post, name="Create_post"),
    path("signup/", views.Sign_up, name="Sign_up"),
    path("login/", views.Login, name="Login"),
    path("displaypost/", views.Display_post, name="Display_post"),
    path("viewpost/<int:id>/", views.Viewpost, name="getpost"),
    path("comment/", views.Comment, name="Comment"),
    path("deletepost/<int:id>/", views.Delete_post, name="Delete_post"),
    path("forum/", views.Forum.as_view(), name="Forum"),
    path("displaycomment/", views.DisplayComment.as_view(), name="DisplayComment"),
   
        

        
]
