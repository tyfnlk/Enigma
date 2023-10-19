import Enigma
import flet as ft


class EnigmaApp(ft.UserControl):
    def build(self):
        self.enigma = Enigma.enigma()

        self.tf = ft.TextField()
        self.encryptBtn = ft.FloatingActionButton("Encrypt", on_click=self.encryptMsg)
        self.decryptBtn = ft.FloatingActionButton("Decrypt")

        self.msgList = ft.Column()

        taskRow = ft.Column(controls=[ft.Row(controls=[self.tf, self.encryptBtn, self.decryptBtn]), self.msgList])

        return taskRow

    def encryptMsg(self, e):
        task = Cypher(self.tf.value, self.msgDelete)
        self.msgList.controls.append(task)
        self.tf.value = ""
        self.update()

    def decryptMsg(self, e):
        pass

    def msgDelete(self, e):
        pass


class Cypher(ft.UserControl):
    def __init__(self, text, delete):
        super().__init__()

        self.message = text
        self.delete = delete

    def build(self):
        self.displaytext = ft.Text("hello")
        self.displayView = ft.Row(controls=[self.message, ft.IconButton(ft.icons.DELETE, on_click=self.removeCypher)])

        return self.displayView

    def removeCypher(self, e):
        pass


def main(page: ft.page):
    page.title = "Enigma App By Terry Leeshanok"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "BLUE"

    enigmaApp = EnigmaApp()

    page.add(enigmaApp)

    # def encryptMessage(msg):
    #     temp = textField.value
    #     temp= enigma.encrypt(temp)
    #     encryption = ft.Text(temp)
    #     encryptRow = ft.Row(controls=[encryption])
    #     page.add(encryptRow)
    #
    # def derrcryptMessage(msg):
    #     temp = textField.value
    #     temp= enigma.encrypt(temp)
    #     encryption = ft.Text(temp)
    #     encryptRow = ft.Row(controls=[encryption])
    #     page.add(encryptRow)
    #
    # enigma = Enigma.enigma()
    #
    # page.window_width=500
    # page.window_height=700
    # textField = ft.TextField(width=300)
    # encryptBtn = ft.ElevatedButton(text="Encrypt",on_click=encryptMessage)
    # decryptBtn = ft.ElevatedButton(text="Decrypt", on_click=decryptMessage)
    # mainrow=ft.Row(controls=[textField,encryptBtn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    # page.add(mainrow)
    #


ft.app(target=main)
