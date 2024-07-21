from django.urls import path
from .views  import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
       #categorie
    path('api/categorie/', CategorieListCreateView.as_view(), name='Categorie-list-create'),
    path('api/categorie/<int:pk>/', CategorieRetrieveUpdateDeleteView.as_view(), name='Categorie-retrieve-update-delete'),
    #sous categorie
    path('api/souscategorie/', SousCategorieListCreateView.as_view(), name='SousCategorie-list-create'),
    path('api/souscategorie/<int:pk>/', SousCategorieRetrieveUpdateDeleteView.as_view(), name='SousCategorie-retrieve-update-delete'), 
    path('api/souscategoriedetail/', SousCategorieListView.as_view(), name='SousCategorie-list'),
    #courses

    path('api/course/', CourseListCreateView.as_view(), name='course-list-create'),
    path('api/course/<int:pk>/', CourseRetrieveUpdateDeleteView.as_view(), name='course-retrieve-update-delete'),
    path('api/course/category/<str:category_name>/', views.CoursesByCategory.as_view(), name='courses-by-category'),
    path('api/course/souscategory/<str:subcategory_name>/', views.CoursesBySubCategory.as_view(), name='courses-by-subcategory'),
    path('api/coursedetail/', CourseListView.as_view(), name='course-list'),
    path('api/courses/', CourseListView.as_view(), name='course-list'),
    #favorite
    path('api/favorite/', FavoriteListCreateView.as_view(), name='favorite-list-create'),
    path('api/favorite/<int:pk>/', FavoriteRetrieveUpdateDeleteView.as_view(), name='favorite-retrieve-update-delete'),    
    path('api/favoritesbyuser/', UserFavoritesView.as_view(), name='user-favorites'),
    
    #subscribe
    
    path('api/subscribe/', SubscribeListCreateView.as_view(), name='subscribe-list-create'),
    path('api/subscribe/<int:pk>/', SubscribeRetrieveUpdateDeleteView.as_view(), name='subscribe-retrieve-update-delete'), 
    path('api/subscribedetails/', SubscribeListView.as_view(), name='subscribe-list'),
    path('api/check_subscription/<int:user_id>/', check_subscriptions, name='check_subscriptions'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)