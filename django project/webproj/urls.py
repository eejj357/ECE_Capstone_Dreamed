"""
URL configuration for webproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mainpage.views import main1
from mainpage2.views import main2
from detail.views import detail
from detail2.views import detail2


urlpatterns = [
    path('', main1),  # 127.0.0.1/
    path('main2/', main2),  # 127.0.0.1/main2/
    path('admin/', admin.site.urls),  # 127.0.0.1/admin/
    path('상시오디션정보/', detail),  # 127.0.0.1/상시오디션정보/
    path('정기오디션정보/', detail2),  # 127.0.0.1/정기오디션정보/
    # path('submit_year/', main1, name='submit_year'),
]
