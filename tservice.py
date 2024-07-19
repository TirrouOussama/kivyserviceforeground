import kivy
from kivy.app import App
from jnius import autoclass, cast
import time

from kvdroid.tools import launch_app

from kvdroid.tools.package import all_main_activities
from kvdroid.tools.package import package_info
from kvdroid.tools import launch_app_activity




cnt = 0
while True:
	time.sleep(1)
	print('service is running', cnt)
	cnt += 1

	###### this block is start app from background
	
	if cnt == 20:
		print('resuming app')
		launch_app("org.testapppck.testapp")

