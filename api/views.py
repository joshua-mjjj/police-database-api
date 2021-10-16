from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


@api_view(['POST', 'GET'])		
def UsersList(request):
		users = Client.objects.all().order_by('-id')
		serializer = User_Serializer(users, many=True)
		return Response(serializer.data)

    # def get_queryset(self):
    #     queryset = User.objects.filter(account_type='service_provider')
    #     query = self.request.query_params.get('q', None)
    #     print("query", query)
    #     if query is not None:
    #         providers = []
    #         for provider in queryset:
    #             services = [service.name.lower() for service in provider.services]
    #             print(services)
    #             for service in services:
    #                 if query.lower() in service:
    #                     providers.append(provider)
    #         queryset = providers
    #         print(provider)
    #     return queryset



	
	
	

	