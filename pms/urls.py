from django.conf.urls import url,include
from django.contrib import admin
 
from . import view
from . import search
 
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^account/', include('TestModel.urls')),
]
