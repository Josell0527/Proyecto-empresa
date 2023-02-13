import flet as ft

def main(page: ft.Page):
    vertical_alignment= ft.MainAxisAlignment.CENTER
    img = ft.Image(src=f"/Imagenes/logo2.png", width=100, height=100)
    
    

    page.add(img)
ft.app(target=main, assets_dir="Imagenes")  