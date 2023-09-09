import flet as ft
from flet import UserControl, ControlEvent, Page, padding, margin
from openpyxl import load_workbook


class Login(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.page.data = []

    def gtt(self, e: ControlEvent):
        if e.data == "true":
            self.page.views[0].controls[0].content.content.controls[2].content.controls[
                5].content.controls[2].content.color = '#1E90FF'
            e.control.content.color = '#1E90FF'
        else:
            self.page.views[0].controls[0].content.content.controls[2].content.controls[
                5].content.controls[2].content.color = None
            e.control.content.color = '#28282B'
        self.page.update()

    def trs(self, e: ControlEvent):
        if e.control.label == 'Enter Your Email' or e.control.label == 'Email Not Found':
            e.control.label = 'Email'
            e.control.label_style = ft.TextStyle(color='')
            self.page.update()
        else:
            if e.control.label == 'Enter Your Password' or e.control.label == 'Password Incorrect':
                e.control.label = 'Password'
                e.control.label_style = ft.TextStyle(color='')
                self.page.update()

    def create(self):
        a = ft.TextField(
            width=450,
            border='underline',
            label="Email",
            content_padding=padding.only(top=-5),
            text_style=ft.TextStyle(font_family='Poppins', size=18),
            on_focus=self.trs
        )
        b = ft.TextField(
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

        def login(self):
            global email, password
            email = ''
            password = ''
            wb = load_workbook('data_base.xlsx')
            ws = wb.active
            for row in ws:
                if a.value == row[1].value:
                    email = row[1].value
                    password = row[2].value
                    break

            if a.value == '' or b.value == '':
                if a.value == '':
                    a.label = 'Enter Your Email'
                    a.label_style = ft.TextStyle(color='Red')
                if b.value == '':
                    b.label = 'Enter Your Password'
                    b.label_style = ft.TextStyle(color='Red')
                self.page.update()
            else:
                if a.value == email and b.value == password:
                    self.page.data.append(a.value)
                    self.page.go("/accountverefication")
                else:
                    if email == '':
                        a.value = ''
                        a.label = 'Email Not Found'
                        a.label_style = ft.TextStyle(color='Red')
                        self.page.update()
                    if b.value != password:
                        b.value = ''
                        b.label = 'Password Incorrect'
                        b.label_style = ft.TextStyle(color='Red')
                        self.page.update()

        t = ft.View(
            "/",
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
                                            "Log-In", font_family="Poppins", size=25, weight='bold', color='#28282B')
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )

                            ),
                            ft.Container(
                                margin=margin.only(top=5),
                                width=480,
                                content=ft.Column(
                                    [
                                        a, b,
                                        ft.Container(
                                            width=450,
                                            alignment=ft.alignment.center_left,
                                            content=ft.TextButton(
                                                width=185,
                                                style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(
                                                        radius=5),
                                                    padding=5,
                                                    animation_duration=100
                                                ),
                                                content=ft.Row(
                                                    [
                                                        ft.Image(
                                                            src='img/fr.svg', width=30, height=30, color='#1E90FF'),
                                                        ft.Text(
                                                            value="Forgot Your Password", color='#1E90FF'),
                                                    ], spacing=5
                                                )
                                            )
                                        ),
                                        ft.Divider(
                                            height=10, color='transparent'),
                                        ft.Row(
                                            [
                                                ft.ElevatedButton(
                                                    width=220,
                                                    height=40,
                                                    content=ft.Text(
                                                        "Sign-In", font_family="Poppins", size=17, weight='bold', color='#28282B'),
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(
                                                            radius=5),
                                                        shadow_color='#00FFFF',
                                                        color='#28282B',
                                                        elevation={
                                                            ft.MaterialState.PRESSED: 0,
                                                            ft.MaterialState.DEFAULT: 4,
                                                        },
                                                        animation_duration=100,
                                                        bgcolor='#F0FFFF'
                                                    ), on_click=login
                                                ),
                                                ft.ElevatedButton(
                                                    width=220,
                                                    height=40,
                                                    content=ft.Text(
                                                        "Create Account", font_family="Poppins", size=17, weight='bold', color='#28282B'),
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(
                                                            radius=5),
                                                        shadow_color='#00FFFF',
                                                        color='#28282B',
                                                        elevation={
                                                            ft.MaterialState.PRESSED: 0,
                                                            ft.MaterialState.DEFAULT: 4,
                                                        },
                                                        animation_duration=100,
                                                        bgcolor='#F0FFFF'
                                                    ), on_click=lambda _: self.page.go("/signin")

                                                )
                                            ], alignment=ft.MainAxisAlignment.CENTER,
                                        ), ft.Container(
                                            width=450,
                                            height=180,
                                            alignment=ft.alignment.center,
                                            content=ft.Column(
                                                controls=[
                                                    ft.Divider(
                                                        height=40, color='transparent'),
                                                    ft.Text(
                                                        "Log-In with", font_family="Poppins", size=15, weight='bold', color='#28282B'),
                                                    ft.Container(width=120,
                                                                 content=ft.Divider(height=1),),
                                                    ft.Row(
                                                        controls=[
                                                            ft.TextButton(
                                                                on_hover=self.gtt,
                                                                style=ft.ButtonStyle(
                                                                    shape=ft.CircleBorder(),
                                                                    padding=0,
                                                                    animation_duration=100,
                                                                    elevation={
                                                                        ft.MaterialState.PRESSED: 0,
                                                                        ft.MaterialState.DEFAULT: 5,
                                                                    },
                                                                    shadow_color='#00FFFF',
                                                                    bgcolor='#F0FFFF',
                                                                ),
                                                                content=ft.Image(
                                                                    width=50,
                                                                    height=50,
                                                                    src='img/github-svgrepo-com.svg',
                                                                    fit=ft.ImageFit.CONTAIN,
                                                                    color='#28282B')

                                                            ),
                                                            ft.TextButton(
                                                                on_hover=self.gtt,
                                                                style=ft.ButtonStyle(
                                                                    shape=ft.CircleBorder(),
                                                                    padding=0,
                                                                    animation_duration=100,
                                                                    elevation={
                                                                        ft.MaterialState.PRESSED: 0,
                                                                        ft.MaterialState.DEFAULT: 5,
                                                                    },
                                                                    shadow_color='#00FFFF',
                                                                    bgcolor='#F0FFFF',
                                                                ),
                                                                content=ft.Image(
                                                                    width=50,
                                                                    height=50,
                                                                    src='img/ggsv.svg',
                                                                    fit=ft.ImageFit.CONTAIN,
                                                                    color='#28282B')

                                                            ),
                                                            ft.TextButton(
                                                                on_hover=self.gtt,
                                                                style=ft.ButtonStyle(
                                                                    shape=ft.CircleBorder(),
                                                                    padding=0,
                                                                    animation_duration=100,
                                                                    elevation={
                                                                        ft.MaterialState.PRESSED: 0,
                                                                        ft.MaterialState.DEFAULT: 5,
                                                                    },
                                                                    shadow_color='#00FFFF',
                                                                    bgcolor='#F0FFFF',
                                                                ),
                                                                content=ft.Image(
                                                                    width=50,
                                                                    height=50,
                                                                    src='img/fcb2.svg',
                                                                    fit=ft.ImageFit.CONTAIN,
                                                                    color='#28282B')

                                                            ),
                                                            ft.TextButton(
                                                                on_hover=self.gtt,
                                                                style=ft.ButtonStyle(
                                                                    shape=ft.CircleBorder(),
                                                                    padding=0,
                                                                    animation_duration=100,
                                                                    elevation={
                                                                        ft.MaterialState.PRESSED: 0,
                                                                        ft.MaterialState.DEFAULT: 5,
                                                                    },
                                                                    shadow_color='#00FFFF',
                                                                    bgcolor='#F0FFFF',
                                                                ),
                                                                content=ft.Image(
                                                                    width=50,
                                                                    height=50,
                                                                    src='img/in1.svg',
                                                                    fit=ft.ImageFit.CONTAIN,
                                                                    color='#28282B')
                                                            )
                                                        ], alignment=ft.MainAxisAlignment.CENTER
                                                    ),


                                                ], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10
                                            )
                                        )

                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )
                            )
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            ),


            ], padding=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        return t
