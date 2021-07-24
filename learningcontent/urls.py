from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from learningcontent import views

urlpatterns = [
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^subject/$', views.SubjectList.as_view()),
    url(r'^category/subject/(?P<pk>[0-9]+)/$', views.SubjectCategoryList.as_view()),
    url(r'^subject/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()),
    url(r'^content/$', views.ContentList.as_view()),
    url(r'^subject/content/(?P<pk>[0-9]+)/$', views.ContentSubjectList.as_view()),
    url(r'^content/(?P<pk>[0-9]+)/$', views.ContentDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)