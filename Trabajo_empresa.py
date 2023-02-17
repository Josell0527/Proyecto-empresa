import flet as ft

def main(page: ft.Page):



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
      
        if (vDatos[0]==vIntroducidos[0])and (vDatos[1]==vIntroducidos[1]):
            print ("Entrar")
        else:
            dlg = ft.AlertDialog(title=ft.Text("Usuario y contraseña incorectos"),on_dismiss=lambda e: print("Dialog dismissed!"))
            page.dialog = dlg
            dlg.open = True
            page.update()


    #page.bgcolor=
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False
    
    img = ft.Image(src=f"/Imagenes/logo3.png", width=200, height=200)
    
    usuario = ft.TextField(label="Usuario", width=300)
    contraseña = ft.TextField(label="Contraseña", width=300)
    
    botonguardar=ft.FilledButton(text="Iniciar sesión", on_click=comprobardatos)

    
    page.add(img, usuario, contraseña, botonguardar)
    
    
ft.app(target=main, assets_dir="Imagenes")  