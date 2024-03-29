from django.urls import path, include

from . import views
from .views import LoginView

urlpatterns = [
    path('account/login/', LoginView.as_view(), name='login'),
    path('account/register/', views.register, name='register'),
    path('account/updated/', views.updated, name='updated'),
    path('account/profile/<int:pk>/', views.AccountUpdateView.as_view(), name='profile'),

    path('account/', include('django.contrib.auth.urls')),

    path('account/', views.SimulatorListView.as_view(), name='dashboard'),
    path('account/simulator/create/', views.SimulatorCreateView.as_view(), name='create'),
    path('account/simulator/<int:pk>/update/', views.SimulatorUpdateView.as_view(), name='update'),
    path('account/simulator/<int:pk>/delete/', views.SimulatorDeleteView.as_view(), name='delete'),
    path('account/simulator/<int:pk>/update_token/', views.update_token, name='change_token'),

    path('simulator/explore/', views.ExploreSimulatorListView.as_view(), name='explore'),
    path('simulator/explore/<slug:tag>/', views.ExploreSimulatorListView.as_view(), name='explore_tag'),
    path('simulator/published/<slug:token>/', views.access_simulator, name='simulator'),
    path('simulator/published/<slug:token>/<int:pk>/details/', views.ExploreSimulatorUpdateView.as_view(),
         name='details')
]
