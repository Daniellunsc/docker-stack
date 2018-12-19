new_service=""

launch: 
	. ../env/bin/activate; python services/users/user.py & 
	. ../env/bin/activate; python services/todo/todo.py &
	# . ../env/bin/activate; python app.py

create_service:
	. ../env/bin/activate; cd services && mkdir $(new_service) && cd $(new_service) 
	. ../env/bin/activate; cd services/$(new_service) && mkdir models
	. ../env/bin/activate; cd services/$(new_service) && touch $(new_service).py

shutdown:
	. ../env/bin/activate; ps -ef | grep "services/users/user.py" | grep -v grep | awk '{print $$2}' | xargs kill 
	. ../env/bin/activate; ps -ef | grep "services/todo/todo.py" | grep -v grep | awk '{print $$2}' | xargs kill   
	. ../env/bin/activate; ps -ef | grep "app.py" | grep -v grep | awk '{print $$2}' | xargs kill  