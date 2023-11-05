import time

import flet as ft
import Enigma

class EnigmaApp(ft.UserControl):

    def build(self):
        # create Enigma
        self.enigma = Enigma.enigma()

        self.new_message = ft.TextField(hint_text="Enter Message", expand= True)
        self.messages =ft.Column()
        self.messages.scroll = "adaptive"

        self.r1 = ft.TextField(value =self.enigma.rotor1.counter)
        self.r2 = ft.TextField(value=self.enigma.rotor2.counter)
        self.r3 = ft.TextField(value=self.enigma.rotor3.counter)

        return ft.Column(
            width =600,
            controls=[


                ft.Row(
                    controls=[
                        self.new_message,
                        ft.ElevatedButton("Encrypt", on_click=self.encryptMsg),
                        ft.ElevatedButton("Decrypt", on_click=self.decryptMsg),
                    ],
                ),
                ft.ElevatedButton("ResetRotors", on_click=self.resetRotors),
                self.messages
            ],
        )
    def encryptMsg(self,e):
        temp = self.enigma.encrypt(self.new_message.value)
        self.new_message.value=" "
        self.messages.controls.append(ft.Text(temp, color="White"))
        self.update()
    def decryptMsg(self,e):
        temp = self.enigma.decrypt(self.new_message.value)
        self.new_message.value = " "
        self.messages.controls.append(
            ft.Row(
                controls=[
                    ft.Text(temp, color="blue"),
                    ft.IconButton(icon=ft.icons.DELETE_SWEEP, on_click=self.deleteMsg)
                ])
            )

        self.update()
    def resetRotors(self,e):
        self.enigma.resetEnigma()

    def deleteMsg(self,e):
        self.messages.controls.remove(e)
        self.update()




def main(page: ft.Page):

    title = ft.Text(value="Enigma Simulator", size="24")
    #page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.add(title)


    enigmaApp = EnigmaApp()
    page.add(enigmaApp)



ft.app(target=main)