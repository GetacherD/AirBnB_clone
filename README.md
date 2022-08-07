"""        ___    ______  ____      _____    _ __     _   _____
          / _ \     | |  | (-) )   | |---)) | |\ \   | | | |---))
         / / \ \    | |  | (_) )   | |___)) | | \ \  | | | |___))
        / /___\ \   | |  | | \ \   | |---)) | |  \ \ | | | |---))
       /_/     \_\__|_|__|_|  \_\  |_|___)) | |   \_\|_| |_|___))
"""
AirBnBClone is a complete web application, integrating database storage, 
a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

Command intepreter
start ./console.py

#Usage
help -> to view helps available

help [topic] -> detail help/syntax for any command supported

create [ModelName] -> create new Object

all [ModelName]  -> list all objects
all   -> display all objects from any model
update [ModelName] [id] [attr] [val] add/update attribute
show [ModelName] [id] -> show detail of object given id

to see more type help


examples

	run console as ./console
	(hbnb)help

	Documented commands (type help <topic>):
	========================================
	EOF  all  create  destroy  help  quit  show  update

	(hbnb)create User
	39a8e8e0-f7c3-485c-a921-39f14453f5d2
	(hbnb)show User 39a8e8e0-f7c3-485c-a921-39f14453f5d2
	{'id': '39a8e8e0-f7c3-485c-a921-39f14453f5d2', 'created_at': d	       atetime.datetime(2022, 8, 7, 11, 29, 30, 725517), 'updated_at	          ': datetime.datetime(2022, 8, 7, 11, 29, 30, 725580), '__class         __': 'User'}
	(hbnb)create User
	ed77191f-1c49-47c6-a673-56d097b2414d
	(hbnb)all User
	["[User] (39a8e8e0-f7c3-485c-a921-39f14453f5d2) {'id': '39a8e8e0-f7c3-485c-a921-39f14453f5d2', 'created_at': datetime.datetime(2022, 8, 7,	  11, 29, 30, 725517), 'updated_at': datetime.datetime(2022, 8, 7, 11, 29, 30, 725580), '__class__': 'User'}", "[User] (ed77191f-1c49-47c6-a        673-56d097b2414d) {'id': 'ed77191f-1c49-47c6-a673-56d097b2414d', 'created_at': datetime.datetime(2022, 8, 7, 11, 31, 3, 624629), 'updated_        at': datetime.datetime(2022, 8, 7, 11, 31, 3, 624675), '__class__': 'User'}"]
	(hbnb)




   
