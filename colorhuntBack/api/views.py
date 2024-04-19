from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView

from api.models import Palette
from api.serializers import PaletteSerializer
# Create your views here.

class PalettesList(APIView):
    def get(self, request):
        return Response(PaletteSerializer(Palette.objects.all(), many=True).data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = PaletteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class PaletteDetail(APIView):
    def get_object(self, id):
        try:
            return Palette.objects.get(id=id)
        except Palette.DoesNotExist:
            return None
    
    def get(self, r, id):
        palette = self.get_object(id)
        if palette == None:
            return Response(status=HTTP_404_NOT_FOUND)
        return Response(PaletteSerializer(palette).data)
    
    def put(self, r, id):
        palette = self.get_object(id)
        if palette == None:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = PaletteSerializer(palette, data=r.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, r, id):
        palette = self.get_object(id)
        if palette == None:
            return Response(status=HTTP_404_NOT_FOUND)
        palette.delete()
        return Response(status=HTTP_204_NO_CONTENT)
        