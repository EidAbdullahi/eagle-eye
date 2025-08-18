from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('project/', views.project, name="project"),
    path('team/', views.team, name="team"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),

    # ✅ Webmail redirect → goes to cPanel login port (no loop)
    path("webmail/", RedirectView.as_view(
        url=settings.WEBMAIL_URL,
        permanent=False
    ), name="webmail_redirect"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.ABOUT_IMAGES_URL, document_root=settings.ABOUT_IMAGES_ROOT)
