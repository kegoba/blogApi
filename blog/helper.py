@api_view(["POST", "GET"])
def Sign_up(request):
    if request.method == "POST":
        create_user = Userserializer(data= request.data)
        if create_user.is_valid():
            create_user.save()
            return Response(create_user.data, status = status.HTTP_200_OK)
        return Response(create_user.errors, status.HTTP_400_BAD_REQUEST)
    return Response(create_user.data, status.HTTP_200_OK)






@api_view(["POST", "GET"])
def Display_post(request):
    if request.method == "GET":
        qry = Post.objects.all()
        posts = Postserializer(qry, many=True)
        return Response(posts.data, status = status.HTTP_200_OK)
        return Response(posts.errors, status.HTTP_400_BAD_REQUEST)




@api_view(["POST","GET"])
def Login(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        user = User.objects.get(email = email)
        if (user.password == password):
            print(user.email, user.password)
            return Response({"message": "login successful"}, status = status.HTTP_200_OK)        
        return Response( {"message": "login login error "}, status=status.HTTP_400_BAD_REQUEST)
           




@api_view(["POST","GET"])
def Login2(request):
    if request.method == "POST":
        user =  Userserializer(data= { "email": request.data.get("email") , "password": request.data.get("password")})
        email = (user.initial_data["email"])
        password = (user.initial_data["password"])
        print(email, password)
        return Response({"message": "login successful"}, status = status.HTTP_200_OK)        
    return Response( {"message": "login login error "}, status=status.HTTP_400_BAD_REQUEST)           