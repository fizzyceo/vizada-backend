from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView,ListAPIView
from rest_framework.permissions import *
from .signals import delete_image_file 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .utils import *
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import *
#pour categorie

class CategorieListCreateView(ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    #permission_classes=[IsAuthenticated]

class CategorieRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    #permission_classes=[IsAuthenticated]

#pour sous categorie
class SousCategorieListView(ListAPIView):
    queryset = SousCategorie.objects.all()
    serializer_class = SousCategoriegetSerializer
   # permission_classes=[IsAuthenticated]

class SousCategorieListCreateView(ListCreateAPIView):
    queryset = SousCategorie.objects.all()
    serializer_class = SousCategorieSerializer
   # permission_classes=[IsAuthenticated]

class SousCategorieRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = SousCategorie.objects.all()
    serializer_class = SousCategorieSerializer
  #  permission_classes=[IsAuthenticated]

#pour course
class CourseListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes=[IsAuthenticated]

class CourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def perform_destroy(self, instance):
        delete_image_file(sender=Course, instance=instance)
        instance.delete()    

class FavoriteListCreateView(ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes=[IsAuthenticated]

class FavoriteRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes=[IsAuthenticated]


class SubscribeListView(ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribegetSerializer
    #permission_classes=[IsAuthenticated]


class SubscribeListCreateView(ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        subscribe_instance = serializer.save()
        send_admin_email(subscribe_instance)

class SubscribeRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    #permission_classes=[IsAuthenticated]



class CoursesByCategory(APIView):
    def get(self, request, category_name):
        try:
            category = Categorie.objects.get(Nomcategorie=category_name)
            subcategories = SousCategorie.objects.filter(Id_c=category)
            courses = Course.objects.filter(Id_sc__in=subcategories)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Categorie.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)


class CoursesBySubCategory(APIView):
    def get(self, request, subcategory_name):
        try:
            subcategory = SousCategorie.objects.get(Nomsouscategorie=subcategory_name)
            courses = Course.objects.filter(Id_sc=subcategory)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SousCategorie.DoesNotExist:
            return Response({"error": "Subcategory not found"}, status=status.HTTP_404_NOT_FOUND)


class UserFavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        favorites = Favorite.objects.filter(Id_user=user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)
    
# class CourseListCreateView(ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer    
#     def create(self, request, *args, **kwargs):        
#         if isinstance(request.data, list):
#             serializer = self.get_serializer(data=request.data, many=True)        
#         else:
#             serializer = self.get_serializer(data=request.data)        
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursegetSerializer



# @api_view(["POST"])
# def base64_image_upload_api_view(request):
#     if request.method == "POST":
#         data = request.data
#         serializer = CourseSerializer(data=data)
#         if serializer.is_valid():
#             Course = serializer.save()
#             data = serializer.data
#             return Response(data=data)
#         return Response(serializer.errors, status=400)
    


# @csrf_exempt 
# def CourseApi(request, id=0): 
#     if request.method == 'GET': 
 
#         rendezvous_list = rendezvous.objects.filter(dateR__date=date_obj).order_by('dateR').reverse() 
#         serializer = rendezvousplusSerializer(rendezvous_list, many=True) 
#         return JsonResponse(serializer.data, safe=False) 
#     elif request.method == 'PUT': 
#         data = JSONParser().parse(request) 
#         rdv = rendezvous.objects.get(id=data['id']) 
#         serializer = rendezvousSerializer(rdv, data=data) 
#         if serializer.is_valid(): 
#             serializer.save() 
#             return JsonResponse("Updated Successfully", safe=False) 
#         return JsonResponse(serializer.errors,safe=False) 
#     elif request.method == 'DELETE': 
#         rdv = rendezvous.objects.get(id=id) 
#         rdv.delete() 
#         return JsonResponse("Deleted Successfully", safe=False)

# from django.utils import timezone  
# from django.shortcuts import get_object_or_404
# from datetime import timedelta
# @api_view(['GET'])
# def check_subscriptions(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     subscriptions = Subscribe.objects.filter(Id_user=user)
#     today = timezone.now().date()
    
#     for subscription in subscriptions:
#         if subscription.Datesub:
#             start_date = subscription.Datesub.date()
#             if subscription.typeS == 'monthly':
#                 end_date = start_date + timedelta(days=30)
#             elif subscription.typeS == 'yearly':
#                 end_date = start_date + timedelta(days=365)
            
#             if today > end_date:
#                 subscription.active = -1
#                 subscription.save()
    
#     active_subscriptions = subscriptions.filter(active=0)
#     serialized_data = SubscribeSerializer(active_subscriptions, many=True).data  
#     return Response(serialized_data)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Subscribe
from django.shortcuts import get_object_or_404
from datetime import timedelta
from .serializers import SubscribeSerializer  
from django.db.models import Q

@api_view(['GET'])
def check_subscriptions(request, user_id):
    user = get_object_or_404(User, id=user_id)
    subscriptions = Subscribe.objects.filter(Id_user=user)
    today = timezone.now()
    
    for subscription in subscriptions:
        if subscription.DateDebSession:
            start_date = subscription.DateDebSession
            if subscription.typeS == 'monthly':
                end_date = start_date + timedelta(days=30)
            elif subscription.typeS == 'yearly':
                end_date = start_date + timedelta(days=365)
            
            if today > end_date:
                subscription.active = -1
                subscription.save()
    
    active_subscriptions = subscriptions.filter(Q(active=0) | Q(active=1))
    serialized_data = SubscribeSerializer(active_subscriptions, many=True).data
    return Response(serialized_data)
