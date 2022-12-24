import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image
import os
import cv2
import pygame
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import random
import cv2
import mediapipe as mp
import pyautogui
import math
from enum import IntEnum
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from google.protobuf.json_format import MessageToDict
import screen_brightness_control as sbcontrol
from typing import Union, Tuple, Optional
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller
import mediapipe as mp
import math
import time
import cv2
import os
from unicodedata import name
from matplotlib.pyplot import text
import playsound
import speech_recognition as sr
from datetime import date
import time
import sys
import ctypes
import wikipedia
import datetime
from pynput.keyboard import Key, Controller
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from threading import Thread
import modulechatbot
from os.path import isfile, join
import datetime
import pyttsx3
from os import listdir
import pyautogui
import math
import cv2
import numpy as np
import time
import mediapipe as mp
import HandTrackingModule as htm






# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")
customtkinter.set_widget_scaling(1.2)




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("App CV2")
        self.geometry(f"{1100}x{580}")

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "test_images")

        # Add ảnh
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(
            image_path, "CustomTkinter_logo_single.png")), size=(40, 40))

        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(25, 25))

        self.guide_image = customtkinter.CTkImage(Image.open(os.path.join(
            image_path, "guide.png")), size=(25, 25))


        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.sidebar_frame, text="  Virual mouse", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40, border_spacing=10, text="Trang chủ",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, padx=20, pady=10)

        self.guide_button = customtkinter.CTkButton(self.sidebar_frame, text="Hướng dẫn sử dụng", command=self.create_toplevel)
        self.guide_button.grid(row=2, column=0, padx=20, pady=10)

        

        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(
            row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button

    
        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Nhập đóng góp của bạn vào đây")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(
            20, 0), pady=(20, 20), sticky="nsew")
    

        self.main_button_1 = customtkinter.CTkButton(
            master=self, fg_color="transparent", border_width=2, text="Xác nhận", text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(
            20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250, height=250)
        self.textbox.grid(row=0, column=1, padx=(
            20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=200, height=650)
        self.tabview.grid(row=0, column=2, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CHUỘT ẢO")
        self.tabview.add("BÀN PHÍM ẢO")
        self.tabview.add("CHỨC NĂNG KHÁC")
        self.tabview.tab("CHUỘT ẢO").grid_columnconfigure(
            0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("BÀN PHÍM ẢO").grid_columnconfigure(0, weight=1)

        ################### Tạo các button chức năng########

        self.virual_mouse = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Chuột ảo",
                                                    command=self.virual_mouse)

        self.virual_mouse.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.virual_mouse_beta = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Chuột ảo (Đang phát triển)",
                                                    command=self.virualmouse_beta)

        self.virual_mouse_beta.grid(row=7, column=0, padx=20, pady=(10, 10))

        self.ai_typing = customtkinter.CTkButton(self.tabview.tab("BÀN PHÍM ẢO"), text="Tập gõ chữ 10 ngón",
                                                    command=self.typingai)

        self.ai_typing.grid(row=2, column=0, padx=20, pady=(0, 10))


        self.zoom_anh1 = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Zoom ảnh",
                                                    command=self.zoom_anh)

        self.zoom_anh1.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.banphim_ao1 = customtkinter.CTkButton(self.tabview.tab("BÀN PHÍM ẢO"), text="Bàn phím ảo",
                                                    command=self.banphim_ao)

        self.banphim_ao1.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.paint_virual = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Vẽ trong không gian",
                                                    command=self.virual_paint)

        self.paint_virual.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.present_control = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Điều khiển thuyết trình",
                                                    command=self.control_present)

        self.present_control.grid(row=5, column=0, padx=20, pady=(10, 10))

        self.bot_chat = customtkinter.CTkButton(self.tabview.tab("CHỨC NĂNG KHÁC"), text="Trợ lý ảo",
                                                    command=self.chat_bot)

        self.bot_chat.grid(row=1, column=1, padx=80, pady=(10, 10))
        
        self.subway_play = customtkinter.CTkButton(self.tabview.tab("CHỨC NĂNG KHÁC"), text="Kết hợp chơi game để tập thể dục tại nhà (Đang bảo trì)",
                                                    command=self.play_subway)

        self.subway_play.grid(row=2, column=1, padx=80, pady=(10, 10))

        self.control_volume = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Tăng chỉnh âm lượng bằng cử chỉ",
                                                    command=self.volume_control)

        self.control_volume.grid(row=6, column=0, padx=80, pady=(10, 10))

###############################################################


        self.label_tab_2 = customtkinter.CTkLabel(
            self.tabview.tab("BÀN PHÍM ẢO"), text="Vui lòng hướng camera xuống bàn phím của bạn")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(
            20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(
            master=self.radiobutton_frame, text="Đánh giá:")
        self.label_radio_group.grid(
            row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, text="Tốt", value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, text="Khá", value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, text="Yếu", value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(
            row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(
            20, 10), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.switch_1 = customtkinter.CTkSwitch(
            master=self.checkbox_slider_frame, command=lambda: print("switch 1 toggle"))
        self.switch_1.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.switch_2 = customtkinter.CTkSwitch(
            master=self.checkbox_slider_frame)
        self.switch_2.grid(row=4, column=0, pady=(10, 20), padx=20, sticky="n")

        # # create slider and progressbar frame
        # self.slider_progressbar_frame = customtkinter.CTkFrame(
        #     self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(
        #     row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.progressbar_1 = customtkinter.CTkProgressBar(
        #     self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=1, column=0, padx=(
        #     20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_2 = customtkinter.CTkProgressBar(
        #     self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=2, column=0, padx=(
        #     20, 10), pady=(10, 10), sticky="ew")
        # self.slider_1 = customtkinter.CTkSlider(
        #     self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        # self.slider_1.grid(row=3, column=0, padx=(
        #     20, 10), pady=(10, 10), sticky="ew")
        # self.slider_2 = customtkinter.CTkSlider(
        #     self.slider_progressbar_frame, orientation="vertical")
        # self.slider_2.grid(row=0, column=1, rowspan=5, padx=(
        #     10, 10), pady=(10, 10), sticky="ns")
        # self.progressbar_3 = customtkinter.CTkProgressBar(
        #     self.slider_progressbar_frame, orientation="vertical")
        # self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(
        #     10, 20), pady=(10, 10), sticky="ns")

        # set default values
        self.checkbox_2.configure(state="disabled")
        self.switch_2.configure(state="disabled")
        self.checkbox_1.select()
        self.switch_1.select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("120%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()
        self.textbox.insert("1.0", "\nChúc bạn có \nmột trải nghiệm tuyệt vời cùng\nvới ứng dụng\ncủa chúng tôi.\nVà bây giờ hãy\ntrải nghiệm nó.")
        self.textbox.configure(state="disabled")

        self.select_frame_by_name("home")
        

    def select_frame_by_name(self, name):
        # set button color for selected button
        
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")

            

        self.guide_button.configure(fg_color=("gray75", "gray25") if name == "guide" else "transparent")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def user_feedback(self):

        self._user_input: Union[str, None] = None
        self._running: bool = False
        self._text = text

        self.title(title)
        self.lift()  # lift window on top
        self.attributes("-topmost", True)  # stay on top
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self._user_input = self._entry.get()
        self.grab_release()
        self.destroy()


    def home_button_event(self):
        
        self.select_frame_by_name("home")

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Nhập đóng góp của bạn vào đây")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(
            20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(
            master=self, fg_color="transparent", border_width=2, text="Xác nhận", text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(
            20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250, height=250)
        self.textbox.grid(row=0, column=1, padx=(
            20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=200)
        self.tabview.grid(row=0, column=2, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CHUỘT ẢO")
        self.tabview.add("BÀN PHÍM ẢO")
        self.tabview.add("CHỨC NĂNG KHÁC")
        self.tabview.tab("CHUỘT ẢO").grid_columnconfigure(
            0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("BÀN PHÍM ẢO").grid_columnconfigure(0, weight=1)

        ########################################## Tạo các button chức năng#################################

        self.virual_mouse = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Chuột ảo",
                                                    command=self.virual_mouse)

        self.virual_mouse.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.virual_mouse_beta = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Chuột ảo (Đang phát triển)",
                                                    command=self.virualmouse_beta)

        self.virual_mouse_beta.grid(row=7, column=0, padx=20, pady=(10, 10))

        self.ai_typing = customtkinter.CTkButton(self.tabview.tab("BÀN PHÍM ẢO"), text="Tập gõ chữ 10 ngón",
                                                    command=self.typingai)

        self.ai_typing.grid(row=2, column=0, padx=20, pady=(0, 10))

        self.zoom_anh1 = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Zoom ảnh",
                                                    command=self.zoom_anh)

        self.zoom_anh1.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.banphim_ao1 = customtkinter.CTkButton(self.tabview.tab("BÀN PHÍM ẢO"), text="Bàn phím ảo",
                                                    command=self.banphim_ao)

        self.banphim_ao1.grid(row=3, column=0, padx=20, pady=(10, 10))
        
        self.paint_virual = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Vẽ trong không gian",
                                                    command=self.virual_paint)

        self.paint_virual.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.present_control = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Điều khiển thuyết trình",
                                                    command=self.control_present)

        self.present_control.grid(row=5, column=0, padx=20, pady=(10, 10))

        self.bot_chat = customtkinter.CTkButton(self.tabview.tab("CHỨC NĂNG KHÁC"), text="Trợ lý ảo",
                                                    command=self.chat_bot)

        self.bot_chat.grid(row=1, column=1, padx=80, pady=(10, 10))

        self.subway_play = customtkinter.CTkButton(self.tabview.tab("CHỨC NĂNG KHÁC"), text="Kết hợp chơi game để tập thể dục tại nhà",
                                                    command=self.play_subway)

        self.subway_play.grid(row=2, column=1, padx=80, pady=(10, 10))

        self.control_volume = customtkinter.CTkButton(self.tabview.tab("CHUỘT ẢO"), text="Tăng chỉnh âm lượng bằng cử chỉ",
                                                    command=self.volume_control)

        self.control_volume.grid(row=6, column=0, padx=80, pady=(10, 10))


###########################################################




        self.label_tab_2 = customtkinter.CTkLabel(
            self.tabview.tab("BÀN PHÍM ẢO"), text="Vui lòng hướng camera xuống bàn phím của bạn")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create radiobutton frame
        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(
            20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(
            master=self.radiobutton_frame, text="Đánh giá:")
        self.label_radio_group.grid(
            row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, text="Tốt", value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, text="Khá", value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, text="Yếu", value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(
            row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(
            20, 10), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.switch_1 = customtkinter.CTkSwitch(
            master=self.checkbox_slider_frame, command=lambda: print("switch 1 toggle"))
        self.switch_1.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.switch_2 = customtkinter.CTkSwitch(
            master=self.checkbox_slider_frame)
        self.switch_2.grid(row=4, column=0, pady=(10, 20), padx=20, sticky="n")

        # create slider and progressbar frame
        # self.slider_progressbar_frame = customtkinter.CTkFrame(
        #     self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(
        #     row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.progressbar_1 = customtkinter.CTkProgressBar(
        #     self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=1, column=0, padx=(
        #     20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_2 = customtkinter.CTkProgressBar(
        #     self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=2, column=0, padx=(
        #     20, 10), pady=(10, 10), sticky="ew")
        # self.slider_1 = customtkinter.CTkSlider(
        #     self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        # self.slider_1.grid(row=3, column=0, padx=(
        #     20, 10), pady=(10, 10), sticky="ew")
        # self.slider_2 = customtkinter.CTkSlider(
        #     self.slider_progressbar_frame, orientation="vertical")
        # self.slider_2.grid(row=0, column=1, rowspan=5, padx=(
        #     10, 10), pady=(10, 10), sticky="ns")
        # self.progressbar_3 = customtkinter.CTkProgressBar(
        #     self.slider_progressbar_frame, orientation="vertical")
        # self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(
        #     10, 20), pady=(10, 10), sticky="ns")

        # set default values
        self.checkbox_2.configure(state="disabled")
        self.switch_2.configure(state="disabled")
        self.checkbox_1.select()
        self.switch_1.select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("120%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()
        self.textbox.insert("1.0", "\nChúc bạn có \nmột trải nghiệm tuyệt vời cùng\nvới ứng dụng\ncủa chúng tôi.\nVà bây giờ hãy\ntrải nghiệm nó.")
        self.textbox.configure(state="disabled")

        self.select_frame_by_name("home")


    # Def CHUỘT ẢO
    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("800x400")
        window.title("Hướng dẫn sử dụng")

        # create label on CTkToplevel window
        hdsd = customtkinter.CTkTextbox(window, width=250)
        hdsd.pack(side="top", fill="both", expand=True)

        hdsd.insert("0.0",  "Chuột ảo được điều khiển bằng cử chỉ giúp tương tác với máy tính của con người trở nên đơn giản bằng cách sử dụng Cử chỉ tay và Khẩu lệnh. Máy tính hầu như không yêu cầu tiếp xúc trực tiếp. Tất cả các thao tác i/o có thể được kiểm soát hầu như bằng cách sử dụng cử chỉ tay tĩnh và động cùng với trợ lý giọng nói. Dự án này sử dụng thuật toán Machine Learning và Computer Vision tiên tiến nhất để nhận dạng cử chỉ tay và lệnh thoại, hoạt động trơn tru mà không cần bất kỳ yêu cầu phần cứng bổ sung nào. Nó tận dụng các mô hình như CNN do MediaPipe triển khai chạy trên pybind11. Nó bao gồm hai mô-đun: Một mô-đun hoạt động trực tiếp trên tay bằng cách sử dụng tính năng Phát hiện tay của MediaPipe và mô-đun khác sử dụng Găng tay có màu đồng nhất bất kỳ. Hiện tại nó hoạt động trên nền tảng Windows, MacOs, Linux.\n Các chức năng chính thì được ghi trong phần tabview. Để xem chi tiết hơn vui lòng truy cập đường link sau\n'https://github.com/MinhNhat18092007/KHKT'")
        hdsd.configure(state="disabled")

    def virual_mouse(self):
        class handDetector():
            def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
                self.mode = mode
                self.maxHands = maxHands
                self.modelComplex = modelComplexity
                self.detectionCon = detectionCon
                self.trackCon = trackCon

                self.mpHands = mp.solutions.hands
                self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, 
                                                self.detectionCon, self.trackCon)

                self.mpDraw = mp.solutions.drawing_utils
                self.tipIds = [4, 8, 12, 16, 20]

            def findHands(self, img, draw=True):
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                self.results = self.hands.process(imgRGB)
                # print(results.multi_hand_landmarks)

                if self.results.multi_hand_landmarks:
                    for handLms in self.results.multi_hand_landmarks:
                        if draw:
                            self.mpDraw.draw_landmarks(img, handLms,
                                                    self.mpHands.HAND_CONNECTIONS)

                return img

            def findPosition(self, img, handNo=0, draw=True):
                xList = []
                yList = []
                bbox = []
                self.lmList = []
                if self.results.multi_hand_landmarks:
                    myHand = self.results.multi_hand_landmarks[handNo]
                    for id, lm in enumerate(myHand.landmark):
                        # print(id, lm)
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        xList.append(cx)
                        yList.append(cy)
                        # print(id, cx, cy)
                        self.lmList.append([id, cx, cy])
                        if draw:
                            cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

                    xmin, xmax = min(xList), max(xList)
                    ymin, ymax = min(yList), max(yList)
                    bbox = xmin, ymin, xmax, ymax

                    if draw:
                        cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                                    (0, 255, 0), 2)

                return self.lmList, bbox

            def fingersUp(self):
                fingers = []
                if len(self.lmList):
                    if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0]-1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                    for id in range(1,5):
                        if self.lmList[self.tipIds[id]][2]< self.lmList[self.tipIds[id]-2][2]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                else:
                    fingers = [0,0,0,0,0]
                return fingers

            def findDistance(self, p1, p2, img, draw=True,r=15, t=3):
                x1, y1 = self.lmList[p1][1:]
                x2, y2 = self.lmList[p2][1:]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                if draw:
                    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
                    cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
                    cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
                    cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
                length = math.hypot(x2 - x1, y2 - y1)

                return length, img, [x1, y1, x2, y2, cx, cy]


##########################
        wCam, hCam = 640, 480
        frameR = 100 # Frame Reduction
        smoothening = 7
        #########################

        pTime = 0
        plocX, plocY = 0, 0
        clocX, clocY = 0, 0

        cap = cv2.VideoCapture(0)
        cap.set(3, wCam)
        cap.set(4, hCam)
        detector = handDetector(maxHands=1)
        wScr, hScr = pyautogui.size()
        print(wScr, hScr)

        while True:
            # 1. Find hand Landmarks
            success, img = cap.read()
            img = detector.findHands(img)
            lmList, bbox = detector.findPosition(img)
            # 2. Get the tip of the index and middle fingers
            if len(lmList) != 0:
                x1, y1 = lmList[8][1:]
                x2, y2 = lmList[12][1:]
                # print(x1, y1, x2, y2)
            
            # 3. Check which fingers are up
            fingers = detector.fingersUp()
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
            (255, 0, 255), 2)
            # 4. Only Index Finger : Moving Mode
            if fingers[1] == 1 and fingers[2] == 0:
                # 5. Convert Coordinates
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                # 6. Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
            
                # 7. Move Mouse
                pyautogui.moveTo(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY
                
            # 8. Both Index and middle fingers are up : Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1:
                # 9. Find distance between fingers
                length, img, lineInfo = detector.findDistance(8, 12, img)
                print(length)
                # 10. Click mouse if distance short
                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]),
                    15, (0, 255, 0), cv2.FILLED)
                    
                    pyautogui.click()
            
            # 11. Frame Rate
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
            (255, 0, 0), 3)
            # 12. Display
            cv2.imshow("Image", img)
            if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
                break
        cap.release()  # giải phóng camera
        cv2.destroyAllWindows()  # thoát tất cả các cửa sổ


    def virualmouse_beta(self):
        pyautogui.FAILSAFE = False
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands

        frame = 100

        # Gesture Encodings

        class Gest(IntEnum):
            # Binary Encoded
            """
            Enum for mapping all hand gesture to binary number.
            """

            FIST = 0
            PINKY = 1
            RING = 2
            MID = 4
            LAST3 = 7
            INDEX = 8
            FIRST2 = 12
            LAST4 = 15
            THUMB = 16
            PALM = 31

            # Extra Mappings
            V_GEST = 33
            TWO_FINGER_CLOSED = 34
            PINCH_MAJOR = 35
            PINCH_MINOR = 36

        # Multi-handedness Labels

        class HLabel(IntEnum):
            MINOR = 0
            MAJOR = 1

        # Convert Mediapipe Landmarks to recognizable Gestures

        class HandRecog:
            """
            Convert Mediapipe Landmarks to recognizable Gestures.
            """

            def __init__(self, hand_label):
                """
                Xây dựng tất cả các thuộc tính cần thiết cho đối tượng HandRecog.

                Thông số
                ----------
                    ngón tay: int
                        Đại diện cho cử chỉ tương ứng với Enum 'Gest',
                        lưu trữ cử chỉ được tính toán cho khung hình hiện tại.
                    ori_gesture : int
                        Đại diện cho cử chỉ tương ứng với Enum 'Gest',
                        cửa hàng cử chỉ đang được sử dụng.
                    prev_gesture : int
                        Đại diện cho cử chỉ tương ứng với Enum 'Gest',
                        lưu trữ cử chỉ được tính cho khung hình trước đó.
                    frame_count : int
                        tổng số không. số khung hình kể từ khi 'ori_gesture' được cập nhật.
                    hand_result : Đối tượng
                        Các mốc thu được từ mediapipe.
                    nhãn_tay : int
                        Đại diện cho nhiều tay tương ứng với Enum 'HLabel'.
                """

                self.finger = 0
                self.ori_gesture = Gest.PALM
                self.prev_gesture = Gest.PALM
                self.frame_count = 0
                self.hand_result = None
                self.hand_label = hand_label

            def update_hand_result(self, hand_result):
                self.hand_result = hand_result

            def get_signed_dist(self, point):
                """
                returns signed euclidean distance between 'point'.

                Parameters
                ----------
                point : list contaning two elements of type list/tuple which represents 
                    landmark point.

                Returns
                -------
                float
                """

                sign = -1
                if self.hand_result.landmark[point[0]].y < self.hand_result.landmark[point[1]].y:
                    sign = 1
                dist = (self.hand_result.landmark[point[0]].x -
                        self.hand_result.landmark[point[1]].x) ** 2
                dist += (self.hand_result.landmark[point[0]].y -
                        self.hand_result.landmark[point[1]].y) ** 2
                dist = math.sqrt(dist)
                return dist * sign

            def get_dist(self, point):
                """
                returns euclidean distance between 'point'.

                Parameters
                ----------
                point : list contaning two elements of type list/tuple which represents 
                    landmark point.

                Returns
                -------
                float
                """
                dist = (self.hand_result.landmark[point[0]].x -
                        self.hand_result.landmark[point[1]].x) ** 2
                dist += (self.hand_result.landmark[point[0]].y -
                        self.hand_result.landmark[point[1]].y) ** 2
                dist = math.sqrt(dist)
                return dist

            def get_dz(self, point):
                """
                returns absolute difference on z-axis between 'point'.

                Parameters
                ----------
                point : list contaning two elements of type list/tuple which represents 
                    landmark point.

                Returns
                -------
                float
                """
                return abs(self.hand_result.landmark[point[0]].z - self.hand_result.landmark[point[1]].z)

            # Function to find Gesture Encoding using current finger_state.
            # Finger_state: 1 if finger is open, else 0
            def set_finger_state(self):
                """
                set 'finger' by computing ratio of distance between finger tip 
                , middle knuckle, base knuckle.

                Returns
                -------
                None
                """
                if self.hand_result == None:
                    return

                points = [[8, 5, 0], [12, 9, 0], [16, 13, 0], [20, 17, 0]]
                self.finger = 0
                self.finger = self.finger | 0  # thumb
                for idx, point in enumerate(points):

                    dist = self.get_signed_dist(point[:2])
                    dist2 = self.get_signed_dist(point[1:])

                    try:
                        ratio = round(dist / dist2, 1)
                    except:
                        ratio = round(dist1 / 0.01, 1)

                    self.finger = self.finger << 1
                    if ratio > 0.5:
                        self.finger = self.finger | 1

            # Xử lý biến động do tiếng ồn
            def get_gesture(self):
                """
                returns int representing gesture corresponding to Enum 'Gest'.
                sets 'frame_count', 'ori_gesture', 'prev_gesture', 
                handles fluctations due to noise.

                Returns
                -------
                int
                """
                if self.hand_result == None:
                    return Gest.PALM

                current_gesture = Gest.PALM
                if self.finger in [Gest.LAST3, Gest.LAST4] and self.get_dist([8, 4]) < 0.05:
                    if self.hand_label == HLabel.MINOR:
                        current_gesture = Gest.PINCH_MINOR
                    else:
                        current_gesture = Gest.PINCH_MAJOR

                elif Gest.FIRST2 == self.finger:
                    point = [[8, 12], [5, 9]]
                    dist1 = self.get_dist(point[0])
                    dist2 = self.get_dist(point[1])
                    ratio = dist1 / dist2
                    if ratio > 1.7:
                        current_gesture = Gest.V_GEST
                    else:
                        if self.get_dz([8, 12]) < 0.1:
                            current_gesture = Gest.TWO_FINGER_CLOSED
                        else:
                            current_gesture = Gest.MID

                else:
                    current_gesture = self.finger

                if current_gesture == self.prev_gesture:
                    self.frame_count += 1
                else:
                    self.frame_count = 0

                self.prev_gesture = current_gesture

                if self.frame_count > 4:
                    self.ori_gesture = current_gesture
                return self.ori_gesture

        # Executes commands according to detected gestures

        class Controller:
            """
            Thực hiện các lệnh theo cử chỉ được phát hiện.

            Thuộc tính
            ----------
            tx_old : int
                tọa độ x vị trí chuột trước đó
            ty_old : int
                vị trí chuột trước tọa độ y
            cờ: bool
                đúng nếu cử chỉ V được phát hiện
            lấy cờ : bool
                đúng nếu cử chỉ FIST được phát hiện
            pinchmajorflag : bool
                true nếu cử chỉ PINCH được phát hiện thông qua bàn tay CHÍNH,
                trên trục x 'Controller.changesystembrightness',
                trên trục y 'Controller.changesystemvolume'.
            pinchminorflag : bool
                true nếu cử chỉ PINCH được phát hiện thông qua tay MINOR,
                trên trục x 'Controller.scrollHorizontal',
                trên trục y 'Controller.scrollVertical'.
            pinchstartxcoord : int
                tọa độ x của mốc tay khi bắt đầu thao tác chụm.
            pinchstartycoord : int
                tọa độ y của mốc tay khi bắt đầu thao tác chụm.
            pinchdirectionflag : bool
                đúng nếu chuyển động cử chỉ véo dọc theo trục x,
                mặt khác sai
            prevpinchlv : int
                các cửa hàng được lượng tử hóa phóng đại của sự dịch chuyển cử chỉ chụm trước đó, từ
                điểm xuất phát
            nhúmlv : int
                các cửa hàng được lượng tử hóa phóng đại của sự dịch chuyển cử chỉ véo, từ
                điểm xuất phát
            số lượng khung hình: int
                số cửa hàng số khung hình kể từ khi 'pinchlv' được cập nhật.
            prev_hand : tuple
                lưu trữ tọa độ (x, y) của bàn tay trong khung trước đó.
            pinch_threshold : thả nổi
                kích thước bước để lượng tử hóa 'pinchlv'.
            """

            tx_old = 0
            ty_old = 0
            trial = True
            flag = False
            grabflag = False
            pinchmajorflag = False
            pinchminorflag = False
            pinchstartxcoord = None
            pinchstartycoord = None
            pinchdirectionflag = None
            prevpinchlv = 0
            pinchlv = 0
            framecount = 0
            prev_hand = None
            pinch_threshold = 0.3

            def getpinchylv(hand_result):
                """trả về khoảng cách giữa tọa độ y bắt đầu nhúm và vị trí tay hiện tại tọa độ y."""
                dist = round((Controller.pinchstartycoord -
                            hand_result.landmark[8].y) * 10, 1)
                return dist

            def getpinchxlv(hand_result):
                """trả về khoảng cách giữa nhúm bắt đầu x tọa độ và vị trí tay x tọa độ hiện tại."""
                dist = round(
                    (hand_result.landmark[8].x - Controller.pinchstartxcoord) * 10, 1)
                return dist

            def changesystembrightness():
                """sets system brightness based on 'Controller.pinchlv'."""
                currentBrightnessLv = sbcontrol.get_brightness(display=0) / 100.0
                currentBrightnessLv += Controller.pinchlv / 50.0
                if currentBrightnessLv > 1.0:
                    currentBrightnessLv = 1.0
                elif currentBrightnessLv < 0.0:
                    currentBrightnessLv = 0.0
                sbcontrol.fade_brightness(
                    int(100 * currentBrightnessLv), start=sbcontrol.get_brightness(display=0))

            def changesystemvolume():
                """sets system volume based on 'Controller.pinchlv'."""
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                currentVolumeLv = volume.GetMasterVolumeLevelScalar()
                currentVolumeLv += Controller.pinchlv / 50.0
                if currentVolumeLv > 1.0:
                    currentVolumeLv = 1.0
                elif currentVolumeLv < 0.0:
                    currentVolumeLv = 0.0
                volume.SetMasterVolumeLevelScalar(currentVolumeLv, None)

            def scrollVertical():
                """scrolls on screen vertically."""
                pyautogui.scroll(120 if Controller.pinchlv > 0.0 else -120)

            def scrollHorizontal():
                """scrolls on screen horizontally."""
                pyautogui.keyDown('shift')
                pyautogui.keyDown('ctrl')
                pyautogui.scroll(-120 if Controller.pinchlv > 0.0 else 120)
                pyautogui.keyUp('ctrl')
                pyautogui.keyUp('shift')

            # Xác định vị trí Bàn tay để có được Vị trí con trỏ
            # Ổn định con trỏ bằng cách giảm chấn

            def get_position(hand_result):
                """
                trả về tọa độ của vị trí tay hiện tại.

                Xác định vị trí tay để có được vị trí con trỏ cũng ổn định con trỏ bằng cách
                làm giảm chuyển động giật của tay.

                Returns
                -------
                tuple(float, float)
                """

                point = 9
                position = [hand_result.landmark[point].x,
                            hand_result.landmark[point].y]
                sx, sy = pyautogui.size()
                x_old, y_old = pyautogui.position()
                x = int(position[0] * sx)
                y = int(position[1] * sy)
                if Controller.prev_hand is None:
                    Controller.prev_hand = x, y
                delta_x = x - Controller.prev_hand[0]
                delta_y = y - Controller.prev_hand[1]

                distsq = delta_x ** 2 + delta_y ** 2
                ratio = 1
                Controller.prev_hand = [x, y]

                if distsq <= 25:
                    ratio = 0
                elif distsq <= 900:
                    ratio = 0.07 * (distsq ** (1 / 2))
                else:
                    ratio = 2.1
                x, y = x_old + delta_x * ratio, y_old + delta_y * ratio
                return (x, y)

            def pinch_control_init(hand_result):
                """Initializes attributes for pinch gesture."""
                Controller.pinchstartxcoord = hand_result.landmark[8].x
                Controller.pinchstartycoord = hand_result.landmark[8].y
                Controller.pinchlv = 0
                Controller.prevpinchlv = 0
                Controller.framecount = 0

            # Hold final position for 5 frames to change status
            def pinch_control(hand_result, controlHorizontal, controlVertical):
                """
                gọi 'controlHorizontal' hoặc 'controlVertical' dựa trên các cờ nhúm,
                'framecount' và đặt 'pinchlv'.

                Thông số
                ----------
                hand_result : Đối tượng
                    Các mốc thu được từ mediapipe.
                controlHorizontal : chức năng gọi lại được liên kết với chiều ngang
                    cử chỉ nhéo.
                controlVertical : chức năng gọi lại được liên kết với dọc
                    cử chỉ nhéo.ack function assosiated with vertical
                    pinch gesture. 

                Returns
                -------
                None
                """
                if Controller.framecount == 5:
                    Controller.framecount = 0
                    Controller.pinchlv = Controller.prevpinchlv

                    if Controller.pinchdirectionflag == True:
                        controlHorizontal()  # x

                    elif Controller.pinchdirectionflag == False:
                        controlVertical()  # y

                lvx = Controller.getpinchxlv(hand_result)
                lvy = Controller.getpinchylv(hand_result)

                if abs(lvy) > abs(lvx) and abs(lvy) > Controller.pinch_threshold:
                    Controller.pinchdirectionflag = False
                    if abs(Controller.prevpinchlv - lvy) < Controller.pinch_threshold:
                        Controller.framecount += 1
                    else:
                        Controller.prevpinchlv = lvy
                        Controller.framecount = 0

                elif abs(lvx) > Controller.pinch_threshold:
                    Controller.pinchdirectionflag = True
                    if abs(Controller.prevpinchlv - lvx) < Controller.pinch_threshold:
                        Controller.framecount += 1
                    else:
                        Controller.prevpinchlv = lvx
                        Controller.framecount = 0

            def handle_controls(gesture, hand_result):
                """Thực hiện tất cả các chức năng cử chỉ."""
                x, y = None, None
                if gesture != Gest.PALM:
                    x, y = Controller.get_position(hand_result)

                # flag reset
                if gesture != Gest.FIST and Controller.grabflag:
                    Controller.grabflag = False
                    pyautogui.mouseUp(button="left")

                if gesture != Gest.PINCH_MAJOR and Controller.pinchmajorflag:
                    Controller.pinchmajorflag = False

                if gesture != Gest.PINCH_MINOR and Controller.pinchminorflag:
                    Controller.pinchminorflag = False

                # implementation
                if gesture == Gest.V_GEST:
                    Controller.flag = True
                    pyautogui.moveTo(x, y, duration=0.1)

                elif gesture == Gest.FIST:
                    if not Controller.grabflag:
                        Controller.grabflag = True
                        pyautogui.mouseDown(button="left")
                    pyautogui.moveTo(x, y, duration=0.1)

                elif gesture == Gest.MID and Controller.flag:
                    pyautogui.click()
                    Controller.flag = False

                elif gesture == Gest.INDEX and Controller.flag:
                    pyautogui.click(button='right')
                    Controller.flag = False

                elif gesture == Gest.TWO_FINGER_CLOSED and Controller.flag:
                    pyautogui.doubleClick()
                    Controller.flag = False

                elif gesture == Gest.PINCH_MINOR:
                    if Controller.pinchminorflag == False:
                        Controller.pinch_control_init(hand_result)
                        Controller.pinchminorflag = True
                    Controller.pinch_control(
                        hand_result, Controller.scrollHorizontal, Controller.scrollVertical)

                elif gesture == Gest.PINCH_MAJOR:
                    if Controller.pinchmajorflag == False:
                        Controller.pinch_control_init(hand_result)
                        Controller.pinchmajorflag = True
                    Controller.pinch_control(
                        hand_result, Controller.changesystembrightness, Controller.changesystemvolume)

        '''
        ----------------------------------------  Main Class  ----------------------------------------
            Entry point of Gesture Controller
        '''

        class GestureController:
            """
            Handles camera, obtain landmarks from mediapipe, entry point
            for whole program.

            Attributes
            ----------
            gc_mode : int
                indicates weather gesture controller is running or not,
                1 if running, otherwise 0.
            cap : Object
                object obtained from cv2, for capturing video frame.
            CAM_HEIGHT : int
                highet in pixels of obtained frame from camera.
            CAM_WIDTH : int
                width in pixels of obtained frame from camera.
            hr_major : Object of 'HandRecog'
                object representing major hand.
            hr_minor : Object of 'HandRecog'
                object representing minor hand.
            dom_hand : bool
                True if right hand is domaniant hand, otherwise False.
                default True.
            """
            gc_mode = 0
            cap = None
            CAM_HEIGHT = None
            CAM_WIDTH = None
            hr_major = None  # Right Hand by default
            hr_minor = None  # Left hand by default
            dom_hand = True

            def __init__(self):
                """Initilaizes attributes."""
                GestureController.gc_mode = 1
                GestureController.cap = cv2.VideoCapture(0)
                GestureController.CAM_HEIGHT = GestureController.cap.get(
                    cv2.CAP_PROP_FRAME_HEIGHT)
                GestureController.CAM_WIDTH = GestureController.cap.get(
                    cv2.CAP_PROP_FRAME_WIDTH)

            def classify_hands(results):
                """
                sets 'hr_major', 'hr_minor' based on classification(left, right) of 
                hand obtained from mediapipe, uses 'dom_hand' to decide major and
                minor hand.
                """
                left, right = None, None
                try:
                    handedness_dict = MessageToDict(results.multi_handedness[0])
                    if handedness_dict['classification'][0]['label'] == 'Right':
                        right = results.multi_hand_landmarks[0]
                    else:
                        left = results.multi_hand_landmarks[0]
                except:
                    pass

                try:
                    handedness_dict = MessageToDict(results.multi_handedness[1])
                    if handedness_dict['classification'][0]['label'] == 'Right':
                        right = results.multi_hand_landmarks[1]
                    else:
                        left = results.multi_hand_landmarks[1]
                except:
                    pass

                if GestureController.dom_hand == True:
                    GestureController.hr_major = right
                    GestureController.hr_minor = left
                else:
                    GestureController.hr_major = left
                    GestureController.hr_minor = right

            def start(self):
                """
                Entry point of whole programm, caputres video frame and passes, obtains
                landmark from mediapipe and passes it to 'handmajor' and 'handminor' for
                controlling.
                """

                handmajor = HandRecog(HLabel.MAJOR)
                handminor = HandRecog(HLabel.MINOR)

                with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.9, min_tracking_confidence=0.9) as hands:
                    while GestureController.cap.isOpened() and GestureController.gc_mode:
                        success, image = GestureController.cap.read()

                        if not success:
                            print("Ignoring empty camera frame.")
                            continue

                        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                        image.flags.writeable = False
                        results = hands.process(image)

                        image.flags.writeable = True
                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                        if results.multi_hand_landmarks:
                            GestureController.classify_hands(results)
                            handmajor.update_hand_result(
                                GestureController.hr_major)
                            handminor.update_hand_result(
                                GestureController.hr_minor)

                            handmajor.set_finger_state()
                            handminor.set_finger_state()
                            gest_name = handminor.get_gesture()

                            if gest_name == Gest.PINCH_MINOR:
                                Controller.handle_controls(
                                    gest_name, handminor.hand_result)
                            else:
                                gest_name = handmajor.get_gesture()
                                Controller.handle_controls(
                                    gest_name, handmajor.hand_result)

                            for hand_landmarks in results.multi_hand_landmarks:
                                mp_drawing.draw_landmarks(
                                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                        else:
                            Controller.prev_hand = None
                        cv2.imshow('Gesture Controller', image)
                        if cv2.waitKey(1) == ord("q"):
                            break
                GestureController.cap.release()
                cv2.destroyAllWindows()

        gc1 = GestureController()
        gc1.start()

    def typingai(self):
        import cv2
        import pygame
        import numpy as np
        from cvzone.HandTrackingModule import HandDetector
        import random

        width, height = 1280, 720
        cap = cv2.VideoCapture(1)
        cap.set(3, 1280)
        cap.set(4, 720)

        scale = 4

        widthKeyboard = 275*scale
        heightKeyboard = 72*scale

        initialWarpPoints = [[489, 291], [1111, 277], [493, 483], [1149, 453]]
        pts1 = np.float32(initialWarpPoints)
        pts2 = np.float32([[0, 0], [widthKeyboard, 0], [0, heightKeyboard], [widthKeyboard, heightKeyboard]])


        #Variables
        isFirstFrame = True
        currentKey = 'y'
        currentKeyPressed = False
        scoreCorrect = 0
        scoreWrong = 0
        delayCount = 0


        #Bouding box of each keyh and the correct figner
        keyLocations = {
            # First Row
            'q': [28, 0, 16, 15, 'left_pinky'],
            'w': [47, 0, 16, 15, 'left_ring'],
            'e': [67, 0, 16, 15, 'left_middle'],
            'r': [86, 0, 16, 15, 'left_index'],
            't': [105, 0, 16, 15, 'left_index'],
            'y': [124, 0, 16, 15, 'right_index'],
            'u': [143, 0, 16, 15, 'right_index'],
            'i': [162, 0, 16, 15, 'right_middle'],
            'o': [182, 0, 16, 15, 'right_ring'],
            'p': [201, 0, 16, 15, 'right_pinky'],
            # Second Row
            'a': [32, 19, 16, 15, 'left_pinky'],
            's': [52, 19, 16, 15, 'left_ring'],
            'd': [71, 19, 16, 15, 'left_middle'],
            'f': [90, 19, 16, 15, 'left_index'],
            'g': [109, 19, 16, 15, 'left_index'],
            'h': [129, 19, 16, 15, 'right_index'],
            'j': [148, 19, 16, 15, 'right_index'],
            'k': [167, 19, 16, 15, 'right_middle'],
            'l': [187, 19, 16, 15, 'right_ring'],
            # Third Row
            'z': [42, 37, 16, 16, 'left_pinky'],
            'x': [62, 37, 16, 16, 'left_ring'],
            'c': [81, 37, 16, 16, 'left_middle'],
            'v': [100, 37, 16, 16, 'left_index'],
            'b': [119, 37, 16, 16, 'left_index'],
            'n': [138, 37, 16, 16, 'right_index'],
            'm': [158, 37, 16, 16, 'right_index']
        }
        pygame.init()

        #Create Window/Display
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Daỵ gõ chữ 10 ngón")

        #Initialize Clock for FPS
        fps = 30
        clock = pygame.time.Clock()

        # Creating a dic for positions of the keys in the backgroudn image
        # Creating a dic for positions of the keys in the background image
        rows = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
        rowsStart = [192, 214, 235]
        keyLocationsBackground = {}
        for i, row in enumerate(rows):
            for j, alphabet in enumerate(row):
                keyLocationsBackground[alphabet] = [rowsStart[i] + 76 * j, 364 + 74 * i, 62, 62]

        detector = HandDetector(detectionCon=0.4, maxHands=2)

        fingerIds = {
            "8": "index",
            "12": "middle",
            "16": "ring",
            "20": "pinky"
        }

        # warp point to find the correct locations of the finger tips on the warped keyboard image
        def warpPoint(p, matrix):
            px = (matrix[0][0] * p[0] + matrix[0][1] * p[1] + matrix[0][2]) / (
                (matrix[2][0] * p[0] + matrix[2][1] * p[1] + matrix[2][2]))
            py = (matrix[1][0] * p[0] + matrix[1][1] * p[1] + matrix[1][2]) / (
                (matrix[2][0] * p[0] + matrix[2][1] * p[1] + matrix[2][2]))
            return int(px), int(py)

        # check if finger tip point is in the key bounding box
        def checkInside(point, x, y, w, h):
            return x < point[0] < x + w and y < point[1] < y + h
        

        while True:

            imgBackground = cv2.imread("Background.png")
            currentKeyPressed = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    myKey = getattr(pygame, "K_{}".format(currentKey))
                    if event.key == myKey:
                        print(f'{currentKey} key was pressed')
                        currentKeyPressed = True
                    # else:
                    #     currentKeyPressed = False







            success, img = cap.read()
            if isFirstFrame: cv2.imwrite("Sample.jpg", img)
            




            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgWarp = cv2.warpPerspective(img, matrix, (widthKeyboard, heightKeyboard))
            imgWarp = cv2.flip(imgWarp, -1)
            hands, img = detector.findHands(img)
            for point in initialWarpPoints:
                cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)

            if hands:
                if len(hands) == 2:
                    cv2.putText(imgBackground, "Detection: SOlid", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                else:
                    cv2.putText(imgBackground, "Detection: Weak", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)


                for hand in hands:
                    handType = hand['type'].lower()
                    

                    if currentKeyPressed and delayCount==0:

                        #get the bbox info of the correct key to check the finger loction
                        key = currentKey
                        value = keyLocations[key]
                        x,y,w,h = value[0]*scale, value[1]*scale, value[2]*scale, value[3]*scale
                        correctFinger = value[4]
                        cv2.rectangle(imgWarp, (x,y), (x+w, y + h), (50, 200, 50), cv2.FILLED)
                        # whick finger is presssing the y key

                        for id,finger in fingerIds.items():
                            point = hand["lmList"][int(id)]
                            px, py = warpPoint(point, matrix)
                            px = widthKeyboard - px
                            py = heightKeyboard - py
                            cv2.circle(imgWarp, (px, py), 5, (0, 0, 255), cv2.FILLED)
                            if checkInside((px, py), x, y, w, h):
                                print(handType + "_" + finger, correctFinger)
                                if handType + "_" + finger == correctFinger:
                                    print("Correct")
                                    scoreCorrect +=1
                                    currentKey = list(keyLocations)[random.randint(0, 25)]
                                    color = (0, 255, 0)
                                else:
                                    print("wrong")
                                    scoreWrong +=1
                                    color = (0, 0, 255)
                                delayCount = 1


                                if currentKeyPressed:
                                    valueCurrent = keyLocationsBackground[currentKey]
                                    x, y, w, h = valueCurrent
                                    cv2.rectangle(imgBackground, (x, y), (x + w, y + h), color, cv2.FILLED)
                                    cv2.rectangle(imgBackground, (505, 129), (505 + 285, 129 + 177), color, cv2.FILLED)





            #Draw the bouding bbox on the warp image
            for key, value in keyLocations.items():
                x,y,w,h = value[0]*scale, value[1]*scale, value[2]*scale, value[3]*scale
                cv2.rectangle(imgWarp, (x, y), (x + w, y + h), (255, 0, 255), 2)


            cv2.imshow("Minh Nhat", img)
            cv2.imshow("B2W1234", imgWarp)

            #Draw on the backgrund imgae
            

            #Draw all the alphabets on the background image
            for key, val in keyLocationsBackground.items():
                x, y, w, h = val
                cv2.putText(imgBackground, key, (x + 15, y + 45), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)

            cv2.putText(imgBackground, currentKey, (590, 260), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 20)


            cv2.putText(imgBackground, str(scoreCorrect), (185, 245), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)
            cv2.putText(imgBackground, str(scoreWrong), (1035, 245), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)

            if delayCount != 0:
                delayCount +=1
                if delayCount >=5:
                    delayCount = 0



            # OpenCV  Display
            imgRGB = cv2.cvtColor(imgBackground, cv2.COLOR_BGR2RGB)
            imgRGB = np.rot90(imgRGB)
            frame = pygame.surfarray.make_surface(imgRGB).convert()
            frame = pygame.transform.flip(frame, True, False)
            window.blit(frame, (0, 0))


            #Update Display
            pygame.display.update()
            #SETFPS
            clock.tick(fps)

            if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
                break
        cap.release()  # giải phóng camera
        cv2.destroyAllWindows()  # thoát tất cả các cửa sổ

    def zoom_anh(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 1280)
        cap.set(4, 720)

        detector = HandDetector(detectionCon=0.8)
        startDist = None
        scale = 0
        cx, cy = 500, 500   

        while True:
            success, img = cap.read()
            hands, img = detector.findHands(img)
            img1 = cv2.imread("anhtest.png")

            if len(hands) == 2:
                
                #print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1]))
                if detector.fingersUp(hands[0]) == [1,1,0,0,0] and \
                    detector.fingersUp(hands[1]) == [1,1,0,0,0]:
                    # print("Zoom Gesture")
                    lmList1 = hands[0]["lmList"]
                    lmList2 = hands[1]["lmList"]

                    if startDist is None:
                        length, info, img = detector.findDistance(lmList1[8][:2], lmList2[8][:2], img)
                        print(length)
                        startDist = length
                    length, info, img = detector.findDistance(lmList1[8][:2], lmList2[8][:2], img) 
                    scale = int((length - startDist)//2)
                    cx, cy = info[4:]
                    print(scale)
            else:
                startDist = None
            try:
                h1, w1, _ = img1.shape
                newH, newW = ((h1 + scale)//2)*2, ((w1 + scale)//2)*2
                img1 = cv2.resize(img1, (newW, newH))

                img[cy - newH//2 : cy + newH//2, cx - newW//2 : cx + newW//2] = img1
            except:
                pass

            cv2.imshow("mnaht", img)
            if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
                break
        cap.release()  # giải phóng camera
        cv2.destroyAllWindows()  # thoát tất cả các cửa sổ

    def banphim_ao(self):


        class HandDetector:
            """
            Finds Hands using the mediapipe library. Exports the landmarks
            in pixel format. Adds extra functionalities like finding how
            many fingers are up or the distance between two fingers. Also
            provides bounding box info of the hand found.
            """

            def __init__(self, mode=False, maxHands=2, detectionCon=0.5, minTrackCon=0.5):
                """
                :param mode: In static mode, detection is done on each image: slower
                :param maxHands: Maximum number of hands to detect
                :param detectionCon: Minimum Detection Confidence Threshold
                :param minTrackCon: Minimum Tracking Confidence Threshold
                """
                self.mode = mode
                self.maxHands = maxHands
                self.detectionCon = detectionCon
                self.minTrackCon = minTrackCon

                self.mpHands = mp.solutions.hands
                self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                                self.detectionCon, self.minTrackCon)
                self.mpDraw = mp.solutions.drawing_utils
                self.tipIds = [4, 8, 12, 16, 20]
                self.fingers = []
                self.lmList = []

            def findHands(self, img, draw=True):
                """
                Finds hands in a BGR image.
                :param img: Image to find the hands in.
                :param draw: Flag to draw the output on the image.
                :return: Image with or without drawings
                """
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                self.results = self.hands.process(imgRGB)

                if self.results.multi_hand_landmarks:
                    for handLms in self.results.multi_hand_landmarks:
                        if draw:
                            self.mpDraw.draw_landmarks(img, handLms,
                                                    self.mpHands.HAND_CONNECTIONS)
                return img

            def findPosition(self, img, handNo=0, draw=True):
                """
                Finds landmarks of a single hand and puts them in a list
                in pixel format. Also finds the bounding box around the hand.

                :param img: main image to find hand in
                :param handNo: hand id if more than one hand detected
                :param draw: Flag to draw the output on the image.
                :return: list of landmarks in pixel format; bounding box
                """

                xList = []
                yList = []
                bbox = []
                bboxInfo =[]
                self.lmList = []
                if self.results.multi_hand_landmarks:
                    myHand = self.results.multi_hand_landmarks[handNo]
                    for id, lm in enumerate(myHand.landmark):
                        h, w, c = img.shape
                        px, py = int(lm.x * w), int(lm.y * h)
                        xList.append(px)
                        yList.append(py)
                        self.lmList.append([px, py])
                        if draw:
                            cv2.circle(img, (px, py), 5, (255, 0, 255), cv2.FILLED)
                    xmin, xmax = min(xList), max(xList)
                    ymin, ymax = min(yList), max(yList)
                    boxW, boxH = xmax - xmin, ymax - ymin
                    bbox = xmin, ymin, boxW, boxH
                    cx, cy = bbox[0] + (bbox[2] // 2), \
                            bbox[1] + (bbox[3] // 2)
                    bboxInfo = {"id": id, "bbox": bbox,"center": (cx, cy)}

                    if draw:
                        cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                                    (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),
                                    (0, 255, 0), 2)

                return self.lmList, bboxInfo

            def fingersUp(self):
                """
                Finds how many fingers are open and returns in a list.
                Considers left and right hands separately
                :return: List of which fingers are up
                """
                if self.results.multi_hand_landmarks:
                    myHandType = self.handType()
                    fingers = []
                    # Thumb
                    if myHandType == "Right":
                        if self.lmList[self.tipIds[0]][0] > self.lmList[self.tipIds[0] - 1][0]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                    else:
                        if self.lmList[self.tipIds[0]][0] < self.lmList[self.tipIds[0] - 1][0]:
                            fingers.append(1)
                        else:
                            fingers.append(0)

                    # 4 Fingers
                    for id in range(1, 5):
                        if self.lmList[self.tipIds[id]][1] < self.lmList[self.tipIds[id] - 2][1]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                return fingers

            def findDistance(self, p1, p2, img, draw=True):
                """
                Find the distance between two landmarks based on their
                index numbers.
                :param p1: Point1 - Index of Landmark 1.
                :param p2: Point2 - Index of Landmark 2.
                :param img: Image to draw on.
                :param draw: Flag to draw the output on the image.
                :return: Distance between the points
                        Image with output drawn
                        Line information
                """

                if self.results.multi_hand_landmarks:
                    x1, y1 = self.lmList[p1][0], self.lmList[p1][1]
                    x2, y2 = self.lmList[p2][0], self.lmList[p2][1]
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                    if draw:
                        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
                        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

                    length = math.hypot(x2 - x1, y2 - y1)
                    return length, img, [x1, y1, x2, y2, cx, cy]

            def handType(self):
                """
                Checks if the hand is left or right
                :return: "Right" or "Left"
                """
                if self.results.multi_hand_landmarks:
                    if self.lmList[17][0] < self.lmList[5][0]:
                        return "Right"
                    else:
                        return "Left"

        cap = cv2.VideoCapture(0)
        cap.set(3, 1280)
        cap.set(4, 720)

        detector = HandDetector(detectionCon=int(0.8))
        keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
                ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]
        finalText = ""

        keyboard = Controller()


        def drawAll(img, buttonList):
            for button in buttonList:
                x, y = button.pos
                w, h = button.size
                cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                                20, rt=0)
                cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
            return img


        #
        # def drawAll(img, buttonList):
        #     imgNew = np.zeros_like(img, np.uint8)
        #     for button in buttonList:
        #         x, y = button.pos
        #         cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
        #                           20, rt=0)
        #         cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
        #                       (255, 0, 255), cv2.FILLED)
        #         cv2.putText(imgNew, button.text, (x + 40, y + 60),
        #                     cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
        #
        #     out = img.copy()
        #     alpha = 0.5
        #     mask = imgNew.astype(bool)
        #     print(mask.shape)
        #     out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
        #     return out


        class Button():
            def __init__(self, pos, text, size=[85, 85]):
                self.pos = pos
                self.size = size
                self.text = text


        buttonList = []
        for i in range(len(keys)):
            for j, key in enumerate(keys[i]):
                buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList, bboxInfo = detector.findPosition(img)
            img = drawAll(img, buttonList)

            if lmList:
                for button in buttonList:
                    x, y = button.pos
                    w, h = button.size

                    if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                        cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65),
                                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        l, _, _ = detector.findDistance(8, 12, img, draw=False)
                        print(l)

                        ## when clicked
                        if l < 43:
                            keyboard.press(button.text)
                            cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                            cv2.putText(img, button.text, (x + 20, y + 65),
                                        cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                            finalText += button.text
                            sleep(0.15)

            cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
            cv2.putText(img, finalText, (60, 430),
                        cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

            cv2.imshow("Image", img)
            
            if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
                break
            # cap.release()  # giải phóng camera
            # cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
            
    def virual_paint(self):
        class handDetector():
            def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
                self.mode = mode
                self.maxHands = maxHands
                self.detectionCon = detectionCon
                self.trackCon = trackCon

                self.mpHands = mp.solutions.hands
                self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                                self.detectionCon, self.trackCon)
                self.mpDraw = mp.solutions.drawing_utils
                self.tipIds = [4, 8, 12, 16, 20]

            def findHands(self, img, draw=True):
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                self.results = self.hands.process(imgRGB)
                # print(results.multi_hand_landmarks)

                if self.results.multi_hand_landmarks:
                    for handLms in self.results.multi_hand_landmarks:
                        if draw:
                            self.mpDraw.draw_landmarks(img, handLms,
                                                    self.mpHands.HAND_CONNECTIONS)

                return img

            def findPosition(self, img, handNo=0, draw=True):
                xList = []
                yList = []
                bbox = []
                self.lmList = []
                if self.results.multi_hand_landmarks:
                    myHand = self.results.multi_hand_landmarks[handNo]
                    for id, lm in enumerate(myHand.landmark):
                        # print(id, lm)
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        xList.append(cx)
                        yList.append(cy)
                        # print(id, cx, cy)
                        self.lmList.append([id, cx, cy])
                        if draw:
                            cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

                    xmin, xmax = min(xList), max(xList)
                    ymin, ymax = min(yList), max(yList)
                    bbox = xmin, ymin, xmax, ymax

                    if draw:
                        cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                                    (0, 255, 0), 2)

                return self.lmList, bbox

            def fingersUp(self):
                fingers = []
                # Thumb
                if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Fingers
                for id in range(1, 5):

                    if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # totalFingers = fingers.count(1)

                return fingers

            def findDistance(self, p1, p2, img, draw=True,r=15, t=3):
                x1, y1 = self.lmList[p1][1:]
                x2, y2 = self.lmList[p2][1:]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                if draw:
                    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
                    cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
                    cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
                    cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
                length = math.hypot(x2 - x1, y2 - y1)

                return length, img, [x1, y1, x2, y2, cx, cy]

                
        ##############
        brushThickness = 15
        eraserThickness = 100

        folderPath = "Header"
        myList = os.listdir(folderPath)
        print(myList)
        overlayList = []

        for imPath in myList:
            image = cv2.imread(f'{folderPath}/{imPath}')
            overlayList.append(image)

        print(len(overlayList))
        header = overlayList[0]
        drawColor = (255, 0, 255)



        cap = cv2.VideoCapture(0)
        cap.set(3, 1280)
        cap.set(4, 720)

        detector = handDetector(detectionCon=int(0.65))

        xp, yp = 0, 0

        tipIds = [4, 8, 12, 16, 20]
        imgCanvas = np.zeros((720, 1280, 3), np.uint8)

        while True:

            # 1. Import image
            success, img = cap.read()
            img = cv2.flip(img, 1)

            # 2. Find Hand Landmarks
            img = detector.findHands(img)
            lmList, bbox = detector.findPosition(img, draw=False)

            if len(lmList) != 0:
                
                # print(lmList)
        
                # tip of index and middle fingers
                x1, y1 = lmList[8][1:]
                x2, y2 = lmList[12][1:]


                # 3. Chekc which fingers are up
                fingers = detector.fingersUp()


                # 4. If Selection Mode - Two fingers are up

                if fingers[1] and fingers[2]:
                    xp, yp = 0, 0
                    print("Selection Mode")
                    # Checking for the click

                    if y1 < 125:
                        if 250 < x1 < 450:
                            header = overlayList[0]
                            drawColor = (255, 0, 255)
                        elif 550 < x1 < 750:
                            header = overlayList[1]
                            drawColor = (255, 0, 0)
                        if 800 < x1 < 950:
                            header = overlayList[2]
                            drawColor = (0, 255, 0)
                        if 1050 < x1 < 1200:
                            header = overlayList[3]
                            drawColor = (0, 0, 0)
                    cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
                # 5. If Drawign Mode - Index finger is up

                if fingers[1] and fingers[2] == False:
                    cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
                    print("Drawing Mode")

                    if xp==0 and yp==0:
                        xp, yp = x1, y1

                    if drawColor == (0, 0, 0):
                        cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                        cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
                    else:
                        cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                        cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

                    xp, yp = x1, y1


            imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
            _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
            imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
            img = cv2.bitwise_and(img, imgInv)
            img = cv2.bitwise_or(img, imgCanvas)


            # Setting the header image
            img[0:125, 0:1280] = header
            # img = cv2.addWeighted(img, 0.5, imgCanvas, 0,5, 0)






            cv2.imshow("Mnaht", img)
            # cv2.imshow("Canva", imgCanvas)
            # cv2.imshow("Inv", imgInv)
            if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
                break
        cap.release()  # giải phóng camera
        cv2.destroyAllWindows()  # thoát tất cả các cửa sổ


    def control_present(self):
        

        width, height = 1280, 720
        folderPath = "Presentation"

        cap = cv2.VideoCapture(0)
        cap.set(3, width)
        cap.set(4, height)

        # Tìm vị trí bản trình bản trong os
        pathImages = sorted(os.listdir(folderPath), key=len)
        #print(pathImages)

        # Variables
        imgNumber = 0
        hs, ws = int(120*1), int(213*1)
        gestureThreshold = 300
        buttonPressed = False
        buttonCouter = 0
        buttonDelay = 25
        annotations = [[]]
        annotationNumber = 0
        annotationStart = False

        # hand detector
        detector = HandDetector(detectionCon=int(0.8), maxHands=1)




        while True:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            pathFullImage = os.path.join(folderPath,pathImages[imgNumber])
            imgCurrent = cv2.imread(pathFullImage)



            hands, img = detector.findHands(img)
            cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

            if hands and buttonPressed is False:
                hand = hands[0]
                fingers = detector.fingersUp(hand)
                cx, cy = hand['center']
                lmList = hand['lmList']
                

                



                
                xVal = int(np.interp(lmList[8][0], [width // 2, w], [0, width]))
                yVal = int(np.interp(lmList[8][1], [150, height-150], [0, height]))

                indexFinger = xVal, yVal


                if cy <= gestureThreshold:
                    annotationStart = False
                    if fingers == [1,0,0,0,0]:
                        annotationStart = False
                        print('left')
                        if imgNumber > 0:
                            buttonPressed = True
                            annotations = [[]]
                            annotationNumber = 0
                            

                            imgNumber -=1
                if cy <= gestureThreshold:

                    if fingers == [0,0,0,0,1]:
                        annotationStart = False
                        print('right')
                        if imgNumber < len(pathImages)-1:
                            buttonPressed = True
                            annotations = [[]]
                            annotationNumber = 0
                            

                            imgNumber +=1
                
            


                # Hàm vẽ
                if fingers == [0,1,1,0,0]:
                    cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
                    annotationStart = False


                if fingers == [0, 1, 0, 0, 0]:
                    if annotationStart is False:
                        annotationStart = True
                        annotationNumber +=1
                        annotations.append([])
                    cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
                    annotations[annotationNumber].append(indexFinger)
                else:
                    annotationStart = False
                

                if fingers == [0, 1, 1, 1, 0]:
                    if annotations:
                        if annotationNumber >= 0:
                            annotations.pop(-1)
                            annotationNumber -=1
                            buttonPressed = True
            else:
                annotationStart = False


            if buttonPressed:
                buttonCouter +=1
                if buttonCouter > buttonDelay:
                    buttonCouter = 0
                    buttonPressed = False


            for i in range(len(annotations)):
                for j in range(len(annotations[i])):
                    if j !=0:
                        cv2.line(imgCurrent, annotations[i][j - 1],annotations[i][j],(0, 0 ,200), 12)


            # thêm webcam vào slide
            imgSmall = cv2.resize(img, (ws, hs))

            h, w, _ = imgCurrent.shape
            imgCurrent[0:hs, w-ws:w] = imgSmall












            cv2.imshow("Slide", imgCurrent)
            if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
                break
        cap.release()  # giải phóng camera
        cv2.destroyAllWindows()  # thoát tất cả các cửa sổ

    def chat_bot(self):
        # -------------Object Initialization---------------
        today = date.today()
        r = sr.Recognizer()
        keyboard = Controller()
        engine = pyttsx3.init('sapi5')
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)


        # ________________________________________________
        # ----------------Variables------------------------
        file_exp_status = False
        files =[]
        path = ''
        is_awake = True  #Bot status




        # ------------------Functions----------------------




        wikipedia.set_lang('vi') 
        language = 'vi'
        path = ChromeDriverManager().install()
        def reply(audio):
            modulechatbot.ChatBot.addAppMsg(audio)

            print(audio)
            # engine.speak.say(audio)
            engine.runAndWait()

        def speak(text):
            print("Tôi: {}".format(text))
            tts = gTTS(text=text, lang=language, slow=False)
            filename = 'voice.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove("voice.mp3")
            

        speak('Đây là những gì tôi tìm thấy được')

        def get_audio():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Tôi: ", end='')
                text = r.listen(source, phrase_time_limit=5)
                r.energy_threshold = 500
                r.dynamic_energy_threshold = False
                try:
                    text = r.recognize_google(text, language="vi-VN")
                    print(text)
                    return text
                except sr.RequestError:
                    speak('vui lòng kiểm tra lại đường dẫn')
                except sr.UnknownValueError:
                    print('Không thể nhận dạng được âm thanh')
                    pass
                

        def stop():
            speak("Hẹn gặp lại bạn sau!")

        def get_text():
            for i in range(3):
                text = get_audio()
                if text:
                    return text.lower()
                elif i < 2:
                    speak("Tôi không nghe rõ. Bạn nói lại được không!")
                    reply("Tôi không nghe rõ. Bạn nói lại được không!")
            time.sleep(2)
            stop()
            return 0

        def wish():
            hour = int(datetime.datetime.now().hour)

            if hour>=0 and hour<12:
                speak("Chào buổi sáng!")
                reply("Chào buổi sáng!")
            elif hour>=12 and hour<18:
                speak("Chào buổi chiều!")   
                reply("Chào buổi chiều!")   
            else:
                reply("Chào buổi tối!")  
                speak("Chào buổi tối!")  
                
            reply("Tôi là Alex, tôi có thể giúp gì cho bạn?")
            speak("Tôi là Alex, tôi có thể giúp gì cho bạn?")



        def get_time(text):
            now = datetime.datetime.now()
            if "giờ" in text:
                speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
            elif "ngày" in text:
                speak("Hôm nay là ngày %d tháng %d năm %d" %
                    (now.day, now.month, now.year))
                reply("Hôm nay là ngày %d tháng %d năm %d" %
                    (now.day, now.month, now.year))
                
            else:
                speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
                reply("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")


        def open_application(text):
            if "google" in text:
                speak("Mở Google Chrome")
                os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            elif "word" in text:
                speak("Mở Microsoft Word")
                os.startfile("C:\\Program Files (x86)\Microsoft Office\\root\Office16\\WINWORD.EXE")
            elif "excel" in text:
                speak("Mở Microsoft Excel")
                os.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\EXCEL.EXE")
            else:
                speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
                reply("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")

        def open_website(text):
            reg_ex = re.search('mở (.+)', text)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain
                webbrowser.open(url)
                speak("Trang web bạn yêu cầu đã được mở.")
                reply("Trang web bạn yêu cầu đã được mở.")
                return True
            else:
                return False

        def open_google_and_search(text):
            search_for = text.split("kiếm", 1)[1]
            driver = webdriver.Chrome(path)
            driver.get("https://www.google.com")
            que = driver.find_element_by_xpath("//input[@name='q']")
            que.send_keys(str(search_for))
            que.send_keys(Keys.RETURN)

        def send_email(text):
            speak('Bạn gửi email cho ai nhỉ')
            reply('Bạn gửi email cho ai nhỉ')
            recipient = get_text()
            if 'yến' in recipient:
                speak('Nội dung bạn muốn gửi là gì')
                reply('Nội dung bạn muốn gửi là gì')
                content = get_text()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('luongngochungcntt@gmail.com', 'hung23081997')
                mail.sendmail('luongngochungcntt@gmail.com',
                            'hungdhv97@gmail.com', content.encode('utf-8'))
                mail.close()
                speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
                reply('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
            else:
                speak('Tôi không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')
                reply('Tôi không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')

        def current_weather():
            speak("Bạn muốn xem thời tiết ở đâu ạ.")
            reply("Bạn muốn xem thời tiết ở đâu ạ.")
            ow_url = "http://api.openweathermap.org/data/2.5/weather?"
            city = get_text()
            if not city:
                pass
            api_key = "fe8d8c65cf345889139d8e545f57819a"
            call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
            response = requests.get(call_url)
            data = response.json()
            if data["cod"] != "404":
                city_res = data["main"]
                current_temperature = city_res["temp"]
                current_pressure = city_res["pressure"]
                current_humidity = city_res["humidity"]
                suntime = data["sys"]
                sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
                sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
                wthr = data["weather"]
                weather_description = wthr[0]["description"]
                now = datetime.datetime.now()
                content = """
                Hôm nay là ngày {day} tháng {month} năm {year}
                Mặt trời mọc vào {hourrise} giờ {minrise} phút
                Mặt trời lặn vào {hourset} giờ {minset} phút
                Nhiệt độ trung bình là {temp} độ C
                Áp suất không khí là {pressure} héc tơ Pascal
                Độ ẩm là {humidity}%
                Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                                hourset = sunset.hour, minset = sunset.minute, 
                                                                                temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
                speak(content)
                reply(content)
                time.sleep(20)
            else:
                speak("Không tìm thấy địa chỉ của bạn")
                reply("Không tìm thấy địa chỉ của bạn")

        def play_song():
            speak('Xin mời bạn chọn tên bài hát')
            reply('Xin mời bạn chọn tên bài hát')
            mysong = get_text()
            while True:
                result = YoutubeSearch(mysong, max_results=10).to_dict()
                if result:
                    break
            url = 'https://www.youtube.com' + result[0]['url_suffix']
            webbrowser.open(url)
            speak("Bài hát bạn yêu cầu đã được mở.")
            reply("Bài hát yêu thích của bạn đã được mở")

        def change_wallpaper():
            api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
            url = 'https://api.unsplash.com/photos/random?client_id=' + \
                api_key  # pic from unspalsh.com
            f = urllib2.urlopen(url)
            json_string = f.read()
            f.close()
            parsed_json = json.loads(json_string)
            photo = parsed_json['urls']['full']
            # Location where we download the image to.
            urllib2.urlretrieve(photo, "C:/Users/Night Fury/Downloads/a.png")
            image=os.path.join("C:/Users/Night Fury/Downloads/a.png")
            ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
            speak('Hình nền máy tính vừa được thay đổi')
            reply('Hình nền máy tính vừa được thay đổi')

        def read_news():
            speak("Bạn muốn đọc báo về gì")
            reply("Bạn muốn đọc báo về gì")
            
            queue = get_text()
            params = {
                'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
                "q": queue,
            }
            api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
            api_response = api_result.json()
            print("Tin tức")

            for number, result in enumerate(api_response['articles'], start=1):
                print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
            """)
                if number <= 3:
                    webbrowser.open(result['url'])

        def tell_me_about():
            try:
                speak("Bạn muốn nghe về gì ạ")
                reply("Bạn muốn nghe về gì ạ")
                text = get_text()
                contents = wikipedia.summary(text).split('\n')
                speak(contents[0])
                reply(contents[0])
                time.sleep(10)
                for content in contents[1:]:
                    speak("Bạn muốn nghe thêm không")
                    reply("Bạn muốn nghe thêm không")
                    ans = get_text()
                    if "có" not in ans:
                        break    
                    speak(content)
                    reply(content)
                    time.sleep(10)

                speak('Cảm ơn bạn đã lắng nghe!!!')
                reply('Cảm ơn bạn đã lắng nghe!!!')
            except:
                speak("Tôi không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
                reply("Tôi không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")

        def help_me():
            speak("""Tôi có thể giúp bạn thực hiện các câu lệnh sau đây:
            1. Chào hỏi
            2. Hiển thị giờ
            3. Mở website, application
            4. Tìm kiếm trên Google
            5. Gửi email
            6. Dự báo thời tiết
            7. Mở video nhạc
            8. Thay đổi hình nền máy tính
            9. Đọc báo hôm nay
            10. Kể bạn biết về thế giới """)


            reply("""Tôi có thể giúp bạn thực hiện các câu lệnh sau đây:
            1. Chào hỏi
            2. Hiển thị giờ
            3. Mở website, application
            4. Tìm kiếm trên Google
            5. Gửi email
            6. Dự báo thời tiết
            7. Mở video nhạc
            8. Thay đổi hình nền máy tính
            9. Đọc báo hôm nay
            10. Kể bạn biết về thế giới """)
            time.sleep(20)

        def respond(text):
            
            global file_exp_status, files, is_awake, path
            print(text)
            text.replace('hãy','')
            modulechatbot.eel.addUserMsg(text)

            file_exp_status = False
            files =[]
            path = ''
            is_awake = True  #Bot status

            if is_awake == False:
                if 'wake up' in text:
                    is_awake = True
                    wish()

            # STATIC CONTROLS
            
            if 'hello' in text:
                wish()

            elif 'what is your name' in text:
                speak('My name is MNhat!')
                reply('My name is MNhat!')

            elif 'date' in text:
                speak(today.strftime("%B %d, %Y"))
                reply(today.strftime("%B %d, %Y"))

            elif 'time' in text:
                speak(str(datetime.datetime.now()).split(" ")[1].split('.')[0])
                reply(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

            elif 'tìm kiếm' in text:
                speak('Searching for ' + text.split('tìm kiếm')[1])
                reply('Searching for ' + text.split('tìm kiếm')[1])
                url = 'https://google.com/search?q=' + text.split('tìm kiếm')[1]
                try:
                    webbrowser.get().open(url)
                    speak('Xin lỗi bạn')
                    reply('Xin lỗi bạn')
                except:
                    speak('Vui lòng kiểm tra lại đường tuyền internet')
                    reply('Vui lòng kiểm tra lại đường tuyền internet')



            elif 'địa điểm' in text:
                speak('Bạn muốn tìm kiếm địa điểm nào ?')
                reply('Bạn muốn tìm kiếm địa điểm nào ?')
                temp_audio = get_audio()
                modulechatbot.eel.addUserMsg(temp_audio)
                speak('Locating...')
                url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
                try:
                    webbrowser.get().open(url)
                    speak('Đây là những gì tôi tìm thấy được')
                    reply('Đây là những gì tôi tìm thấy được')
                except:
                    speak('Vui lòng kiểm tra đường truyền của bạn')
                    reply('Vui lòng kiểm tra đường truyền của bạn')

            elif ('bye' in text) or ('by' in text) or ('bay' in text):
                speak("Chào bạn, hãy quay lại gặp tôi sớm nhất có thể nhé")
                reply("Chào bạn, hãy quay lại gặp tôi sớm nhất có thể nhé")
                is_awake = False

            elif ('exit' in text) or ('terminate' in text):
                if Gesture_Controller.GestureController.gc_mode:
                    Gesture_Controller.GestureController.gc_mode = 0
                modulechatbot.ChatBot.close()
                #sys.exit() always raises SystemExit, Handle it in main loop
                sys.exit()
                
            # Các chức năng chính
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                        stop()
            elif "có thể làm gì" in text:
                help_me()
            elif "chào trợ lý ảo" in text:
                wish(name)
            elif "hiện tại" in text:
                get_time(text)
            elif "mở" in text:
                if 'mở google và tìm kiếm' in text:
                    open_google_and_search(text)
                elif "." in text:
                    open_website(text)
                else:
                    open_application(text)
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            elif "thời tiết" in text:
                current_weather()
            elif "chơi nhạc" in text:
                play_song()
                speak("đã mở thành công")
                reply("đã mở thành công")

            
            
            elif "hình nền" in text:
                change_wallpaper()
            elif "đọc báo" in text:
                read_news()
            elif "định nghĩa" in text:
                tell_me_about()


            # DYNAMIC CONTROLS

            elif 'copy' in text:
                with keyboard.pressed(Key.ctrl):
                    keyboard.press('c')
                    keyboard.release('c')
                speak('Đã copy xong')
                reply('Đã copy xong')
                
            elif 'page' in text or 'pest'  in text or 'paste' in text:
                with keyboard.pressed(Key.ctrl):
                    keyboard.press('v')
                    keyboard.release('v')
                speak('Đã paste xong')
                reply('Đã paste xong')
                
            # File Navigation (Default Folder set to C://)
            elif 'list' in text:
                counter = 0
                path = 'C://'
                files = listdir(path)
                filestr = ""
                for f in files:
                    counter+=1
                    print(str(counter) + ':  ' + f)
                    filestr += str(counter) + ':  ' + f + '<br>'
                file_exp_status = True
                speak('Không tồn tại file này trong máy tính của bạn')
                reply('Không tồn tại file này trong máy tính của bạn')
                modulechatbot.ChatBot.addAppMsg(filestr)
                
            elif file_exp_status == True:
                counter = 0   
                if 'open' in text:
                    if isfile(join(path,files[int(text.split(' ')[-1])-1])):
                        os.startfile(path + files[int(text.split(' ')[-1])-1])
                        file_exp_status = False
                    else:
                        try:
                            path = path + files[int(text.split(' ')[-1])-1] + '//'
                            files = listdir(path)
                            filestr = ""
                            for f in files:
                                counter+=1
                                filestr += str(counter) + ':  ' + f + '<br>'
                                print(str(counter) + ':  ' + f)
                            speak('Đã mở thành công')
                            reply('Đã mở thành công')
                            modulechatbot.ChatBot.addAppMsg(filestr)
                            
                        except:
                            speak('Bạn không có quyền để truy cập mục địa chỉ này')
                            reply('Bạn không có quyền để truy cập mục địa chỉ này')
                                            
                if 'back' in text:
                    filestr = ""
                    if path == 'C://':
                        speak('Xin lỗi, đây là thư mục gốc')
                        reply('Xin lỗi, đây là thư mục gốc')
                    else:
                        a = path.split('//')[:-2]
                        path = '//'.join(a)
                        path += '//'
                        files = listdir(path)
                        for f in files:
                            counter+=1
                            filestr += str(counter) + ':  ' + f + '<br>'
                            print(str(counter) + ':  ' + f)
                        speak('ok')
                        reply('ok')
                        modulechatbot.ChatBot.addAppMsg(filestr)

                        
            else: 
                speak('Tôi không có chức năng để làm điều này !')
                reply('Tôi không có chức năng để làm điều này !')



        t1 = Thread(target = modulechatbot.ChatBot.start)
        t1.start()

        # Lock main thread until Chatbot has started
        while not modulechatbot.ChatBot.started:
            time.sleep(0.5)

        wish()
        text = None
        while True:
            if modulechatbot.ChatBot.isUserInput():
                #take input from GUI
                text = modulechatbot.ChatBot.popUserInput()
            else:
                #take input from Voice
                text = get_text()
            

            #process text
            if ('hãy' in text) or ('hi' in text) or ('hai' in text) or ('2' in text):
                try:
                    respond(text)
            
                except SystemExit:
                        speak("Thoát thành công ứng dụng")

    def play_subway(self):
        # Kushal N JNV Bangalore Urban 9th B

        

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
        """mp_drawing = mp.solutions.mediapipe.python.solutions.drawing_utils"""
        mp_drawing = mp.solutions.drawing_utils


        def detectPose(image, pose, blankImage=False):
            output_image = image.copy()

            if blankImage:
                blank_image = np.zeros((720, 1920, 3), np.uint8)
                output_image = blank_image

            imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            results = pose.process(imageRGB)

            height, width, _ = image.shape

            landmarks = []

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks,
                                        connections=mp_pose.POSE_CONNECTIONS)

                for landmark in results.pose_landmarks.landmark:
                    landmarks.append((int(landmark.x * width), int(landmark.y * height),
                                    (landmark.z * width)))
            return output_image, landmarks, results


        def calculateAngle(landmark1, landmark2, landmark3):
            x1, y1, _ = landmark1
            x2, y2, _ = landmark2
            x3, y3, _ = landmark3
            angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
            if angle < 0:
                angle += 360
            return angle


        def classifyPose(landmarks, output_image):
            label = 'Unknown Pose'

            color = (0, 0, 255)

            left_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                            landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])

            right_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])

            left_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])

            right_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])

            left_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                            landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])

            right_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])

            input(left_elbow_angle, right_elbow_angle, left_shoulder_angle, right_shoulder_angle, left_knee_angle,
                right_knee_angle)

            if left_elbow_angle > 165 and left_elbow_angle < 195 and right_elbow_angle > 165 and right_elbow_angle < 195:

                if left_shoulder_angle > 80 and left_shoulder_angle < 110 and right_shoulder_angle > 80 and right_shoulder_angle < 110:

                    if left_knee_angle > 165 and left_knee_angle < 195 or right_knee_angle > 165 and right_knee_angle < 195:

                        if left_knee_angle > 90 and left_knee_angle < 120 or right_knee_angle > 90 and right_knee_angle < 120:
                            label = 'Warrior II Pose'

                    if left_knee_angle > 160 and left_knee_angle < 195 and right_knee_angle > 160 and right_knee_angle < 195:
                        label = 'T Pose'

            if left_knee_angle > 165 and left_knee_angle < 195 or right_knee_angle > 165 and right_knee_angle < 195:

                if left_knee_angle > 315 and left_knee_angle < 335 or right_knee_angle > 25 and right_knee_angle < 45:
                    label = 'Tree Pose'

            if label != 'Unknown Pose':
                color = (0, 255, 0)

            cv2.putText(output_image, label, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

            return output_image, label


        def checkHandsJoined(img, results, draw=False):
            height, width, _ = img.shape

            output_img = img.copy()

            left_wrist_landmark = (results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * width,
                                results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * height)
            right_wrist_landmark = (results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * width,
                                    results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * height)

            distance = int(
                math.hypot(left_wrist_landmark[0] - right_wrist_landmark[0], left_wrist_landmark[1] - right_wrist_landmark[1]))

            if distance < 130:
                hand_status = 'Hands Joined'
                color = (0, 255, 0)

            else:
                hand_status = 'Hands Not Joined'
                color = (0, 0, 255)

            if draw:
                cv2.putText(output_img, hand_status, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 3)
                cv2.putText(output_img, f'Distance: {distance}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, color, 3)

            return output_img, hand_status


        def checkLeftRight(img, results, draw=False):
            horizontal_position = None

            height, width, c = img.shape

            output_image = img.copy()

            left_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width)
            right_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * width)

            if (right_x <= width // 2 and left_x <= width // 2):
                horizontal_position = 'Left'

            elif (right_x >= width // 2 and left_x >= width // 2):
                horizontal_position = 'Right'

            elif (right_x >= width // 2 and left_x <= width // 2):
                horizontal_position = 'Center'

            if draw:
                cv2.putText(output_image, horizontal_position, (5, height - 10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
                cv2.line(output_image, (width // 2, 0), (width // 2, height), (255, 255, 255), 2)

            return output_image, horizontal_position


        def checkJumpCrouch(img, results, MID_Y=250, draw=False):
            height, width, _ = img.shape

            output_image = img.copy()

            left_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height)
            right_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * height)

            actual_mid_y = abs(right_y + left_y) // 2

            lower_bound = MID_Y - 15
            upper_bound = MID_Y + 100

            if (actual_mid_y < lower_bound):
                posture = 'Jumping'

            elif (actual_mid_y > upper_bound):
                posture = 'Crouching'

            else:
                posture = 'Standing'

            if draw:
                cv2.putText(output_image, posture, (5, height - 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
                cv2.line(output_image, (0, MID_Y), (width, MID_Y), (255, 255, 255), 2)

            return output_image, posture


        if __name__ == '__main__':

            pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)

            cap = cv2.VideoCapture(0)
            cap.set(3, 1280)
            cap.set(4, 720)
            pTime = 0

            game_started = False
            x_pos_index = 1
            y_pos_index = 1
            MID_Y = None
            counter = 0
            num_of_frames = 10

            while True:
                success, img = cap.read()
                img = cv2.flip(img, 1)
                h, w, _ = img.shape
                img = cv2.resize(img, (1280, 720))
                img, landmarks, results = detectPose(img, pose_video)
                if landmarks:
                    if game_started:
                        img, horizontal_position = checkLeftRight(img, results, draw=True)
                        if (horizontal_position == 'Left' and x_pos_index != 0) or (
                                horizontal_position == 'Center' and x_pos_index == 2):

                            pyautogui.press('left')

                            x_pos_index -= 1

                        elif (horizontal_position == 'Right' and x_pos_index != 2) or (
                                horizontal_position == 'Center' and x_pos_index == 0):

                            pyautogui.press('right')

                            x_pos_index += 1

                    else:

                        cv2.putText(img, 'JOIN BOTH HANDS TO START THE GAME.', (5, h - 10), cv2.FONT_HERSHEY_PLAIN,
                                    2, (0, 255, 0), 3)

                    if checkHandsJoined(img, results)[1] == 'Hands Joined':

                        counter += 1

                        if counter == num_of_frames:

                            if not (game_started):

                                game_started = True
                                left_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * h)
                                right_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * h)
                                MID_Y = abs(right_y + left_y) // 2
                                pyautogui.click(x=1300, y=800, button='left')
                            else:
                                pyautogui.press('space')

                            counter = 0

                    else:

                        counter = 0

                    if MID_Y:

                        img, posture = checkJumpCrouch(img, results, MID_Y, draw=True)

                        if posture == 'Jumping' and y_pos_index == 1:

                            pyautogui.press('up')
                            y_pos_index += 1

                        elif posture == 'Crouching' and y_pos_index == 1:

                            pyautogui.press('down')

                            y_pos_index -= 1

                        elif posture == 'Standing' and y_pos_index != 1:

                            y_pos_index = 1
                        print(posture)


                else:

                    counter = 0

                cTime = time.time()
                fps = 1 / (cTime - pTime)
                pTime = cTime

                cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

                cv2.imshow('Subway', img)
                if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
                    break
                cap.release()  # giải phóng camera
                cv2.destroyAllWindows()  # thoát tất cả các cửa sổ

    def volume_control(self):

        ################################
        wCam, hCam = 640, 480
        ################################

        cap = cv2.VideoCapture(0)
        cap.set(3, wCam)
        cap.set(4, hCam)
        pTime = 0

        detector = htm.handDetector(detectionCon=int(1), maxHands=1)

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # volume.GetMute()
        # volume.GetMasterVolumeLevel()
        volRange = volume.GetVolumeRange()
        minVol = volRange[0]
        maxVol = volRange[1]
        vol = 0
        volBar = 400
        volPer = 0
        area = 0
        colorVol = (255, 0, 0)

        while True:
            success, img = cap.read()

            # Find Hand
            img = detector.findHands(img)
            lmList, bbox = detector.findPosition(img, draw=True)
            if len(lmList) != 0:

                # Filter based on size
                area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
                # print(area)
                if 250 < area < 1000:

                    # Find Distance between index and Thumb
                    length, img, lineInfo = detector.findDistance(4, 8, img)
                    # print(length)

                    # Convert Volume
                    volBar = np.interp(length, [50, 200], [400, 150])
                    volPer = np.interp(length, [50, 200], [0, 100])

                    # Reduce Resolution to make it smoother
                    smoothness = 10
                    volPer = smoothness * round(volPer / smoothness)

                    # Check fingers up
                    fingers = detector.fingersUp()
                    # print(fingers)

                    # If pinky is down set volume
                    if not fingers[4]:
                        volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                        cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                        colorVol = (0, 255, 0)
                    else:
                        colorVol = (255, 0, 0)

            # Drawings
            cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
            cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
            cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 0, 0), 3)
            cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
            cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX,
                        1, colorVol, 3)

            # Frame rate
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 0, 0), 3)

            cv2.imshow("Img", img)
            if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
                break



if __name__ == "__main__":
    app = App()
    app.mainloop()
