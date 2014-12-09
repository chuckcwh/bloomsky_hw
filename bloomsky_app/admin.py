from django.contrib import admin
from bloomsky_app.models import Q1_weatherInfo, Q2_timestamp, Q3_table2, Q3_table1

admin.site.register(Q1_weatherInfo)
admin.site.register(Q2_timestamp)
admin.site.register(Q3_table1)
admin.site.register(Q3_table2)