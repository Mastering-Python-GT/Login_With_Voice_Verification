from flet import UserControl, Page, margin
import flet as ft
import time
from threading import Thread
import sounddevice as sd
from openpyxl import load_workbook
from scipy.io.wavfile import write
import numpy as np
from rec import Rec


class VoiceReg(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def create(self):
        global status
        status = False

        def toggle_icon_button1(e):
            global status, c, t
            if e.control.selected == False:
                status = True
                kk.value = ''
                self.page.update()
                fg.disabled = True
                fg.style.color = "grey"
                e.control.selected = True
                t1 = Thread(target=task)
                t1.start()
                t = Rec()
                try:
                    if t.args.samplerate is None:
                        device_info = sd.query_devices(t.args.device, 'input')
                        t.args.samplerate = int(
                            device_info['default_samplerate'])

                        with sd.InputStream(samplerate=t.args.samplerate, device=t.args.device,
                                            channels=t.args.channels, callback=t.callback):
                            c = t.q.get()
                            while e.control.selected == True:
                                c = np.append(c, t.q.get(), axis=0)
                except KeyboardInterrupt:
                    t.parser.exit(0)
                except Exception as e:
                    t.parser.exit(type(e).__name__ + ': ' + str(e))

                e.control.selected = False
                fg.disabled = False
                fg.style.color = "#1E90FF"
            else:
                e.control.selected = False
                sd.stop()

        def toggle_icon_button2(e):
            global c, t
            if e.control.selected == False:
                e.control.selected = True
                e.control.update()
                sd.play(c, t.args.samplerate)
                sd.wait()
                e.control.selected = False
                e.control.update()
            else:
                e.control.selected = False
                sd.stop()
                e.control.update()

        kk = ft.Text(value='', font_family="Poppins",
                     size=15, weight='bold', color='Red')

        def register(self):
            global c, t
            if status == True:
                wb = load_workbook('data_base.xlsx')
                ws = wb.active
                ws.append([self.page.data[0], self.page.data[1],
                          self.page.data[2], (self.page.data[1]+'.mp3')])
                wb.save('data_base.xlsx')
                write(f'{self.page.data[1]}.mp3', t.args.samplerate, c)
                self.page.go("/")
            else:
                kk.value = "Register Your Voice"
                self.page.update()

        def task():
            while True:
                if ff.selected == True:
                    time.sleep(0.3)
                    c.scale = 1
                    self.page.update()
                    time.sleep(0.5)
                    c.scale = 0.5
                    self.page.update()
                else:
                    break

        c = ft.Container(
            width=60,
            height=60,
            bgcolor="#99FF3131",
            border_radius=50,
            scale=ft.transform.Scale(scale=0.5),
            animate_scale=ft.animation.Animation(400),
        )
        ff = ft.IconButton(
            bgcolor='#ECFFDC',
            width=40,
            height=40,
            icon_size=40,
            icon=ft.icons.MIC_ROUNDED,
            selected_icon=ft.icons.MIC_OFF_ROUNDED,
            selected=False,
            style=ft.ButtonStyle(
                color='#1E90FF',
                padding=0
            ),
            on_click=toggle_icon_button1
        )
        fg = ft.IconButton(
            disabled=True,
            bgcolor='#ECFFDC',
            width=40,
            height=40,
            icon_size=40,
            icon=ft.icons.PLAY_CIRCLE_OUTLINED,
            selected_icon=ft.icons.STOP_CIRCLE_OUTLINED,
            selected=False,
            style=ft.ButtonStyle(
                color='grey',
                padding=0
            ),
            on_click=toggle_icon_button2)

        t = ft.View(
            "/voiceregister",
            [
                ft.Container(
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
                            blur_style=ft.ShadowBlurStyle.OUTER
                        ),
                        content=ft.Column(
                            [
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
                                                "Voice Registration", font_family="Poppins", size=20, weight='bold', color='#28282B')
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    )

                                ),
                                ft.Container(
                                    width=480,
                                    padding=5,
                                    content=ft.Column(
                                        [
                                            ft.Text('press the record button and say the sentence to register your voice',
                                                    font_family="Poppins", size=15, color='#28282B', text_align='center')
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    )
                                ),
                                ft.Container(
                                    width=480,
                                    padding=5,
                                    border=ft.border.all(
                                        1, ft.colors.AMBER_100),
                                    border_radius=5,
                                    content=ft.Column(
                                        [
                                            ft.Text('hello guys welcome to Mastering Python channel and this is a demonstration of voice verification,' +
                                                    ' if you found this tutorial helpful please support me by subscribing to my channel and leave a like to the video' +
                                                    ', if you have any issue about this tutorial just ask me in the comments section.',
                                                    font_family="Poppins", size=15, color='#28282B', text_align='justify')
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    )
                                ),
                                ft.Row(
                                    [
                                        ft.Stack(
                                            [
                                                c,
                                                ft.Row(
                                                    [
                                                        ff
                                                    ], vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER,
                                                    width=60,
                                                    height=60,
                                                )
                                            ]
                                        ),
                                        fg
                                    ], vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                kk,
                                ft.Divider(height=30, color='transparent'),
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
                                            on_click=lambda _: self.page.go(
                                                "/signin")
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
                                                ), on_click=register
                                            )
                                        )
                                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    )
                                )
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    )
                )
            ], padding=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        return t
