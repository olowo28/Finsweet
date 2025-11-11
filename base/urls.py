from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name="index"),
   path('aboutus/', views.aboutus, name="aboutus"),
   path('authors/', views.authors, name="author"),
   path('blog/', views.blog, name="blog"),
   path('blogpost/', views.blogpost, name="blogpost"),
   path('category/', views.category, name="category"),
   path('privacy/', views.privacy, name="privacy" ),
   path('contact/', views.contactroom, name="contact"),
   path('subscribe/', views.subscriberoom, name="subscribe")
]

