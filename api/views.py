from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User,Label
from .serializers import UserSerializer, LabelSerializer

@api_view(['GET'])
def getData(request):
    # person = {'name':'dennis', 'age':66888}
    print(request, '!!!!!dsads!!')
    return Response(" root route working !!!!!!")


@api_view(['GET'])
def allUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def clear(request):
    User.objects.all().delete()
    Label.objects.all().delete()
    return Response("all deleted")

@api_view(['GET'])
def allLabels(request):
    labels = Label.objects.all()
    serializer = LabelSerializer(labels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addLabel(request):
    serializer = LabelSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def delLabels(request):
    idxToDel = list(request.data)[0]
    # username = list(request.data)[0]
    labels = Label.objects.filter(id = idxToDel ).delete()
    # for lb in labels:
    #     print(lb.name, lb.user)
    # serializer = LabelSerializer(labels, many=True)
    return Response(idxToDel)

@api_view(['POST'])
def EditLabels(request):
    idToEdit = request.data['id']
    newName = request.data['name']
    print(idToEdit, newName)
    labels = Label.objects.filter(pk = idToEdit).update(name=newName)
    # print(labels)
    # for lb in labels:
    #     print(lb.name, lb.user)
    # serializer = LabelSerializer(labels, many=True)
    return Response(request.data['name'])

@api_view(['POST'])
def myLabels(request):
    print(list(request.data)[0])
    username = list(request.data)[0]
    labels = Label.objects.filter(user = username )
    # for lb in labels:
    #     print(lb.name, lb.user)
    serializer = LabelSerializer(labels, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def addUser(request):
    users = User.objects.all()
    for u in users:
        if u.email == request.data['email']:
            print('!!!!!!exist!!!!!!')
            return Response( f"Hi {u.name}, You hava an account! please sign in!" )
    serializer = UserSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    print(request.data)
    msg = "email is incorrect"
    users = User.objects.al()
    for u in users:
        if u.email == request.data['email']:
            msg = "password is incorrect"
            if u.password == request.data['password']:
                msg = "login successful !"

    return Response(msg)