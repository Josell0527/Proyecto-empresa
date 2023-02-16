import flet as ft

def main(page: ft.Page):
    #page.bgcolor=
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False
    
    img = ft.Image(src=f"/Imagenes/logo3.png", width=200, height=200)
    
    usuario = ft.TextField(label="Usuario", width=300)
    contraseña = ft.TextField(label="Contraseña", width=300)
    
    botonguardar=ft.FilledButton(text="Iniciar sesión")
    
    page.add(img, usuario, contraseña, botonguardar)
    
    
ft.app(target=main, assets_dir="Imagenes")  