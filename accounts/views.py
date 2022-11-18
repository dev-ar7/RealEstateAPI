import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model, login, logout
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .models import User
from .serializer import UserSerializer


@csrf_exempt
def signIN(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if  not re.match('^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', username):
            return JsonResponse({'Error': 'Please enter a valid password!'})
        if len(password) > 6 :
            return JsonResponse({'Error': 'Passwords must be atleast SIX characters long!'})

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(username = username)
            if user.check_password(password):
                get_user = UserModel.objects.filter(username = username).values().first()
                get_user.pop('password')
                user.save()
                login(request, user)
            else:
                return JsonResponse({'Error': 'Invalid Password'})
        except:
            return JsonResponse({'Error': 'Invalid Email'})
    return JsonResponse({'Error': 'Method not allowed'})


@csrf_exempt
def signOUT(request, id):

    logout(request)
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk = id)
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'Error': 'Invalid user'})
    return JsonResponse({'Error': 'Successfully logged out'})


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    def get_permissions(self):
        
        permission_class = []
        if self.action == 'create' :
            permission_class = [AllowAny]
        elif self.action == 'reterive' or self.action == 'update' or self.action == 'destroy':
            permission_class = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_class = [IsAdminUser]

        return [permission() for permission in permission_class]