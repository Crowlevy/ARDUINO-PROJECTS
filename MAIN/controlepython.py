import serial 
import speech_recognition as sp
import pyttsx3
import time
import threading
import queue
import pygame
import tkinter as tk

arduino=serial.Serial("COM7",9600, timeout=5)
recognizer=sp.Recognizer()
engine=pyttsx3.init()

verifica_led=[]

def musica():
    pygame.init()
    pygame.mixer_music.load("nobru.mp3")
    pygame.mixer_music.play()
    pygame.event.wait()

def manter_leds():
    arduino.write(b"A\n")
def controlar_leds(leds):
    arduino.write(f"leds {leds}\n".encode())
def apagar_luzes():
    arduino.write('D'.encode())
def falar(texto):
    engine.say(texto)
    print(texto)
    engine.runAndWait()
def reconhecer_fala():
    with sp.Microphone() as source:
        print("OUVINDO...")
        audio=recognizer.listen(source,timeout=5)
        if audio=='':
            falar("FALE ALGO")
        try:
            resposta=recognizer.recognize_google(audio,language="pt-BR").lower()
            print("VOCÊ DISSE:",resposta)
            return resposta
        except sp.UnknownValueError:
            print("não foi possível entender")
            return ""
thread_luzes=threading.Thread(target=manter_leds)
thread_luzes.daemon=True
thread_luzes.start()

def main():
    while True:
        tempo=time.time()
        consulta=reconhecer_fala()
        manter_leds()
        if "led" in consulta or "ligar" in consulta or "leds" in consulta:
            falar("QUAL LED DESEJA ACENDER")
            resposta=reconhecer_fala()
            controlar_leds(resposta)
            falar("LED LIGADO")
        elif "acender" in consulta:
            falar("QUER LIGAR TODOS?")
            resposta=reconhecer_fala()
            if resposta== 'sim':
                manter_leds()
        elif "apagar" in consulta:
            apagar_luzes()
        elif "otávio" in consulta:
            falar("ELE É VEADO")
            musica()
        elif "sair" in consulta:
            falar("FOI BOM TE CONHECER")
            break
        tempo_final=time.time()-tempo
        print(tempo_final)
main()