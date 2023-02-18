from rest_framework.response import Response
from rest_framework import status
from .models import Hopitals
from .serializers import hospitalsSerializers
from rest_framework.views import APIView

class touslesHopital(APIView):

    def get(self,request):
        hospitals = Hopitals.objects.all()
        serial = hospitalsSerializers(hospitals, many=True)
        return Response(serial.data)

    def post(self,request):
        serializer=hospitalsSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)