import flet as ft

def main(page: ft.Page):
    page.title = "NEC"
    page.window_width=320
    page.window_height=450
    page.window_resizable = False
    RADIUS = 10
    text = ft.TextField(text_size=50, read_only=True, border="underline")
    page.add(text)
    btn_pl = ft.TextButton(text='+', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_bk = ft.TextButton(text='←', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_r = ft.TextButton(text='(', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_l = ft.TextButton(text=')', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    page.add(ft.Row(
        controls=[btn_bk, btn_r, btn_l, btn_pl],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    btn_7 = ft.TextButton(text='7', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_8 = ft.TextButton(text='8', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_9 = ft.TextButton(text='9', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_m = ft.TextButton(text='-', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    page.add(ft.Row(
        controls=[btn_7, btn_8, btn_9, btn_m],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    btn_4 = ft.TextButton(text='4', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_5 = ft.TextButton(text='5', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_6 = ft.TextButton(text='6', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_mp = ft.TextButton(text='x', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    page.add(ft.Row(
        controls=[btn_4, btn_5, btn_6, btn_mp],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    btn_1 = ft.TextButton(text='1', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_2 = ft.TextButton(text='2', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_3 = ft.TextButton(text='3', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_div = ft.TextButton(text='/', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    page.add(ft.Row(
        controls=[btn_1, btn_2, btn_3, btn_div],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    btn_c = ft.TextButton(text='C', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_0 = ft.TextButton(text='0', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_p = ft.TextButton(text='.', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    btn_eq = ft.TextButton(text='=', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)))
    page.add(ft.Row(
        controls=[btn_c, btn_0, btn_p, btn_eq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    navigation = ft.NavigationBar(destinations=[
        ft.NavigationDestination(label="Simple", icon=ft.icons.ABC),
        ft.NavigationDestination(label="Pro", icon=ft.icons.CALCULATE),
    ])
    page.add(navigation)
    page.update()

ft.app(target = main)