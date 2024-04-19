from rest_framework import serializers

from api.models import Palette


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = '__all__'
        
        def create(self, data):
            return Palette.objects.create(**data)
        
        def update(self, instance, data):
            instance.likes = data.get('likes', instance.likes)
            instance.color1 = data.get('color1', instance.color1)
            instance.color2 = data.get('color2', instance.color2)
            instance.color3 = data.get('color3', instance.color3)
            instance.color4 = data.get('color4', instance.color4)
            instance.save()
            return instance
        
        