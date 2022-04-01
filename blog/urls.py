from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('core.urls')),
    path('profile/', user_views.profile, name='profile' ),
    path('register/', user_views.register, name='register' ),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name='login' ),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    
    # API urls 
    
    path('posts/', include('postApi.urls')),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)