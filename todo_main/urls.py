from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # التطبيق الرئيسي (المهام)
    path('', include('todo.urls')),

    # تسجيل الدخول والخروج باستخدام قوالب مخصصة
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # تضمين باقي صفحات المصادقة الجاهزة (مثل تغيير كلمة المرور)
    path('accounts/', include('django.contrib.auth.urls')),
]

# دعم تحميل الملفات أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
