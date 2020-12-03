from django.urls import path, include
from user import urls as userurls
from branch import urls as branchurls
from subject import urls as subjecturls
from document import urls as documenturls

from restapi import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/', include(userurls)),
    path('branch/', include(branchurls)),
    path('subject/', include(subjecturls)),
    path('document/', include(documenturls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
