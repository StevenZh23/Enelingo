from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.uix.card import MDCard

KV = '''
ScreenManager:
    MainScreen:

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
                            ScrollView:
                                MDList:
                                    id: device_list
                                    spacing: "10dp"


                        Screen:
                            name: "appliances"
                            ScrollView:
                                MDList:
                                    id: appliance_list
                                    spacing: "10dp"

                        Screen:
                            name: "energy"
                            ScrollView:
                                MDList:
                                    id: home_energy_list
                                    spacing: "10dp"

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

class MainApp(MDApp):

    full_name  = "George Burdell" #Set Name with this Variable

    image_path = "Images\profile_picture.jpg"

    budget_dollars = 40 #Set Budget

    used_dollars = 30.40 #Set used money

    remaining_dollars = budget_dollars - used_dollars #Set Remaining Money

    budget_used_percentage = (used_dollars / budget_dollars)*100 #Set Used Percentage



    def build(self):
        return Builder.load_string(KV)

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
    
    def go_to_profile(self):
        print("go to profile")

    def go_to_weekly_budget(self):
        print("go to weekly budget") 
    
    def open_device_page(self):
        print("Navigate to device-specific page.")

MainApp().run()

