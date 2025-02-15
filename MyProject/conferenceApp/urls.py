from django.urls import path
from .views import conferenceList, ConferenceListView, ConferenceDetailsView, ConferenceCreateView, ConferenceUpdateView, ConferenceDeleteView
urlpatterns = [
    path('list/', conferenceList, name="conference_list"),
    path('listView/', ConferenceListView.as_view(), name="conference_listView"),
    path('detailsView/<int:pk>', ConferenceDetailsView.as_view(), name="conference_detailsView"),
    path('create/', ConferenceCreateView.as_view(), name="conference_createView"),
    path('update/<int:pk>', ConferenceUpdateView.as_view(), name="conference_updateView"),
    path('delete/<int:pk>', ConferenceDeleteView.as_view(), name="conference_deleteView"),
]