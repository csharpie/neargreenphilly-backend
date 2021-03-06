from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_swagger_view(title='NearGreen API')

urlpatterns = [
    url(r'^analytics/locations_aggregation/$', views.AnalyticsLocationSummary.as_view()),
    url(r'^analytics/locations_categories_aggregation/$',
        views.AnalyticsLocationSummaryCategory.as_view()),
    url(r'^authorization/retrieve_token/', obtain_jwt_token),
    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),
    url(r'^locations/community_gardens/$',
        views.CommunityGardenLocationList.as_view()),
    url(r'^locations/food_pantries/$', views.FoodPantryLocationList.as_view()),
    url(r'^locations/grocery_stores/$', views.GroceryStoreLocationList.as_view()),
    url(r'^locations/super_markets/$', views.SuperMarketLocationList.as_view()),
    url(r'^hours/$', views.HourList.as_view()),
    url(r'^hours/(?P<pk>[0-9]+)/$', views.HourDetail.as_view()),
    url(r'^nearby_locations/?$', views.NearbyLocationList.as_view()),
    url(r'^$', schema_view)
]


urlpatterns = format_suffix_patterns(urlpatterns)
