# .. Imports
from rest_framework_nested import routers

from authentication.views import AccountViewSet

import django
from django.conf.urls import include, patterns, url

from views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
     '',
    # ... URLs
    url(r'^api/v1/', include(router.urls)),

    url('^.*$', IndexView.as_view(), name='index'),
)