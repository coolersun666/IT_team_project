from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from manicurer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'manicurer/', include('manicurer.urls', namespace='manicurer')),

                  # above maps any URLs starting
                  # with rango/ to be handled by
                  # the rango application
                  url(r'^admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
