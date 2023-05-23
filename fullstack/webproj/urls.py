from django.contrib import admin
from django.urls import path
from sangsi.views import sangsi_list, sangsi_detail, filtered_sangsi_list
from jeonggi.views import jeonggi_list, jeonggi_detail, filtered_jeonggi_list


urlpatterns = [
    path('admin/', admin.site.urls),  # 127.0.0.1/admin/

    path('상시오디션목록/', sangsi_list, name='sangsi_list'),  # 127.0.0.1/상시오디션목록/

    path('정기오디션목록/', jeonggi_list, name='jeonggi_list'),  # 127.0.0.1/정기오디션목록/
    path('정기오디션상세정보/<int:pk>/', jeonggi_detail, name='jeonggi_detail'),  # 127.0.0.1/정기오디션상세정보/

    path('filtered_sangsi_list/', filtered_sangsi_list, name='filtered_sangsi_list'),
    path('filtered_jeonggi_list/', filtered_jeonggi_list, name='filtered_jeonggi_list'),
]