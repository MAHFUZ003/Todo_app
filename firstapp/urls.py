from django.urls import path
from firstapp.views import home,add,show,Delete,edit,Complete,ccomplete
# Create your views here.
urlpatterns = [
   path('',home,name = 'homepage' ),
   path('addtask/',add,name = 'addtask' ),
   path('showtask/',show,name = 'showtask' ),
   path('delete/<int:id>',Delete,name = 'delete' ),
   path('edit/<int:id>',edit,name = 'edit' ),
   path('Complete/<int:id>',Complete ,name = 'Complete' ),
   path('ccomplete/',ccomplete ,name = 'ccomplete' ),
]
