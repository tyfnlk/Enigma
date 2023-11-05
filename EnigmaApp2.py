import time

import flet as ft
import Enigma

class EnigmaApp(ft.UserControl):

    def build(self):
        # create Enigma object
        self.enigma = Enigma.enigma()
        #create objects for encryption/decryption widget
        self.new_message = ft.TextField(hint_text="Enter Message", expand= True)
        self.encryptBtn = ft.ElevatedButton("Encrypt", on_click=self.encryptMsg)
        self.decryptBtn = ft.ElevatedButton("Decrypt", on_click=self.decryptMsg)
        #sub column for control buttons
        self.cryptBtns = ft.Column(controls=[self.encryptBtn,self.decryptBtn])

        self.messages = ft.Column()
        self.messages.scroll = "adaptive"

        #putting all the objects into the encryption/decryption widget
        self.messagesControl =ft.Column(controls=[
            ft.Row(controls=[
                self.new_message, self.cryptBtns
            ]),
            self.messages
        ])

        self.r1 = ft.TextField(value =self.enigma.rotor1.counter)
        self.r2 = ft.TextField(value=self.enigma.rotor2.counter)
        self.r3 = ft.TextField(value=self.enigma.rotor3.counter)

        return self.messagesControl

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



class Message(ft.UserControl):
    #msg = original message
    #cryption = en/decryption
    #ype = 0/1 encryption/decryption
    def __init__(self,msg,cryption,type,deleteMsg):
        super.__init__()
        self.msg= msg
        self.cryption = cryption
        self.type=type
        self.deleteMsg = deleteMsg

    def build(self):
        self.displayMsg= ft.Text(value=self.cryption)
        self.orginalMsg= ft.Text(value= self.msg)
        self.editBtn = ft.IconButton(ft.icons.SWITCH_ACCESS_SHORTCUT, on_click=self.switchView)
        self.originalView = ft.Row(controls = [self.displayMsg, self.editBtn])

    def switchView(self):
        pass
class RotorWidget(ft.UserControl):
    def __init__(self, enigma: Enigma):
        self.enigma = enigma
        self.r1 = ft.TextField(value =self.enigma.rotor1.counter)
        self.r2 = ft.TextField(value=self.enigma.rotor2.counter)
        self.r3 = ft.TextField(value=self.enigma.rotor3.counter)




def main(page: ft.Page):

    title = ft.Text(value="Enigma Simulator", size="24")
    #page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.add(title)


    enigmaApp = EnigmaApp()
    page.add(enigmaApp)



ft.app(target=main)