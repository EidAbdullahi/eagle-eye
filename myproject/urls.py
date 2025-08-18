from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect   # 👈 added

# redirect view for /webmail
def webmail_redirect(request):
    # redirect users to the actual cPanel webmail login
    return redirect("https://www.eagleyesecurityservice.com:2096")

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
    path('webmail/', webmail_redirect, name='webmail'),  # 👈 added
]

# Only serve local media/static during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.ABOUT_IMAGES_URL, document_root=settings.ABOUT_IMAGES_ROOT)
