
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.graphics.texture import Texture
from kivy.graphics import *
from kivy.utils import platform
from jnius import autoclass, cast


class initialscreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def start_service(self, nm):
        from android import mActivity
        #print('Service started____ ', nm)
        context =  mActivity.getApplicationContext()

        SERVICE_NAME = str(context.getPackageName()) + '.Service' + nm

        self.service_target = autoclass(SERVICE_NAME)

        self.service_target.start(mActivity,'icon', 'logger', 'Connecting', '')

        return self.service_target
     

    def stop_service(self, nm):
        from android import mActivity
        context = mActivity.getApplicationContext()


        SERVICE_NAME = str(context.getPackageName()) + '.Service' + nm

        Service = autoclass(SERVICE_NAME)

        Intent = autoclass('android.content.Intent')
        service_intent = Intent(mActivity, Service)


        mActivity.stopService(service_intent)

class theapp(App):
    def build(self):
        self.screenm = ScreenManager(transition=FadeTransition())

        self.initialscreen = initialscreen()
        screen = Screen(name = 'initialscreen')
        screen.add_widget(self.initialscreen)
        self.screenm.add_widget(screen)
        self.get_permit()
        return self.screenm





    def get_permit(self):
        if platform == 'android':
            from android.permissions import Permission, request_permissions 

            def callback(permissions, results):
                granted_permissions = [perm for perm, res in zip(permissions, results) if res]
                denied_permissions = [perm for perm, res in zip(permissions, results) if not res]

                if denied_permissions:
                    print('Denied permissions:', denied_permissions)

                elif granted_permissions:
                    print('Got all permissions')
                else:
                    print('No permissions were granted or denied')

            requested_permissions = [
                Permission.INTERNET,
                Permission.FOREGROUND_SERVICE,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.SYSTEM_ALERT_WINDOW
            ]
            request_permissions(requested_permissions, callback)



if __name__ == "__main__":
    theapp().run()