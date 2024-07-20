from rest_framework import serializers
from .models import *
from users.models import *
from drf_extra_fields.fields import Base64ImageField
import base64
class CourseSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Course
        fields = '__all__'
    def update(self, instance, validated_data):
        if 'image' not in validated_data:
            validated_data['image'] = instance.image
        return super().update(instance, validated_data)
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if instance.image:
    #         with open(instance.image.path, "rb") as image_file:
    #             encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    #             representation['image'] = encoded_string
    #     return representation
    
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class SousCategorieAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousCategorie
        fields = '__all__'

class SousCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousCategorie
        fields = '__all__'

class SousCategoriegetSerializer(serializers.ModelSerializer):
    nom_categorie = CategorieSerializer(source='Id_c', read_only=True)

    class Meta:
        model = SousCategorie
        fields = ['id','Nomsouscategorie','nom_categorie']
    '''''
class SousCategoriewithnomSerializer(serializers.ModelSerializer):
    Id_c = serializers.SlugRelatedField(slug_field='Nomcategorie', queryset=Categorie.objects.all())

    class Meta:
        model = SousCategorie
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        nom_categorie = representation['Id_c']
        categorie = Categorie.objects.filter(Nomcategorie=nom_categorie).first()
        if categorie:
            representation['Id_c'] = categorie.id
        return representation
'''


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'




class UsersubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

class CategoriesubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'Nomcategorie']


class SubscribegetSerializer(serializers.ModelSerializer):
    user = UsersubscribeSerializer(source='Id_user', read_only=True)
    categorie = CategoriesubscribeSerializer(source='Id_c', read_only=True)

    class Meta:
        model = Subscribe
        fields = ['id','DateDebSession', 'Datesub', 'typeS', 'user', 'categorie', 'active']

class CoursegetSerializer(serializers.ModelSerializer):
    Souscategorie = SousCategorieAddSerializer(source='Id_sc', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'Nomc', 'Descriptionc', 'prix', 'image', 'Souscategorie','link']
        
    def update(self, instance, validated_data):
        if 'image' not in validated_data:
            validated_data['image'] = instance.image
        return super().update(instance, validated_data)