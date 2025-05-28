from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Stock
from ..serializers import StockSerializer
from django.db import DatabaseError
from rest_framework.serializers import ValidationError

class StockView(APIView):
    def get(self, request):
        try:
            stocks = Stock.objects.all()
            serializer = StockSerializer(stocks, many=True)

            return Response(serializer.data, status.HTTP_200_OK)
        
        except Stock.DoesNotExist as e:
            message = {"error": f"Data doesn't exist. {e}"}
            return Response(message, status.HTTP_404_NOT_FOUND)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    
    def post(self, request):
        try:
            data = request.data
            
            serializer = StockSerializer(data = data)
            if serializer.is_valid():
                serializer.save()

                return Response("Successfully created.", status.HTTP_201_CREATED)
            
            raise ValidationError(serializer.errors)
        
        except ValidationError as e:
            message = {"error": f"Invalid data. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        


class StockDetailsView(APIView):
    def put(self, request, pk):
        try:
            data = request.data
            stock = Stock.objects.get(id = pk)
            serializer = StockSerializer(stock, data = data)
            
            if serializer.is_valid():
                serializer.save()

                return Response("Successfully updated", status.HTTP_202_ACCEPTED)
            
            raise ValidationError(serializer.errors)

        except ValidationError as e:
            message = {"error": f"Invalid data. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except Stock.DoesNotExist as e:
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
            stock = Stock.objects.get(id = pk)
            stock.delete()

            return Response("Deleted stock", status.HTTP_200_OK)
        
        except Stock.DoesNotExist as e:
            message = {"error": f"Data doesn't exist. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR) 

        