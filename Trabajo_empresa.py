import flet as ft

def main(page: ft.Page):
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False

    

    def leerFichero():
        #Devolver la lista con los ususarios y contraseñas
        vDatos = []
        f = open("usuario.txt", "r") 
        for i in f:
            vDatos.append(i.replace("\n",""))
        f.close()

        return vDatos

    def comprobardatos(e):
        #Obtener datos del fichero de contraseñas
        vDatos = leerFichero()
        print (vDatos)
        #Obtener datos introducidos por teclado
        vIntroducidos=[]
        vIntroducidos.append(usuario.value)
        vIntroducidos.append(contraseña.value)
        print (vIntroducidos)
        #Comprobar login

        if intentos.value>1:
            if (vDatos[0]==vIntroducidos[0])and (vDatos[1]==vIntroducidos[1]):
                print ("Entrar")
                dlg1 = ft.AlertDialog(title=ft.Text("Sesión iniciada"),on_dismiss=lambda e: print("Dialog dismissed!"))
                page.dialog = dlg1
                dlg1.open = True
                page.update()
                page.clean()
            else:
                dlg = ft.AlertDialog(title=ft.Text("Usuario y contraseña incorrectos"),on_dismiss=lambda e: print("Dialog dismissed!"))
                page.dialog = dlg
                dlg.open = True
                usuario.value=""
                contraseña.value=""
                intentos.value=int(intentos.value)-1
                print(intentos.value)
                page.update()
        else:
            usuario.value=""
            contraseña.value=""
            dlg2 = ft.AlertDialog(title=ft.Text("Número de intentos alcalzado"),on_dismiss=lambda e: print("Dialog dismissed!"))
            page.dialog = dlg2
            dlg2.open = True
            page.window_close()
    
    page.vertical_alignment = ft.MainAxisAlignment.END
    
    img = ft.Image(src=f"/Imagenes/logo3.png", width=200, height=200)
    
    usuario = ft.TextField(label="Usuario", width=300)
    contraseña = ft.TextField(label="Contraseña", width=300, password=True, can_reveal_password=True)
    intentos = ft.TextField(value=3)
    
    botonguardar= ft.FilledButton(text="Iniciar sesión", on_click=comprobardatos)
    botonguardar.bgcolor= "#6e1010"
    
    img2 = ft.Image(src=f"/Imagenes/fondo2.png", width=200, height=200)

    
    page.add(img, usuario, contraseña, botonguardar, img2)
    
    
ft.app(target=main, assets_dir="Imagenes")  