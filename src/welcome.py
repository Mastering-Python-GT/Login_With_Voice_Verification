import flet as ft
from flet import UserControl, ControlEvent, Page, padding, margin
from openpyxl import load_workbook


class Welcome(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.page.data = []

    def create(self):
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
                                            "Welcome", font_family="Poppins", size=25, weight='bold', color='#28282B')
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )

                            ),
                            ft.Divider(height=80, color='transparent'),
                            ft.Container(
                                alignment=ft.alignment.center,
                                width=450,
                                content=ft.TextButton(
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
                                        "Log-Out", font_family="Poppins", size=20),
                                    on_click=lambda _: self.page.go("/")
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


# ft.ElevatedButton(
        #     width=450,
        #     height=40,
        #     content=ft.Text(
        #         "Log-In", font_family="Poppins", size=17, weight='bold', color='#28282B'),
        #     style=ft.ButtonStyle(
        #         shape=ft.RoundedRectangleBorder(
        #             radius=5),
        #         shadow_color='#00FFFF',
        #         color='#28282B',
        #         elevation={
        #             ft.MaterialState.PRESSED: 0,
        #             ft.MaterialState.DEFAULT: 4,
        #         },
        #         animation_duration=100,
        #         bgcolor='#F0FFFF'
        #     )
        # ),
"""

,
                                                    ft.Row(
                                                        [
                                                            ft.Container(
                                                                content=ft.TextButton(
                                                                    width=50,
                                                                    height=50,
                                                                    on_hover=self.gtt2,
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
                                                                        width=42,
                                                                        height=42,
                                                                        src='img/ca.svg',
                                                                        fit=ft.ImageFit.CONTAIN,
                                                                        color='#28282B'),
                                                                    on_click=lambda _: self.page.go(
                                                                        "/signin")

                                                                )
                                                            ),
                                                            ft.Container(
                                                                content=ft.Row(
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
                                                                )
                                                            )


                                                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=100
                                                    ),



"""

# ft.Divider(height=20, color='transparent')
# ft.Container(
#     padding=padding.only(left=20),
#     width=450,
#     height=145,
#     content=ft.Column(
#         [
#             ft.Row(
#                 [
#                     ft.Text(
#                         "Create Account", font_family="Poppins", size=15, color='#28282B'),
#                     ft.Text(
#                         "Log-In with", font_family="Poppins", size=15, color='#28282B')

#                 ], alignment=ft.MainAxisAlignment.START, spacing=145
#             ),
#             ft.Row(
#                 [
#                     ft.Container(width=125,
#                                  content=ft.Divider(thickness=2, height=2)),
#                     ft.Container(width=90,
#                                  content=ft.Divider(thickness=2, height=2))
#                 ], alignment=ft.MainAxisAlignment.START, spacing=142
#             )
#         ], spacing=10
#     )
# )
