from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .serializers import *
from rest_framework.decorators import api_view
from knox.models import AuthToken
from rest_framework import status
import numpy as np

\

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerialzer
    def post(self, request, *args, **kwargs):
        print(request.data['unique_ID'])
        if(request.data['unique_ID'] == 'UGA120'): # only allow some users to login 
            construct = {
              'username': request.data['username'],
              'email': request.data['email'],
              'password': request.data['password']
            }
            # print(construct)
            serializer = self.get_serializer(data=construct)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]
                })
        else:
            return Response({
                "error": "Please make sure you are authorized to register on HRMIS",
                "status": status.HTTP_400_BAD_REQUEST
                })

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        print(request.data['uniqueID'])
        if(request.data['uniqueID'] == 'UGAPOLICE001' or request.data['uniqueID'] == 'UGAPOLICE002'):
            print("logging in now")
            construct = {
              'username': request.data['username'],
              'password': request.data['password']
            }
            # print(construct)
            serializer = self.get_serializer(data=construct)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]
                })
        else:
            return Response({
                "error": "Please make sure you are authorized to log into the system",
                "status": 3000
                })

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        print(request.data['uniqueID'])
        if(request.data['uniqueID'] == 'UGAPOLICE001' or request.data['uniqueID'] == 'UGAPOLICE002'):
            print("changing password now")
            construct = {
              'old_password': request.data['old_password'],
              'new_password': request.data['new_password']
            }
            self.object = self.get_object()
            serializer = self.get_serializer(data=construct)
            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "error": "Please make sure you are provide a valid uniqueID to complete this task.",
                "status": 4000
                })



# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    # def get_object(self):
    #   return self.request.user
    def get(self, request):
        user = request.user
        # queryset = Status.objects.filter(user=user)
        serializer = UserSerializer(user, many=False)
        # print(get_status)
        return Response(serializer.data)

class AutoComplete(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get(self, request):
        serializer = UserSerializer(request.user, many=False)
        suggestions = ["wiring", "alignment", "electrics", "engines", "wheel_balancing", "flat_tyres", "computer_aided_mechanics"]
        return Response({
            "suggestions": suggestions
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer






# permission_classes = [permissions.IsAuthenticated, ]
    # def get_queryset(self):
    #   return  self.request.user.statuses.all() # using the related name "statuses" to query status of a user
    # def perform_create(self, serializer):
    #   query = self.request.user.statuses.all()
    #   if(len(query) == 0):
    #       serializer.save(user=self.request.user)
    #   else:
    #       raise serializers.ValidationError(
 #                    {'status': 'A status already exists'}
 #                )
        
    # def perform_update(self, serializer):
    #   serializer.save(user=self.request.user)