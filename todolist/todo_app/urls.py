
from django.urls import path,include
from todo_app import views
urlpatterns = [
    path('',views.listalltodos,name='listalltodos'),
    path('listalltodos',views.listalltodos,name='listalltodos'),
    path('addtodo',views.addtodo,name='addtodo'),
    path('edittodo/<int:id>',views.edittodo,name='edittodo'),
    path('deletetodo/<int:id>',views.deletetodo,name='deletetodo'),
    
]
