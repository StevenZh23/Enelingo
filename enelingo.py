from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ListProperty
from kivy.graphics import Color, Rectangle


KV = '''
ScreenManager:
    RegisterScreen:
        name: "register"

    MainScreen:
        name: "main"

    ProfileScreen:
        name: "profile"

    ProfileSettingsScreen:
        name: "profileSettings"

    BudgetTrackingPage:
        name: "budgetpage"

    UploadPage:
        name: "upload_page"

<BudgetTrackingPage>:
    name: "budget"
    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"

        MDTopAppBar:
            title: "Your Weekly Budget"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]

        MDLabel:
            text: "Your Weekly Budget"
            halign: "center"
            font_style: "H4"

        MDTextField:
            id: weekly_budget_input
            text: "40.00"
            hint_text: "Set your budget"
            size_hint_x: None
            width: "200dp"
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Save Budget"
            pos_hint: {"center_x": 0.5}
            on_release: app.save_budget(weekly_budget_input.text)

        BarGraph:
            data: [40, 30, 50, 20, 60, 70, 35]

<BarGraph>:
    size_hint: None, None
    size: self.parent.width, "200dp"
    pos_hint: {"center_x": 0.5}

<ProfileSettingsScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)

        Image:
            id: profile_pic
            source: "placeholder.png"
            size_hint: None, None
            size: dp(150), dp(150)
            pos_hint: {"center_x": 0.5}
            allow_stretch: True
            keep_ratio: True
            on_touch_down: app.open_file_manager_ps()

        MDTextField:
            id: first_name
            hint_text: "First Name"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8

        MDTextField:
            id: last_name
            hint_text: "Last Name"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8

        MDTextField:
            id: email
            hint_text: "Email"
            #input_type: "email"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8

        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8

        MDTextField:
            id: city
            hint_text: "City of Residence"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8

        MDRaisedButton:
            text: "Save and Go Back"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.5
            on_release: app.go_back_to_home()

<RegisterScreen>:
    BoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)

        MDTextField:
            id: first_name
            hint_text: "First Name"

        MDTextField:
            id: last_name
            hint_text: "Last Name"

        MDTextField:
            id: email
            hint_text: "Email"
            #input_type: "email"

        MDTextField:
            id: password
            hint_text: "Password"
            password: True

        MDTextField:
            id: city
            hint_text: "City of Residence"

        MDRaisedButton:
            text: "Next"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_to_profile()

<ProfileScreen>:
    BoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)

        Image:
            id: profile_pic
            source: "placeholder.png"
            size_hint: None, None
            size: dp(100), dp(100)
            pos_hint: {"center_x": 0.5}
            allow_stretch: True
            keep_ratio: True
            on_touch_down: app.open_file_manager()

        MDTextField:
            id: username
            hint_text: "Username"

        MDRaisedButton:
            text: "Go to Home"
            pos_hint: {"center_x": 0.5}
            on_release: app.go_to_home()

<UploadPage>:

    canvas.before:
        Color:
            rgba: 0, 0, 0, 1  # Black background
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        orientation: "vertical"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: "56dp"

            MDIconButton:
                icon: "arrow-left"
                bold: True
                theme_text_color: "Custom"
                text_color: [1, 1, 1, 1]  # White text
                on_release: app.go_home()

            MDLabel:
                text: "Upload Image of Device / Appliance"
                halign: "left"
                bold: True
                theme_text_color: "Custom"
                text_color: [1, 1, 1, 1]  # White text
                font_style: "H6"

        MDBoxLayout:
            orientation: "vertical"
            padding: dp(20)

            MDBoxLayout:
                size_hint: (None, None)
                size: dp(200), dp(200)
                pos_hint: {"center_x": 0.5}
                md_bg_color: app.theme_cls.primary_light
                radius: [dp(10)]
                canvas.before:
                    Color:
                        rgba: self.md_bg_color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: self.radius

                MDIconButton:
                    icon: "plus"
                    user_font_size: "100sp"
                    theme_text_color: "Hint"
                    pos_hint: {"center_y": 0.5}
                    on_release: app.open_file_manager()

            MDLabel:
                text: "Please upload images of high quality for best results"
                halign: "center"
                bold: True
                theme_text_color: "Custom"
                text_color: [1, 1, 1, 1]  # White text
                font_style: "Caption"

<MainScreen>:
    name: "main"
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1  # Black background
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: "10dp"  # Overall padding for the screen
        spacing: "5dp"  # Reduced spacing between widgets

        # Top Bar
        BoxLayout:
            size_hint_y: None
            height: "40dp"
            orientation: 'horizontal'

            MDLabel:
                text: f"${app.remaining_dollars:.2f}"
                font_style: "H6"
                halign: "left"
                valign: "center"
                theme_text_color: "Custom"
                text_color: [1, 1, 1, 1]  # White text

            ImageButton:
                id: imgbtn
                source: f"{app.image_path}"  # Replace with your image file path
                size_hint: None, None
                size: "40dp", "40dp"
                allow_stretch: True
                on_press: app.go_to_profile()

        MDLabel:
            text: "Hello"
            bold: True
            font_style: "H4"
            halign: "left"
            theme_text_color: "Custom"
            text_color: [1, 1, 1, 1]  # White text
            size_hint_y: None
            height: "40dp"  # Reduced height to reduce spacing
            padding: 0

        MDLabel:
            text: f"{app.full_name}"
            bold: True
            font_style: "H4"
            halign: "left"
            theme_text_color: "Custom"
            text_color: [1, 1, 1, 1]  # White text
            size_hint_y: None
            height: "40dp"  # Reduced height to reduce spacing
            padding: 0

        # Navigation Buttons
        BoxLayout:
            size_hint_y: None
            height: "40dp"  # Reduced height to reduce spacing
            spacing: "5dp"  # Reduced spacing between buttons

            MDRaisedButton:
                text: "Budget"
                on_release: root.switch_tab("budget")

            MDRaisedButton:
                text: "Challenges"
                on_release: root.switch_tab("challenges")

            MDRaisedButton:
                text: "Social"
                on_release: root.switch_tab("social")

        # Swipeable Main Sections
        ScreenManager:
            id: main_sections

            Screen:
                name: "budget"

                BoxLayout:
                    orientation: 'vertical'
                    padding: "10dp"
                    spacing: "10dp"

                    # Weekly Budget Widget
                    WeeklyBudgetCard:

                    # Swipeable Content Sections
                    BoxLayout:
                        size_hint_y: None
                        height: "40dp"
                        spacing: "10dp"

                        MDRaisedButton:
                            text: "My Devices"
                            on_release: root.switch_tab_manager("devices")

                        MDRaisedButton:
                            text: "My Appliances"
                            on_release: root.switch_tab_manager("appliances")

                        MDRaisedButton:
                            text: "Home Energy"
                            on_release: root.switch_tab_manager("energy")

                    ScreenManager:
                        id: tab_manager

                        Screen:
                            name: "devices"

                            BoxLayout:
                                orientation: 'vertical'

                                ScrollView:

                                    MDList:
                                        id: device_list
                                        spacing: "10dp"

                                MDRaisedButton:
                                    text: "+"
                                    on_release: app.go_to_upload()


                        Screen:
                            name: "appliances"

                            BoxLayout:
                                orientation: 'vertical'

                                ScrollView:

                                    MDList:
                                        id: appliance_list
                                        spacing: "10dp"

                                MDRaisedButton:
                                    text: "+"
                                    on_release: app.go_to_upload()

                        Screen:
                            name: "energy"

                            BoxLayout:
                                orientation: 'vertical'

                                ScrollView:

                                    MDList:
                                        id: home_energy_list
                                        spacing: "10dp"

                                MDRaisedButton:
                                    text: "+"
                                    on_release: app.go_to_upload()

            Screen:
                name: "challenges"
                ChallengeScreen:

            Screen:
                name: "social"
                SocialScreen:

<ChallengeScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: "10dp"
        spacing: "10dp"

        MDLabel:
            text: "Challenges Screen"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: [1, 1, 1, 1]  # White text

<SocialScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: "10dp"
        spacing: "10dp"

        MDLabel:
            text: "Social Screen"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: [1, 1, 1, 1]  # White text

<DeviceCard>:
    size_hint_y: None
    height: "50dp"
    MDCard:
        id: card
        orientation: "horizontal"
        padding: "10dp"
        spacing: "10dp"  # Add spacing between text and icon
        on_release: root.toggle_color()

        BoxLayout:
            orientation: "vertical"
            size_hint_x: 0.8  # Adjust the width of the text box
            spacing: "2dp"
            MDLabel:
                text: root.device_name
                font_style: "Subtitle1"
                halign: "left"
                valign: "center"
                theme_text_color: "Custom"
                text_color: [1, 1, 1, 1]  # White text

            MDLabel:
                text: f"{root.wattage}W/h"  # Example usage text
                font_style: "Caption"
                halign: "left"
                valign: "center"
                theme_text_color: "Custom"
                text_color: [0.8, 0.8, 0.8, 1]  # Light grey text

        MDIconButton:
            icon: "dots-vertical"
            size_hint: None, None
            size: "24dp", "24dp"  # Ensure small, consistent size
            pos_hint: {"center_y": 0.5}  # Center vertically
            theme_text_color: "Custom"
            text_color: [1, 1, 1, 1]  # White icon


<WeeklyBudgetCard>:
    size_hint_y: None
    height: "150dp"
    padding: "0dp"
    spacing: "10dp"
    orientation: "vertical"

    WidgetCard:
        size_hint: None, None
        size: "300dp", "140dp"  # Adjust size as needed
        pos_hint: {"center_x": 0.5}
        md_bg_color: [0.1, 0.1, 0.1, 1]  # Dark grey background
        radius: [15, 15, 15, 15]  # Circular edges (top-left, top-right, bottom-right, bottom-left)
        elevation: 0
        padding: "10dp"
        on_press: app.go_to_weekly_budget()

        MDBoxLayout:
            orientation: "vertical"
            spacing: "10dp"

            MDLabel:
                text: "Your Weekly Budget"
                font_style: "H6"
                halign: "left"
                theme_text_color: "Custom"
                text_color: [1, 1, 1, 1]  # White text

            MDLabel:
                text: "Set your weekly budget"
                font_style: "Caption"
                halign: "left"
                theme_text_color: "Custom"
                text_color: [0.8, 0.8, 0.8, 1]  # Light grey text

            MDBoxLayout:
                orientation: "vertical"
                spacing: "10dp"

                MDProgressBar:
                    value: app.budget_used_percentage
                    color: [0, 0.4, 1, 1]  # Blue progress bar

                MDLabel:
                    text: f"{app.budget_used_percentage}% of ${app.budget_dollars} used"
                    font_style: "Caption"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: [0.8, 0.8, 0.8, 1]  # Light grey text



'''

class ProfileScreen(Screen):
    pass
class ProfileSettingsScreen(Screen):
    pass
class RegisterScreen(Screen):
    pass

class UploadPage(Screen):
    pass

class MainScreen(Screen):


    def switch_tab(self, tab_name):
        self.ids.main_sections.current = tab_name

    def switch_tab_manager(self, tab_name):
        self.ids.tab_manager.current = tab_name

class ImageButton(ButtonBehavior, Image):
    pass

class WeeklyBudgetCard(BoxLayout):
    pass

class WidgetCard(MDCard, ButtonBehavior):
    pass

class ChallengeScreen(BoxLayout):
    pass

class SocialScreen(BoxLayout):
    pass

class DeviceCard(BoxLayout):
    device_name = StringProperty("Device")
    wattage = NumericProperty(0)
    is_active = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.card.md_bg_color = [0.1, 0.1, 0.1, 1]

    def toggle_color(self):
        if self.is_active:
            self.ids.card.md_bg_color = [0.1, 0.1, 0.1, 1]
        else:
            self.ids.card.md_bg_color = [0.1, 0.8, 0.1, 1]
        self.is_active = not self.is_active

Window.minimum_width = 400
Window.minimum_height = 700

class BudgetTrackingPage(Screen):
    pass
class BarGraph(RelativeLayout):
    data = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(data=self.update_graph)

    def update_graph(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0.2, 0.8, 1, 1)
            bar_width = self.width / (len(self.data) * 2)
            for idx, value in enumerate(self.data):
                bar_height = value / max(self.data) * self.height
                x = idx * (2 * bar_width) + bar_width / 2
                Rectangle(pos=(x, self.y), size=(bar_width, bar_height))

class UploadImageApp(MDApp):
    selected_file_path = None  # Class-level variable to store the selected file path

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        # File manager setup
        self.file_manager = MDFileManager(
            exit_manager=self.close_file_manager,
            select_path=self.select_file,
        )

        # Screen manager setup
        Builder.load_string(KV)
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(UploadPage(name="upload_page"))
        self.screen_manager.add_widget(MainScreen(name="hmain"))
        return self.screen_manager

    def file_manager_open(self):
        self.file_manager.show('/')  # You can set the default directory here.

    def close_file_manager(self, *args):
        self.file_manager.close()

    def select_file(self, path):
        self.selected_file_path = path  # Save the file path to the variable
        self.file_manager.close()
        print(f"File saved in variable: {self.selected_file_path}")

class MainApp(MDApp):


    full_name  = "George Burdell" #Set Name with this Variable

    image_path = "Images\profile_picture.jpg"

    budget_dollars = 40 #Set Budget

    used_dollars = 30.40 #Set used money

    remaining_dollars = budget_dollars - used_dollars #Set Remaining Money

    budget_used_percentage = (used_dollars / budget_dollars)*100 #Set Used Percentage



    def build(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_profile_pic,
        )
        self.file_manager_ps = MDFileManager(
            exit_manager=self.close_file_manager_ps,
            select_path=self.update_profile_picture,
        )
        return Builder.load_string(KV)

    def switch_to_profile(self):
        self.root.current = "profile"

    def go_to_home(self):
        self.root.get_screen("main").ids.imgbtn.source = MainApp.image_path
        self.root.current = "main"

    def go_to_profile(self):
        self.root.current = "profileSettings"
        self.root.get_screen("profileSettings").ids.profile_pic.source = MainApp.image_path


    def open_file_manager(self):
        self.file_manager.show('/')


    def select_profile_pic(self, path):
        self.root.get_screen("profile").ids.profile_pic.source = path
        MainApp.image_path = path
        self.root.get_screen("main").ids.imgbtn.source = path
        self.file_manager.close()

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def restart_app(self):
        self.root.current = "register"

    def on_start(self):
        self.populate_devices()
        self.populate_appliances()
        self.populate_home_energy()


    def populate_devices(self):
        devices = ["Desktop PC", "Laptop", "Smartphone", "Tablet"]
        wattages = [120, 200, 40, 60]
        for i in range(len(devices)):
            self.root.get_screen("main").ids.device_list.add_widget(DeviceCard(device_name=devices[i], wattage=wattages[i]))

    def populate_appliances(self):
        appliances = ["Desktop PC", "Laptop", "Smartphone", "Tablet"]
        wattages = [120, 200, 40, 60]
        for i in range(len(appliances)):
            self.root.get_screen("main").ids.appliance_list.add_widget(DeviceCard(device_name=appliances[i], wattage=wattages[i]))

    def populate_home_energy(self):
        home_energys = ["Desktop PC", "Laptop", "Smartphone", "Tablet"]
        wattages = [120, 200, 40, 60]
        for i in range(len(home_energys)):
            self.root.get_screen("main").ids.home_energy_list.add_widget(DeviceCard(device_name=home_energys[i], wattage=wattages[i]))


    def go_back_to_home(self):
        self.root.get_screen("main").ids.imgbtn.source = MainApp.image_path
        self.root.current = "main"

    def go_to_upload(self):
        self.root.current = "upload_page"

    def go_to_weekly_budget(self):
        self.root.current = "budgetpage"

    def open_device_page(self):
        print("Navigate to device-specific page.")

    def update_profile_picture(self, path):
        self.root.get_screen("profileSettings").ids.profile_pic.source = path
        MainApp.image_path = path
        self.file_manager_ps.close()

    def close_file_manager_ps(self, *args):
        self.file_manager_ps.close()

    def open_file_manager_ps(self):
        self.file_manager_ps.show('/')  # Start the file manager at the root directory

    def save_budget(self, new_budget):
        print(f"Budget set to: {new_budget}")

    def go_home(self):
        self.root.current = "main"


MainApp().run()

