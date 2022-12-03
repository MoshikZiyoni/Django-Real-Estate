from django.forms import ModelForm
from rest_framework.serializers import ModelSerializer
from property.models import Property,Project






class Propertyserializers(ModelSerializer):
    class Meta:
        model = Property
        fields='__all__'


    
class Projectserializers(ModelSerializer):
    class Meta:
        model = Project
        fields='__all__'