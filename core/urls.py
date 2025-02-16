from django.contrib import admin
from django.urls import path, include
from .views import home, save, edit, update, delete, update_page

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota padrão para a página inicial
    path('', home, name='home'),

    # Rotas do CRUD
    path('save/', save, name="save"),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),

    # Django-Allauth (Login com Google)
    path('accounts/', include('allauth.urls')),

    # Rota para a página de redirecionamento pós-login
    path('update/', update_page, name='update'),
]
