import flet as ft
from signin import Signin
from login import Login
from a_vere import AVerefication
from voi_reg import VoiceReg
from welcome import Welcome
def main(page: ft.Page):
    page.fonts = {
        "Poppins": "img/Poppins-Medium.ttf"
    }
    page.title = "Voice Verification"
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(Login(page).create())
        if page.route == "/signin":
            page.views.append(Signin(page).create())
        if page.route== "/accountverefication":
            page.views.append(AVerefication(page).create())
        if page.route== "/voiceregister":
            page.views.append(VoiceReg(page).create())
        if page.route== "/welcome":
            page.views.append(Welcome(page).create())
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
