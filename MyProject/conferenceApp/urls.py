from django.urls import path
from .views import conferenceList, ConferenceListView, ConferenceDetailsView
urlpatterns = [
    path('list/', conferenceList, name="conference_list"),
    path('listView/', ConferenceListView.as_view(), name="conference_listView"),
    path('detailsView/<int:pk>', ConferenceDetailsView.as_view(), name="conference_detailsView"),
]