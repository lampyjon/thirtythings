from django.urls import path, include

from django.contrib import admin


admin.autodiscover()

import mainapp.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", mainapp.views.index, name="index"),
    path("add/", mainapp.views.add_food, name="add"),
    path("delete/<int:food_id>/", mainapp.views.delete_food, name="delete"),
    path("eat/<int:food_id>/<int:period_id>/", mainapp.views.eat_food, name="eat"),
    path("uneat/<int:food_id>/<int:period_id>/", mainapp.views.uneat_food, name="uneat"),
    path("view/<int:period_id>/", mainapp.views.index, name="period"),

    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
]
