"""kcmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path
import kcmapp.views , account.views , payment.views
from kcmproject.settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , kcmapp.views.main , name = 'main'),
    path('write/', kcmapp.views.write , name = 'write'),
    path('read/', kcmapp.views.read , name = 'read'),
    path('detail/<str:id>', kcmapp.views.detail , name = 'detail'),
    path('edit/<str:id>', kcmapp.views.edit , name = 'edit'),
    path('delete/<str:id>', kcmapp.views.delete , name = 'delete'),
    path('signup/', account.views.signup, name='signup'), 
    path('login/', account.views.login, name='login'), 
    path('logout/', account.views.logout, name='logout'),
    path('update/', account.views.update, name='update'),
    path('people/<str:username>/', account.views.people, name='people'),
    path('password/', account.views.password, name='password'),
    path('profile/', account.views.profile_edit, name='profile_edit'),
    path('<int:cashbooks_id>/comments/write/', kcmapp.views.comment_write, name='comment_write'),
    path('<int:cashbooks_id>/comment/<int:comment_id>/update/', kcmapp.views.comment_update, name="comment_update"),
    path('<int:cashbooks_id>/comments/<int:comment_id>/delete/', kcmapp.views.comment_delete, name="comment_delete"),  
    path('hashtag/', kcmapp.views.hashtag, name = 'hashtag'),
    path('hashtag_list/', kcmapp.views.hashtag_list, name = 'hashtag_list'),
    path('hashtag_add/', kcmapp.views.hashtag_add, name = 'hashtag_add'),
    path('like/<str:id>/',kcmapp.views.likes,name = 'likes'),
    path('payment',payment.views.payment ,name = 'payment'),
    path('window',payment.views.window),
    path('success', payment.views.success),
    path('fail', payment.views.fail),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
