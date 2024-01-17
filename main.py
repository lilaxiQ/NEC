import flet as ft
import keyboard

def main(page: ft.Page):
    #page settings
    page.title = "NEC"
    page.window_width=250
    page.window_height=340
    page.window_resizable = False
    RADIUS = 10
    text = ft.TextField(text_size=30, read_only=True, border="underline")
    page.add(text)
    def keyboardInput(e):
        data = e.control.data
        if data not in ['e', 'b', '=']:
            text.value += str(data)
        elif data == 'e':
            text.value = ''
        elif data == 'b':
            text.value = text.value[:-1]
        elif data == '=':
            try:
                text.value = str(eval(text.value))
            except ZeroDivisionError:
                text.value = 'Division by 0'
            except SyntaxError:
                text.value = ''
        page.update()

    #buttons group 1
    btn_pl = ft.TextButton(text='+', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '+', on_click = keyboardInput)
    btn_bk = ft.TextButton(text='←', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = 'b', on_click = keyboardInput)
    btn_r = ft.TextButton(text='(', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '(', on_click = keyboardInput)
    btn_l = ft.TextButton(text=')', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = ')', on_click = keyboardInput)
    page.add(ft.Row(
        controls=[btn_bk, btn_r, btn_l, btn_pl],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    #buttons group 2
    btn_7 = ft.TextButton(text='7', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '7', on_click = keyboardInput)
    btn_8 = ft.TextButton(text='8', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '8', on_click = keyboardInput)
    btn_9 = ft.TextButton(text='9', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '9', on_click = keyboardInput)
    btn_m = ft.TextButton(text='-', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '-', on_click = keyboardInput)
    page.add(ft.Row(
        controls=[btn_7, btn_8, btn_9, btn_m],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    #buttons group 3
    btn_4 = ft.TextButton(text='4', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '4', on_click = keyboardInput)
    btn_5 = ft.TextButton(text='5', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '5', on_click = keyboardInput)
    btn_6 = ft.TextButton(text='6', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '6', on_click = keyboardInput)
    btn_mp = ft.TextButton(text='x', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '*', on_click = keyboardInput)
    page.add(ft.Row(
        controls=[btn_4, btn_5, btn_6, btn_mp],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    #buttons group 4
    btn_1 = ft.TextButton(text='1', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '1', on_click = keyboardInput)
    btn_2 = ft.TextButton(text='2', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '2', on_click = keyboardInput)
    btn_3 = ft.TextButton(text='3', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '3', on_click = keyboardInput)
    btn_div = ft.TextButton(text='/', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '/', on_click = keyboardInput)
    page.add(ft.Row(
        controls=[btn_1, btn_2, btn_3, btn_div],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    #buttons group 5
    btn_c = ft.TextButton(text='C', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = 'e', on_click = keyboardInput)
    btn_0 = ft.TextButton(text='0', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '0', on_click = keyboardInput)
    btn_p = ft.TextButton(text='.', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '.', on_click = keyboardInput)
    btn_eq = ft.TextButton(text='=', style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=RADIUS)), data = '=', on_click = keyboardInput)
    page.add(ft.Row(
        controls=[btn_c, btn_0, btn_p, btn_eq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ))
    page.update()

#initialization
ft.app(target = main)