from django.conf.urls import url
from django.contrib import admin


from .views import (
	index,
	addTodo,
	completeTodo,
	deleteCompleted,
	deleteAll,
	)

urlpatterns = [
	url(r'^$', index, name = 'index'),
	url(r'^add/$', addTodo, name = 'add' ),
	url(r'^complete/(?P<todo_id>\d+)/$', completeTodo, name = 'complete'),
	url(r'^deletecomplete/$', deleteCompleted, name = 'deletecomplete' ),
	url(r'^deleteall/$', deleteAll, name = 'deleteall' ),

]