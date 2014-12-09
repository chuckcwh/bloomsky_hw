from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'bloomsky_app.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),

    # ajax call
    #Question 1
    url(r'^weather_data/POST/$', 'bloomsky_app.views.post_weather_data', name='post_weather_data'),
    url(r'^weather_data/GET/$', 'bloomsky_app.views.get_weather_data', name='get_weather_data'),

    #Question 2
    url(r'^timestamp/POST/$', 'bloomsky_app.views.post_timestamp', name='post_timestamp'),

    #Question 3
    url(r'^time_compare/POST/$', 'bloomsky_app.views.post_time_compare', name='post_time_compare'),
    url(r'^acquire_id/GET/$', 'bloomsky_app.views.get_acquire_id', name='get_acquire_id'),

)
