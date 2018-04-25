"""colophon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from core.views.dashboard import DashboardView
from core.views.upload_design_document import UploadDesignDocumentView
from core.views.design_documents.design_document_detail import DesignDocumentDetailView
from core.views.design_documents.design_document_edit import DesignDocumentEditView
from core.views.design_documents.design_document_favorite import DesignDocumentFavoriteView
from core.views.profile.profile import ProfileView
from core.views.profile.profile_posts import ProfilePostsView
from core.views.s3.sign_s3 import SignS3View

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('upload/', UploadDesignDocumentView.as_view(), name='upload'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/posts/', ProfilePostsView.as_view(), name='profile_posts'),
    path(
        'document/<int:document_id>/',
        DesignDocumentDetailView.as_view(),
        name='design_document_detail'
    ),
    path(
        'document/<int:document_id>/edit/',
        DesignDocumentEditView.as_view(),
        name='design_document_edit'
    ),
    path(
        'document/<int:document_id>/favorite/',
        DesignDocumentFavoriteView.as_view(),
        name='design_document_favorite'
    ),
    path('sign_s3/', SignS3View.as_view()),
]
