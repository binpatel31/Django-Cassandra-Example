from rest_framework import serializers
from .models import orm


class ormSerializer(serializers.Serializer):
    '''
    #use this when using serializers.ModelSerializer 
    class Meta:
        model = ormModel
        fields = ['ormID','first_name','last_name']

    '''  
    #IF WE HAVE USED SERIALIZER THEN CODE BELOW IS USED
    ###now here specify all fields that you specified in your class
    ormID = serializers.UUIDField() 
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    ### create and update method 
    def create(self, validated_data):
        return orm.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ormID = validated_data.get('ormID', instance.ormID)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
#    '''
