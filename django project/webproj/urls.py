from django.contrib import admin
from django.urls import path
from sangsi.views import main1
from junggi.views import junggi_list, junggi_detail
from detail.views import detail


urlpatterns = [
    path('admin/', admin.site.urls),  # 127.0.0.1/admin/

    path('상시오디션목록/', main1),  # 127.0.0.1/상시오디션목록/
    path('정기오디션목록/', junggi_list, name='junggi_list'),  # 127.0.0.1/정기오디션목록/
    path('상시오디션상세정보/', detail),  # 127.0.0.1/상시오디션상세정보/
    path('정기오디션상세정보/<int:pk>/', junggi_detail, name='junggi_detail'),  # 127.0.0.1/정기오디션상세정보/
]
