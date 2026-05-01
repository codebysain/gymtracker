from django.urls import path


from .views import workout_list, workout_create, workout_update, workout_delete, add_set, signup, edit_set, delete_set

urlpatterns = [
    path('', workout_list, name='workout_list'),
    path('create/', workout_create, name='workout_create'),
    path('update/<int:pk>/', workout_update, name='workout_update'),
    path('delete/<int:pk>/', workout_delete, name='workout_delete'),
    path('add-set/<int:workout_id>/', add_set, name='add_set'),
    path('signup/', signup, name='signup'),
    path('set/edit/<int:pk>/', edit_set, name='edit_set'),
    path('set/delete/<int:pk>/', delete_set, name='delete_set'),
]