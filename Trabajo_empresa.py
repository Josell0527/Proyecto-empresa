import flet as ft

def main(page: ft.Page):
    #page.bgcolor=
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False
    
    img = ft.Image(src=f"/Imagenes/logo2.png", width=100, height=100)
    
    usuario = ft.TextField(label="Usuario", width=300)
    contraseña = ft.TextField(label="Contraseña", width=300)
    
    botonguardar=ft.FilledButton(text="Iniciar sesión")

    
    page.add(img, usuario, contraseña, botonguardar)
    
ft.app(target=main, assets_dir="Imagenes")  