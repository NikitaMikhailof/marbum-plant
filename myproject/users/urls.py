from django.urls import path
from . import views 
from . import utils


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('show_posts/<slug:cat_slug>/', views.CategoryListView.as_view(), name='show_category'),
    path('show_tags/<slug:tag_slug>/', views.TagListView.as_view() , name='show_tag'),
    path('autocomplete/', utils.EquipmentAutocomplete.as_view(), name='equipment-autocomplete'),
    path('autocomplete_profile/', utils.ProfileAutocomplete.as_view(), name='profile-autocomplete'),
    path('search/', views.search_equipment, name='search_equipment'),
    path('search_journal/', views.search_journal, name='search_journal'),
    path('search_comment/', views.search_comment, name='search_comment'),
    path('search_profile/', views.search_profile, name='search_profile'),
    path('post/<slug:post_slug>/', views.ShowDetailEquipment.as_view(), name='equipment'),
    path('post/journal_equipment/<slug:equipment_slug>/', views.JournalRecordsEquipment.as_view(), name='journal_equipment'),
    path('post/comment_equipment/<slug:comment_slug>/', views.CommentRecordsEquipment.as_view(), name='comment_equipment'),
    path('journal/', views.JournalListView.as_view(), name='journal'),
    path('comment/', views.CommentListView.as_view(), name='comment'),
    path('schema_equipment/', views.SchemaEquipmentListView.as_view(), name='schema_equipment'),
    path('journal_record/', views.journal_record, name='journal_record'),
    path('comment_record/', views.comment_record, name='comment_record'),
    path('profile/', views.profile, name='profile'),
    path('profile_comments/<int:pk>', views.profile_comments, name='profile_comments'),
    path('profile_journals/<int:pk>', views.profile_journals, name='profile_journals'),
    path('profile_search_comments/', views.profile_search_comments, name='profile_search_comments'),
    path('profile_search_journal/', views.profile_search_journal, name='profile_search_journal'),
    path('detail_profile/<int:pk>/', views.detail_profile, name='detail_profile'),
    path('profile_messages_input/<int:pk>', views.profile_messages_input, name='profile_messages_input'),
    path('profile_messages_output/<int:pk>', views.profile_messages_output, name='profile_messages_output'),
    path('profile_message_output/', views.profile_message_output, name='profile_message_output'),
    path('profile_message_input/', views.profile_message_input, name='profile_message_input'),
    path('list_profiles/', views.ProfileListView.as_view(), name='list_profiles'),
    path('send_message/', views.send_message, name='send_message'),
] 