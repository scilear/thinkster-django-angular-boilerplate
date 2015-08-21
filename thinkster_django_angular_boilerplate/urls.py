# .. Imports
from rest_framework_nested import routers

from authentication.views import AccountViewSet

import django

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = django.conf.urls.patterns(
     '',
    # ... URLs
    url(r'^api/v1/', include(router.urls)),

    url('^.*$', IndexView.as_view(), name='index'),
)