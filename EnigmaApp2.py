import time

import flet as ft
import Enigma

class EnigmaApp(ft.UserControl):

    def build(self):
        # create Enigma object
        self.enigma = Enigma.enigma()

        # controls for rotors
        self.r1 = ft.Text(value=self.enigma.rotor1.counter)
        self.r2 = ft.Text(value=self.enigma.rotor2.counter)
        self.r3 = ft.Text(value=self.enigma.rotor3.counter)
        # edit views for rotors
        self.r1edit = ft.TextField(value=self.enigma.rotor1.counter)
        self.r2edit = ft.TextField(value=self.enigma.rotor2.counter)
        self.r3edit = ft.TextField(value=self.enigma.rotor3.counter)

        self.rotorEditBtn = ft.ElevatedButton('Edit', on_click=self.rotorEdit)
        self.rotorResetBtn = ft.ElevatedButton('Reset', on_click=self.rotorReset)
        self.rotorSaveBtn = ft.ElevatedButton('Save', on_click=self.saveRotor)
        # rotor display
        self.rotorTracker = ft.Row(controls=[self.r1, self.r2, self.r3], alignment=ft.MainAxisAlignment.CENTER)
        self.rotorTrackerEdit = ft.Row(controls=[self.r1edit, self.r2edit, self.r3edit, self.rotorSaveBtn], alignment=ft.MainAxisAlignment.CENTER, visible=False)
        self.rotorEditBtn = ft.ElevatedButton('Edit', on_click=self.rotorEdit)
        self.rotorResetBtn = ft.ElevatedButton('Reset', on_click=self.rotorReset)
        self.rotorSaveBtn = ft.ElevatedButton('Save', on_click=self.saveRotor)

        #create objects for encryption/decryption widget creation
        self.new_message = ft.TextField(hint_text="Enter Message", expand=True)
        self.encryptBtn = ft.ElevatedButton("Encrypt", on_click=self.encryptMsg)
        self.decryptBtn = ft.ElevatedButton("Decrypt", on_click=self.decryptMsg)

        #sub column for control buttons
        self.cryptBtns = ft.Column(controls=[self.encryptBtn,self.decryptBtn])
        self.rotors = ft.Column()
        self.messages = ft.Column()
        self.messages.scroll = "adaptive"

        #putting all the objects into the encryption/decryption widget
        self.messagesControl =ft.Column(controls=[
            self.rotorTracker,
            self.rotorTrackerEdit,
            ft.Row(controls=[
                ft.ElevatedButton('Reset', on_click=self.rotorReset), ft.ElevatedButton('Edit', on_click=self.rotorEdit)
            ], alignment=ft.MainAxisAlignment.CENTER),
            self.rotors,
            ft.Row(controls=[
                self.new_message, self.cryptBtns
            ]),
            self.messages
        ])


        return self.messagesControl

    def encryptMsg(self,e):
        # identify variables needed to make message object
        msg = self.new_message.value
        cryption = 'Encryption:', self.enigma.encrypt(self.new_message.value)

        #create message object
        message = Message(msg,cryption,type)

        self.messages.controls.append(message)

        #clear text box
        self.new_message.value=" "

        #update (from user controls)
        self.updateRotor()
        self.update()
    def decryptMsg(self,e):
        # identify variables needed to make message object
        msg = self.new_message.value
        cryption = 'Decryption:', self.enigma.decrypt(self.new_message.value)

        #create message object
        message = Message(msg,cryption,type)

        self.messages.controls.append(message)

        #clear text box
        self.new_message.value=" "

        #update (from user controls)
        self.updateRotor()
        self.update()
        pass

    def updateRotor(self):
        self.r1.value = self.enigma.rotor1.counter
        self.r2.value = self.enigma.rotor2.counter
        self.r3.value = self.enigma.rotor3.counter

        self.update()

    def rotorReset(self,e):
        self.enigma.resetEnigma()
        self.updateRotor()
        self.update()

    def rotorEdit(self,e):
        if self.rotorTrackerEdit.visible ==False:
            self.rotorTrackerEdit.visible = True
            self.rotorTracker.visible = False
        else:
            self.rotorTrackerEdit.visible = False
            self.rotorTracker.visible = True
        self.update()

    def saveRotor(self,e):
        self.enigma.rotor1.setCounter(self.r1edit.value)
        self.enigma.rotor2.setCounter(self.r2edit.value)
        self.enigma.rotor3.setCounter(self.r3edit.value)
        self.updateRotor()
        self.update()

class Message(ft.UserControl):
    #msg = original message
    #cryption = en/decryption
    #ype = 0/1 encryption/decryption
    def __init__(self,msg,cryption,type):
        super().__init__()
        self.msg= msg
        self.cryption = cryption
        self.type=0

    def build(self):
        self.displayMsg= ft.Text(value=self.cryption, selectable=True)
        self.orginalMsg= ft.Text(value=('original:', self.msg), selectable=True)
        self.editBtn = ft.IconButton(ft.icons.SWITCH_ACCESS_SHORTCUT, on_click=self.switchView)

        self.displayView = ft.Row(controls=[self.displayMsg, ft.IconButton(ft.icons.SWITCH_ACCESS_SHORTCUT, on_click=self.switchView)])
        self.originalView = ft.Row(visible=False, controls=[self.orginalMsg, ft.IconButton(ft.icons.SWITCH_ACCESS_SHORTCUT, on_click=self.switchView)])

        return ft.Column(controls=[self.displayView, self.originalView])
    def switchView(self,e):
        if self.type ==0:
            self.displayView.visible= False
            self.originalView.visible= True
            self.type=1
        else:
            self.displayView.visible= True
            self.originalView.visible= False
            self.type=0
        self.update()








def main(page: ft.Page):

    title = ft.Text(value="Enigma Simulator", size="24")
    #page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.add(title)


    enigmaApp = EnigmaApp()
    page.add(enigmaApp)



ft.app(target=main)