"""Marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup/commercant', views.signup_commercant, name='signupCommercant'),
    path('signup/client', views.signup_client, name='signupClient'),
	path('search/', views.search, name="search"),
	path('search/<str:keyword>/<int:page>', views.search, name="search"),
    path('panier/afficher/', views.afficher_panier, name="afficher_panier"),
    path('panier/ajout/<int:idproduit>', views.ajout_panier, name="ajout_panier"),
    path('panier/supprimer/<int:idproduit>', views.supprimer_panier, name="supprimer_panier"),
    path('panier/quantite/<int:idproduit>', views.quantite_panier, name="quantite_less_panier"),
    path('panier/reset/', views.reset_panier, name="reset_panier"),
	path('gestion/', include('app.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
