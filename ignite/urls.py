from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home.urls")),

]#+static(settings.MEDIA_URL,settings.MEDIA_ROOT)