from django.urls import path

from apps.sofascore.views import (
    SofascoreEventView,
    SofascoreScheduleView,
    SofascoreTeamView,
)

app_name = "sofascore"

urlpatterns = [
    path("event/<str:event_id>/", SofascoreEventView.as_view(), name="event-detail"),
    path("team/<str:team_id>/", SofascoreTeamView.as_view(), name="team-detail"),
    path("schedule/<str:sport>/<str:date>/", SofascoreScheduleView.as_view(), name="schedule-detail"),
]
