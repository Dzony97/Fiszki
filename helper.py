screen_helper = """

#:import NoTransition kivy.uix.screenmanager.NoTransition


ScreenManager:
    WelcomeScreen:
    LoginScreen:
    Registration:
    MainScreen:
    SettingsScreen:

<WelcomeScreen>:
    name: 'welcome'
    MDLabel:
        text: 'FISZKI'
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": .8}
        font_style: 'H2'
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
    MDFloatingActionButton:
        icon: "play"
        pos_hint: {"center_x": .5, "center_y": 0.2}
        on_press: root.manager.current = 'login'

<LoginScreen>:
    name: 'login'
    Screen:
        MDLabel :
            text : 'LOGIN'
            font_size: '48dp'
            halign: 'center'
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            pos_hint: {"center_y": 0.83}
        MDTextField:
            hint_text: 'Username'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {"center_x": 0.5, "center_y": 0.65}
            icon_right : "account"
            on_text: self.text = self.text.replace(" ", "")
            write_tab: False
        MDTextField:
            id: psswd
            hint_text: 'Password'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            icon_right : "eye-off"
            password: True
            on_text: self.text = self.text.replace(" ", "")
            write_tab: False
        BoxLayout:
            size_hint: 0.85, None
            height: "30dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            spacing: "5dp"
            MDCheckbox:
                id: cb
                size_hint: None, None
                width: "30dp"
                height: "30dp"
                on_press:
                    psswd.password = False if psswd.password == True else True
                    psswd.icon_right = "eye" if psswd.icon_right == "eye-off" else "eye-off"
            MDLabel:
                text: "[ref=Show Password]Show Password[/ref]"
                markup: True
                on_ref_press:
                    cb.active = False if cb.active == True else True
                    psswd.password = False if psswd.password == True else True
                    psswd.icon_right = "eye" if psswd.icon_right == "eye-off" else "eye-off"
        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.85, None
            height: "30dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.125}
            spacing: "15dp"
            MDFlatButton:
                text: 'SIGN IN'
                font_size: "22dp"
                size_hint_x: 1
                md_bg_color: app.theme_cls.primary_color
                on_press: root.manager.current = 'main'
            MDFlatButton:
                text: 'SIGN UP'
                font_size: "22dp"
                size_hint_x: 1
                md_bg_color: app.theme_cls.primary_color
                on_press: root.manager.current = 'registration'

<Registration>:
    name: 'registration'
    Screen:
        MDLabel :
            text : 'SIGN UP'
            font_size: '48dp'
            halign: 'center'
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            pos_hint: {"center_y": 0.9}
        MDTextField:
            hint_text: 'Username'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            icon_right : "account"
            on_text: self.text = self.text.replace(" ", "")
            write_tab: False
        MDTextField:
            id: email
            hint_text: 'Email'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            icon_right : "email"
        MDTextField:
            id: psswd
            hint_text: 'Password'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            icon_right : "eye-off"
            password: True
            on_text: self.text = self.text.replace(" ", "")
            write_tab: False
        MDTextField:
            id: psswd
            hint_text: 'Repeat Password'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            icon_right : "eye-off"
        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.85, None
            height: "30dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.065}
            spacing: "15dp"
            MDFlatButton:
                text: 'SIGN UP'
                font_size: "22dp"
                size_hint_x: 1
                md_bg_color: app.theme_cls.primary_color
                on_press: root.manager.current = 'login'
            MDFlatButton:
                text: 'BACK'
                font_size: "22dp"
                size_hint_x: 1
                md_bg_color: app.theme_cls.primary_color
                on_press: root.manager.current = 'login'

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation:'vertical'
        md_bg_color: app.theme_cls.primary_color
        specific_text_color: 1, 1, 1, 1

        MDBottomNavigation:
                    
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Zestawy'
                icon: 'folder-star'

                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: 'Gotowe zestawy'
                        haling: 'left'
                        pos_hint: {"center_y": 0.95}

                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding: "16dp"
                            spacing: "16dp"
                            height: self.minimum_height
                            MDFillRoundFlatIconButton:
                                icon: 'folder'
                                size_hint: 0.9, None
                                height: "48dp"
                                text: 'TEST'
                                halign: 'center'
                                pos_hint: {"center_x": 0.5}
                                spacing: "30dp"
                                padding: "30dp"
                                font_size: "20dp"
                            MDFillRoundFlatIconButton:
                                icon: 'folder'
                                size_hint: 0.9, None
                                height: "48dp"
                                text: 'TEST'
                                halign: 'center'
                                pos_hint: {"center_x": 0.5}
                                spacing: "30dp"
                                padding: "30dp"
                                font_size: "20dp"
                            MDFillRoundFlatIconButton:
                                icon: 'folder'
                                size_hint: 0.9, None
                                height: "48dp"
                                text: 'TEST'
                                halign: 'center'
                                pos_hint: {"center_x": 0.5}
                                spacing: "30dp"
                                padding: "30dp"
                                font_size: "20dp"
                            MDFillRoundFlatIconButton:
                                icon: 'folder'
                                size_hint: 0.9, None
                                height: "48dp"
                                text: 'TEST'
                                halign: 'center'
                                pos_hint: {"center_x": 0.5}
                                spacing: "30dp"
                                padding: "30dp"
                                font_size: "20dp"
            
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Folder'
                icon: 'folder'
                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: 'Moje zestawy'
                        haling: 'left'
                        right_action_items: [["plus", lambda x: app.root.get_screen('main').show_popup()]]
                        pos_hint: {"center_y": 1}

                    ScrollView:
                        GridLayout:
                            size_hint_y: None
                            cols: 1
                            id: my_container
                            spacing: "53dp"
                            padding: "30dp"
                            height: self.minimum_height
                            

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Random'
                icon: 'rotate-left'

                MDRelativeLayout:

                    MDTopAppBar:
                        title: 'Losowe słowo'
                        haling: 'left'
                        pos_hint: {"top": 1}

                    MDRaisedButton:
                        id: random
                        text: "Losuj"
                        md_bg_color: app.theme_cls.primary_color
                        pos_hint: {"center_x": 0.5, "center_y": 0.45}
                        size_hint: 0.6, 0.3
                        on_press: app.root.get_screen('main').change()
                        font_size: "20dp"

                    MDIconButton:
                        icon: 'thumb-up'
                        pos_hint: {"center_x": 0.350, "center_y": 0.22}
                        size_hint: 0.25, 0.1
                        md_bg_color: 1, 0, 0, 1

                    MDIconButton:
                        icon: 'thumb-down'
                        pos_hint: {"center_x": 0.650, "center_y": 0.22}
                        size_hint: 0.25, 0.1
                        md_bg_color: 0, 1, 0, 1
                        

            MDBottomNavigationItem:
                name: 'screen 4'
                text: 'Profil'
                icon: 'account'

                MDRelativeLayout:

                    MDTopAppBar:
                        title: 'Profil'
                        haling: 'left'   
                        pos_hint: {"top": 1}

                    MDIconButton:
                        icon: "account"
                        icon_size: "64dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.6}

                    MDRaisedButton:
                        text: "Ustawienia"
                        md_bg_color: app.theme_cls.primary_color
                        pos_hint: {"center_x": 0.5, "center_y": 0.45}
                        size_hint: 0.7, 0.1
                        font_size: "18dp"
                        on_press: root.manager.current = 'settings'

<SettingsScreen>:
    name: 'settings'

    MDRelativeLayout:
        MDTopAppBar:
            title: 'Ustawienia'
            haling: 'right'
            left_action_items: [["arrow-left", lambda x: app.change_screen('main')]]
            pos_hint: {"center_y": 0.95}

        MDRaisedButton:
            text: "Zmień hasło"
            size_hint: 1, 0.1
            pos_hint: {"top": 0.5}
        MDRaisedButton:
            text: "O Fiszki"
            size_hint: 1, 0.1
            pos_hint: {"top": 0.4}
        MDRaisedButton:
            text: "Ustaw motyw"
            size_hint: 1, 0.1
            pos_hint: {"top": 0.3}
        MDRaisedButton:
            text: "Usuń konto"
            size_hint: 1, 0.1
            pos_hint: {"top": 0.2}
        MDRaisedButton:
            text: "Wyloguj się"
            size_hint: 1, 0.1
            pos_hint: {"top": 0.1}

<CustomWidget>:    
    MDFillRoundFlatIconButton:
        id: custom_button
        icon: 'folder'
        size_hint: 0.9, None
        text: ""
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        spacing: "30dp"
        padding: "30dp"
        font_size: "20dp" 

<Content>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None

    MDTextField:
        id: text_field
        hint_text: "Podaj nazwę folderu"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
    
"""