from django.urls import path
from . import views

urlpatterns = [
    #* authentication
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.reg_user, name="registration"),

    path('', views.index_page, name="index"),
    path('delete/group/<int:pk>', views.delete_group, name="delete_group"),

    # open note in a new page
    path('notes/new', views.new_note, name="note_new"),
    path('notes/<str:pk>', views.note_page, name="note_page" ),
    path('notes/delete/<str:pk>', views.delete_note, name="note_delete" ),

    #* APIs list - GROUP
    # api pattern list 
    path('api/', views.api_overview, name="api"),
    # api - group list 
    path('api/groups/', views.api_groups, name="api-groups" ),
    # api - group - create
    path('api/groups/create/', views.api_create_group, name="api-groups-create" ),
    # api - group detail
    path('api/groups/<str:pk>/', views.api_group_by_id, name="api-groups-detail" ),
    #api - group's Notes list 
    path('api/groups/<str:pk>/notes/', views.api_group_notes, name="api-groups-notes"),
    # api - group - update
    path('api/groups/update/<str:pk>/', views.api_update_group, name="api-groups-update"),
    # api - group - delete 
    path('api/groups/delete/<str:pk>/', views.api_delete_group, name="api-group-delete"),
    
    #* APIs list - NOTE
    path('api/notes/', views.api_notes, name="api-notes"),
    path('api/notes/create/', views.api_create_notes, name="api-notes-create"),
    path('api/notes/<str:pk>/', views.api_notes_by_id, name="api-notes-detail"),
    path('api/notes/update/<str:pk>/', views.api_update_notes, name="api-notes-update"),
    path('api/notes/delete/<str:pk>/', views.api_delete_notes, name="api-notes-delete"),
]