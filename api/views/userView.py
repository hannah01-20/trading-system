from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ..serializers import UserSerializer, UserCreationSerializer
from django.db import DatabaseError
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..custom import IsUnAuthenticated
import json

class UserView(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsUnAuthenticated()]
        
        return [IsAuthenticated()]

    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)

            return Response(serializer.data, status.HTTP_200_OK)
        
        except DatabaseError as e:
            message = {"error": "Database error occurred."}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": "Something went wrong."}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def post(self, request):
        try:
            data = request.data

            print(data)
            
            serializer = UserCreationSerializer()
            validated_data = serializer.validate(data)
            serializer.create(validated_data)

            return Response("Successfully created.", status.HTTP_201_CREATED)
        
        except ValidationError as e:
            message = {"error": f"Invalid data. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            print(e)
            message = {"error": "Something went wrong."}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserDetailsView(APIView): 
    def get(self, request, pk):
        try:
            user = User.objects.get(id = pk)
            serializer = UserSerializer(user)

            return Response(serializer.data, status.HTTP_200_OK)
    
        except User.DoesNotExist as e:
            message = {"error": f"Invalid data. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": "Something went wrong."}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, pk):
        try:
            data = request.data
            user = User.objects.get(id = pk)
            serializer = UserSerializer(user, data = data)
            
            if serializer.is_valid():
                serializer.save()

                return Response("Successfully updated", status.HTTP_202_ACCEPTED)
            
            raise ValidationError(serializer.errors)

        except ValidationError as e:
            message = {"error": f"Invalid data. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist as e:
            message = {"error": f"Data doesn't exist. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)  
        
    def delete(self, request, pk):
        try:
            stock = User.objects.get(id = pk)
            stock.delete()

            return Response("Deleted user", status.HTTP_200_OK)
        
        except User.DoesNotExist as e:
            message = {"error": f"Data doesn't exist. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR) 