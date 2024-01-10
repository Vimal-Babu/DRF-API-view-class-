from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PersonSerializer

class PersonView(APIView):
    def get(self,request):
        objperson = Person.objects.all()
        serializer = PersonSerializer(objperson,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj,data = data,partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj,data = data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'person deleted'},status = status.HTTP_204_NO_CONTENT)