import flet as ft
from flet import *


class Signin(UserControl):
    
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.page.data=[]

    def trs(self, e: ControlEvent):
        if e.control.label == 'Enter Your User Name':
            e.control.label = 'User Name'
            e.control.label_style = ft.TextStyle(color='')
            self.page.update()
        
        if e.control.label == 'Enter Your Email':
            e.control.label = 'Email'
            e.control.label_style = ft.TextStyle(color='')
            self.page.update()

        if e.control.label == 'Enter Your Password':
            e.control.label = 'Password'
            e.control.label_style = ft.TextStyle(color='')
            self.page.update()

    def create(self):

        def next(self):

            if txt1.value == '' or txt2.value == '' or txt3.value == '' or txt4.value == '' :
                if txt1.value == '':
                    txt1.label = 'Enter Your User Name'
                    txt1.label_style = ft.TextStyle(color='Red')
                if txt2.value == '':
                    txt2.label = 'Enter Your Email'
                    txt2.label_style = ft.TextStyle(color='Red')
                if txt3.value == '':
                    txt3.label = 'Enter Your Password'
                    txt3.label_style = ft.TextStyle(color='Red')
                if txt4.value == '':
                    txt4.label = 'Enter Your Password'
                    txt4.label_style = ft.TextStyle(color='Red')
                self.page.update()
            else:
                self.page.data.append(txt1.value)
                self.page.data.append(txt2.value)
                self.page.data.append(txt3.value)
                self.page.go("/voiceregister")

        txt1 = ft.TextField(
            width=450,
            border='underline',
            label="User Name",
            content_padding=padding.only(
                top=-5),
            text_style=ft.TextStyle(
                font_family='Poppins', size=18),
            on_focus=self.trs
        )
        txt2 = ft.TextField(
            width=450,
            border='underline',
            label="Email",
            content_padding=padding.only(
                top=-5),
            text_style=ft.TextStyle(
                font_family='Poppins', size=18),
            on_focus=self.trs
        )
        txt3 = ft.TextField(
            width=450,
            border='underline',
            label="Password",
            content_padding=padding.only(
                top=-5),
            text_style=ft.TextStyle(
                font_family='Poppins', size=18),
            password=True,
            can_reveal_password=True,
            on_focus=self.trs
        )
        txt4 = ft.TextField(
            width=450,
            border='underline',
            label="Repeat Password",
            content_padding=padding.only(
                top=-5),
            text_style=ft.TextStyle(
                font_family='Poppins', size=18),
            password=True,
            can_reveal_password=True,
            on_focus=self.trs
        )
        t = ft.View(
            "/signin",
            [ft.Container(
                expand=True,
                image_src="img/zze.jpg",
                image_fit=ft.ImageFit.COVER,
                alignment=ft.alignment.center,
                content=ft.Container(
                    alignment=ft.alignment.center,
                    border_radius=20,
                    width=500,
                    height=600,
                    bgcolor='#FFFAFA',
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=5,
                        color=ft.colors.AMBER_100,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=margin.only(top=20),
                                width=64,
                                height=64,
                                image_src="img/voice.png",
                                image_fit=ft.ImageFit.CONTAIN,
                                shadow=ft.BoxShadow(
                                    spread_radius=0,
                                    blur_radius=10,
                                    color='#00FFFF',
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                )
                            ),
                            ft.Container(
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Text(
                                            "Voice Verefication", font_family="Poppins", size=40, weight='bold', color='#28282B'),
                                        ft.Text(
                                            "Create Account", font_family="Poppins", size=25, weight='bold', color='#28282B')
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )

                            ),
                            ft.Container(
                                margin=margin.only(top=5),
                                width=480,
                                content=ft.Column(
                                    [
                                        txt1,
                                        txt2,
                                        txt3,
                                        txt4
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )

                            ),
                            ft.Divider(height=70, color='transparent'),
                            ft.Container(
                                width=450,
                                content=ft.Row(
                                    [ft.TextButton(
                                        width=110,
                                        height=40,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(
                                                radius=5),
                                            padding=0,
                                            animation_duration=100,
                                            color={
                                                ft.MaterialState.DEFAULT: '#1E90FF',
                                                ft.MaterialState.HOVERED: '#1F51FF'
                                            }
                                        ),
                                        content=ft.Text(
                                            "CANCEL", font_family="Poppins", size=20),
                                        on_click=lambda _: self.page.go("/")
                                    ), ft.Container(
                                        alignment=ft.alignment.center,
                                        content=ft.TextButton(
                                            width=110,
                                            height=40,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(
                                                    radius=5),
                                                padding=5,
                                                animation_duration=100,
                                                # overlay_color='#7DF9FF',
                                                bgcolor={
                                                    ft.MaterialState.DEFAULT: '#1E90FF',
                                                    ft.MaterialState.HOVERED: '#1F51FF'
                                                },
                                            ),

                                            content=ft.Container(
                                                content=ft.Row(
                                                    [
                                                        ft.Text(
                                                            "NEXT", font_family="Poppins", size=20,  color='White'),
                                                        ft.Image(
                                                            src='img/next.svg', width=25, height=25, color='White')

                                                    ], spacing=10, alignment=ft.MainAxisAlignment.CENTER
                                                ),
                                            ), on_click=next
                                        )
                                    )
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                )
                            )

                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            ),], padding=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        return t
