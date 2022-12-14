import matplotlib.pyplot as plt
from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from tkinter import font
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas

import customtkinter
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import re
from datetime import date,datetime, timedelta

from array import *

from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter  #inch
import win32api
from textwrap import wrap


finsysdb = mysql.connector.connect(
    host="localhost", user="root", password="", database="finsys_sale", port="3306"
)
fbcursor = finsysdb.cursor(buffered=True)

root=Tk()
root.geometry("1366x768+0+0")

root.title("Fin sYs")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#-------------------------------------------------------------------------------------------------------------------------Images


pro_pic =PIL.Image.open("profilepic\propic.jpg")
# resized_pro_pic= pro_pic.resize((170,170))
prof_pics=ImageTk.PhotoImage(pro_pic)

selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")
  
right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")
color = PhotoImage(file="images/font_color.png")



imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

notic =PIL.Image.open("images/bell.png")
noti=ImageTk.PhotoImage(notic)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

stn =PIL.Image.open("images/brightness-solid-24.png")
stn_img=ImageTk.PhotoImage(stn)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50))
mai_logo= ImageTk.PhotoImage(resized_image)

sig_up =PIL.Image.open("images/register.png")
resized_sign_up= sig_up.resize((500,400))
sign_up=ImageTk.PhotoImage(resized_sign_up)


#------------------------------------------------------------------------------------------------------------Login Button Function

def main_sign_in():
    
        usr_nm=nm_ent.get()
        usr_pass=pass_ent.get()
        sql_log_sql='select * from auth_user where username=%s'
        vals=(nm_ent.get(),)
        fbcursor.execute(sql_log_sql,vals)
        check_logins=fbcursor.fetchone()
        
        if usr_nm=="" or usr_pass=="" or usr_nm=="Username" or usr_pass=="********":
            messagebox.showerror("Login Failed","Enter username and password")
        else:

            sql_log_sql='select * from auth_user where username=%s'
            vals=(nm_ent.get(),)
            fbcursor.execute(sql_log_sql,vals)
            check_login=fbcursor.fetchone()
            
            if check_login is None:
                messagebox.showerror("Login Failed","Create an account")
            else:
                if check_login[4]==usr_nm and check_login[1]==usr_pass:
                    
                    

                    pro_pic =PIL.Image.open("profilepic\propic"+str(check_logins[0])+".png")
                        # resized_pro_pic= pro_pic.resize((170,170))
                    prof_pics=ImageTk.PhotoImage(pro_pic)

                    dash_pro_pic =PIL.Image.open("profilepic\propic"+str(check_logins[0])+".png")
                    dash_resized_pro_pic= dash_pro_pic.resize((50,50))
                    dash_prof_pics=ImageTk.PhotoImage(dash_resized_pro_pic)
                    
                    try:
                        main_frame_signup.pack_forget()
                    except:
                        pass
                    try:
                        main_frame_signin.pack_forget()
                    except:
                        pass
                    Sys_top_frame=Frame(root, height=70,bg="#213b52")
                    Sys_top_frame.pack(fill=X,)

                    #---------------------------------------------------------------------------------------Top Menu
                    tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Logo Name Frame
                    tp_lb_nm.grid(row=1,column=1,sticky='nsew')
                    tp_lb_nm.grid_rowconfigure(0,weight=1)
                    tp_lb_nm.grid_columnconfigure(0,weight=1)

                    label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
                    label.grid(row=2,column=1,sticky='nsew')
                    label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
                    label.grid(row=2,column=2,sticky='nsew')
                
                    mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",border=0)
                    mnu_btn.grid(row=2,column=4,padx=50)

                    

                    tp_lb_srh=LabelFrame(Sys_top_frame,bg="#213b52")#-------------------------Serch area Frame
                    tp_lb_srh.grid(row=1,column=2,sticky='nsew')
                    tp_lb_srh.grid_rowconfigure(0,weight=1)
                    tp_lb_srh.grid_columnconfigure(0,weight=1)

                    def srh_fn(event):
                        if srh_top.get()=="Search":
                            srh_top.delete(0,END)
                        else:
                            pass

                    

                    #------------------------------------------------------settings 
                    def close_lst_2():
                            lst_prf2.place_forget()
                            set_btn4 = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                            set_btn4.grid(row=2,column=5,padx=(0,30))
                            
                    def settings():
                        

                        # create a list box
                        stng = ("Accounts And Settings","Customize From Style","Chart Of Accounts")

                        stngs = StringVar(value=stng)
                        global lst_prf2
                        lst_prf2 = Listbox(root,listvariable=stngs,height=3 ,selectmode='extended',bg="black",fg="white")

                        lst_prf2.place(relx=0.70, rely=0.10)
                        lst_prf2.bind('<<ListboxSelect>>', )
                        set_btn.grid_forget()
                        set_btn2 = Button(tp_lb_srh, image=stn_img,command=close_lst_2, bg="#213b52", fg="black",border=0)
                        set_btn2.grid(row=2,column=5,padx=(0,30))

                    set_btn = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                    set_btn.grid(row=2,column=5,padx=(0,30))

                    tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Notification
                    tp_lb_nm.grid(row=1,column=3,sticky='nsew')
                    tp_lb_nm.grid_rowconfigure(0,weight=1)
                    tp_lb_nm.grid_columnconfigure(0,weight=1)
                    srh_btn = Button(tp_lb_nm, image=noti, bg="#213b52", fg="black",border=0)
                    srh_btn.grid(row=0,column=0,padx=35)
                    
                    tp_lb_npr=LabelFrame(Sys_top_frame,bg="#213b52")#---------------------------profile area name
                    tp_lb_npr.grid(row=1,column=4,sticky='nsew')
                    tp_lb_npr.grid_rowconfigure(0,weight=1)
                    tp_lb_npr.grid_columnconfigure(0,weight=1)
                    dtl_sqls="select * from auth_user where username=%s"
                    dtl_sqls_val=(nm_ent.get(),)
                    fbcursor.execute(dtl_sqls,dtl_sqls_val,)
                    dtls=fbcursor.fetchone()

                    sql_pro_sql="select * from app1_company where id_id =%s"
                    sql_pro_sql_val=(dtls[0],)
                    fbcursor.execute(sql_pro_sql,sql_pro_sql_val,)
                    dtl_cmp_pro=fbcursor.fetchone()

                    label = Label(tp_lb_npr, text=str(dtl_cmp_pro[1])+"\nOnline",bg="#213b52", fg="white", anchor="center",width=10,height=2,font=('Calibri 16 bold'),border=0)
                    label.grid(row=0,column=1,sticky='nsew')
                    # label = Label(tp_lb_npr, text="Online",bg="#213b52", fg="white",width=15,font=('Calibri 12 bold'),border=0)
                    # label.grid(row=2,column=1,sticky='nsew')

                    
                    
                    def lst_frt():
                        lst_prf.place_forget()
                        srh_btn3 = Button(tp_lb_npr,image=dash_prof_pics, bg="White", fg="black",command=profile)
                        srh_btn3.grid(row=0,column=2,padx=15)
                    def lst_prf_slt(event):
                        def edit_profile():
                            def responsive_widgets_edit(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                                


                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/13
                                y2 = dheight/.53

                                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )                              

                                
                                # dcanvas.coords("bg_polygen_pr",dwidth/16,dheight/.6,dwidth/1.07,dheight/9)
                                dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)
                                dcanvas.coords("pr_img",dwidth/2.3,dheight/5)
                                

                                dcanvas.coords("pr_hr_l",dwidth/16,dheight/6.5,dwidth/1.07,dheight/6.5)
                                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                                dcanvas.coords("pr_crpass_lb",dwidth/17.075,dheight/1.33)
                                dcanvas.coords("pr_crpass_ent",dwidth/17.075,dheight/1.26)
                                dcanvas.coords("pr_re_pass_lb",dwidth/17.075,dheight/1.16)
                                dcanvas.coords("pr_re_pass_ent",dwidth/17.075,dheight/1.1)
                                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)
                                dcanvas.coords("pr_new_pass_lb",dwidth/1.92,dheight/1.33)
                                dcanvas.coords("pr_new_pass_ent",dwidth/1.92,dheight/1.26)

                                
                                #-------------------------------------------------------------------------company section
                                dcanvas.coords("cmp_hd",dwidth/20,dheight/1)
                                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/0.93)
                                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/0.89)
                                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/0.84)
                                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/0.81)
                                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/0.77)
                                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.745)
                                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.712)
                                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.69)
                                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.66)
                                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.64)
                                dcanvas.coords("cmp_file_lb",dwidth/17.075,dheight/.615)
                                dcanvas.coords("cmp_file_ent",dwidth/17.075,dheight/.6)
                                

                                #--------------------------------------------------------------------------company right

                                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/0.93)
                                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/0.89)
                                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/0.84)
                                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/0.81)
                                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/0.77)
                                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.745)
                                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.712)
                                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.69)
                                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.66)
                                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.64)
                                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.57)
                            sql_pro="select * from auth_user where username=%s"
                            sql_pro_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pro,sql_pro_val,)
                            edi_dtl=fbcursor.fetchone()

                            def update_profile():
                                first_name=fr_name_ent.get()
                                pro_email=em_ent.get()
                                last_name=lst_nm_ent.get()
                                pro_username=usr_nm_ent.get()
                                pro_new_pass=pr_new_pass_ent.get()

                                sql_signup='select * from auth_user'
                                fbcursor.execute(sql_signup)
                                check_none=fbcursor.fetchone()

                                if edi_dtl[4]==pro_username and edi_dtl[1]==pr_crpass_ent.get() and pro_new_pass=="" :
                                            passw=pr_crpass_ent.get()
                                    
                                            prof_edit="update auth_user set first_name=%s,last_name=%s,email=%s,username=%s,password=%s where id=%s" #adding values into db
                                            prof_edit_val=(first_name,last_name,pro_email,pro_username,passw,edi_dtl[0])
                                            fbcursor.execute(prof_edit,prof_edit_val)
                                            finsysdb.commit()

                                            #compnay
                                            cmp_name=cmp_nm_ent.get()
                                            cmp_cty=cmp_cty_ent.get()
                                            cmp_pin=cmp_pin_ent.get()
                                            cmp_phn=cmp_ph_ent.get()
                                            cmp_ind=cmp_indest_ent.get()
                                            cmp_addr=cmp_addr_ent.get()
                                            cmp_st=cmp_st_ent.get()
                                            cmp_em=cmp_em_ent.get()
                                            cmp_bname=cmp_lg_ent.get()
                                            cmp_typ=cmp_typ_ent.get()
                                            logo=cmp_file_ent.get()

                                            cmp_edit="update app1_company set cname=%s,caddress=%s,city=%s,state=%s,pincode=%s,cemail=%s,phone=%s,cimg=%s,bname=%s,industry=%s,ctype=%s where id_id =%s" #adding values into db
                                            cmp_edit_val=(cmp_name,cmp_addr,cmp_cty,cmp_st,cmp_pin,cmp_em,cmp_phn,logo,cmp_bname,cmp_ind,cmp_typ,edi_dtl[0])
                                            fbcursor.execute(cmp_edit,cmp_edit_val)
                                            finsysdb.commit()
                                            
                                        
                                else:
                                    # #username same password change
                                    if pr_new_pass_ent.get()=="":
                                        
                                        pro_new_passd=pr_crpass_ent.get()
                                        
                                    else:
                                        pro_new_passd=pr_new_pass_ent.get()
                                    if pro_new_pass==pr_re_pass_ent.get() and pr_re_pass_ent.get()==pro_new_pass:
                                            if pr_crpass_ent.get()==edi_dtl[1]:
                                                print(pro_new_pass)
                                                prof_edit="update auth_user set first_name=%s,last_name=%s,email=%s,username=%s,password=%s where id=%s" #adding values into db
                                                prof_edit_val=(first_name,last_name,pro_email,pro_username,pro_new_passd,edi_dtl[0])
                                                fbcursor.execute(prof_edit,prof_edit_val)
                                                finsysdb.commit()

                                                #compnay
                                                cmp_name=cmp_nm_ent.get()
                                                cmp_cty=cmp_cty_ent.get()
                                                cmp_pin=cmp_pin_ent.get()
                                                cmp_phn=cmp_ph_ent.get()
                                                cmp_ind=cmp_indest_ent.get()
                                                cmp_addr=cmp_addr_ent.get()
                                                cmp_st=cmp_st_ent.get()
                                                cmp_em=cmp_em_ent.get()
                                                cmp_bname=cmp_lg_ent.get()
                                                cmp_typ=cmp_typ_ent.get()
                                                logo=cmp_file_ent.get()

                                                cmp_edit="update app1_company set cname=%s,caddress=%s,city=%s,state=%s,pincode=%s,cemail=%s,phone=%s,cimg=%s,bname=%s,industry=%s,ctype=%s where id_id =%s" #adding values into db
                                                cmp_edit_val=(cmp_name,cmp_addr,cmp_cty,cmp_st,cmp_pin,cmp_em,cmp_phn,logo,cmp_bname,cmp_ind,cmp_typ,edi_dtl[0])
                                                fbcursor.execute(cmp_edit,cmp_edit_val)
                                                finsysdb.commit()
                                                
                                            else:
                                                messagebox.showerror("Updation Failed","Please check your current password")
                                    else:

                                            messagebox.showerror("Updation Failed","password and conform password does not match")
                                        
                                    
                                Sys_top_frame2.pack_forget()
                                Sys_top_frame.pack_forget()
                                Sys_mains_frame_pr_ed.grid_forget()
                                main_frame_signin.pack(fill=X,)

                            sql_pro_cmp="select * from app1_company where id_id=%s"
                            sql_pro_cmp_val=(pro_dtl[0],)
                            fbcursor.execute(sql_pro_cmp,sql_pro_cmp_val,)
                            edi_cmp_dtl=fbcursor.fetchone()

                            Sys_mains_frame_pr.place_forget()
                            global Sys_mains_frame_pr_ed
                            Sys_mains_frame_pr_ed=Frame(tab1, height=750)
                            Sys_mains_frame_pr_ed.grid(row=0,column=0,sticky='nsew')
                            Sys_mains_frame_pr_ed.grid_rowconfigure(0,weight=1)
                            Sys_mains_frame_pr_ed.grid_columnconfigure(0,weight=1)

                            pr_canvas_ed=Canvas(Sys_mains_frame_pr_ed,height=766,width=1340,scrollregion=(0,0,766,1650),bg="#2f516f",border=0)
                            pr_canvas_ed.bind('<Configure>', responsive_widgets_edit)
                            
                            pr_myscrollbar_ed=Scrollbar(Sys_mains_frame_pr_ed,orient="vertical",command=pr_canvas_ed.yview)
                            pr_canvas_ed.configure(yscrollcommand=pr_myscrollbar_ed.set)

                            pr_myscrollbar_ed.pack(side="right",fill="y")
                            pr_canvas_ed.pack(fill=X)

                            rth2 = pr_canvas_ed.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_pr"),smooth=True,)


                            grd1c=Label(pr_canvas_ed, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                            win_inv1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

                            pr_img=Label(pr_canvas_ed,  image = prof_pics,bg="#213b52",width=170,height=170,  anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_img,tags=("pr_img"))

                            pr_canvas_ed.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
                            #----------------------------------------------------------------------------------------Personal info
                            pr_hd=Label(pr_canvas_ed, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

                            fir_name=Label(pr_canvas_ed, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

                            fr_name_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            fr_name_ent.delete(0,END)
                            fr_name_ent.insert(0,edi_dtl[5])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

                            pr_em_lb=Label(pr_canvas_ed, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

                            em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            em_ent.delete(0,END)
                            em_ent.insert(0,edi_dtl[7])
                            def validate(value):
            
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                em_ent.config(fg="black")
                                return True

                            def on_invalid():
                                
                                em_ent.config(fg="red")

                            vcmdem_ent = (pr_canvas_ed.register(validate), '%P')
                            ivcmdem_ent = (pr_canvas_ed.register(on_invalid),)
                            em_ent.config(validate='focusout', validatecommand=vcmdem_ent, invalidcommand=ivcmdem_ent)                              
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

                            pr_crpass_lb=Label(pr_canvas_ed, text="Enter your Current Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_lb,tag=("pr_crpass_lb"))

                            pr_crpass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'),show="*")
                            
                            pr_crpass_ent.delete(0,END)
                            pr_crpass_ent.insert(0,edi_dtl[1])
                            
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_ent,tag=("pr_crpass_ent"))

                            pr_re_pass_lb=Label(pr_canvas_ed, text="Re-type new Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_lb,tag=("pr_re_pass_lb"))

                            pr_re_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'),show="*")
                            def pas_val_fun1(value):
            
                                pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                pr_re_pass_ent.config(fg="black")
                                return True

                            def pass_inval_fun1():
                                pr_re_pass_ent.config(fg="red")

                            pas_val1 = (pr_canvas_ed.register(pas_val_fun1), '%P')
                            pass_inval1 = (pr_canvas_ed.register(pass_inval_fun1),)

                            pr_re_pass_ent.config(validate='focusout', validatecommand=pas_val1, invalidcommand=pass_inval1)

                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_ent,tag=("pr_re_pass_ent"))


                            last_nm_lb=Label(pr_canvas_ed, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

                            lst_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            lst_nm_ent.delete(0,END)
                            lst_nm_ent.insert(0,edi_dtl[6])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

                            usr_nm_lb=Label(pr_canvas_ed, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

                            usr_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            usr_nm_ent.delete(0,END)
                            usr_nm_ent.insert(0,edi_dtl[4])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

                            pr_new_pass_lb=Label(pr_canvas_ed, text="Enter New Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_lb,tag=("pr_new_pass_lb"))

                            pr_new_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'),show="*",)
                            def pas_val_fun2(value):
            
                                pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                pr_new_pass_ent.config(fg="black")
                                return True

                            def pass_inval_fun2():
                                pr_new_pass_ent.config(fg="red")

                            pas_val2 = (pr_canvas_ed.register(pas_val_fun2), '%P')
                            pass_inval2 = (pr_canvas_ed.register(pass_inval_fun2),)

                            pr_new_pass_ent.config(validate='focusout', validatecommand=pas_val2, invalidcommand=pass_inval2)
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_ent,tag=("pr_new_pass_ent"))


                            # #------------------------------------------------------------------------------------------------COMPANY SECTION
                            cmp_hd=Label(pr_canvas_ed, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

                            cmp_nm_lb=Label(pr_canvas_ed, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

                            cmp_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_nm_ent.delete(0,END)
                            cmp_nm_ent.insert(0,edi_cmp_dtl[1])
                            
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

                            cmp_cty_lb=Label(pr_canvas_ed, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

                            cmp_cty_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_cty_ent.delete(0,END)
                            cmp_cty_ent.insert(0,edi_cmp_dtl[3])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

                            cmp_pin_lb=Label(pr_canvas_ed, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

                            cmp_pin_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_pin_ent.delete(0,END)
                            cmp_pin_ent.insert(0,edi_cmp_dtl[5])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

                            cmp_ph_lb=Label(pr_canvas_ed, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

                            cmp_ph_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_ph_ent.delete(0,END)
                            cmp_ph_ent.insert(0,edi_cmp_dtl[7])
                            def validate_telb512(value):
            
                                    pattern = r'^[0-9]\d{9}$'
                                    if re.fullmatch(pattern, value) is None:
                                        
                                        return False
                                    cmp_ph_ent.config(fg="black")
                                    return True

                            def on_invalid_telb512():
                                    cmp_ph_ent.config(fg="red")
                                    
                            v_tel_cmd = (pr_canvas_ed.register(validate_telb512), '%P')
                            iv_tel_cmd = (pr_canvas_ed.register(on_invalid_telb512),)
                            cmp_ph_ent.config(validate='focusout', validatecommand=v_tel_cmd, invalidcommand=iv_tel_cmd)
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

                            cmp_indest_lb=Label(pr_canvas_ed, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

                            cmp_indest_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_indest_ent.delete(0,END)
                            cmp_indest_ent.insert(0,edi_cmp_dtl[10])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

                            # #----------------------------------------------------------------------------------------------------RIGHT SIDE
                            cmp_addr_lb=Label(pr_canvas_ed, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

                            cmp_addr_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_addr_ent.delete(0,END)
                            cmp_addr_ent.insert(0,edi_cmp_dtl[2])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

                            cmp_st_lb=Label(pr_canvas_ed, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

                            cmp_st_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_st_ent.delete(0,END)
                            cmp_st_ent.insert(0,edi_cmp_dtl[4])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

                            cmp_em_lb=Label(pr_canvas_ed, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

                            cmp_em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_em_ent.delete(0,END)
                            cmp_em_ent.insert(0,edi_cmp_dtl[6])
                            def validateb2113(value):
            
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                cmp_em_ent.config(fg="black")
                                return True

                            def on_invalidb2113():
                                
                                cmp_em_ent.config(fg="red")

                            vcmdb2113 = (pr_canvas_ed.register(validateb2113), '%P')
                            ivcmdb2113 = (pr_canvas_ed.register(on_invalidb2113),)
                            cmp_em_ent.config(validate='focusout', validatecommand=vcmdb2113, invalidcommand=ivcmdb2113) 

                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

                            cmp_lg_nm=Label(pr_canvas_ed, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

                            cmp_lg_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_lg_ent.delete(0,END)
                            cmp_lg_ent.insert(0,edi_cmp_dtl[9])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

                            cmp_typ_lb=Label(pr_canvas_ed, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

                            cmp_typ_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_typ_ent.delete(0,END)
                            cmp_typ_ent.insert(0,edi_cmp_dtl[11])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))

                            cmp_file_lb=Label(pr_canvas_ed, text="File",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_lb,tag=("cmp_file_lb"))
                            def fil_ents(event):
                                sql_log_sql='select * from auth_user where username=%s'
                                vals=(nm_ent.get(),)
                                fbcursor.execute(sql_log_sql,vals)
                                check_logins=fbcursor.fetchone()
                                cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                                logo_crp=cmp_logo.split('/',-1)
                                
                                im1 = Image.open(r""+cmp_logo) 
                                im1 = im1.save("profilepic/propic"+str(check_logins[0])+".png")

                                cmp_file_ent.delete("0",END)
                                cmp_file_ent.insert(0,logo_crp[-1])

                            cmp_file_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_file_ent.delete(0,END)
                            cmp_file_ent.insert(0,edi_cmp_dtl[8])
                            cmp_file_ent.bind("<Button-1>",fil_ents)
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_ent,tag=("cmp_file_ent"))


                            btn_edit = Button(pr_canvas_ed, text='Update Profile', command=update_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))

                        
                        selected_indices = lst_prf.curselection()
                        selected_langs = ",".join([lst_prf.get(i) for i in selected_indices])
                        lst_prf.place_forget()

                        def pr_responsive_widgets(event):
                                
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/13
                                y2 = dheight/.6

                                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )                   
                
                                dcanvas.coords("my_pro",dwidth/2.3,dheight/13)
                                dcanvas.coords("pr_img",dwidth/2.3,dheight/5)

                                dcanvas.coords("pr_hr_l",dwidth/16,dheight/6.5,dwidth/1.07,dheight/6.5)
                                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                                
                                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)

                                #-------------------------------------------------------------------------company section
                                dcanvas.coords("cmp_hd",dwidth/20,dheight/1.32)
                                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/1.22)
                                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/1.16)
                                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/1.07)
                                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/1.02)
                                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/.95)
                                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.91)
                                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.86)
                                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.83)
                                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.78)
                                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.755)

                                #--------------------------------------------------------------------------company right

                                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/1.22)
                                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/1.16)
                                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/1.07)
                                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/1.02)
                                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/.95)
                                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.91)
                                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.86)
                                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.83)
                                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.78)
                                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.755)
                                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.71)

                        if selected_langs=="Profile":
                            # canvas.pack_forget()
                            # myscrollbar.pack_forget()
                            # Sys_mains_frame.pack_forget()
                            
                            sql_pro="select * from auth_user where username=%s"
                            sql_pro_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pro,sql_pro_val,)
                            pro_dtl=fbcursor.fetchone()

                            sql_pro_cmp="select * from app1_company where id_id=%s"
                            sql_pro_cmp_val=(pro_dtl[0],)
                            fbcursor.execute(sql_pro_cmp,sql_pro_cmp_val,)
                            pro_cmp_dtl=fbcursor.fetchone()
                            
                            global Sys_mains_frame_pr
                            Sys_mains_frame_pr=Frame(tab1, height=750,bg="#2f516f",)
                            Sys_mains_frame_pr.grid(row=0,column=0,sticky='nsew')
                            Sys_mains_frame_pr.grid_rowconfigure(0,weight=1)
                            Sys_mains_frame_pr.grid_columnconfigure(0,weight=1)

                            pr_canvas=Canvas(Sys_mains_frame_pr,height=700,width=1340,scrollregion=(0,0,700,1300),bg="#2f516f",border=0)
                            pr_canvas.bind("<Configure>", pr_responsive_widgets)
                            
                            pr_myscrollbar=Scrollbar(Sys_mains_frame_pr,orient="vertical",command=pr_canvas.yview)
                            pr_canvas.configure(yscrollcommand=pr_myscrollbar.set)

                            pr_myscrollbar.pack(side="right",fill="y")
                            pr_canvas.pack(fill=X)

                            rth2 = pr_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",smooth=True,tags=("bg_polygen_pr"))

                            grd1c=Label(pr_canvas, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                            win_inv1 = pr_canvas.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

                            pr_canvas.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
                            #----------------------------------------------------------------------------------------Personal info

            
                            pr_img=Label(pr_canvas, image = prof_pics,bg="#213b52",width=170,height=170, anchor="center",)
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_img,tags=("pr_img"))

                            pr_hd=Label(pr_canvas, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

                            fir_name=Label(pr_canvas, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

                            fr_name_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            fr_name_ent.delete(0,END)
                            fr_name_ent.insert(0,pro_dtl[5])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

                            pr_em_lb=Label(pr_canvas, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

                            em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            em_ent.delete(0,END)
                            em_ent.insert(0,pro_dtl[7])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

                            last_nm_lb=Label(pr_canvas, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

                            lst_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            lst_nm_ent.delete(0,END)
                            lst_nm_ent.insert(0,pro_dtl[6])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

                            usr_nm_lb=Label(pr_canvas, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

                            usr_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            usr_nm_ent.delete(0,END)
                            usr_nm_ent.insert(0,pro_dtl[4])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

                            #------------------------------------------------------------------------------------------------COMPANY SECTION
                            cmp_hd=Label(pr_canvas, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

                            cmp_nm_lb=Label(pr_canvas, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

                            cmp_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_nm_ent.delete(0,END)
                            cmp_nm_ent.insert(0,pro_cmp_dtl[1])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

                            cmp_cty_lb=Label(pr_canvas, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

                            cmp_cty_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_cty_ent.delete(0,END)
                            cmp_cty_ent.insert(0,pro_cmp_dtl[3])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

                            cmp_pin_lb=Label(pr_canvas, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

                            cmp_pin_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_pin_ent.delete(0,END)
                            cmp_pin_ent.insert(0,pro_cmp_dtl[5])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

                            cmp_ph_lb=Label(pr_canvas, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

                            cmp_ph_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_ph_ent.delete(0,END)
                            cmp_ph_ent.insert(0,pro_cmp_dtl[7])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

                            cmp_indest_lb=Label(pr_canvas, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

                            cmp_indest_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_indest_ent.delete(0,END)
                            cmp_indest_ent.insert(0,pro_cmp_dtl[10])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

                            #----------------------------------------------------------------------------------------------------RIGHT SIDE
                            cmp_addr_lb=Label(pr_canvas, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

                            cmp_addr_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_addr_ent.delete(0,END)
                            cmp_addr_ent.insert(0,pro_cmp_dtl[2])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

                            cmp_st_lb=Label(pr_canvas, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

                            cmp_st_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_st_ent.delete(0,END)
                            cmp_st_ent.insert(0,pro_cmp_dtl[4])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

                            cmp_em_lb=Label(pr_canvas, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

                            cmp_em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_em_ent.delete(0,END)
                            cmp_em_ent.insert(0,pro_cmp_dtl[6])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

                            cmp_lg_nm=Label(pr_canvas, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

                            cmp_lg_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_lg_ent.delete(0,END)
                            cmp_lg_ent.insert(0,pro_cmp_dtl[9])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

                            cmp_typ_lb=Label(pr_canvas, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

                            cmp_typ_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_typ_ent.delete(0,END)
                            cmp_typ_ent.insert(0,pro_cmp_dtl[11])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))


                            btn_edit = Button(pr_canvas, text='Edit Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))
                        
                        elif selected_langs=="Log Out":
                            
                            Sys_top_frame2.pack_forget()
                            Sys_top_frame.pack_forget()
                            main_frame_signin.pack(fill=X,)
                        elif selected_langs== "Dashboard":
                            try:
                                
                                Sys_mains_frame_pr.grid_forget()
                            except:
                                pass
                            try:
                                Sys_mains_frame_pr_ed.grid_forget()
                            except:
                                pass
                            

                        else:
                            pass
                    def profile2():
                        lst_prf.place_forget()
                        srh_btn4 = Button(tp_lb_npr,image=dash_prof_pics, bg="White", fg="black",command=profile)
                        srh_btn4.grid(row=0,column=2,padx=15)
                    def profile():
                        # create a list box
                        langs = ("Dashboard","Profile","Log Out")

                        langs_var = StringVar(value=langs)
                        global lst_prf
                        lst_prf = Listbox(root,listvariable=langs_var,height=3 ,selectmode='extended',bg="black",fg="white")

                        lst_prf.place(relx=0.90, rely=0.10)
                        lst_prf.bind('<<ListboxSelect>>', lst_prf_slt)
                        srh_btn.grid_forget()
                        srh_btn2 = Button(tp_lb_npr,image=dash_prof_pics, bg="White", fg="black",command=profile2)
                        srh_btn2.grid(row=0,column=2,padx=15)
                
                    srh_btn = Button(tp_lb_npr,image=dash_prof_pics, bg="White", fg="black",command=profile)
                    srh_btn.grid(row=0,column=2,padx=15)

                    Sys_top_frame2=Frame(root, height=10,bg="#213b52")
                    Sys_top_frame2.pack(fill=X,)
                    
                    s = ttk.Style()
                    s.theme_use('default')
                    s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=150,anchor="center", padding=5)
                    s.map('TNotebook.Tab',background=[("selected","#2f516f")])
                    def right_nav():
                        
                        tabControl.pack_forget()
                        btn_nav.place_forget()
                        tabControl2.pack(expand = 1, fill ="both")
                        btn_nav2.place(relx=0, rely=0)
                        try:
                            btn_nav3.place_forget()
                        except:
                            pass
                    def left_nav():
                        
                        tabControl2.pack_forget()
                        btn_nav2.place_forget()
                        tabControl.pack(expand = 1, fill ="both")
                        global btn_nav3
                        btn_nav3=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
                        btn_nav3.place(relx=0.97, rely=0)

                    tabControl = ttk.Notebook(Sys_top_frame2)
                    tab1 = ttk.Frame(tabControl)
                    tab2 = ttk.Frame(tabControl)
                    tab3=  ttk.Frame(tabControl)
                    tab4 = ttk.Frame(tabControl)
                    tab5 = ttk.Frame(tabControl)
                    tab6=  ttk.Frame(tabControl)
                    tab7 = ttk.Frame(tabControl)
                    tab8 = ttk.Frame(tabControl)
                    
                    
                    btn_nav=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
                    btn_nav.place(relx=0.97, rely=0)
                    tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
                    tabControl.add(tab2,compound = LEFT, text ='Banking')
                    tabControl.add(tab3,compound = LEFT, text ='Sales')
                    tabControl.add(tab4,compound = LEFT, text ='Expenses')
                    tabControl.add(tab5,compound = LEFT, text ='Payroll') 
                    tabControl.add(tab6,compound = LEFT, text ='Report')
                    tabControl.add(tab7,compound = LEFT, text ='Taxes')
                    tabControl.add(tab8,compound = LEFT, text ='Accounting')
                    
                    tabControl.pack(expand = 1, fill ="both")


                    
                    tabControl2 = ttk.Notebook(Sys_top_frame2)
                    tab9 =  ttk.Frame(tabControl2)
                    tab10=  ttk.Frame(tabControl2)
                    tab11 = ttk.Frame(tabControl2)
                    tab12=  ttk.Frame(tabControl2)
                    tab13 = ttk.Frame(tabControl2)
                    tab14 = ttk.Frame(tabControl2)
                    tab15 =  ttk.Frame(tabControl2)

                    btn_nav2=Button(Sys_top_frame2,text="<<", command=left_nav, width=3, bg="#213b52",fg="white")
                    
                        
                    tabControl2.add(tab9,compound = LEFT, text ='My Account')
                    tabControl2.add(tab10,compound = LEFT, text ='Cash Management')
                    tabControl2.add(tab11,compound = LEFT, text ='Production')
                    tabControl2.add(tab12,compound = LEFT, text ='Quality Management')
                    tabControl2.add(tab13,compound = LEFT, text ='Project Management')
                    tabControl2.add(tab14,compound = LEFT, text ='Usage Decisions')
                    tabControl2.add(tab15,compound = LEFT, text ='Account & Payable')

                
                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Dash Board}
                    tab1.grid_columnconfigure(0,weight=1)
                    tab1.grid_rowconfigure(0,weight=1)
                    
                    Sys_mains_frame=Frame(tab1,bg="#2f516f",)
                    Sys_mains_frame.grid(row=0,column=0,sticky='nsew')
                    
                    def responsive_wid(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                    
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/13
                        y2 = dheight/6

                        dcanvas.coords("bg_polygen_dash",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )                    

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/3.1
                        y1 = dheight/5
                        y2 = dheight/1.1

                        dcanvas.coords("bg_polygen_dash1",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/2.95
                        x2 = dwidth/1.529
                        y1 = dheight/5
                        y2 = dheight/1.1

                        dcanvas.coords("bg_polygen_dash2",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/1.49
                        x2 = dwidth/1.021
                        y1 = dheight/5
                        y2 = dheight/1.1

                        dcanvas.coords("bg_polygen_dash3",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/3.1
                        y1 = dheight/1.06
                        y2 = dheight/.59
                        
                        #-----------------------------------------second row
                        dcanvas.coords("bg_polygen_dash4",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/2.95
                        x2 = dwidth/1.529
                        y1 = dheight/1.06
                        y2 = dheight/.59

                        dcanvas.coords("bg_polygen_dash5",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/1.49
                        x2 = dwidth/1.021
                        y1 = dheight/1.06
                        y2 = dheight/.59

                        dcanvas.coords("bg_polygen_dash6",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        dcanvas.coords("head_lb",dwidth/2,dheight/8.4)
                    
                        
                        dcanvas.coords("prf_lb",dwidth/53,dheight/4.7)
                        
                        dcanvas.coords("prf_hr",dwidth/53,dheight/3.7,dwidth/3.15,dheight/3.7)
                        dcanvas.coords("net_prf",dwidth/53,dheight/3.2)
                        dcanvas.coords("graph",dwidth/53,dheight/2.2)
                        #--------------------------------------------------------------second
                        dcanvas.coords("exp_hd_lb",dwidth/2.9,dheight/4.7)
                        dcanvas.coords("exp_hr",dwidth/2.9,dheight/3.7,dwidth/1.54,dheight/3.7)
                        dcanvas.coords("graph_2",dwidth/2.9,dheight/2.2)
                        
                        #-----------------------------------------------------------third
                        dcanvas.coords("bnk_lb",dwidth/1.48,dheight/4.7)
                        dcanvas.coords("bank_hr",dwidth/1.48,dheight/3.7,dwidth/1.03,dheight/3.7)
                        dcanvas.coords("inv_lb4",dwidth/1.48,dheight/3.5)
                        dcanvas.coords("inv_lb5",dwidth/1.48,dheight/3)
                        dcanvas.coords("graph9",dwidth/1.48,dheight/2.2)
                        
                        #--------------------------------------------------------------forth
                        dcanvas.coords("incom_lb",dwidth/53,dheight/1.04)
                        
                        dcanvas.coords("incom_hr",dwidth/53,dheight/0.98,dwidth/3.15,dheight/0.98)

                    
                        dcanvas.coords("graph_4",dwidth/53,dheight/0.85)
                
                        #-------------------------------------------------------------fifth
                        dcanvas.coords("inv_lb",dwidth/2.9,dheight/1.04)
                        dcanvas.coords("invs_hr",dwidth/2.9,dheight/0.98,dwidth/1.54,dheight/0.98)
                        dcanvas.coords("inv_lb2",dwidth/2.9,dheight/0.95)
                        dcanvas.coords("inv_lb3",dwidth/2.9,dheight/0.90)
                        dcanvas.coords("graph_5",dwidth/2.9,dheight/0.85)
                        #-------------------------------------------------------------sixth
                        dcanvas.coords("sales_lb",dwidth/1.48,dheight/1.04)
                        dcanvas.coords("sales_hr",dwidth/1.48,dheight/0.98,dwidth/1.03,dheight/0.98)
                        
                        


                        dcanvas.coords("grapg_6",dwidth/1.48,dheight/0.85)
                            
                    Sys_mains_frame.grid_rowconfigure(0,weight=1)
                    Sys_mains_frame.grid_columnconfigure(0,weight=1)

                    canvas = Canvas(Sys_mains_frame,height=700,bg='#2f516f',scrollregion=(0,0,700,1200))
                    sr_Scroll = Scrollbar(Sys_mains_frame,orient=VERTICAL)
                    sr_Scroll.grid(row=0,column=1,sticky='ns')
                    sr_Scroll.config(command=canvas.yview)
                    canvas.bind("<Configure>", responsive_wid)
                    canvas.config(yscrollcommand=sr_Scroll.set)
                    canvas.grid(row=0,column=0,sticky='nsew')

                    

                    cmp_name=Label(canvas, text=dtl_cmp_pro[1],bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                
                    win_inv1 = canvas.create_window(0, 0, anchor="center", window=cmp_name,tag=("head_lb"))

                    

                    
                    rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash"),smooth=True,)
                    # #----------------------------------------------------------------------------------------------------------------grid 1
                    rth1 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash1"),smooth=True,)
                    #-------------------------------------------------------Income
                    sql_incomes="select sum(balance) from app1_accounts1 where cid_id=%s and detype='Income'"
                    sql_incomes_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_incomes,sql_incomes_val,)
                    incom_dtls=fbcursor.fetchone()
                    
                    if incom_dtls[0]==None or incom_dtls[0]=='':
                        tot_inc=0.0
                    else:
                        tot_inc=incom_dtls[0]
                    
                
                    #-----------------------------------------------------expense
                    sql_pro="select sum(balance) from app1_accounts1 where cid_id=%s and detype='Expenses'"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    exp_tot=fbcursor.fetchone()
                
                    if exp_tot[0]==None or exp_tot[0]=="":
                        total_exp=0.0
                    else:
                        total_exp=exp_tot[0]

                    prf_lb=Label(canvas, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=prf_lb, tag=("prf_lb"))

                    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("prf_hr") )
                    
                    try:
                        incomes=float(tot_inc)-float(total_exp)
                    except:
                        incomes=0.0
                
                    try:
                        if float(tot_inc) > float(total_exp):

                            net_prf=Label(canvas, text="NET INCOME: ???"+str(incomes),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                        else:
                            net_prf=Label(canvas, text="NET LOSS: ???"+str(incomes),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    except:
                        net_prf=Label(canvas, text="NET INCOME: ???"+str(incomes),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=net_prf,tag=("net_prf"))

                    figlast = plt.figure(figsize=(8, 4), dpi=50) 


                    x="Income"
                    
                    y=tot_inc
                    plt.barh(x,y, label="Undefined", color="#92a1ae") 
                    plt.legend()
                
                    plt.ylabel("")
                    axes=plt.gca()
                    axes.xaxis.grid()

                    x="Expense"
            
                    try:
                        if exp_tot[0]==None or exp_tot[0]=="":
                            y=0.0
                        else:
                            y=exp_tot[0]
                    except:
                        y=0.0
                    plt.barh(x,y, color="#506579") 
                    plt.legend()
                
                    plt.ylabel("")
                    axes=plt.gca()
                    axes.xaxis.grid()
                    figlast.set_facecolor("#213b52")
                    axes.set_facecolor("#213b52")
                    
                            

                    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph"))
                    # #----------------------------------------------------------------------------------------------------------------grid 2
                    
                    
                    
                    
                    rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash2"),smooth=True,)

                    sql_pro="select sum(balance) from app1_accounts1 where cid_id=%s and detype='Expenses'"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    exp_tots=fbcursor.fetchone()
                    

                    if exp_tots[0] is None:
                            ttl=0.0
                    else:
                            ttl=exp_tots[0]
                
                    try:
                        exp_hd_lb=Label(canvas, text="EXPENSES: ???"+str(ttl),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    except:
                        exp_hd_lb=Label(canvas, text="EXPENSES: ???0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=exp_hd_lb, tag=("exp_hd_lb"))
                    canvas.create_line(0, 0, 0, 0,fill="gray" ,tag=("exp_hr"))
                    fig, ax = plt.subplots(figsize=(8, 4), dpi=50)

                    sql_typ="select balance from app1_accounts1 where cid_id=%s and detype='Expenses'"
                    sql_typ_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_typ,sql_typ_val,)
                    exp_typ=fbcursor.fetchall()

                    sql_typs="select name from app1_accounts1 where cid_id=%s and detype='Expenses'"
                    sql_typs_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_typs,sql_typs_val,)
                    exp_typs=fbcursor.fetchall()
                    
                    
                    try:
                        sql_typs="select name from app1_accounts1 where cid_id=%s and detype='Expenses'"
                        sql_typs_val=(dtl_cmp_pro[0],)
                        fbcursor.execute(sql_typs,sql_typs_val,)
                        exp_typs=fbcursor.fetchall()
                        
                        labels = []
                        for i in exp_typs:
                                labels.append(i[0])
                        size = 0.3
                        
                        arr = np.asarray(exp_typ)
                        vals = np.array(arr)
                    
                        cmap = plt.colormaps["tab20c"]
                        outer_colors = cmap(np.arange(3)*4)
                        
                        # inner_colors = cmap([1, 2, 5, 6, 9, 10])

                        ax.pie(vals.sum(axis=1), radius=1,labels=labels, colors=outer_colors,wedgeprops=dict(width=size, edgecolor='w'))

                        ax.set(aspect="equal", title='Cost Of Sales')
                    
                        fig.set_facecolor("#213b52")
                        ax.set_facecolor("#92a1ae")
                        

                        canvasbar = FigureCanvasTkAgg(fig, master=canvas)
                        
                        canvasbar.draw()
                        canvasbar.get_tk_widget()
                        win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_2"))
                    except:
                        size = 0.3
                        
                        vals = np.array([[60.]])
                    
                        cmap = plt.colormaps["tab20c"]
                        outer_colors = cmap(np.arange(3)*4)
                        
                        # inner_colors = cmap([1, 2, 5, 6, 9, 10])

                        ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,wedgeprops=dict(width=size, edgecolor='w'))

                        ax.set(aspect="equal", title='Cost Of Sales')
                    
                        fig.set_facecolor("#213b52")
                        ax.set_facecolor("#92a1ae")
                        

                        canvasbar = FigureCanvasTkAgg(fig, master=canvas)
                        
                        canvasbar.draw()
                        canvasbar.get_tk_widget()
                        win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_2"))

                    # #----------------------------------------------------------------------------------------------------------------grid 3
                    rth3 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash3"),smooth=True,)

                    bnk_lb=Label(canvas, text="BANK ACCOUNTS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=bnk_lb,tag=("bnk_lb"))
                    canvas.create_line(910, 195, 1290, 195,fill="gray",tag=("bank_hr"))
                    sql_pro="select sum(debit), sum(credit) from app1_bankstatement where cid_id=%s"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    bank_stm=fbcursor.fetchone()
                    if bank_stm[0]==None or bank_stm[0]=="":
                        debit=0.0
                    else:
                        debit=bank_stm[0]
                    if bank_stm[1]==None or bank_stm[1]=="":
                        credit=0.0
                    else:
                        credit=bank_stm[1]
                 

                    inv_lb2=Label(canvas, text="DEBIT:???"+str(debit),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb2, tag=("inv_lb4"))
                    inv_lb3=Label(canvas, text="CREDIT:???"+str(credit),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0,0 , anchor="nw", window=inv_lb3, tag=("inv_lb5"))

                    figlast = plt.figure(figsize=(8, 4), dpi=50) 
                    try:
                        x="Debit"
                        y=debit
                        plt.barh(x,y, label="Undefined", color="#92a1ae") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()

                        x="Credit"
                        y=credit
                        plt.barh(x,y, color="#506579") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()
                        figlast.set_facecolor("#213b52")
                        axes.set_facecolor("#213b52")
                    except:
                        x="Debit"
                        y=0
                        plt.barh(x,y, label="Undefined", color="#92a1ae") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()

                        x="Credit"
                        y=0
                        plt.barh(x,y, color="#506579") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()
                        figlast.set_facecolor("#213b52")
                        axes.set_facecolor("#213b52")

                    
                            

                    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph9"))
                    # #----------------------------------------------------------------------------------------------------------------grid 4
                    rth4 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash4"),smooth=True,)

                    sql_income="select sum(balance) from app1_accounts1 where cid_id=%s and detype='Income'"
                    sql_income_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_income,sql_pro_val,)
                    incom_dtls=fbcursor.fetchone()

                    if incom_dtls[0]==None or incom_dtls[0]=='':
                        tot_incm=0.0
                    else:
                        tot_incm=incom_dtls[0]

                    incom_lb=Label(canvas, text="INCOME: ???"+str(tot_incm),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=incom_lb,tag=("incom_lb"))
                    canvas.create_line(0, 0, 0, 0,fill="gray",tag=("incom_hr") )

                    sql_income_chart="select balance,name from app1_accounts1 where cid_id=%s and detype='Income'"
                    sql_income_chart_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_income_chart,sql_income_chart_val,)
                    incom_chart=fbcursor.fetchall()
                    
                    try:
                        sizes = []
                        for i in incom_chart:
                            sizes.append(i[0])
                    except:
                        sizes=0
                    sql_lb_chart="select name from app1_accounts1 where cid_id=%s and detype='Income'"
                    sql_lb_chart_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_lb_chart,sql_lb_chart_val,)
                    incom_chart_lb=fbcursor.fetchall()
                    try:
                        labels = []
                        for i in incom_chart_lb:
                            labels.append(i[0])
                    except:
                        pass
                    
                    
                    fig1, ax1 = plt.subplots(figsize=(8, 4), dpi=50)
                    patches, texts, autotexts =ax1.pie(sizes, autopct='%1.1f%%',labels=labels,
                    shadow=True, startangle=90)
                    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                    fig1.set_facecolor("#213b52")
                    ax1.set_facecolor("#92a1ae")
                
                    for text in texts:
                        text.set_color('white')
                    for autotext in autotexts:
                        autotext.set_color('black')

                    canvasbar = FigureCanvasTkAgg(fig1, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_4"))

                    # #----------------------------------------------------------------------------------------------------------------grid 5

                    sql_pro="select sum(amtrecvd), sum(baldue),min(invoicedate) from app1_invoice where cid_id=%s"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    exp_totl_inv=fbcursor.fetchone()

                    if exp_totl_inv[0]==None or exp_totl_inv[0]=='':
                        paid=0.0
                    else:
                        paid=exp_totl_inv[0]
                    if exp_totl_inv[1]==None or exp_totl_inv[1]=='':
                        unpaid=0.0
                    else:
                        unpaid=exp_totl_inv[1]

                    rth5 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash5"),smooth=True,)
                    inv_lb=Label(canvas, text="INVOICE",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb, tag=("inv_lb"))

                    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("invs_hr") )
                    inv_lb2=Label(canvas, text="UNPAID:???"+str(unpaid),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb2, tag=("inv_lb2"))
                    inv_lb3=Label(canvas, text="PAID:???"+str(paid),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0,0 , anchor="nw", window=inv_lb3, tag=("inv_lb3"))

                    figlast = plt.figure(figsize=(8, 4), dpi=50)
                    try:
                        x="Unpaid"
                        y=unpaid 
                        plt.barh(x,y, label="Undefined", color="#92a1ae") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()

                        x="Paid"
                        y=paid
                        plt.barh(x,y, color="#506579") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()
                        figlast.set_facecolor("#213b52")
                        axes.set_facecolor("#213b52")
                    except:
                        x="Unpaid"
                        y=0 
                        plt.barh(x,y, label="Undefined", color="#92a1ae") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()

                        x="Paid"
                        y=0
                        plt.barh(x,y, color="#506579") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()
                        figlast.set_facecolor("#213b52")
                        axes.set_facecolor("#213b52")

                    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(480, 780, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_5"))
                    #----------------------------------------------------------------------------------------------------------------grid 6
                    rth6 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash6"),smooth=True,)
                    

                    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("sales_hr") )
                    
                    if exp_totl_inv[2]==None or exp_totl_inv[2]=='':
                        dates_start=date.today()
                    else:
                        dates_start=exp_totl_inv[2] 
                    

                    sql_pro="select invoicedate from app1_invoice where cid_id=%s"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    sal_totl_inv=fbcursor.fetchall()

                    sql_prof="select sum(grandtotal) from app1_invoice where cid_id=%s "
                    sql_prof_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_prof,sql_prof_val,)
                    sal_totl_invs2=fbcursor.fetchone()
                    

                    if sal_totl_invs2[0]==None or sal_totl_invs2[0]=='':
                        tot_sal=0.0
                    else:
                        tot_sal=sal_totl_invs2[0]

                    
                   

                    sales_lb=Label(canvas, text="SALES ???"+str(tot_sal),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=sales_lb, tag=("sales_lb"))

                    
                    figlast = plt.figure(figsize=(8, 4), dpi=50)
                    try:
                        x = []
                        y = []
                        for i in sal_totl_inv:
                            x.append(i[0])
                    
                            sql_pros="select sum(grandtotal) from app1_invoice where cid_id=%s and invoicedate=%s "
                            sql_pros_val=(dtl_cmp_pro[0],i[0],)
                            fbcursor.execute(sql_pros,sql_pros_val,)
                            sal_totl_invs=fbcursor.fetchall()
                            
                            y.insert(-1,sal_totl_invs[0])
                        
                        
                        labels = x

                        plt.plot(x, y)
                        # You can specify a rotation for the tick labels in degrees or with keywords.
                        plt.xticks(x, labels, rotation='horizontal')
                        # Pad margins so that markers don't get clipped by the axes
                        plt.margins(0.2)
                        # Tweak spacing to prevent clipping of tick-labels
                        plt.subplots_adjust(bottom=0.15)
                        figlast.set_facecolor("#213b52")
                    
                    except:
                        x = [1,2]
                        y = [0,0]
                        
                        
                        
                        labels = x

                        plt.plot(x, y)
                        # You can specify a rotation for the tick labels in degrees or with keywords.
                        plt.xticks(x, labels, rotation='horizontal')
                        # Pad margins so that markers don't get clipped by the axes
                        plt.margins(0.2)
                        # Tweak spacing to prevent clipping of tick-labels
                        plt.subplots_adjust(bottom=0.15)
                        figlast.set_facecolor("#213b52")
                    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("grapg_6"))
                    
                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Banking Section(Tab2)

                    tab_bank = ttk.Notebook(tab2)
                    tab2_1 =  ttk.Frame(tab_bank)
                    tab2_2=  ttk.Frame(tab_bank)
                    tab2_3 = ttk.Frame(tab_bank)

                    tab_bank.add(tab2_1,compound = LEFT, text ='Online Banking')
                    tab_bank.add(tab2_2,compound = LEFT, text ='Offline banking')
                    tab_bank.add(tab2_3,compound = LEFT, text ='Bank Reconvilation')

                    
                    tab_bank.pack(expand = 1, fill ="both")

                    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Sales Tab}
                    tab_sales = ttk.Notebook(tab3)
                    tab3_1 =  ttk.Frame(tab_sales)
                    tab3_2=  ttk.Frame(tab_sales)
                    tab3_3 = ttk.Frame(tab_sales)
                    tab3_4=  ttk.Frame(tab_sales)
                    tab3_5=  ttk.Frame(tab_sales)
                    

                    
                        
                    tab_sales.add(tab3_1,compound = LEFT, text ='Sales Records')
                    tab_sales.add(tab3_2,compound = LEFT, text ='Estimate')
                    tab_sales.add(tab3_3,compound = LEFT, text ='Invoices')
                    tab_sales.add(tab3_4,compound = LEFT, text ='Customers')
                    tab_sales.add(tab3_5,compound = LEFT, text ='Product & Services')
                    
                
                    tab_sales.pack(expand = 1, fill ="both")

                    tab3_2.grid_columnconfigure(0,weight=1)
                    tab3_2.grid_rowconfigure(0,weight=1)

                
                    sr_Frame = Frame(tab3_2)
                    sr_Frame.grid(row=0,column=0,sticky='nsew')

                    def responsive_widgets_sales(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                        dcanvas.coords("line1", dwidth/31.6, dheight/2.002, dwidth/1.039, dheight/2.002)
                        dcanvas.coords("line17", dwidth/31.6, dheight/2.002, dwidth/31.6, dheight/1.274)
                        dcanvas.coords("line2", dwidth/31.6, dheight/1.797, dwidth/1.039, dheight/1.797)
                        dcanvas.coords("line3", dwidth/1.039, dheight/2.002, dwidth/1.039, dheight/1.274)
                        dcanvas.coords("line4", dwidth/31.6, dheight/1.63, dwidth/1.039, dheight/1.63)
                        dcanvas.coords("line5", dwidth/31.6, dheight/1.491, dwidth/1.039, dheight/1.491)
                        dcanvas.coords("line6", dwidth/31.6, dheight/1.374, dwidth/1.039, dheight/1.374)
                        dcanvas.coords("line7", dwidth/31.6, dheight/1.274, dwidth/1.039, dheight/1.274)
                        dcanvas.coords("line8", dwidth/7.92, dheight/2.002, dwidth/7.92, dheight/1.274)
                        dcanvas.coords("line9", dwidth/4.22, dheight/2.002, dwidth/4.22, dheight/1.274)
                        dcanvas.coords("line10", dwidth/3.2, dheight/2.002, dwidth/3.2, dheight/1.274)
                        dcanvas.coords("line11", dwidth/2.3, dheight/2.002, dwidth/2.3, dheight/1.274)
                        dcanvas.coords("line12", dwidth/1.9, dheight/2.002, dwidth/1.9, dheight/1.274)
                        dcanvas.coords("line13", dwidth/1.6, dheight/2.002, dwidth/1.6, dheight/1.274)
                        dcanvas.coords("line14", dwidth/1.38, dheight/2.002, dwidth/1.38, dheight/1.274)
                        dcanvas.coords("line15", dwidth/1.28, dheight/2.002, dwidth/1.28, dheight/1.274)
                        dcanvas.coords("line16", dwidth/1.14, dheight/2.002, dwidth/1.14, dheight/1.274)

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/14 
                        y2 = dheight/3.505

                        dcanvas.coords("poly1",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                        
                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.55


                        dcanvas.coords("poly2",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        dcanvas.coords("label1",dwidth/2,dheight/8.24)
                        dcanvas.coords("label2",dwidth/12.67,dheight/1.71)
                        dcanvas.coords("label3",dwidth/5.5,dheight/1.71)
                        dcanvas.coords("label4",dwidth/3.63,dheight/1.71)
                        dcanvas.coords("label5",dwidth/2.67,dheight/1.71)
                        dcanvas.coords("label6",dwidth/2.08,dheight/1.71)
                        dcanvas.coords("label7",dwidth/1.735,dheight/1.71)
                        dcanvas.coords("label8",dwidth/1.48,dheight/1.71)
                        dcanvas.coords("label9",dwidth/1.327,dheight/1.71)
                        dcanvas.coords("label10",dwidth/1.206,dheight/1.71)
                        
                        dcanvas.coords("label11",dwidth/12.67,dheight/1.894)
                        dcanvas.coords("label12",dwidth/5.5,dheight/1.894)
                        dcanvas.coords("label13",dwidth/3.63,dheight/1.894)
                        dcanvas.coords("label14",dwidth/2.67,dheight/1.894)
                        dcanvas.coords("label15",dwidth/2.08,dheight/1.894)
                        dcanvas.coords("label16",dwidth/1.735,dheight/1.894)
                        dcanvas.coords("label17",dwidth/1.48,dheight/1.894)
                        dcanvas.coords("label18",dwidth/1.327,dheight/1.894)
                        dcanvas.coords("label19",dwidth/1.206,dheight/1.894)
                        dcanvas.coords("label20",dwidth/1.088,dheight/1.894)


                        dcanvas.coords("combo1",dwidth/1.28,dheight/2.261)
                        dcanvas.coords("combo2",dwidth/1.115,dheight/2.261)

                        dcanvas.coords("tree_main",dwidth/40,dheight/2)

                    
                    
                    sr_Canvas = Canvas(sr_Frame,bg='#2f516f',scrollregion=(0,0,700,1200))

                    sr_Frame.grid_rowconfigure(0,weight=1)
                    sr_Frame.grid_columnconfigure(0,weight=1)

                    sr_Scroll = Scrollbar(sr_Frame,orient=VERTICAL)
                    sr_Scroll.grid(row=0,column=1,sticky='ns')
                    sr_Scroll.config(command=sr_Canvas.yview)
                    sr_Canvas.bind("<Configure>", responsive_widgets_sales)
                    sr_Canvas.config(yscrollcommand=sr_Scroll.set)
                    sr_Canvas.grid(row=0,column=0,sticky='nsew')


                    sr_Canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))

                    sr_label = Label(sr_Canvas,width=15,height=1,text="SALES RECORDS",font=('arial 25'),background="#1b3857",fg="white")
                    sr_label_win = sr_Canvas.create_window(0,0,anchor="c",window=sr_label,tags=("label1"))
                    sr_Canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

                    sr_Canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

                    sr_transCombo = ttk.Combobox(sr_Canvas,font=('arial 15'),width=14)
                    sr_transCombo['values'] = ['New Transactios','Invoice','Payment','Sales Receipt','Credit Note','Estimate','Delayed Charge','Time Activity']
                    sr_transCombo.current(0)
                    sr_transCombo.bind('<<ComboboxSelected>>',"sr_transCombo_options")
                    sr_transCombo_win = sr_Canvas.create_window(0,0,window=sr_transCombo,tags=("combo2"))

                    srt_actionCombo = ttk.Combobox(sr_Canvas,width=7,font=('arial 15'))
                    srt_actionCombo['values'] = ['Actions','Edit','Delete']
                    srt_actionCombo.current(0)
                    srt_actionCombo.bind("<<ComboboxSelected>>","sr_Actions")
                    sr_Canvas.create_window(0,0,window=srt_actionCombo,tags=("combo1"))

                    sr_tree_style = ttk.Style()
                    sr_tree_style.theme_use("default")
                    sr_tree_style.configure("Treeview",background="#2f516f",foreground="white",rowheight=25,font=(None,11),fieldbackground="#2f516f")
                    sr_tree_style.configure("Treeview.Heading",background="#1b3857",activeforeground="black",foreground="white",font=(None,11))
                    inv_scrollbar = Scrollbar(sr_Frame,orient="vertical")
                    
                    sr_tree = ttk.Treeview(sr_Canvas,height=30,columns=("0","1","2","3","4","5","6","7","8"),show="headings",yscrollcommand=inv_scrollbar.set)
                    sr_tree.column("0",width=110,anchor=CENTER)
                    sr_tree.column("1",width=150,anchor=CENTER)
                    sr_tree.column("2",width=110,anchor=CENTER)
                    sr_tree.column("3",width=230,anchor=CENTER)
                    sr_tree.column("4",width=110,anchor=CENTER)
                    sr_tree.column("5",width=150,anchor=CENTER)
                    sr_tree.column("6",width=140,anchor=CENTER)
                    sr_tree.column("7",width=110,anchor=CENTER)
                    sr_tree.column("8",width=150,anchor=CENTER)
                    sr_tree.heading("0",text="DATE")
                    sr_tree.heading("1",text="TYPE")
                    sr_tree.heading("2",text="NO.")
                    sr_tree.heading("3",text="CUSTOMER")
                    sr_tree.heading("4",text="DUE DATE")
                    sr_tree.heading("5",text="BALANCE")
                    sr_tree.heading("6",text="TOTAL BEFORE")
                    sr_tree.heading("7",text="TAX")
                    sr_tree.heading("8",text="TOTAL")

                    user_sql = "SELECT id FROM auth_user WHERE username=%s"
                    user_val = (nm_ent.get(),)
                    fbcursor.execute(user_sql,user_val)
                    user_data = fbcursor.fetchone()

                    comp_sql = 'SELECT cid FROM app1_company WHERE id_id=%s'
                    comp_val = (user_data[0],)
                    fbcursor.execute(comp_sql,comp_val)
                    comp_data = fbcursor.fetchone()

                    get_payment_sql = "SELECT * FROM app1_payment WHERE cid_id=%s"
                    get_payment_val = (comp_data[0],)
                    fbcursor.execute(get_payment_sql,get_payment_val)
                    get_payment_data = fbcursor.fetchall()
                    
                    get_srp_sql = "SELECT * FROM app1_salesrecpts WHERE cid_id=%s"
                    get_srp_val = (comp_data[0],)
                    fbcursor.execute(get_srp_sql,get_srp_val)
                    get_srp_data = fbcursor.fetchall()

                    get_crdn_sql = "SELECT * FROM app1_credit WHERE cid_id=%s"
                    get_crdn_val = (comp_data[0],)
                    fbcursor.execute(get_crdn_sql,get_crdn_val)
                    get_crdn_data = fbcursor.fetchall()

                    get_est_sql = "SELECT * FROM app1_estimate WHERE cid_id=%s"
                    get_est_val = (comp_data[0],)
                    fbcursor.execute(get_est_sql,get_est_val)
                    get_est_data = fbcursor.fetchall()

                    get_dc_sql = "SELECT * FROM app1_delayedcharge WHERE cid_id=%s"
                    get_dc_val = (comp_data[0],)
                    fbcursor.execute(get_dc_sql,get_dc_val)
                    get_dc_data = fbcursor.fetchall()

                    get_ta_sql = "SELECT * FROM app1_timeactsale WHERE cid_id=%s"
                    get_ta_val = (comp_data[0],)
                    fbcursor.execute(get_ta_sql,get_ta_val)
                    get_ta_data = fbcursor.fetchall()

                    inv_scrollbar.config(command=sr_tree.yview)
                    inv_scrollbar.grid(row=0,column=2,sticky='ns')

                    for child in sr_tree.get_children():
                        sr_tree.delete(child)
                    
                    
                    

                    #3333333333333333333333333333333333333333333333333333333333333333333333333333{{Customer Module}}
                    tab3_2.grid_columnconfigure(0,weight=1)
                    tab3_2.grid_rowconfigure(0,weight=1)

                
                    estm_Frame = Frame(tab3_2)
                    estm_Frame.grid(row=0,column=0,sticky='nsew')

                    def responsive_widgets_estm(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                        

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/14 
                        y2 = dheight/3.505

                        dcanvas.coords("poly1",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                        
                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.55


                        dcanvas.coords("poly2",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        dcanvas.coords("label1",dwidth/2,dheight/8.24)
                        dcanvas.coords("combo1",dwidth/1.28,dheight/2.261)
                        dcanvas.coords("button_estm",dwidth/1.1,dheight/2.261)
                        dcanvas.coords("srh_top",dwidth/9,dheight/2.261)
                        dcanvas.coords("srh_btn6",dwidth/5,dheight/2.261)
                        dcanvas.coords("estmt_srhCombo",dwidth/3.7,dheight/2.261)
                        
                        
                     
                        dcanvas.coords("tree_main",dwidth/40,dheight/2)

                    def create_stm():

                            sr_Canvas_1 = Canvas(estm_Frame,bg='#2f516f',scrollregion=(0,0,700,2500))

                            def responsive_widgets1(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                                
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("poly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.35


                                dcanvas.coords("poly3",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )
                                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                                dcanvas.coords("label2",dwidth/2,dheight/2.4)

                                

                                #sales receipt-----------
                                try:
                                    dcanvas.coords("label21",dwidth/7.91,dheight/1.76)
                                    dcanvas.coords("label22",dwidth/2.47,dheight/1.76)
                                    dcanvas.coords("label23",dwidth/6.13,dheight/1.44)
                                    dcanvas.coords("label24",dwidth/2.27,dheight/1.45)
                                    dcanvas.coords("label25",dwidth/6.13,dheight/0.907)
                                    dcanvas.coords("label26",dwidth/6.13,dheight/0.81)
                                    dcanvas.coords("label27",dwidth/2.27,dheight/0.81)
                                    try:
                                        dcanvas.coords("label28",dwidth/1.395,dheight/0.81)
                                    except:
                                        pass
                                    dcanvas.coords("label29",dwidth/1.225,dheight/1.75)
                                    dcanvas.coords("label30",dwidth/1.2,dheight/1.63)
                                    dcanvas.coords("label31",dwidth/20,dheight/0.675)
                                    dcanvas.coords("label32",dwidth/20,dheight/0.62)
                                    dcanvas.coords("label64",dwidth/20,dheight/0.565)
                                    dcanvas.coords("label65",dwidth/20,dheight/0.519)
                                    dcanvas.coords("label66",dwidth/20,dheight/0.481)
                                    dcanvas.coords("label67",dwidth/2.06,dheight/0.6)
                                    dcanvas.coords("label68",dwidth/2.06,dheight/0.549)
                                    dcanvas.coords("label69",dwidth/2.06,dheight/0.506)
                                    dcanvas.coords("label70",dwidth/2.06,dheight/0.47)
                                    dcanvas.coords("label33",dwidth/7.91,dheight/0.675)
                                    dcanvas.coords("label34",dwidth/4.2,dheight/0.675)
                                    dcanvas.coords("label35",dwidth/2.74,dheight/0.675)
                                    dcanvas.coords("label36",dwidth/2.07,dheight/0.675)
                                    dcanvas.coords("label37",dwidth/1.68,dheight/0.675)
                                    dcanvas.coords("label38",dwidth/1.39,dheight/0.675)
                                    dcanvas.coords("label39",dwidth/1.205,dheight/0.675)
                                    dcanvas.coords("label40",dwidth/1.52,dheight/0.436)
                                    dcanvas.coords("label41",dwidth/1.52,dheight/0.412)
                                    dcanvas.coords("label42",dwidth/1.52,dheight/0.3905)
                                    dcanvas.coords("label435",dwidth/1.54,dheight/1.45)
                                    dcanvas.coords("label25ref",dwidth/1.18,dheight/1.45)

                                    

                                    dcanvas.coords("label44",dwidth/20,dheight/1.135)
                                    dcanvas.coords("label45",dwidth/20,dheight/1.03)
                                    dcanvas.coords("label46",dwidth/7.4,dheight/1.135)
                                    dcanvas.coords("label47",dwidth/3.342,dheight/1.135)
                                    dcanvas.coords("label48",dwidth/2.19,dheight/1.135)
                                    dcanvas.coords("label49",dwidth/1.68,dheight/1.135)
                                    dcanvas.coords("label50",dwidth/1.328,dheight/1.135)
                                    dcanvas.coords("label51",dwidth/1.11,dheight/1.135)
                                    dcanvas.coords("label52",dwidth/1.41,dheight/0.83)
                                    dcanvas.coords("label53",dwidth/1.41,dheight/0.77)
                                    dcanvas.coords("label54",dwidth/1.41,dheight/0.715)

                                    dcanvas.coords("label55",dwidth/2.4,dheight/2.254)
                                    dcanvas.coords("label56",dwidth/1.49,dheight/2.254)
                                    dcanvas.coords("label57",dwidth/2.4,dheight/1.8)
                                    dcanvas.coords("label58",dwidth/2.4,dheight/1.5)
                                    dcanvas.coords("label59",dwidth/2.4,dheight/1.28)
                                    dcanvas.coords("label60",dwidth/1.598,dheight/1.28)
                                    dcanvas.coords("label61",dwidth/1.212,dheight/1.28)
                                    dcanvas.coords("label62",dwidth/2.4,dheight/1.105)
                                    dcanvas.coords("label63",dwidth/2.4,dheight/0.979)

                                    dcanvas.coords("entry13",dwidth/2.72,dheight/1.68)
                                    dcanvas.coords("entry14",dwidth/11,dheight/1.39)
                                    dcanvas.coords("entry15",dwidth/11,dheight/0.885)
                                    dcanvas.coords("entry16",dwidth/11,dheight/0.79)
                                    dcanvas.coords("entry17",dwidth/2.72,dheight/0.79)
                                    dcanvas.coords("entry18",dwidth/5.13,dheight/0.63)
                                    dcanvas.coords("entry19",dwidth/3.39,dheight/0.63)
                                    dcanvas.coords("entry20",dwidth/2.24,dheight/0.63)
                                    dcanvas.coords("entry21",dwidth/1.85,dheight/0.63)
                                    dcanvas.coords("entry22",dwidth/1.5,dheight/0.63)
                                    dcanvas.coords("entry39",dwidth/5.13,dheight/0.5745)
                                    dcanvas.coords("entry40",dwidth/3.39,dheight/0.5745)
                                    dcanvas.coords("entry41",dwidth/2.24,dheight/0.5745)
                                    dcanvas.coords("entry42",dwidth/1.85,dheight/0.5745)
                                    dcanvas.coords("entry43",dwidth/1.5,dheight/0.5745)
                                    dcanvas.coords("entry44",dwidth/5.13,dheight/0.527)
                                    dcanvas.coords("entry45",dwidth/3.39,dheight/0.527)
                                    dcanvas.coords("entry46",dwidth/2.24,dheight/0.527)
                                    dcanvas.coords("entry47",dwidth/1.85,dheight/0.527)
                                    dcanvas.coords("entry48",dwidth/1.5,dheight/0.527)
                                    dcanvas.coords("entry49",dwidth/5.13,dheight/0.487)
                                    dcanvas.coords("entry50",dwidth/3.39,dheight/0.487)
                                    dcanvas.coords("entry51",dwidth/2.24,dheight/0.487)
                                    dcanvas.coords("entry52",dwidth/1.85,dheight/0.487)
                                    dcanvas.coords("entry53",dwidth/1.5,dheight/0.487)

                                    dcanvas.coords("entry23",dwidth/1.35,dheight/0.45)
                                    dcanvas.coords("entry24",dwidth/1.35,dheight/0.435)
                                    dcanvas.coords("entry25",dwidth/1.35,dheight/0.422)
                                    dcanvas.coords("est_entry11",dwidth/1.35,dheight/0.41)
                                    dcanvas.coords("est_entry12",dwidth/1.35,dheight/0.398)
                                    dcanvas.coords("est_entry13",dwidth/1.35,dheight/0.386)
                                    dcanvas.coords("label40",dwidth/1.45,dheight/0.445)
                                    dcanvas.coords("label41",dwidth/1.45,dheight/0.430)
                                    dcanvas.coords("label42",dwidth/1.45,dheight/0.418 )
                                    dcanvas.coords("label43",dwidth/1.60,dheight/0.406)
                                    dcanvas.coords("label44",dwidth/1.45,dheight/0.394)
                                    dcanvas.coords("label45",dwidth/1.46,dheight/0.382)
                                    dcanvas.coords("tcs_sltr",dwidth/1.55,dheight/0.41)
                                    dcanvas.coords("button3",dwidth/28,dheight/3)

                                    dcanvas.coords("entry26",dwidth/11,dheight/0.751)

                                    dcanvas.coords("entry27",dwidth/4.7,dheight/1.057)
                                    dcanvas.coords("entry28",dwidth/2.43,dheight/1.057)
                                    
                                    dcanvas.coords("entry29",dwidth/1.91,dheight/1.057)
                                    dcanvas.coords("entry30",dwidth/1.46,dheight/1.057)

                                    dcanvas.coords("entry31",dwidth/1.275,dheight/0.85)
                                    dcanvas.coords("entry32",dwidth/1.275,dheight/0.784)
                                    dcanvas.coords("entry33",dwidth/1.275,dheight/0.727)
                                    dcanvas.coords("entry34",dwidth/1.525,dheight/1.45)

                                    dcanvas.coords("entry35",dwidth/1.81,dheight/1.24)
                                    dcanvas.coords("entry54",dwidth/1.55,dheight/1.24)
                                    dcanvas.coords("entry36",dwidth/1.33,dheight/1.24)
                                    dcanvas.coords("entry55",dwidth/1.185,dheight/1.24)
                                    dcanvas.coords("entry37",dwidth/2.91,dheight/1.08)
                                    dcanvas.coords("entry56",dwidth/1.55,dheight/1.08)
                                    dcanvas.coords("entry38",dwidth/2.91,dheight/0.96)

                                    dcanvas.coords("combo3",dwidth/11,dheight/1.68)
                                    try:
                                        dcanvas.coords("combo4",dwidth/1.55,dheight/0.79)
                                    except:
                                        pass
                                    dcanvas.coords("combo5",dwidth/7.909,dheight/0.62)
                                    dcanvas.coords("combo6",dwidth/1.206,dheight/0.62)
                                    dcanvas.coords("combo14",dwidth/7.909,dheight/0.5655)
                                    dcanvas.coords("combo15",dwidth/1.206,dheight/0.5655)
                                    dcanvas.coords("combo16",dwidth/7.909,dheight/0.519)
                                    dcanvas.coords("combo17",dwidth/1.206,dheight/0.519)
                                    dcanvas.coords("combo18",dwidth/7.909,dheight/0.481)
                                    dcanvas.coords("combo19",dwidth/1.206,dheight/0.481)

                                    dcanvas.coords("combo7",dwidth/7.4,dheight/1.035)
                                    dcanvas.coords("combo8",dwidth/1.111,dheight/1.035)

                                    dcanvas.coords("combo9",dwidth/1.294,dheight/2.05)
                                    dcanvas.coords("combo10",dwidth/2.91,dheight/1.73)
                                    dcanvas.coords("combo11",dwidth/2.91,dheight/1.45)
                                    dcanvas.coords("combo12",dwidth/2.91,dheight/1.24)

                                    dcanvas.coords("button5",dwidth/3.89,dheight/1.61)
                                    try:
                                        dcanvas.coords("button6",dwidth/1.23,dheight/0.775)
                                    except:
                                        pass
                                    dcanvas.coords("button7",dwidth/1.114,dheight/0.365)
                                    dcanvas.coords("button8",dwidth/1.114,dheight/0.45)

                                    dcanvas.coords("button9",dwidth/1.09,dheight/2.04)
                                    dcanvas.coords("button10",dwidth/1.09,dheight/1.66)
                                    dcanvas.coords("button11",dwidth/1.57,dheight/0.79)

                                    dcanvas.coords("button12",dwidth/1.09,dheight/0.619)
                                    dcanvas.coords("button13",dwidth/1.09,dheight/0.565)
                                    dcanvas.coords("button14",dwidth/1.09,dheight/0.518)
                                    dcanvas.coords("button15",dwidth/1.09,dheight/0.48)
                                    
                                    dcanvas.coords("line17",dwidth/31.6,dheight/0.7,dwidth/1.039,dheight/0.7)
                                    dcanvas.coords("line18",dwidth/31.6,dheight/0.65,dwidth/1.039,dheight/0.65)
                                    dcanvas.coords("line19",dwidth/31.6,dheight/0.59,dwidth/1.039,dheight/0.59)
                                    dcanvas.coords("line20",dwidth/31.6,dheight/0.541,dwidth/1.039,dheight/0.541)
                                    dcanvas.coords("line21",dwidth/31.6,dheight/0.499,dwidth/1.039,dheight/0.499)
                                    dcanvas.coords("line22",dwidth/31.6,dheight/0.464,dwidth/1.039,dheight/0.464)
                                    dcanvas.coords("line23",dwidth/31.6,dheight/0.7,dwidth/31.6,dheight/0.464)
                                    dcanvas.coords("line24",dwidth/1.039,dheight/0.7,dwidth/1.039,dheight/0.464)
                                    dcanvas.coords("line25",dwidth/15,dheight/0.7,dwidth/15,dheight/0.464)
                                    dcanvas.coords("line26",dwidth/5.35,dheight/0.7,dwidth/5.35,dheight/0.464)
                                    dcanvas.coords("line27",dwidth/3.5,dheight/0.7,dwidth/3.5,dheight/0.464)
                                    dcanvas.coords("line28",dwidth/2.28,dheight/0.7,dwidth/2.28,dheight/0.464)
                                    dcanvas.coords("line29",dwidth/1.88,dheight/0.7,dwidth/1.88,dheight/0.464)
                                    dcanvas.coords("line30",dwidth/1.52,dheight/0.7,dwidth/1.52,dheight/0.464)
                                    dcanvas.coords("line31",dwidth/1.277,dheight/0.7,dwidth/1.277,dheight/0.464)
                                    dcanvas.coords("line58",dwidth/1.144,dheight/0.7,dwidth/1.144,dheight/0.464)

                                    dcanvas.coords("line32",dwidth/1.7,dheight/0.451,dwidth/1.039,dheight/0.451)
                                    dcanvas.coords("line33",dwidth/1.7,dheight/0.425,dwidth/1.039,dheight/0.425)
                                    dcanvas.coords("line34",dwidth/1.7,dheight/0.401,dwidth/1.039,dheight/0.401)
                                    dcanvas.coords("line35",dwidth/1.7,dheight/0.38,dwidth/1.039,dheight/0.38)
                                    dcanvas.coords("line36",dwidth/1.7,dheight/0.451,dwidth/1.7,dheight/0.38)
                                    dcanvas.coords("line37",dwidth/1.365,dheight/0.451,dwidth/1.365,dheight/0.38)
                                    dcanvas.coords("line38",dwidth/1.039,dheight/0.451,dwidth/1.039,dheight/0.38)

                                    dcanvas.coords("line39",dwidth/31.6,dheight/1.2,dwidth/1.039,dheight/1.2)
                                    dcanvas.coords("line40",dwidth/31.6,dheight/1.085,dwidth/1.039,dheight/1.085)
                                    dcanvas.coords("line41",dwidth/31.6,dheight/0.99,dwidth/1.039,dheight/0.99)
                                    dcanvas.coords("line42",dwidth/31.6,dheight/0.91,dwidth/1.039,dheight/0.91)
                                    dcanvas.coords("line43",dwidth/31.6,dheight/1.2,dwidth/31.6,dheight/0.91)
                                    dcanvas.coords("line44",dwidth/15,dheight/1.2,dwidth/15,dheight/0.91)
                                    dcanvas.coords("line45",dwidth/4.9,dheight/1.2,dwidth/4.9,dheight/0.91)
                                    dcanvas.coords("line46",dwidth/2.5,dheight/1.2,dwidth/2.5,dheight/0.91)
                                    dcanvas.coords("line47",dwidth/1.95,dheight/1.2,dwidth/1.95,dheight/0.91)
                                    dcanvas.coords("line48",dwidth/1.48,dheight/1.2,dwidth/1.48,dheight/0.91)
                                    dcanvas.coords("line49",dwidth/1.195,dheight/1.2,dwidth/1.195,dheight/0.91)
                                    dcanvas.coords("line50",dwidth/1.039,dheight/1.2,dwidth/1.039,dheight/0.91)

                                    dcanvas.coords("line51",dwidth/1.55,dheight/0.87,dwidth/1.039,dheight/0.87)
                                    dcanvas.coords("line52",dwidth/1.55,dheight/0.8,dwidth/1.039,dheight/0.8)
                                    dcanvas.coords("line53",dwidth/1.55,dheight/0.74,dwidth/1.039,dheight/0.74)
                                    dcanvas.coords("line54",dwidth/1.55,dheight/0.69,dwidth/1.039,dheight/0.69)
                                    dcanvas.coords("line55",dwidth/1.55,dheight/0.87,dwidth/1.55,dheight/0.69)
                                    dcanvas.coords("line56",dwidth/1.29,dheight/0.87,dwidth/1.29,dheight/0.69)
                                    dcanvas.coords("line57",dwidth/1.039,dheight/0.87,dwidth/1.039,dheight/0.69)

                                    dcanvas.coords("line59",dwidth/31.6,dheight/0.7,dwidth/1.039,dheight/0.7)
                                    dcanvas.coords("line60",dwidth/31.6,dheight/0.65,dwidth/1.039,dheight/0.65)
                                    dcanvas.coords("line61",dwidth/31.6,dheight/0.59,dwidth/1.039,dheight/0.59)
                                    dcanvas.coords("line62",dwidth/31.6,dheight/0.541,dwidth/1.039,dheight/0.541)
                                    dcanvas.coords("line63",dwidth/31.6,dheight/0.499,dwidth/1.039,dheight/0.499)
                                    dcanvas.coords("line64",dwidth/31.6,dheight/0.464,dwidth/1.039,dheight/0.464)
                                    dcanvas.coords("line65",dwidth/31.6,dheight/0.7,dwidth/31.6,dheight/0.464)
                                    dcanvas.coords("line66",dwidth/1.039,dheight/0.7,dwidth/1.039,dheight/0.464)
                                    dcanvas.coords("line67",dwidth/15,dheight/0.7,dwidth/15,dheight/0.464)
                                    dcanvas.coords("line68",dwidth/4.5,dheight/0.7,dwidth/4.5,dheight/0.464)
                                    dcanvas.coords("line69",dwidth/2.5,dheight/0.7,dwidth/2.5,dheight/0.464)
                                    dcanvas.coords("line70",dwidth/2,dheight/0.7,dwidth/2,dheight/0.464)
                                    dcanvas.coords("line71",dwidth/1.55,dheight/0.7,dwidth/1.55,dheight/0.464)
                                    dcanvas.coords("line72",dwidth/1.277,dheight/0.7,dwidth/1.277,dheight/0.464)
                                    dcanvas.coords("line73",dwidth/1.144,dheight/0.7,dwidth/1.144,dheight/0.464)

                                    dcanvas.coords("line74",dwidth/1.7,dheight/0.451,dwidth/1.039,dheight/0.451)
                                    dcanvas.coords("line75",dwidth/1.7,dheight/0.425,dwidth/1.039,dheight/0.425)
                                    dcanvas.coords("line76",dwidth/1.7,dheight/0.401,dwidth/1.039,dheight/0.401)
                                    dcanvas.coords("line77",dwidth/1.7,dheight/0.38,dwidth/1.039,dheight/0.38)
                                    dcanvas.coords("line78",dwidth/1.7,dheight/0.451,dwidth/1.7,dheight/0.38)
                                    dcanvas.coords("line79",dwidth/1.365,dheight/0.451,dwidth/1.365,dheight/0.38)
                                    dcanvas.coords("line80",dwidth/1.039,dheight/0.451,dwidth/1.039,dheight/0.38)

                                    dcanvas.coords("label71",dwidth/20,dheight/0.675)
                                    dcanvas.coords("label72",dwidth/20,dheight/0.62)
                                    dcanvas.coords("label73",dwidth/20,dheight/0.565)
                                    dcanvas.coords("label74",dwidth/20,dheight/0.519)
                                    dcanvas.coords("label75",dwidth/20,dheight/0.481)
                                    dcanvas.coords("label76",dwidth/7,dheight/0.675)
                                    dcanvas.coords("label77",dwidth/3.2,dheight/0.675)
                                    dcanvas.coords("label78",dwidth/2.22,dheight/0.675)
                                    dcanvas.coords("label79",dwidth/1.75,dheight/0.675)
                                    dcanvas.coords("label80",dwidth/1.4,dheight/0.675)
                                    dcanvas.coords("label81",dwidth/1.205,dheight/0.675)
                                    dcanvas.coords("label82",dwidth/2.22,dheight/0.6)
                                    dcanvas.coords("label83",dwidth/2.22,dheight/0.549)
                                    dcanvas.coords("label84",dwidth/2.22,dheight/0.506)
                                    dcanvas.coords("label85",dwidth/2.22,dheight/0.47)

                                    dcanvas.coords("combo20",dwidth/6.98,dheight/0.62)
                                    dcanvas.coords("combo21",dwidth/1.206,dheight/0.62)
                                    dcanvas.coords("combo22",dwidth/6.98,dheight/0.5655)
                                    dcanvas.coords("combo23",dwidth/1.206,dheight/0.5655)
                                    dcanvas.coords("combo24",dwidth/6.98,dheight/0.519)
                                    dcanvas.coords("combo25",dwidth/1.206,dheight/0.519)
                                    dcanvas.coords("combo26",dwidth/6.98,dheight/0.481)
                                    dcanvas.coords("combo27",dwidth/1.206,dheight/0.481)

                                    dcanvas.coords("entry57",dwidth/4.32,dheight/0.63)
                                    dcanvas.coords("entry58",dwidth/2.45,dheight/0.63)
                                    dcanvas.coords("entry59",dwidth/1.965,dheight/0.63)
                                    dcanvas.coords("entry60",dwidth/1.525,dheight/0.63)
                                    dcanvas.coords("entry61",dwidth/4.32,dheight/0.5745)
                                    dcanvas.coords("entry62",dwidth/2.45,dheight/0.5745)
                                    dcanvas.coords("entry63",dwidth/1.965,dheight/0.5745)
                                    dcanvas.coords("entry64",dwidth/1.525,dheight/0.5745)
                                    dcanvas.coords("entry65",dwidth/4.32,dheight/0.527)
                                    dcanvas.coords("entry66",dwidth/2.45,dheight/0.527)
                                    dcanvas.coords("entry67",dwidth/1.965,dheight/0.527)
                                    dcanvas.coords("entry68",dwidth/1.525,dheight/0.527)
                                    dcanvas.coords("entry69",dwidth/4.32,dheight/0.487)
                                    dcanvas.coords("entry70",dwidth/2.45,dheight/0.487)
                                    dcanvas.coords("entry71",dwidth/1.965,dheight/0.487)
                                    dcanvas.coords("entry72",dwidth/1.525,dheight/0.487)

                                    dcanvas.coords("line81",dwidth/1.465,dheight/0.7,dwidth/1.465,dheight/0.464)
                                    dcanvas.coords("line82",dwidth/1.2,dheight/0.7,dwidth/1.2,dheight/0.464)
                                    
                                    dcanvas.coords("label86",dwidth/1.65,dheight/0.675)
                                    dcanvas.coords("label87",dwidth/1.325,dheight/0.675)
                                    dcanvas.coords("label88",dwidth/1.115,dheight/0.675)

                                    dcanvas.coords("entry73",dwidth/5.13,dheight/0.63)
                                    dcanvas.coords("entry74",dwidth/3.39,dheight/0.63)
                                    dcanvas.coords("entry75",dwidth/2.24,dheight/0.63)
                                    dcanvas.coords("entry76",dwidth/1.848,dheight/0.63)
                                    dcanvas.coords("entry77",dwidth/1.45,dheight/0.63)
                                    dcanvas.coords("entry78",dwidth/5.13,dheight/0.5745)
                                    dcanvas.coords("entry79",dwidth/3.39,dheight/0.5745)
                                    dcanvas.coords("entry80",dwidth/2.24,dheight/0.5745)
                                    dcanvas.coords("entry81",dwidth/1.848,dheight/0.5745)
                                    dcanvas.coords("entry82",dwidth/1.45,dheight/0.5745)
                                    dcanvas.coords("entry83",dwidth/5.13,dheight/0.527)
                                    dcanvas.coords("entry84",dwidth/3.39,dheight/0.527)
                                    dcanvas.coords("entry85",dwidth/2.24,dheight/0.527)
                                    dcanvas.coords("entry86",dwidth/1.848,dheight/0.527)
                                    dcanvas.coords("entry87",dwidth/1.45,dheight/0.527)
                                    dcanvas.coords("entry88",dwidth/5.13,dheight/0.487)
                                    dcanvas.coords("entry89",dwidth/3.39,dheight/0.487)
                                    dcanvas.coords("entry90",dwidth/2.24,dheight/0.487)
                                    dcanvas.coords("entry91",dwidth/1.848,dheight/0.487)
                                    dcanvas.coords("entry92",dwidth/1.45,dheight/0.487)

                                    dcanvas.coords("combo28",dwidth/1.112,dheight/0.62)
                                    dcanvas.coords("combo29",dwidth/1.112,dheight/0.5655)
                                    dcanvas.coords("combo30",dwidth/1.112,dheight/0.519)
                                    dcanvas.coords("combo31",dwidth/1.112,dheight/0.481)

                                    dcanvas.coords("line83",dwidth/31.6,dheight/1.12,dwidth/1.039,dheight/1.12)
                                    dcanvas.coords("line84",dwidth/31.6,dheight/1,dwidth/1.039,dheight/1)
                                    dcanvas.coords("line85",dwidth/31.6,dheight/0.87,dwidth/1.039,dheight/0.87)
                                    dcanvas.coords("line86",dwidth/31.6,dheight/0.77,dwidth/1.039,dheight/0.77)
                                    dcanvas.coords("line87",dwidth/31.6,dheight/0.69,dwidth/1.039,dheight/0.69)
                                    dcanvas.coords("line88",dwidth/31.6,dheight/0.625,dwidth/1.039,dheight/0.625)
                                    dcanvas.coords("line89",dwidth/31.6,dheight/1.12,dwidth/31.6,dheight/0.625)
                                    dcanvas.coords("line90",dwidth/1.039,dheight/1.12,dwidth/1.039,dheight/0.625)
                                    dcanvas.coords("line91",dwidth/15,dheight/1.12,dwidth/15,dheight/0.625)
                                    dcanvas.coords("line92",dwidth/4.5,dheight/1.12,dwidth/4.5,dheight/0.625)
                                    dcanvas.coords("line93",dwidth/2.5,dheight/1.12,dwidth/2.5,dheight/0.625)
                                    dcanvas.coords("line94",dwidth/2,dheight/1.12,dwidth/2,dheight/0.625)
                                    dcanvas.coords("line95",dwidth/1.5,dheight/1.12,dwidth/1.5,dheight/0.625)
                                    dcanvas.coords("line96",dwidth/1.2,dheight/1.12,dwidth/1.2,dheight/0.625)

                                    dcanvas.coords("line97",dwidth/1.7,dheight/0.6,dwidth/1.039,dheight/0.6)
                                    dcanvas.coords("line98",dwidth/1.7,dheight/0.55,dwidth/1.039,dheight/0.55)
                                    dcanvas.coords("line99",dwidth/1.7,dheight/0.507,dwidth/1.039,dheight/0.507)
                                    dcanvas.coords("line100",dwidth/1.7,dheight/0.47,dwidth/1.039,dheight/0.47)
                                    dcanvas.coords("line101",dwidth/1.7,dheight/0.6,dwidth/1.7,dheight/0.47)
                                    dcanvas.coords("line102",dwidth/1.365,dheight/0.6,dwidth/1.365,dheight/0.47)
                                    dcanvas.coords("line103",dwidth/1.039,dheight/0.6,dwidth/1.039,dheight/0.47)

                                    dcanvas.coords("label89",dwidth/20,dheight/1.05)
                                    dcanvas.coords("label90",dwidth/20,dheight/0.925)
                                    dcanvas.coords("label91",dwidth/20,dheight/0.815)
                                    dcanvas.coords("label92",dwidth/20,dheight/0.725)
                                    dcanvas.coords("label93",dwidth/20,dheight/0.655)
                                    dcanvas.coords("label94",dwidth/7,dheight/1.05)
                                    dcanvas.coords("label95",dwidth/3.2,dheight/1.05)
                                    dcanvas.coords("label96",dwidth/2.22,dheight/1.05)
                                    dcanvas.coords("label97",dwidth/1.72,dheight/1.05)
                                    dcanvas.coords("label98",dwidth/1.34,dheight/1.05)
                                    dcanvas.coords("label99",dwidth/1.121,dheight/1.05)

                                    dcanvas.coords("label100",dwidth/1.52,dheight/0.572)
                                    dcanvas.coords("label101",dwidth/1.52,dheight/0.528)
                                    dcanvas.coords("label102",dwidth/1.52,dheight/0.487)

                                    dcanvas.coords("label103",dwidth/2.22,dheight/0.89)
                                    dcanvas.coords("label104",dwidth/2.22,dheight/0.785)
                                    dcanvas.coords("label105",dwidth/2.22,dheight/0.701)
                                    dcanvas.coords("label106",dwidth/2.22,dheight/0.635)

                                    dcanvas.coords("entry93",dwidth/4.32,dheight/0.952)
                                    dcanvas.coords("entry94",dwidth/2.45,dheight/0.952)
                                    dcanvas.coords("entry95",dwidth/1.967,dheight/0.952)
                                    dcanvas.coords("entry96",dwidth/1.485,dheight/0.952)
                                    dcanvas.coords("entry97",dwidth/4.32,dheight/0.835)
                                    dcanvas.coords("entry98",dwidth/2.45,dheight/0.835)
                                    dcanvas.coords("entry99",dwidth/1.967,dheight/0.835)
                                    dcanvas.coords("entry100",dwidth/1.485,dheight/0.835)
                                    dcanvas.coords("entry101",dwidth/4.32,dheight/0.742)
                                    dcanvas.coords("entry102",dwidth/2.45,dheight/0.742)
                                    dcanvas.coords("entry103",dwidth/1.967,dheight/0.742)
                                    dcanvas.coords("entry104",dwidth/1.485,dheight/0.742)
                                    dcanvas.coords("entry105",dwidth/4.32,dheight/0.667)
                                    dcanvas.coords("entry106",dwidth/2.45,dheight/0.667)
                                    dcanvas.coords("entry107",dwidth/1.967,dheight/0.667)
                                    dcanvas.coords("entry108",dwidth/1.485,dheight/0.667)

                                    dcanvas.coords("entry109",dwidth/1.35,dheight/0.582)
                                    dcanvas.coords("entry110",dwidth/1.35,dheight/0.535)
                                    dcanvas.coords("entry111",dwidth/1.35,dheight/0.494)

                                    dcanvas.coords("combo32",dwidth/6.98,dheight/0.93)
                                    dcanvas.coords("combo33",dwidth/1.112,dheight/0.93)
                                    dcanvas.coords("combo34",dwidth/6.98,dheight/0.815)
                                    dcanvas.coords("combo35",dwidth/1.112,dheight/0.815)
                                    dcanvas.coords("combo36",dwidth/6.98,dheight/0.728)
                                    dcanvas.coords("combo37",dwidth/1.112,dheight/0.728)
                                    dcanvas.coords("combo38",dwidth/6.98,dheight/0.655)
                                    dcanvas.coords("combo39",dwidth/1.112,dheight/0.655)

                                    dcanvas.coords("date",dwidth/2.71,dheight/1.392)
                                    dcanvas.coords("date1",dwidth/1.73,dheight/1.392)

                                    dcanvas.coords("entry87ref",dwidth/1.29,dheight/1.392)

                                except:
                                    pass

                                

                            sr_Scroll_1 = Scrollbar(estm_Frame,orient=VERTICAL)
                            sr_Scroll_1.grid(row=0,column=1,sticky='ns')
                            sr_Scroll_1.config(command=sr_Canvas_1.yview)
                            sr_Canvas_1.bind("<Configure>", responsive_widgets1)
                            sr_Canvas_1.config(yscrollcommand=sr_Scroll_1.set)
                            sr_Canvas_1.grid(row=0,column=0,sticky='nsew')

                            
                            sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
                            es_label1 = Label(sr_Canvas_1,width=18,height=1,text="ESTIMATE",font=('arial 25'),background='#1b3857',fg="white")
                            sr_Canvas_1.create_window(0,0,anchor="c",window=es_label1,tags=("label1"))
                            sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

                            sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly3"))   

                            es_label2 = Label(sr_Canvas_1,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
                            sr_Canvas_1.create_window(0,0,anchor="c",window=es_label2,tags=("label2"))

                            es_label3 = Label(sr_Canvas_1,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                            sr_Canvas_1.create_window(0,0,window=es_label3,tags=("label21"))

                            user_sql = "SELECT id FROM auth_user WHERE username=%s"
                            user_val = (nm_ent.get(),)
                            fbcursor.execute(user_sql,user_val)
                            user_data = fbcursor.fetchone()

                            comp_sql = 'SELECT * FROM app1_company WHERE id_id=%s'
                            comp_val = (user_data[0],)
                            fbcursor.execute(comp_sql,comp_val)
                            comp_data = fbcursor.fetchone()

                            cust_sql = "SELECT firstname,lastname FROM app1_customer WHERE cid_id=%s"
                            cust_val = (comp_data[0],)
                            fbcursor.execute(cust_sql,cust_val)
                            cust_data = fbcursor.fetchall()

                            cust_list = []
                            if not cust_data:
                                cust_list.append('Select Customer')
                            else:
                                for c in cust_data:
                                    cust_list.append(c[0] + " " + c[1])
                                cust_list.insert(0,'Select Customer')

                            def es_fetch_custDetails(event):
                                cust_name = es_custCombo.get()
                                cust_fname = cust_name.split(" ")[0]
                                cust_lname = cust_name.split(" ")[1]

                                cust_sql = "SELECT * FROM app1_customer WHERE firstname=%s and lastname=%s and cid_id=%s"
                                cust_val = (cust_fname,cust_lname,comp_data[0])
                                fbcursor.execute(cust_sql,cust_val)
                                cust_data = fbcursor.fetchone()

                                inv_sql = "SELECT * FROM app1_invoice WHERE customername=%s and cid_id=%s"
                                inv_val = (cust_name,comp_data[0])
                                fbcursor.execute(inv_sql,inv_val)
                                inv_data = fbcursor.fetchall()

                                try:
                                    if not cust_data:
                                        pass
                                    else:
                                        es_email.delete(0,END)
                                        es_email.insert(0,cust_data[9])
                                        es_baddress.delete("1.0","end-1c")
                                        es_baddress.insert("1.0",cust_data[2] + " " + cust_data[3] + "\n" + cust_data[4] + "\n" + cust_data[12] + "\n" + cust_data[13] + "\n" + cust_data[14] + "\n" + cust_data[15] + "\n" + cust_data[16])
                                        es_pofsupply.delete(0,END)
                                        es_pofsupply.insert(0,comp_data[4])
                                except:
                                    pass

                            es_custCombo = ttk.Combobox(sr_Canvas_1,width=15,font=('arial 15'))
                            es_custCombo["values"] = cust_list
                            es_custCombo.current(0)
                            es_custCombo.bind("<<ComboboxSelected>>",es_fetch_custDetails)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=es_custCombo,tags=("combo3"))

                            def sr_addCustomer_1():
                                
                                sr_Frame_2 = Frame(estm_Frame,)
                                sr_Frame_2.grid(row=0,column=0,sticky='nsew')

                                def responsive_widgets2(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                    
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("poly1",x1 + r1,y1,
                                    x1 + r1,y1,
                                    x2 - r1,y1,
                                    x2 - r1,y1,     
                                    x2,y1,     
                                    #--------------------
                                    x2,y1 + r1,     
                                    x2,y1 + r1,     
                                    x2,y2 - r1,     
                                    x2,y2 - r1,     
                                    x2,y2,
                                    #--------------------
                                    x2 - r1,y2,     
                                    x2 - r1,y2,     
                                    x1 + r1,y2,
                                    x1 + r1,y2,
                                    x1,y2,
                                    #--------------------
                                    x1,y2 - r1,
                                    x1,y2 - r1,
                                    x1,y1 + r1,
                                    x1,y1 + r1,
                                    x1,y1,
                                    )

                                    dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                                    
                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.6


                                    dcanvas.coords("poly2",x11 + r2,y11,
                                    x11 + r2,y11,
                                    x21 - r2,y11,
                                    x21 - r2,y11,     
                                    x21,y11,     
                                    #--------------------
                                    x21,y11 + r2,     
                                    x21,y11 + r2,     
                                    x21,y21 - r2,     
                                    x21,y21 - r2,     
                                    x21,y21,
                                    #--------------------
                                    x21 - r2,y21,     
                                    x21 - r2,y21,     
                                    x11 + r2,y21,
                                    x11 + r2,y21,
                                    x11,y21,
                                    #--------------------
                                    x11,y21 - r2,
                                    x11,y21 - r2,
                                    x11,y11 + r2,
                                    x11,y11 + r2,
                                    x11,y11,
                                    )

                                    dcanvas.coords("label1",dwidth/2,dheight/8.24)
                                    dcanvas.coords("label2",dwidth/6,dheight/2.4)
                                    dcanvas.coords("label3",dwidth/8.2,dheight/2)
                                    dcanvas.coords("label4",dwidth/2.8,dheight/2)
                                    dcanvas.coords("label5",dwidth/1.7,dheight/2)
                                    dcanvas.coords("label6",dwidth/8.2,dheight/1.66)
                                    dcanvas.coords("label7",dwidth/2.8,dheight/1.66)
                                    dcanvas.coords("label8",dwidth/8.2,dheight/1.42)
                                    dcanvas.coords("label9",dwidth/2.8,dheight/1.42)
                                    dcanvas.coords("label10",dwidth/1.7,dheight/1.42)
                                    dcanvas.coords("label11",dwidth/8.2,dheight/1.24)
                                    dcanvas.coords("label12",dwidth/2.8,dheight/1.24)
                                    dcanvas.coords("label13",dwidth/1.7,dheight/1.24)
                                    dcanvas.coords("label14",dwidth/5.97,dheight/1.09)
                                    dcanvas.coords("label15",dwidth/8.2,dheight/0.98)
                                    dcanvas.coords("label16",dwidth/1.71,dheight/0.98)
                                    dcanvas.coords("label17",dwidth/1.58,dheight/1.09)
                                    dcanvas.coords("label18",dwidth/8.2,dheight/0.824)
                                    dcanvas.coords("label19",dwidth/2.62,dheight/0.824)
                                    dcanvas.coords("label20",dwidth/1.7,dheight/0.824)
                                    dcanvas.coords("label21",dwidth/1.185,dheight/0.824)
                                    dcanvas.coords("label22",dwidth/8.2,dheight/0.76)
                                    dcanvas.coords("label23",dwidth/2.62,dheight/0.76)
                                    dcanvas.coords("label24",dwidth/1.7,dheight/0.76)
                                    dcanvas.coords("label25",dwidth/1.185,dheight/0.76)
                                    dcanvas.coords("label26",dwidth/1.28,dheight/1.087)
                                    dcanvas.coords("label27",dwidth/6.3,dheight/0.699)

                                    dcanvas.coords("line1",dwidth/21,dheight/2.2,dwidth/1.055,dheight/2.2)

                                    dcanvas.coords("combo1",dwidth/20,dheight/1.9)
                                    dcanvas.coords("combo2",dwidth/20,dheight/1.37)

                                    dcanvas.coords("entry2",dwidth/3.52,dheight/1.9)
                                    dcanvas.coords("entry3",dwidth/1.94,dheight/1.9)
                                    dcanvas.coords("entry4",dwidth/20,dheight/1.6)
                                    dcanvas.coords("entry5",dwidth/3.52,dheight/1.6)
                                    dcanvas.coords("entry6",dwidth/3.52,dheight/1.38)
                                    dcanvas.coords("entry7",dwidth/1.94,dheight/1.38)
                                    dcanvas.coords("entry8",dwidth/20,dheight/1.21)
                                    dcanvas.coords("entry9",dwidth/3.52,dheight/1.21)
                                    dcanvas.coords("entry10",dwidth/1.94,dheight/1.21)
                                    dcanvas.coords("entry11",dwidth/20,dheight/0.96)
                                    dcanvas.coords("entry12",dwidth/1.95,dheight/0.96)
                                    dcanvas.coords("entry13",dwidth/20,dheight/0.81)
                                    dcanvas.coords("entry14",dwidth/3.23,dheight/0.81)
                                    dcanvas.coords("entry15",dwidth/1.94,dheight/0.81)
                                    dcanvas.coords("entry16",dwidth/1.296,dheight/0.81)
                                    dcanvas.coords("entry17",dwidth/20,dheight/0.749)
                                    dcanvas.coords("entry18",dwidth/3.23,dheight/0.749)
                                    dcanvas.coords("entry19",dwidth/1.94,dheight/0.749)
                                    dcanvas.coords("entry20",dwidth/1.296,dheight/0.749)

                                    dcanvas.coords("check1",dwidth/1.45,dheight/1.11)
                                    dcanvas.coords("check2",dwidth/20,dheight/0.71)

                                    dcanvas.coords("button1",dwidth/2,dheight/0.655)
                                    dcanvas.coords("button2",dwidth/27,dheight/3)

                                sr_Canvas_2 = Canvas(sr_Frame_2,bg='#2f516f',scrollregion=(0,0,700,1200))

                                sr_Frame_2.grid_columnconfigure(0,weight=1)
                                sr_Frame_2.grid_rowconfigure(0,weight=1)

                                sr_Scroll_2 = Scrollbar(sr_Frame_2,orient=VERTICAL)
                                sr_Scroll_2.grid(row=0,column=1,sticky='ns')
                                sr_Scroll_2.config(command=sr_Canvas_2.yview)
                                sr_Canvas_2.bind("<Configure>", responsive_widgets2)
                                sr_Canvas_2.config(yscrollcommand=sr_Scroll_2.set)
                                sr_Canvas_2.grid(row=0,column=0,sticky='nsew')

                                sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
                                cust_label1 = Label(sr_Canvas_2,width=18,height=1,text="ADD CUSTOMER",font=('arial 25'),background='#1b3857',fg="white")
                                sr_Canvas_2.create_window(0,0,anchor="c",window=cust_label1,tags=("label1"))
                                sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

                                sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

                                cust_label2 = Label(sr_Canvas_2,width=20,height=1,text="Customer Information",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label2,tags=('label2'))

                                sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))

                                cust_label3 = Label(sr_Canvas_2,width=20,height=1,text="Title",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label3,tags=('label3'))

                                cust_title = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                                cust_title['values'] = ['Mr','Mrs','Miss','Ms',]
                                cust_title.current(0)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

                                cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

                                cust_fname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

                                cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

                                cust_lname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

                                cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

                                cust_company = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

                                cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

                                cust_location = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

                                cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

                                def select_GSTtype(event):
                                    if cust_gtype.get() == 'GST unregistered' or cust_gtype.get() == 'Consumer' or cust_gtype.get() == 'Overseas':
                                        sr_Canvas_2.itemconfig("label9",state='hidden')
                                        sr_Canvas_2.itemconfig("entry6",state='hidden')
                                    else:
                                        sr_Canvas_2.itemconfig("label9",state='normal')
                                        sr_Canvas_2.itemconfig("entry6",state='normal')

                                cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                                cust_gtype['values'] = ['Choose...','GST registered- Regular','GST registered- Composition','GST unregistered','Consumer','Overseas','SEZ',"Deemed exports - EOU's STP's EHTP's etc"]
                                cust_gtype.current(0)
                                cust_gtype.bind("<<ComboboxSelected>>",select_GSTtype)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

                                cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

                                gstinVar = StringVar()
                                cust_gin = Entry(sr_Canvas_2,textvariable=gstinVar,width=20,font=('arial 15'),background='#2f516f',foreground='grey')
                                cust_gin.insert(0,'29APPCK7465F1Z1')

                                def del_placeholder(event):
                                    if cust_gin.get() == '29APPCK7465F1Z1':
                                        cust_gin.delete(0,END)
                                        cust_gin.config(fg="white")
                                    else:
                                        pass

                                cust_gin.bind("<FocusIn>",del_placeholder)

                                def ret_placeholder(event):
                                    if cust_gin.get() == '':
                                        cust_gin.insert(0,'29APPCK7465F1Z1')
                                        cust_gin.config(fg="grey")
                                    else:
                                        pass
                                cust_gin.bind("<FocusOut>",ret_placeholder)
                                
                                def validate_gstin(value):
                                    pattern = r'[0-9]{2}[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[a-zA-Z]{1}[0-9a-zA-Z]{1}'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_gin.config(fg="white")
                                        return True

                                def invalid_gstin():
                                    cust_gin.config(fg="red")

                                valid_cmndGSTIN = (sr_Canvas_2.register(validate_gstin),'%P')
                                invalid_cmndGSTIN = (sr_Canvas_2.register(invalid_gstin),)
                                cust_gin.config(validate='focusout',validatecommand=valid_cmndGSTIN,invalidcommand=invalid_cmndGSTIN)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

                                cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

                                panVar = StringVar()
                                cust_pan = Entry(sr_Canvas_2,width=20,textvariable=panVar,font=('arial 15'),background='#2f516f',foreground='grey')
                                cust_pan.insert(0,'APPCK7465F')

                                def del_placeholder(event):
                                    if cust_pan.get() == 'APPCK7465F':
                                        cust_pan.delete(0,END)
                                        cust_pan.config(fg="white")
                                    else:
                                        pass

                                cust_pan.bind("<FocusIn>",del_placeholder)

                                def ret_placeholder(event):
                                    if cust_pan.get() == '':
                                        cust_pan.insert(0,'APPCK7465F')
                                        cust_pan.config(fg="grey")
                                    else:
                                        pass
                                cust_pan.bind("<FocusOut>",ret_placeholder)

                                def validate_pan(value):
                                    pattern = r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_pan.config(fg="white")
                                        return True

                                def invalid_pan():
                                    cust_pan.config(fg="red")

                                valid_cmndPAN = (sr_Canvas_2.register(validate_pan),'%P')
                                invalid_cmndPAN = (sr_Canvas_2.register(invalid_pan),)
                                cust_pan.config(validate='focusout',validatecommand=valid_cmndPAN,invalidcommand=invalid_cmndPAN)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

                                cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

                                emailVar = StringVar()
                                cust_email = Entry(sr_Canvas_2,textvariable=emailVar,width=20,font=('arial 15'),background='#2f516f',foreground='white')

                                def validate_email(value):
                                    pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_email.config(fg="white")
                                        return True

                                def invalid_email():
                                    cust_email.config(fg="red")

                                valid_cmndEMAIL = (sr_Canvas_2.register(validate_email),'%P')
                                invalid_cmndEMAIL = (sr_Canvas_2.register(invalid_email),)
                                cust_email.config(validate='focusout',validatecommand=valid_cmndEMAIL,invalidcommand=invalid_cmndEMAIL)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

                                cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

                                webVar = StringVar()
                                cust_web = Entry(sr_Canvas_2,textvariable=webVar,width=20,font=('arial 15'),background='#2f516f',foreground='white')

                                def validate_web(value):
                                    pattern = r'www.+[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_web.config(fg="white")
                                        return True

                                def invalid_web():
                                    cust_web.config(fg="red")

                                valid_cmndWEB = (sr_Canvas_2.register(validate_web),'%P')
                                invalid_cmndWEB = (sr_Canvas_2.register(invalid_web),)
                                cust_web.config(validate='focusout',validatecommand=valid_cmndWEB,invalidcommand=invalid_cmndWEB)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

                                cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

                                mobVar = StringVar()
                                cust_mob = Entry(sr_Canvas_2,textvariable=mobVar,width=20,font=('arial 15'),background='#2f516f',foreground='white')

                                def validate_mobile(value):
                                    pattern = r'[7-9][0-9]{9}'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_mob.config(fg="white")
                                        return True

                                def invalid_mobile():
                                    cust_mob.config(fg="red")

                                valid_cmndMOB = (sr_Canvas_2.register(validate_mobile),'%P')
                                invalid_cmndMOB = (sr_Canvas_2.register(invalid_mobile),)
                                cust_mob.config(validate='focusout',validatecommand=valid_cmndMOB,invalidcommand=invalid_cmndMOB)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

                                cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

                                cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

                                cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=48,height=3,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

                                cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

                                cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

                                cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=48,height=3,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

                                cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

                                cust_city = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

                                cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

                                cust_state = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

                                cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

                                cust_city1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

                                cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

                                cust_state1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
                                #--
                                cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin Code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

                                cust_pin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

                                cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

                                cust_country = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

                                cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

                                cust_pin1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

                                cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

                                cust_country1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country1,tags=("entry20"))

                                def sameas_billaddress():
                                    if sameasVar.get() == True:
                                        bill_address = cust_st1.get("1.0","end-1c")
                                        bill_city = cust_city.get()
                                        bill_state = cust_state.get()
                                        bill_pin = cust_pin.get()
                                        bill_country = cust_country.get()

                                        cust_st2.delete("1.0","end-1c")
                                        cust_st2.insert("1.0",bill_address)
                                        cust_city1.delete(0,END)
                                        cust_city1.insert(0,bill_city)
                                        cust_state1.delete(0,END)
                                        cust_state1.insert(0,bill_state)
                                        cust_pin1.delete(0,END)
                                        cust_pin1.insert(0,bill_pin)
                                        cust_country1.delete(0,END)
                                        cust_country1.insert(0,bill_country)
                                    else:
                                        pass

                                sameasVar = BooleanVar()
                                cust_sameb = Checkbutton(sr_Canvas_2,variable=sameasVar,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857",command=sameas_billaddress)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_sameb,tags=("check1"))

                                cust_label26 = Label(sr_Canvas_2,width=20,height=1,text="Same as billing address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label26,tags=('label26'))

                                termVar = BooleanVar()
                                cust_term = Checkbutton(sr_Canvas_2,variable=termVar,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_term,tags=("check2"))

                                cust_label27 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label27,tags=('label27'))

                                def sr_create_newCustomer():
                                    title = cust_title.get()
                                    firstname = cust_fname.get()
                                    lastname = cust_lname.get()
                                    company = cust_company.get()
                                    location = cust_location.get()
                                    gsttype = cust_gtype.get()
                                    gstin = gstinVar.get()
                                    panno = panVar.get()
                                    email = emailVar.get()
                                    website = webVar.get()
                                    mobile = mobVar.get()
                                    street = cust_st1.get("1.0","end-1c")
                                    city = cust_city.get()
                                    state = cust_state.get()
                                    pincode = cust_pin.get()
                                    country = cust_country.get()
                                    shipstreet = cust_st2.get("1.0","end-1c")
                                    shipcity = cust_city1.get()
                                    shipstate = cust_state1.get()
                                    shippincode = cust_pin1.get()
                                    shipcountry = cust_country1.get()

                                    
                                    user_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    user_val = (nm_ent.get(),)
                                    fbcursor.execute(user_sql,user_val)
                                    user_data = fbcursor.fetchone()

                                    comp_sql = 'SELECT cid FROM app1_company WHERE id_id=%s'
                                    comp_val = (user_data[0],)
                                    fbcursor.execute(comp_sql,comp_val)
                                    comp_data = fbcursor.fetchone()
                                    cid  = comp_data[0]

                                    
                                    
                                    if gsttype == "GST unregistered" or gsttype == "Consumer" or gsttype == "Overseas":
                                        gstin = ''
                                        if validate_pan(panno) is False:
                                            pass 
                                        elif validate_email(email) is False: 
                                            pass
                                        elif validate_web(website) is False:
                                            pass 
                                        elif validate_mobile(mobile) is False:
                                            pass
                                        else:
                                            if termVar.get() == False:
                                                pass
                                            else:
                                                if gsttype == "Choose...":
                                                    pass
                                                else:
                                                    ins_cust_sql = "INSERT INTO app1_customer(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
                                                    ins_cust_val = (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid,)
                                                    fbcursor.execute(ins_cust_sql,ins_cust_val)
                                                    finsysdb.commit()
                                                    sr_Frame_2.destroy()
                                                    cust_sql = "SELECT firstname,lastname FROM app1_customer"
                                                    fbcursor.execute(cust_sql,)
                                                    cust_data = fbcursor.fetchall()

                                                    cust_list = []
                                                    if not cust_data:
                                                        cust_list.append('Select Customer')
                                                    else:
                                                        for c in cust_data:
                                                            cust_list.append(c[0] + " " + c[1])
                                                        cust_list.insert(0,'Select Customer')
                                                        es_custCombo["values"] = cust_list
                                                    sr_Frame_1.grid(row=0,column=0,sticky='nsew')
                                    elif gstin == '29APPCK7465F1Z1' or panno == 'APPCK7465F':
                                        pass
                                    else:
                                        if validate_gstin(gstin) is False: 
                                            pass
                                        elif validate_pan(panno) is False:
                                            pass 
                                        elif validate_email(email) is False: 
                                            pass
                                        elif validate_web(website) is False:
                                            pass
                                        elif validate_mobile(mobile) is False:
                                            pass
                                        else:
                                            if termVar.get() == False:
                                                pass
                                            else:
                                                if gsttype == "Choose...":
                                                    pass
                                                else:
                                                    ins_cust_sql = "INSERT INTO app1_customer(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
                                                    ins_cust_val = (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid,)
                                                    fbcursor.execute(ins_cust_sql,ins_cust_val)
                                                    finsysdb.commit()
                                                    sr_Frame_2.destroy()
                                                    cust_sql = "SELECT firstname,lastname FROM app1_customer"
                                                    fbcursor.execute(cust_sql,)
                                                    cust_data = fbcursor.fetchall()

                                                    cust_list = []
                                                    if not cust_data:
                                                        cust_list.append('Select Customer')
                                                    else:
                                                        for c in cust_data:
                                                            cust_list.append(c[0] + " " + c[1])
                                                        cust_list.insert(0,'Select Customer')
                                                        es_custCombo["values"] = cust_list
                                                    
                                
                                cust_save = Button(sr_Canvas_2,text="Submit Form",font=('arial 12 bold'),width=40,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0,command=lambda:sr_create_newCustomer())
                                sr_Canvas_2.create_window(0,0,window=cust_save,tags=("button1"))

                                def es_goBack():
                                    sr_Frame_2.grid_forget()
                                    

                                back_btn = Button(sr_Canvas_2,text='???  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:es_goBack())
                                sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button2"))

                            es_plus = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:sr_addCustomer_1())
                            sr_Canvas_1.create_window(0,0,window=es_plus,tags=("button5"))

                            es_label4 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label4,tags=('label22'))

                            es_email = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=es_email,tags=("entry13"))

                            es_label5 = Label(sr_Canvas_1,width=20,height=1,text="Billing Address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label5,tags=('label23'))

                            es_baddress = Text(sr_Canvas_1,width=20,font=('arial 15'),height=7,background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=es_baddress,tags=("entry14"))

                            es_label7 = Label(sr_Canvas_1,width=20,height=1,text="Place of Supply",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label7,tags=('label25'))

                            es_pofsupply = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=es_pofsupply,tags=("entry15"))

                            es_label7 = Label(sr_Canvas_1,width=20,height=1,text="Reference Number",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label7,tags=('label25ref'))
                            
                            est_entry_ref = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')                           
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry_ref,tags=("entry87ref"))

                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line17"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line18"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line19"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line20"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line21"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line22"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line23"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line24"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line25"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line26"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line27"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line28"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line29"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line81"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line82"))

                            

                            es_label13 = Label(sr_Canvas_1,width=3,height=1,text="#",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label13,tags=('label31'))

                            es_label14 = Label(sr_Canvas_1,width=3,height=1,text="1",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label14,tags=('label32'))

                            es_label29 = Label(sr_Canvas_1,width=3,height=1,text="2",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label29,tags=('label64'))

                            es_label30 = Label(sr_Canvas_1,width=3,height=1,text="3",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label30,tags=('label65'))

                            es_label31 = Label(sr_Canvas_1,width=3,height=1,text="4",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label31,tags=('label66'))

                            es_label18 = Label(sr_Canvas_1,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label18,tags=('label33'))

                            es_label19 = Label(sr_Canvas_1,width=10,height=1,text="HSN",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label19,tags=('label34'))

                            es_label20 = Label(sr_Canvas_1,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label20,tags=('label35'))

                            es_label21 = Label(sr_Canvas_1,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label21,tags=('label36'))

                            es_label22 = Label(sr_Canvas_1,width=10,height=1,text="Price",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label22,tags=('label86'))

                            es_label23 = Label(sr_Canvas_1,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label23,tags=('label87'))

                            es_label24 = Label(sr_Canvas_1,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label24,tags=('label88'))

                            user_sql = "SELECT id FROM auth_user WHERE username=%s"
                            user_val = (nm_ent.get(),)
                            fbcursor.execute(user_sql,user_val)
                            user_data = fbcursor.fetchone()

                            comp_sql = 'SELECT * FROM app1_company WHERE id_id=%s'
                            comp_val = (user_data[0],)
                            fbcursor.execute(comp_sql,comp_val)
                            comp_data = fbcursor.fetchone()

                            get_inventory_sql = "SELECT * FROM app1_inventory WHERE cid_id=%s" 
                            get_inventory_val = (comp_data[0],)                      
                            fbcursor.execute(get_inventory_sql,get_inventory_val)
                            get_inventory_data = fbcursor.fetchall()

                            get_noninventory_sql = "SELECT * FROM app1_noninventory WHERE cid_id=%s" 
                            get_noninventory_val = (comp_data[0],)                      
                            fbcursor.execute(get_noninventory_sql,get_noninventory_val)
                            get_noninventory_data = fbcursor.fetchall()

                            get_bundle_sql = "SELECT * FROM app1_bundle WHERE cid_id=%s" 
                            get_bundle_val = (comp_data[0],)                      
                            fbcursor.execute(get_bundle_sql,get_bundle_val)
                            get_bundle_data = fbcursor.fetchall()

                            product_list = []

                            if not get_inventory_data:
                                pass
                            else:
                                for i in get_inventory_data:
                                    product_list.append(i[2])

                            if not get_noninventory_data:
                                pass
                            else:
                                for n in get_noninventory_data:
                                    product_list.append(n[2])

                            if not get_bundle_data:
                                pass
                            else:
                                for b in get_bundle_data:
                                    product_list.append(b[2])
                            
                            # product_list.insert(0,"Select Product")

                            def es_fetch_proDetails1(event):
                                pass

                            est_entry1 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry1['values'] = product_list
                            est_entry1.current(0)
                            est_entry1.bind("<<ComboboxSelected>>",es_fetch_proDetails1)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry1,tags=("combo5"))

                            est_entry2 = Entry(sr_Canvas_1,width=9,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry2,tags=("entry73"))

                            est_entry3 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry3,tags=("entry74"))

                            def est_calculateTotal1(event,s):
                                pass

                            est_entry4 = Spinbox(sr_Canvas_1,from_=0,to=100,width=7,font=('arial 15'),background='#2f516f',foreground='white',justify=RIGHT)
                            est_entry4.bind("<Key>",lambda event,sp = 1:est_calculateTotal1(event,sp))
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry4,tags=("entry75"))

                            est_entry5 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry5,tags=("entry76"))

                            est_entry6 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            est_entry6.delete(0,END)
                            est_entry6.insert(0,0)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry6,tags=("entry77"))
                            def calcu_cmd(event):
                                pass
                                    
                            est_entry7 = ttk.Combobox(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='black')
                            cplace_gstlist = ['Choose','28.0% GST(28%)','18.0% GST(18%)','12.0% GST(12%)','06.0% GST(06%)',
                                '05.0% GST(05%)','03.0% GST(03%)','0.25% GST(0.25%)','0.0% GST(0%)','Exempt GST(0%)','Out of Scope(0%)']
                            est_entry7['values'] = cplace_gstlist
                            est_entry7.current(0)
                            est_entry7.bind('<<ComboboxSelected>>',calcu_cmd)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry7,tags=("combo28"))

                            def es_fetch_proDetails2(event):
                                pass

                            est_entry11 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry11['values'] = product_list
                            est_entry11.current(0)
                            est_entry11.bind("<<ComboboxSelected>>",es_fetch_proDetails2)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry11,tags=("combo14"))

                            est_entry12 = Entry(sr_Canvas_1,width=9,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry12,tags=("entry78"))

                            est_entry13 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry13,tags=("entry79"))

                            est_entry14 = Spinbox(sr_Canvas_1,from_=0,to=100,width=7,font=('arial 15'),background='#2f516f',foreground='white',justify=RIGHT)
                            est_entry14.bind("<Key>",lambda event,sp = 2:est_calculateTotal1(event,sp))
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry14,tags=("entry80"))

                            est_entry15 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry15,tags=("entry81"))

                            est_entry16 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            est_entry16.delete(0,END)
                            est_entry16.insert(0,0)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry16,tags=("entry82"))

                            est_entry17 = ttk.Combobox(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry17['values'] = cplace_gstlist
                            est_entry17.current(0)
                            est_entry17.bind('<<ComboboxSelected>>',calcu_cmd)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry17,tags=("combo29"))

                            def es_fetch_proDetails3(event):
                                try:
                                    get_pro_sql = "SELECT * FROM app1_inventory WHERE name=%s AND cid_id=%s"
                                    get_pro_val = (est_entry18.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql,get_pro_val)
                                    get_pro_data = fbcursor.fetchone()
                                except:
                                    pass

                                try:
                                    get_pro_sql1 = "SELECT * FROM app1_noninventory WHERE name=%s AND cid_id=%s"
                                    get_pro_val1 = (est_entry18.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql1,get_pro_val1)
                                    get_pro_data1 = fbcursor.fetchone()
                                except:
                                    pass

                                try:
                                    get_pro_sql3 = "SELECT * FROM app1_bundle WHERE name=%s AND cid_id=%s"
                                    get_pro_val3 = (est_entry18.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql3,get_pro_val3)
                                    get_pro_data3 = fbcursor.fetchone()
                                except:
                                    pass

                                #--------------------------------------------------------
                                if get_pro_data is not None:
                                    try:
                                        sr_Canvas_1.itemconfig("label69",state='normal')
                                        es_label34.config(text="Available Qty : " + get_pro_data[7])
                                        est_entry19.delete(0,END)
                                        est_entry19.insert(0,get_pro_data[4])
                                        est_entry20.delete(0,END)
                                        est_entry20.insert(0,get_pro_data[11])
                                        est_entry22.delete(0,END)
                                        est_entry22.insert(0,get_pro_data[12])
                                    except:
                                        pass
                                elif get_pro_data1 is not None:
                                    try:
                                        sr_Canvas_1.itemconfig("label69",state='normal')
                                        es_label34.config(text="Available Qty : " + get_pro_data1[17])
                                        est_entry19.delete(0,END)
                                        est_entry19.insert(0,get_pro_data1[4])
                                        est_entry20.delete(0,END)
                                        est_entry20.insert(0,get_pro_data1[7])
                                        est_entry22.delete(0,END)
                                        est_entry22.insert(0,get_pro_data1[8])
                                    except:
                                        pass
                                else:
                                    try:
                                        sr_Canvas_1.itemconfig("label69",state='hidden')
                                        est_entry19.delete(0,END)
                                        est_entry19.insert(0,get_pro_data3[3])
                                        est_entry20.delete(0,END)
                                        est_entry20.insert(0,get_pro_data3[4])
                                        est_entry22.delete(0,END)
                                        est_entry22.insert(0,get_pro_data3[33])
                                    except:
                                        pass

                            est_entry18 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry18['values'] = product_list
                            est_entry18.current(0)
                            est_entry18.bind("<<ComboboxSelected>>",es_fetch_proDetails3)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry18,tags=("combo16"))

                            est_entry19 = Entry(sr_Canvas_1,width=9,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry19,tags=("entry83"))

                            est_entry20 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry20,tags=("entry84"))

                            est_entry21 = Spinbox(sr_Canvas_1,from_=0,to=100,width=7,font=('arial 15'),background='#2f516f',foreground='white',justify=RIGHT)
                            est_entry21.bind("<Key>",lambda event,sp = 3:est_calculateTotal1(event,sp))
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry21,tags=("entry85"))

                            est_entry22 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry22,tags=("entry86"))

                            est_entry23 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            est_entry23.delete(0,END)
                            est_entry23.insert(0,0)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry23,tags=("entry87"))

                            est_entry24 = ttk.Combobox(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry24['values'] = cplace_gstlist
                            est_entry24.current(0)
                            est_entry24.bind('<<ComboboxSelected>>',calcu_cmd)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry24,tags=("combo30"))

                            def es_fetch_proDetails4(event):
                                try:
                                    get_pro_sql = "SELECT * FROM app1_inventory WHERE name=%s AND cid_id=%s"
                                    get_pro_val = (est_entry25.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql,get_pro_val)
                                    get_pro_data = fbcursor.fetchone()
                                except:
                                    pass

                                try:
                                    get_pro_sql1 = "SELECT * FROM app1_noninventory WHERE name=%s AND cid_id=%s"
                                    get_pro_val1 = (est_entry25.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql1,get_pro_val1)
                                    get_pro_data1 = fbcursor.fetchone()
                                except:
                                    pass

                                try:
                                    get_pro_sql3 = "SELECT * FROM app1_bundle WHERE name=%s AND cid_id=%s"
                                    get_pro_val3 = (est_entry25.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql3,get_pro_val3)
                                    get_pro_data3 = fbcursor.fetchone()
                                except:
                                    pass

                                #--------------------------------------------------------
                                if get_pro_data is not None:
                                    try:
                                        sr_Canvas_1.itemconfig("label70",state='normal')
                                        es_label35.config(text="Available Qty : " + get_pro_data[7])
                                        est_entry26.delete(0,END)
                                        est_entry26.insert(0,get_pro_data[4])
                                        est_entry27.delete(0,END)
                                        est_entry27.insert(0,get_pro_data[11])
                                        est_entry29.delete(0,END)
                                        est_entry29.insert(0,get_pro_data[12])
                                    except:
                                        pass
                                elif get_pro_data1 is not None:
                                    try:
                                        sr_Canvas_1.itemconfig("label70",state='normal')
                                        es_label35.config(text="Available Qty : " + get_pro_data1[17])
                                        est_entry26.delete(0,END)
                                        est_entry26.insert(0,get_pro_data1[4])
                                        est_entry27.delete(0,END)
                                        est_entry27.insert(0,get_pro_data1[7])
                                        est_entry29.delete(0,END)
                                        est_entry29.insert(0,get_pro_data1[8])
                                    except:
                                        pass
                                else:
                                    try:
                                        sr_Canvas_1.itemconfig("label70",state='hidden')
                                        est_entry26.delete(0,END)
                                        est_entry26.insert(0,get_pro_data3[3])
                                        est_entry27.delete(0,END)
                                        est_entry27.insert(0,get_pro_data3[4])
                                        est_entry29.delete(0,END)
                                        est_entry29.insert(0,get_pro_data3[33])
                                    except:
                                        pass

                            est_entry25 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry25['values'] = product_list
                            est_entry25.current(0)
                            est_entry25.bind("<<ComboboxSelected>>",es_fetch_proDetails4)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry25,tags=("combo18"))

                            est_entry26 = Entry(sr_Canvas_1,width=9,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry26,tags=("entry88"))

                            est_entry27 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry27,tags=("entry89"))

                            est_entry28 = Spinbox(sr_Canvas_1,from_=0,to=100,width=7,font=('arial 15'),background='#2f516f',foreground='white',justify=RIGHT)
                            est_entry28.bind("<Key>",lambda event,sp = 4:est_calculateTotal1(event,sp))
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry28,tags=("entry90"))

                            est_entry29 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry29,tags=("entry91"))

                            est_entry30 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            est_entry30.delete(0,END)
                            est_entry30.insert(0,0)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry30,tags=("entry92"))

                            est_entry31 = ttk.Combobox(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry31['values'] = cplace_gstlist
                            est_entry31.current(0)
                            est_entry31.bind('<<ComboboxSelected>>',calcu_cmd)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry31,tags=("combo31"))

                            es_label32 = Label(sr_Canvas_1,width=17,height=1,text="",font=('arial 8'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label32,state=HIDDEN,tags=('label67'))

                            es_label33 = Label(sr_Canvas_1,width=17,height=1,text="",font=('arial 8'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label33,state=HIDDEN,tags=('label68'))

                            es_label34 = Label(sr_Canvas_1,width=17,height=1,text="",font=('arial 8'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label34,state=HIDDEN,tags=('label69'))

                            es_label35 = Label(sr_Canvas_1,width=17,height=1,text="",font=('arial 8'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label35,state=HIDDEN,tags=('label70'))

                            es_label25 = Label(sr_Canvas_1,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label25,tags=('label40'))

                            es_label26 = Label(sr_Canvas_1,width=10,height=1,text="CGST",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label26,tags=('label41'))

                            es_label27 = Label(sr_Canvas_1,width=10,height=1,text="SGST",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label27,tags=('label42'))

                            est_entry8 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry8,tags=("entry23"))

                            est_entry9 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry9,tags=("entry24"))

                            est_entry10 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry10,tags=("entry25"))


                            es_label25 = Label(sr_Canvas_1,width=10,height=1,text="TCS",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label25,tags=('label43'))

                            tax_Combo = ttk.Combobox(sr_Canvas_1,width=8,font=('arial 15'))
                            tax_Combo["values"] = "cust_list"
                            tax_Combo.current(0)
                            tax_Combo.bind("<<ComboboxSelected>>","es_fetch_custDetails")
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=tax_Combo,tags=("tcs_sltr"))

                            es_label26 = Label(sr_Canvas_1,width=10,height=1,text="Roundoff",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label26,tags=('label44'))

                            es_label27 = Label(sr_Canvas_1,height=1,text="Estimate Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label27,tags=('label45'))



                            est_entry11 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry11,tags=("est_entry11"))

                            est_entry12 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry12,tags=("est_entry12"))

                            est_entry13 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry13,tags=("est_entry13"))

                            

                            save_btn = Button(sr_Canvas_1,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0,command=lambda:"es_saveEstimate()")
                            sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button7")) 

                            def sr_goBack():
                                sr_Canvas_1.grid_forget()
                                

                            back_btn = Button(sr_Canvas_1,text='???  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
                            sr_Canvas_1.create_window(0,0,window=back_btn,tags=("button3"))
                            #--------------
                            es_label6 = Label(sr_Canvas_1,width=20,height=1,text="Estimate Date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label6,tags=('label24'))

                            es_label28 = Label(sr_Canvas_1,width=20,height=1,text="Expiration Date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label28,tags=('label435'))

                            cwidth = root.winfo_screenwidth()

                            es_estdate = DateEntry(sr_Canvas_1,width=19,date_pattern="yyyy-mm-dd",font=('arial 15'),background='#2f516f',foreground='white')

                            es_expdate = DateEntry(sr_Canvas_1,width=19,date_pattern="yyyy-mm-dd",font=('arial 15'),background='#2f516f',foreground='white') 

                            if cwidth > 1280:
                                sr_Canvas_1.create_window(495,442,anchor='nw',window=es_estdate,tags=("date"))
                                sr_Canvas_1.create_window(775,442,anchor='nw',window=es_expdate,tags=("date1"))
                            elif cwidth <= 1024:
                                sr_Canvas_1.create_window(370,455,anchor='nw',window=es_estdate,tags=("date"))
                                sr_Canvas_1.create_window(580,455,anchor='nw',window=es_expdate,tags=("date1"))
                            else:
                                sr_Canvas_1.create_window(465,407,anchor='nw',window=es_estdate,tags=("date"))
                                sr_Canvas_1.create_window(730,407,anchor='nw',window=es_expdate,tags=("date1"))
                    #------------------------------------------------------------------------------------view area
                    def row_selection(event):
                        estm_Canvas_1= Canvas(estm_Frame,bg='#2f516f',scrollregion=(0,0,700,2000))
                        

                        def edit_estim_fn():
                            sr_Canvas_1 = Canvas(estm_Frame,bg='#2f516f',scrollregion=(0,0,700,2500))

                            def responsive_widgets1(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                                
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("poly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.35


                                dcanvas.coords("poly3",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )
                                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                                dcanvas.coords("label2",dwidth/2,dheight/2.4)

                                

                                #sales receipt-----------
                                try:
                                    dcanvas.coords("label21",dwidth/7.91,dheight/1.76)
                                    dcanvas.coords("label22",dwidth/2.47,dheight/1.76)
                                    dcanvas.coords("label23",dwidth/6.13,dheight/1.44)
                                    dcanvas.coords("label24",dwidth/2.27,dheight/1.45)
                                    dcanvas.coords("label25",dwidth/6.13,dheight/0.907)
                                    dcanvas.coords("label26",dwidth/6.13,dheight/0.81)
                                    dcanvas.coords("label27",dwidth/2.27,dheight/0.81)
                                    try:
                                        dcanvas.coords("label28",dwidth/1.395,dheight/0.81)
                                    except:
                                        pass
                                    dcanvas.coords("label29",dwidth/1.225,dheight/1.75)
                                    dcanvas.coords("label30",dwidth/1.2,dheight/1.63)
                                    dcanvas.coords("label31",dwidth/20,dheight/0.675)
                                    dcanvas.coords("label32",dwidth/20,dheight/0.62)
                                    dcanvas.coords("label64",dwidth/20,dheight/0.565)
                                    dcanvas.coords("label65",dwidth/20,dheight/0.519)
                                    dcanvas.coords("label66",dwidth/20,dheight/0.481)
                                    dcanvas.coords("label67",dwidth/2.06,dheight/0.6)
                                    dcanvas.coords("label68",dwidth/2.06,dheight/0.549)
                                    dcanvas.coords("label69",dwidth/2.06,dheight/0.506)
                                    dcanvas.coords("label70",dwidth/2.06,dheight/0.47)
                                    dcanvas.coords("label33",dwidth/7.91,dheight/0.675)
                                    dcanvas.coords("label34",dwidth/4.2,dheight/0.675)
                                    dcanvas.coords("label35",dwidth/2.74,dheight/0.675)
                                    dcanvas.coords("label36",dwidth/2.07,dheight/0.675)
                                    dcanvas.coords("label37",dwidth/1.68,dheight/0.675)
                                    dcanvas.coords("label38",dwidth/1.39,dheight/0.675)
                                    dcanvas.coords("label39",dwidth/1.205,dheight/0.675)
                                    dcanvas.coords("label40",dwidth/1.52,dheight/0.436)
                                    dcanvas.coords("label41",dwidth/1.52,dheight/0.412)
                                    dcanvas.coords("label42",dwidth/1.52,dheight/0.3905)
                                    dcanvas.coords("label435",dwidth/1.54,dheight/1.45)
                                    dcanvas.coords("label25ref",dwidth/1.18,dheight/1.45)

                                    

                                    dcanvas.coords("label44",dwidth/20,dheight/1.135)
                                    dcanvas.coords("label45",dwidth/20,dheight/1.03)
                                    dcanvas.coords("label46",dwidth/7.4,dheight/1.135)
                                    dcanvas.coords("label47",dwidth/3.342,dheight/1.135)
                                    dcanvas.coords("label48",dwidth/2.19,dheight/1.135)
                                    dcanvas.coords("label49",dwidth/1.68,dheight/1.135)
                                    dcanvas.coords("label50",dwidth/1.328,dheight/1.135)
                                    dcanvas.coords("label51",dwidth/1.11,dheight/1.135)
                                    dcanvas.coords("label52",dwidth/1.41,dheight/0.83)
                                    dcanvas.coords("label53",dwidth/1.41,dheight/0.77)
                                    dcanvas.coords("label54",dwidth/1.41,dheight/0.715)

                                    dcanvas.coords("label55",dwidth/2.4,dheight/2.254)
                                    dcanvas.coords("label56",dwidth/1.49,dheight/2.254)
                                    dcanvas.coords("label57",dwidth/2.4,dheight/1.8)
                                    dcanvas.coords("label58",dwidth/2.4,dheight/1.5)
                                    dcanvas.coords("label59",dwidth/2.4,dheight/1.28)
                                    dcanvas.coords("label60",dwidth/1.598,dheight/1.28)
                                    dcanvas.coords("label61",dwidth/1.212,dheight/1.28)
                                    dcanvas.coords("label62",dwidth/2.4,dheight/1.105)
                                    dcanvas.coords("label63",dwidth/2.4,dheight/0.979)

                                    dcanvas.coords("entry13",dwidth/2.72,dheight/1.68)
                                    dcanvas.coords("entry14",dwidth/11,dheight/1.39)
                                    dcanvas.coords("entry15",dwidth/11,dheight/0.885)
                                    dcanvas.coords("entry16",dwidth/11,dheight/0.79)
                                    dcanvas.coords("entry17",dwidth/2.72,dheight/0.79)
                                    dcanvas.coords("entry18",dwidth/5.13,dheight/0.63)
                                    dcanvas.coords("entry19",dwidth/3.39,dheight/0.63)
                                    dcanvas.coords("entry20",dwidth/2.24,dheight/0.63)
                                    dcanvas.coords("entry21",dwidth/1.85,dheight/0.63)
                                    dcanvas.coords("entry22",dwidth/1.5,dheight/0.63)
                                    dcanvas.coords("entry39",dwidth/5.13,dheight/0.5745)
                                    dcanvas.coords("entry40",dwidth/3.39,dheight/0.5745)
                                    dcanvas.coords("entry41",dwidth/2.24,dheight/0.5745)
                                    dcanvas.coords("entry42",dwidth/1.85,dheight/0.5745)
                                    dcanvas.coords("entry43",dwidth/1.5,dheight/0.5745)
                                    dcanvas.coords("entry44",dwidth/5.13,dheight/0.527)
                                    dcanvas.coords("entry45",dwidth/3.39,dheight/0.527)
                                    dcanvas.coords("entry46",dwidth/2.24,dheight/0.527)
                                    dcanvas.coords("entry47",dwidth/1.85,dheight/0.527)
                                    dcanvas.coords("entry48",dwidth/1.5,dheight/0.527)
                                    dcanvas.coords("entry49",dwidth/5.13,dheight/0.487)
                                    dcanvas.coords("entry50",dwidth/3.39,dheight/0.487)
                                    dcanvas.coords("entry51",dwidth/2.24,dheight/0.487)
                                    dcanvas.coords("entry52",dwidth/1.85,dheight/0.487)
                                    dcanvas.coords("entry53",dwidth/1.5,dheight/0.487)

                                    dcanvas.coords("entry23",dwidth/1.35,dheight/0.45)
                                    dcanvas.coords("entry24",dwidth/1.35,dheight/0.435)
                                    dcanvas.coords("entry25",dwidth/1.35,dheight/0.422)
                                    dcanvas.coords("est_entry11",dwidth/1.35,dheight/0.41)
                                    dcanvas.coords("est_entry12",dwidth/1.35,dheight/0.398)
                                    dcanvas.coords("est_entry13",dwidth/1.35,dheight/0.386)
                                    dcanvas.coords("label40",dwidth/1.45,dheight/0.445)
                                    dcanvas.coords("label41",dwidth/1.45,dheight/0.430)
                                    dcanvas.coords("label42",dwidth/1.45,dheight/0.418 )
                                    dcanvas.coords("label43",dwidth/1.60,dheight/0.406)
                                    dcanvas.coords("label44",dwidth/1.45,dheight/0.394)
                                    dcanvas.coords("label45",dwidth/1.46,dheight/0.382)
                                    dcanvas.coords("tcs_sltr",dwidth/1.55,dheight/0.41)
                                    dcanvas.coords("button3",dwidth/28,dheight/3)

                                    dcanvas.coords("entry26",dwidth/11,dheight/0.751)

                                    dcanvas.coords("entry27",dwidth/4.7,dheight/1.057)
                                    dcanvas.coords("entry28",dwidth/2.43,dheight/1.057)
                                    
                                    dcanvas.coords("entry29",dwidth/1.91,dheight/1.057)
                                    dcanvas.coords("entry30",dwidth/1.46,dheight/1.057)

                                    dcanvas.coords("entry31",dwidth/1.275,dheight/0.85)
                                    dcanvas.coords("entry32",dwidth/1.275,dheight/0.784)
                                    dcanvas.coords("entry33",dwidth/1.275,dheight/0.727)
                                    dcanvas.coords("entry34",dwidth/1.525,dheight/1.45)

                                    dcanvas.coords("entry35",dwidth/1.81,dheight/1.24)
                                    dcanvas.coords("entry54",dwidth/1.55,dheight/1.24)
                                    dcanvas.coords("entry36",dwidth/1.33,dheight/1.24)
                                    dcanvas.coords("entry55",dwidth/1.185,dheight/1.24)
                                    dcanvas.coords("entry37",dwidth/2.91,dheight/1.08)
                                    dcanvas.coords("entry56",dwidth/1.55,dheight/1.08)
                                    dcanvas.coords("entry38",dwidth/2.91,dheight/0.96)

                                    dcanvas.coords("combo3",dwidth/11,dheight/1.68)
                                    try:
                                        dcanvas.coords("combo4",dwidth/1.55,dheight/0.79)
                                    except:
                                        pass
                                    dcanvas.coords("combo5",dwidth/7.909,dheight/0.62)
                                    dcanvas.coords("combo6",dwidth/1.206,dheight/0.62)
                                    dcanvas.coords("combo14",dwidth/7.909,dheight/0.5655)
                                    dcanvas.coords("combo15",dwidth/1.206,dheight/0.5655)
                                    dcanvas.coords("combo16",dwidth/7.909,dheight/0.519)
                                    dcanvas.coords("combo17",dwidth/1.206,dheight/0.519)
                                    dcanvas.coords("combo18",dwidth/7.909,dheight/0.481)
                                    dcanvas.coords("combo19",dwidth/1.206,dheight/0.481)

                                    dcanvas.coords("combo7",dwidth/7.4,dheight/1.035)
                                    dcanvas.coords("combo8",dwidth/1.111,dheight/1.035)

                                    dcanvas.coords("combo9",dwidth/1.294,dheight/2.05)
                                    dcanvas.coords("combo10",dwidth/2.91,dheight/1.73)
                                    dcanvas.coords("combo11",dwidth/2.91,dheight/1.45)
                                    dcanvas.coords("combo12",dwidth/2.91,dheight/1.24)

                                    dcanvas.coords("button5",dwidth/3.89,dheight/1.61)
                                    try:
                                        dcanvas.coords("button6",dwidth/1.23,dheight/0.775)
                                    except:
                                        pass
                                    dcanvas.coords("button7",dwidth/1.114,dheight/0.365)
                                    dcanvas.coords("button8",dwidth/1.114,dheight/0.45)

                                    dcanvas.coords("button9",dwidth/1.09,dheight/2.04)
                                    dcanvas.coords("button10",dwidth/1.09,dheight/1.66)
                                    dcanvas.coords("button11",dwidth/1.57,dheight/0.79)

                                    dcanvas.coords("button12",dwidth/1.09,dheight/0.619)
                                    dcanvas.coords("button13",dwidth/1.09,dheight/0.565)
                                    dcanvas.coords("button14",dwidth/1.09,dheight/0.518)
                                    dcanvas.coords("button15",dwidth/1.09,dheight/0.48)
                                    
                                    dcanvas.coords("line17",dwidth/31.6,dheight/0.7,dwidth/1.039,dheight/0.7)
                                    dcanvas.coords("line18",dwidth/31.6,dheight/0.65,dwidth/1.039,dheight/0.65)
                                    dcanvas.coords("line19",dwidth/31.6,dheight/0.59,dwidth/1.039,dheight/0.59)
                                    dcanvas.coords("line20",dwidth/31.6,dheight/0.541,dwidth/1.039,dheight/0.541)
                                    dcanvas.coords("line21",dwidth/31.6,dheight/0.499,dwidth/1.039,dheight/0.499)
                                    dcanvas.coords("line22",dwidth/31.6,dheight/0.464,dwidth/1.039,dheight/0.464)
                                    dcanvas.coords("line23",dwidth/31.6,dheight/0.7,dwidth/31.6,dheight/0.464)
                                    dcanvas.coords("line24",dwidth/1.039,dheight/0.7,dwidth/1.039,dheight/0.464)
                                    dcanvas.coords("line25",dwidth/15,dheight/0.7,dwidth/15,dheight/0.464)
                                    dcanvas.coords("line26",dwidth/5.35,dheight/0.7,dwidth/5.35,dheight/0.464)
                                    dcanvas.coords("line27",dwidth/3.5,dheight/0.7,dwidth/3.5,dheight/0.464)
                                    dcanvas.coords("line28",dwidth/2.28,dheight/0.7,dwidth/2.28,dheight/0.464)
                                    dcanvas.coords("line29",dwidth/1.88,dheight/0.7,dwidth/1.88,dheight/0.464)
                                    dcanvas.coords("line30",dwidth/1.52,dheight/0.7,dwidth/1.52,dheight/0.464)
                                    dcanvas.coords("line31",dwidth/1.277,dheight/0.7,dwidth/1.277,dheight/0.464)
                                    dcanvas.coords("line58",dwidth/1.144,dheight/0.7,dwidth/1.144,dheight/0.464)

                                    dcanvas.coords("line32",dwidth/1.7,dheight/0.451,dwidth/1.039,dheight/0.451)
                                    dcanvas.coords("line33",dwidth/1.7,dheight/0.425,dwidth/1.039,dheight/0.425)
                                    dcanvas.coords("line34",dwidth/1.7,dheight/0.401,dwidth/1.039,dheight/0.401)
                                    dcanvas.coords("line35",dwidth/1.7,dheight/0.38,dwidth/1.039,dheight/0.38)
                                    dcanvas.coords("line36",dwidth/1.7,dheight/0.451,dwidth/1.7,dheight/0.38)
                                    dcanvas.coords("line37",dwidth/1.365,dheight/0.451,dwidth/1.365,dheight/0.38)
                                    dcanvas.coords("line38",dwidth/1.039,dheight/0.451,dwidth/1.039,dheight/0.38)

                                    dcanvas.coords("line39",dwidth/31.6,dheight/1.2,dwidth/1.039,dheight/1.2)
                                    dcanvas.coords("line40",dwidth/31.6,dheight/1.085,dwidth/1.039,dheight/1.085)
                                    dcanvas.coords("line41",dwidth/31.6,dheight/0.99,dwidth/1.039,dheight/0.99)
                                    dcanvas.coords("line42",dwidth/31.6,dheight/0.91,dwidth/1.039,dheight/0.91)
                                    dcanvas.coords("line43",dwidth/31.6,dheight/1.2,dwidth/31.6,dheight/0.91)
                                    dcanvas.coords("line44",dwidth/15,dheight/1.2,dwidth/15,dheight/0.91)
                                    dcanvas.coords("line45",dwidth/4.9,dheight/1.2,dwidth/4.9,dheight/0.91)
                                    dcanvas.coords("line46",dwidth/2.5,dheight/1.2,dwidth/2.5,dheight/0.91)
                                    dcanvas.coords("line47",dwidth/1.95,dheight/1.2,dwidth/1.95,dheight/0.91)
                                    dcanvas.coords("line48",dwidth/1.48,dheight/1.2,dwidth/1.48,dheight/0.91)
                                    dcanvas.coords("line49",dwidth/1.195,dheight/1.2,dwidth/1.195,dheight/0.91)
                                    dcanvas.coords("line50",dwidth/1.039,dheight/1.2,dwidth/1.039,dheight/0.91)

                                    dcanvas.coords("line51",dwidth/1.55,dheight/0.87,dwidth/1.039,dheight/0.87)
                                    dcanvas.coords("line52",dwidth/1.55,dheight/0.8,dwidth/1.039,dheight/0.8)
                                    dcanvas.coords("line53",dwidth/1.55,dheight/0.74,dwidth/1.039,dheight/0.74)
                                    dcanvas.coords("line54",dwidth/1.55,dheight/0.69,dwidth/1.039,dheight/0.69)
                                    dcanvas.coords("line55",dwidth/1.55,dheight/0.87,dwidth/1.55,dheight/0.69)
                                    dcanvas.coords("line56",dwidth/1.29,dheight/0.87,dwidth/1.29,dheight/0.69)
                                    dcanvas.coords("line57",dwidth/1.039,dheight/0.87,dwidth/1.039,dheight/0.69)

                                    dcanvas.coords("line59",dwidth/31.6,dheight/0.7,dwidth/1.039,dheight/0.7)
                                    dcanvas.coords("line60",dwidth/31.6,dheight/0.65,dwidth/1.039,dheight/0.65)
                                    dcanvas.coords("line61",dwidth/31.6,dheight/0.59,dwidth/1.039,dheight/0.59)
                                    dcanvas.coords("line62",dwidth/31.6,dheight/0.541,dwidth/1.039,dheight/0.541)
                                    dcanvas.coords("line63",dwidth/31.6,dheight/0.499,dwidth/1.039,dheight/0.499)
                                    dcanvas.coords("line64",dwidth/31.6,dheight/0.464,dwidth/1.039,dheight/0.464)
                                    dcanvas.coords("line65",dwidth/31.6,dheight/0.7,dwidth/31.6,dheight/0.464)
                                    dcanvas.coords("line66",dwidth/1.039,dheight/0.7,dwidth/1.039,dheight/0.464)
                                    dcanvas.coords("line67",dwidth/15,dheight/0.7,dwidth/15,dheight/0.464)
                                    dcanvas.coords("line68",dwidth/4.5,dheight/0.7,dwidth/4.5,dheight/0.464)
                                    dcanvas.coords("line69",dwidth/2.5,dheight/0.7,dwidth/2.5,dheight/0.464)
                                    dcanvas.coords("line70",dwidth/2,dheight/0.7,dwidth/2,dheight/0.464)
                                    dcanvas.coords("line71",dwidth/1.55,dheight/0.7,dwidth/1.55,dheight/0.464)
                                    dcanvas.coords("line72",dwidth/1.277,dheight/0.7,dwidth/1.277,dheight/0.464)
                                    dcanvas.coords("line73",dwidth/1.144,dheight/0.7,dwidth/1.144,dheight/0.464)

                                    dcanvas.coords("line74",dwidth/1.7,dheight/0.451,dwidth/1.039,dheight/0.451)
                                    dcanvas.coords("line75",dwidth/1.7,dheight/0.425,dwidth/1.039,dheight/0.425)
                                    dcanvas.coords("line76",dwidth/1.7,dheight/0.401,dwidth/1.039,dheight/0.401)
                                    dcanvas.coords("line77",dwidth/1.7,dheight/0.38,dwidth/1.039,dheight/0.38)
                                    dcanvas.coords("line78",dwidth/1.7,dheight/0.451,dwidth/1.7,dheight/0.38)
                                    dcanvas.coords("line79",dwidth/1.365,dheight/0.451,dwidth/1.365,dheight/0.38)
                                    dcanvas.coords("line80",dwidth/1.039,dheight/0.451,dwidth/1.039,dheight/0.38)

                                    dcanvas.coords("label71",dwidth/20,dheight/0.675)
                                    dcanvas.coords("label72",dwidth/20,dheight/0.62)
                                    dcanvas.coords("label73",dwidth/20,dheight/0.565)
                                    dcanvas.coords("label74",dwidth/20,dheight/0.519)
                                    dcanvas.coords("label75",dwidth/20,dheight/0.481)
                                    dcanvas.coords("label76",dwidth/7,dheight/0.675)
                                    dcanvas.coords("label77",dwidth/3.2,dheight/0.675)
                                    dcanvas.coords("label78",dwidth/2.22,dheight/0.675)
                                    dcanvas.coords("label79",dwidth/1.75,dheight/0.675)
                                    dcanvas.coords("label80",dwidth/1.4,dheight/0.675)
                                    dcanvas.coords("label81",dwidth/1.205,dheight/0.675)
                                    dcanvas.coords("label82",dwidth/2.22,dheight/0.6)
                                    dcanvas.coords("label83",dwidth/2.22,dheight/0.549)
                                    dcanvas.coords("label84",dwidth/2.22,dheight/0.506)
                                    dcanvas.coords("label85",dwidth/2.22,dheight/0.47)

                                    dcanvas.coords("combo20",dwidth/6.98,dheight/0.62)
                                    dcanvas.coords("combo21",dwidth/1.206,dheight/0.62)
                                    dcanvas.coords("combo22",dwidth/6.98,dheight/0.5655)
                                    dcanvas.coords("combo23",dwidth/1.206,dheight/0.5655)
                                    dcanvas.coords("combo24",dwidth/6.98,dheight/0.519)
                                    dcanvas.coords("combo25",dwidth/1.206,dheight/0.519)
                                    dcanvas.coords("combo26",dwidth/6.98,dheight/0.481)
                                    dcanvas.coords("combo27",dwidth/1.206,dheight/0.481)

                                    dcanvas.coords("entry57",dwidth/4.32,dheight/0.63)
                                    dcanvas.coords("entry58",dwidth/2.45,dheight/0.63)
                                    dcanvas.coords("entry59",dwidth/1.965,dheight/0.63)
                                    dcanvas.coords("entry60",dwidth/1.525,dheight/0.63)
                                    dcanvas.coords("entry61",dwidth/4.32,dheight/0.5745)
                                    dcanvas.coords("entry62",dwidth/2.45,dheight/0.5745)
                                    dcanvas.coords("entry63",dwidth/1.965,dheight/0.5745)
                                    dcanvas.coords("entry64",dwidth/1.525,dheight/0.5745)
                                    dcanvas.coords("entry65",dwidth/4.32,dheight/0.527)
                                    dcanvas.coords("entry66",dwidth/2.45,dheight/0.527)
                                    dcanvas.coords("entry67",dwidth/1.965,dheight/0.527)
                                    dcanvas.coords("entry68",dwidth/1.525,dheight/0.527)
                                    dcanvas.coords("entry69",dwidth/4.32,dheight/0.487)
                                    dcanvas.coords("entry70",dwidth/2.45,dheight/0.487)
                                    dcanvas.coords("entry71",dwidth/1.965,dheight/0.487)
                                    dcanvas.coords("entry72",dwidth/1.525,dheight/0.487)

                                    dcanvas.coords("line81",dwidth/1.465,dheight/0.7,dwidth/1.465,dheight/0.464)
                                    dcanvas.coords("line82",dwidth/1.2,dheight/0.7,dwidth/1.2,dheight/0.464)
                                    
                                    dcanvas.coords("label86",dwidth/1.65,dheight/0.675)
                                    dcanvas.coords("label87",dwidth/1.325,dheight/0.675)
                                    dcanvas.coords("label88",dwidth/1.115,dheight/0.675)

                                    dcanvas.coords("entry73",dwidth/5.13,dheight/0.63)
                                    dcanvas.coords("entry74",dwidth/3.39,dheight/0.63)
                                    dcanvas.coords("entry75",dwidth/2.24,dheight/0.63)
                                    dcanvas.coords("entry76",dwidth/1.848,dheight/0.63)
                                    dcanvas.coords("entry77",dwidth/1.45,dheight/0.63)
                                    dcanvas.coords("entry78",dwidth/5.13,dheight/0.5745)
                                    dcanvas.coords("entry79",dwidth/3.39,dheight/0.5745)
                                    dcanvas.coords("entry80",dwidth/2.24,dheight/0.5745)
                                    dcanvas.coords("entry81",dwidth/1.848,dheight/0.5745)
                                    dcanvas.coords("entry82",dwidth/1.45,dheight/0.5745)
                                    dcanvas.coords("entry83",dwidth/5.13,dheight/0.527)
                                    dcanvas.coords("entry84",dwidth/3.39,dheight/0.527)
                                    dcanvas.coords("entry85",dwidth/2.24,dheight/0.527)
                                    dcanvas.coords("entry86",dwidth/1.848,dheight/0.527)
                                    dcanvas.coords("entry87",dwidth/1.45,dheight/0.527)
                                    dcanvas.coords("entry88",dwidth/5.13,dheight/0.487)
                                    dcanvas.coords("entry89",dwidth/3.39,dheight/0.487)
                                    dcanvas.coords("entry90",dwidth/2.24,dheight/0.487)
                                    dcanvas.coords("entry91",dwidth/1.848,dheight/0.487)
                                    dcanvas.coords("entry92",dwidth/1.45,dheight/0.487)

                                    dcanvas.coords("combo28",dwidth/1.112,dheight/0.62)
                                    dcanvas.coords("combo29",dwidth/1.112,dheight/0.5655)
                                    dcanvas.coords("combo30",dwidth/1.112,dheight/0.519)
                                    dcanvas.coords("combo31",dwidth/1.112,dheight/0.481)

                                    dcanvas.coords("line83",dwidth/31.6,dheight/1.12,dwidth/1.039,dheight/1.12)
                                    dcanvas.coords("line84",dwidth/31.6,dheight/1,dwidth/1.039,dheight/1)
                                    dcanvas.coords("line85",dwidth/31.6,dheight/0.87,dwidth/1.039,dheight/0.87)
                                    dcanvas.coords("line86",dwidth/31.6,dheight/0.77,dwidth/1.039,dheight/0.77)
                                    dcanvas.coords("line87",dwidth/31.6,dheight/0.69,dwidth/1.039,dheight/0.69)
                                    dcanvas.coords("line88",dwidth/31.6,dheight/0.625,dwidth/1.039,dheight/0.625)
                                    dcanvas.coords("line89",dwidth/31.6,dheight/1.12,dwidth/31.6,dheight/0.625)
                                    dcanvas.coords("line90",dwidth/1.039,dheight/1.12,dwidth/1.039,dheight/0.625)
                                    dcanvas.coords("line91",dwidth/15,dheight/1.12,dwidth/15,dheight/0.625)
                                    dcanvas.coords("line92",dwidth/4.5,dheight/1.12,dwidth/4.5,dheight/0.625)
                                    dcanvas.coords("line93",dwidth/2.5,dheight/1.12,dwidth/2.5,dheight/0.625)
                                    dcanvas.coords("line94",dwidth/2,dheight/1.12,dwidth/2,dheight/0.625)
                                    dcanvas.coords("line95",dwidth/1.5,dheight/1.12,dwidth/1.5,dheight/0.625)
                                    dcanvas.coords("line96",dwidth/1.2,dheight/1.12,dwidth/1.2,dheight/0.625)

                                    dcanvas.coords("line97",dwidth/1.7,dheight/0.6,dwidth/1.039,dheight/0.6)
                                    dcanvas.coords("line98",dwidth/1.7,dheight/0.55,dwidth/1.039,dheight/0.55)
                                    dcanvas.coords("line99",dwidth/1.7,dheight/0.507,dwidth/1.039,dheight/0.507)
                                    dcanvas.coords("line100",dwidth/1.7,dheight/0.47,dwidth/1.039,dheight/0.47)
                                    dcanvas.coords("line101",dwidth/1.7,dheight/0.6,dwidth/1.7,dheight/0.47)
                                    dcanvas.coords("line102",dwidth/1.365,dheight/0.6,dwidth/1.365,dheight/0.47)
                                    dcanvas.coords("line103",dwidth/1.039,dheight/0.6,dwidth/1.039,dheight/0.47)

                                    dcanvas.coords("label89",dwidth/20,dheight/1.05)
                                    dcanvas.coords("label90",dwidth/20,dheight/0.925)
                                    dcanvas.coords("label91",dwidth/20,dheight/0.815)
                                    dcanvas.coords("label92",dwidth/20,dheight/0.725)
                                    dcanvas.coords("label93",dwidth/20,dheight/0.655)
                                    dcanvas.coords("label94",dwidth/7,dheight/1.05)
                                    dcanvas.coords("label95",dwidth/3.2,dheight/1.05)
                                    dcanvas.coords("label96",dwidth/2.22,dheight/1.05)
                                    dcanvas.coords("label97",dwidth/1.72,dheight/1.05)
                                    dcanvas.coords("label98",dwidth/1.34,dheight/1.05)
                                    dcanvas.coords("label99",dwidth/1.121,dheight/1.05)

                                    dcanvas.coords("label100",dwidth/1.52,dheight/0.572)
                                    dcanvas.coords("label101",dwidth/1.52,dheight/0.528)
                                    dcanvas.coords("label102",dwidth/1.52,dheight/0.487)

                                    dcanvas.coords("label103",dwidth/2.22,dheight/0.89)
                                    dcanvas.coords("label104",dwidth/2.22,dheight/0.785)
                                    dcanvas.coords("label105",dwidth/2.22,dheight/0.701)
                                    dcanvas.coords("label106",dwidth/2.22,dheight/0.635)

                                    dcanvas.coords("entry93",dwidth/4.32,dheight/0.952)
                                    dcanvas.coords("entry94",dwidth/2.45,dheight/0.952)
                                    dcanvas.coords("entry95",dwidth/1.967,dheight/0.952)
                                    dcanvas.coords("entry96",dwidth/1.485,dheight/0.952)
                                    dcanvas.coords("entry97",dwidth/4.32,dheight/0.835)
                                    dcanvas.coords("entry98",dwidth/2.45,dheight/0.835)
                                    dcanvas.coords("entry99",dwidth/1.967,dheight/0.835)
                                    dcanvas.coords("entry100",dwidth/1.485,dheight/0.835)
                                    dcanvas.coords("entry101",dwidth/4.32,dheight/0.742)
                                    dcanvas.coords("entry102",dwidth/2.45,dheight/0.742)
                                    dcanvas.coords("entry103",dwidth/1.967,dheight/0.742)
                                    dcanvas.coords("entry104",dwidth/1.485,dheight/0.742)
                                    dcanvas.coords("entry105",dwidth/4.32,dheight/0.667)
                                    dcanvas.coords("entry106",dwidth/2.45,dheight/0.667)
                                    dcanvas.coords("entry107",dwidth/1.967,dheight/0.667)
                                    dcanvas.coords("entry108",dwidth/1.485,dheight/0.667)

                                    dcanvas.coords("entry109",dwidth/1.35,dheight/0.582)
                                    dcanvas.coords("entry110",dwidth/1.35,dheight/0.535)
                                    dcanvas.coords("entry111",dwidth/1.35,dheight/0.494)

                                    dcanvas.coords("combo32",dwidth/6.98,dheight/0.93)
                                    dcanvas.coords("combo33",dwidth/1.112,dheight/0.93)
                                    dcanvas.coords("combo34",dwidth/6.98,dheight/0.815)
                                    dcanvas.coords("combo35",dwidth/1.112,dheight/0.815)
                                    dcanvas.coords("combo36",dwidth/6.98,dheight/0.728)
                                    dcanvas.coords("combo37",dwidth/1.112,dheight/0.728)
                                    dcanvas.coords("combo38",dwidth/6.98,dheight/0.655)
                                    dcanvas.coords("combo39",dwidth/1.112,dheight/0.655)

                                    dcanvas.coords("date",dwidth/2.71,dheight/1.392)
                                    dcanvas.coords("date1",dwidth/1.73,dheight/1.392)

                                    dcanvas.coords("entry87ref",dwidth/1.29,dheight/1.392)

                                except:
                                    pass

                                

                            sr_Scroll_1 = Scrollbar(estm_Frame,orient=VERTICAL)
                            sr_Scroll_1.grid(row=0,column=1,sticky='ns')
                            sr_Scroll_1.config(command=sr_Canvas_1.yview)
                            sr_Canvas_1.bind("<Configure>", responsive_widgets1)
                            sr_Canvas_1.config(yscrollcommand=sr_Scroll_1.set)
                            sr_Canvas_1.grid(row=0,column=0,sticky='nsew')

                            
                            sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
                            es_label1 = Label(sr_Canvas_1,width=18,height=1,text="ESTIMATE",font=('arial 25'),background='#1b3857',fg="white")
                            sr_Canvas_1.create_window(0,0,anchor="c",window=es_label1,tags=("label1"))
                            sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

                            sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly3"))   

                            es_label2 = Label(sr_Canvas_1,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
                            sr_Canvas_1.create_window(0,0,anchor="c",window=es_label2,tags=("label2"))

                            es_label3 = Label(sr_Canvas_1,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                            sr_Canvas_1.create_window(0,0,window=es_label3,tags=("label21"))

                            user_sql = "SELECT id FROM auth_user WHERE username=%s"
                            user_val = (nm_ent.get(),)
                            fbcursor.execute(user_sql,user_val)
                            user_data = fbcursor.fetchone()

                            comp_sql = 'SELECT * FROM app1_company WHERE id_id=%s'
                            comp_val = (user_data[0],)
                            fbcursor.execute(comp_sql,comp_val)
                            comp_data = fbcursor.fetchone()

                            cust_sql = "SELECT firstname,lastname FROM app1_customer WHERE cid_id=%s"
                            cust_val = (comp_data[0],)
                            fbcursor.execute(cust_sql,cust_val)
                            cust_data = fbcursor.fetchall()

                            cust_list = []
                            if not cust_data:
                                cust_list.append('Select Customer')
                            else:
                                for c in cust_data:
                                    cust_list.append(c[0] + " " + c[1])
                                cust_list.insert(0,'Select Customer')

                            def es_fetch_custDetails(event):
                                cust_name = es_custCombo.get()
                                cust_fname = cust_name.split(" ")[0]
                                cust_lname = cust_name.split(" ")[1]

                                cust_sql = "SELECT * FROM app1_customer WHERE firstname=%s and lastname=%s and cid_id=%s"
                                cust_val = (cust_fname,cust_lname,comp_data[0])
                                fbcursor.execute(cust_sql,cust_val)
                                cust_data = fbcursor.fetchone()

                                inv_sql = "SELECT * FROM app1_invoice WHERE customername=%s and cid_id=%s"
                                inv_val = (cust_name,comp_data[0])
                                fbcursor.execute(inv_sql,inv_val)
                                inv_data = fbcursor.fetchall()

                                try:
                                    if not cust_data:
                                        pass
                                    else:
                                        es_email.delete(0,END)
                                        es_email.insert(0,cust_data[9])
                                        es_baddress.delete("1.0","end-1c")
                                        es_baddress.insert("1.0",cust_data[2] + " " + cust_data[3] + "\n" + cust_data[4] + "\n" + cust_data[12] + "\n" + cust_data[13] + "\n" + cust_data[14] + "\n" + cust_data[15] + "\n" + cust_data[16])
                                        es_pofsupply.delete(0,END)
                                        es_pofsupply.insert(0,comp_data[4])
                                except:
                                    pass

                            es_custCombo = ttk.Combobox(sr_Canvas_1,width=15,font=('arial 15'))
                            es_custCombo["values"] = cust_list
                            es_custCombo.current(0)
                            es_custCombo.bind("<<ComboboxSelected>>",es_fetch_custDetails)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=es_custCombo,tags=("combo3"))

                            def sr_addCustomer_1():
                                
                                sr_Frame_2 = Frame(estm_Frame,)
                                sr_Frame_2.grid(row=0,column=0,sticky='nsew')

                                def responsive_widgets2(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                    
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("poly1",x1 + r1,y1,
                                    x1 + r1,y1,
                                    x2 - r1,y1,
                                    x2 - r1,y1,     
                                    x2,y1,     
                                    #--------------------
                                    x2,y1 + r1,     
                                    x2,y1 + r1,     
                                    x2,y2 - r1,     
                                    x2,y2 - r1,     
                                    x2,y2,
                                    #--------------------
                                    x2 - r1,y2,     
                                    x2 - r1,y2,     
                                    x1 + r1,y2,
                                    x1 + r1,y2,
                                    x1,y2,
                                    #--------------------
                                    x1,y2 - r1,
                                    x1,y2 - r1,
                                    x1,y1 + r1,
                                    x1,y1 + r1,
                                    x1,y1,
                                    )

                                    dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                                    
                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.6


                                    dcanvas.coords("poly2",x11 + r2,y11,
                                    x11 + r2,y11,
                                    x21 - r2,y11,
                                    x21 - r2,y11,     
                                    x21,y11,     
                                    #--------------------
                                    x21,y11 + r2,     
                                    x21,y11 + r2,     
                                    x21,y21 - r2,     
                                    x21,y21 - r2,     
                                    x21,y21,
                                    #--------------------
                                    x21 - r2,y21,     
                                    x21 - r2,y21,     
                                    x11 + r2,y21,
                                    x11 + r2,y21,
                                    x11,y21,
                                    #--------------------
                                    x11,y21 - r2,
                                    x11,y21 - r2,
                                    x11,y11 + r2,
                                    x11,y11 + r2,
                                    x11,y11,
                                    )

                                    dcanvas.coords("label1",dwidth/2,dheight/8.24)
                                    dcanvas.coords("label2",dwidth/6,dheight/2.4)
                                    dcanvas.coords("label3",dwidth/8.2,dheight/2)
                                    dcanvas.coords("label4",dwidth/2.8,dheight/2)
                                    dcanvas.coords("label5",dwidth/1.7,dheight/2)
                                    dcanvas.coords("label6",dwidth/8.2,dheight/1.66)
                                    dcanvas.coords("label7",dwidth/2.8,dheight/1.66)
                                    dcanvas.coords("label8",dwidth/8.2,dheight/1.42)
                                    dcanvas.coords("label9",dwidth/2.8,dheight/1.42)
                                    dcanvas.coords("label10",dwidth/1.7,dheight/1.42)
                                    dcanvas.coords("label11",dwidth/8.2,dheight/1.24)
                                    dcanvas.coords("label12",dwidth/2.8,dheight/1.24)
                                    dcanvas.coords("label13",dwidth/1.7,dheight/1.24)
                                    dcanvas.coords("label14",dwidth/5.97,dheight/1.09)
                                    dcanvas.coords("label15",dwidth/8.2,dheight/0.98)
                                    dcanvas.coords("label16",dwidth/1.71,dheight/0.98)
                                    dcanvas.coords("label17",dwidth/1.58,dheight/1.09)
                                    dcanvas.coords("label18",dwidth/8.2,dheight/0.824)
                                    dcanvas.coords("label19",dwidth/2.62,dheight/0.824)
                                    dcanvas.coords("label20",dwidth/1.7,dheight/0.824)
                                    dcanvas.coords("label21",dwidth/1.185,dheight/0.824)
                                    dcanvas.coords("label22",dwidth/8.2,dheight/0.76)
                                    dcanvas.coords("label23",dwidth/2.62,dheight/0.76)
                                    dcanvas.coords("label24",dwidth/1.7,dheight/0.76)
                                    dcanvas.coords("label25",dwidth/1.185,dheight/0.76)
                                    dcanvas.coords("label26",dwidth/1.28,dheight/1.087)
                                    dcanvas.coords("label27",dwidth/6.3,dheight/0.699)

                                    dcanvas.coords("line1",dwidth/21,dheight/2.2,dwidth/1.055,dheight/2.2)

                                    dcanvas.coords("combo1",dwidth/20,dheight/1.9)
                                    dcanvas.coords("combo2",dwidth/20,dheight/1.37)

                                    dcanvas.coords("entry2",dwidth/3.52,dheight/1.9)
                                    dcanvas.coords("entry3",dwidth/1.94,dheight/1.9)
                                    dcanvas.coords("entry4",dwidth/20,dheight/1.6)
                                    dcanvas.coords("entry5",dwidth/3.52,dheight/1.6)
                                    dcanvas.coords("entry6",dwidth/3.52,dheight/1.38)
                                    dcanvas.coords("entry7",dwidth/1.94,dheight/1.38)
                                    dcanvas.coords("entry8",dwidth/20,dheight/1.21)
                                    dcanvas.coords("entry9",dwidth/3.52,dheight/1.21)
                                    dcanvas.coords("entry10",dwidth/1.94,dheight/1.21)
                                    dcanvas.coords("entry11",dwidth/20,dheight/0.96)
                                    dcanvas.coords("entry12",dwidth/1.95,dheight/0.96)
                                    dcanvas.coords("entry13",dwidth/20,dheight/0.81)
                                    dcanvas.coords("entry14",dwidth/3.23,dheight/0.81)
                                    dcanvas.coords("entry15",dwidth/1.94,dheight/0.81)
                                    dcanvas.coords("entry16",dwidth/1.296,dheight/0.81)
                                    dcanvas.coords("entry17",dwidth/20,dheight/0.749)
                                    dcanvas.coords("entry18",dwidth/3.23,dheight/0.749)
                                    dcanvas.coords("entry19",dwidth/1.94,dheight/0.749)
                                    dcanvas.coords("entry20",dwidth/1.296,dheight/0.749)

                                    dcanvas.coords("check1",dwidth/1.45,dheight/1.11)
                                    dcanvas.coords("check2",dwidth/20,dheight/0.71)

                                    dcanvas.coords("button1",dwidth/2,dheight/0.655)
                                    dcanvas.coords("button2",dwidth/27,dheight/3)

                                sr_Canvas_2 = Canvas(sr_Frame_2,bg='#2f516f',scrollregion=(0,0,700,1200))

                                sr_Frame_2.grid_columnconfigure(0,weight=1)
                                sr_Frame_2.grid_rowconfigure(0,weight=1)

                                sr_Scroll_2 = Scrollbar(sr_Frame_2,orient=VERTICAL)
                                sr_Scroll_2.grid(row=0,column=1,sticky='ns')
                                sr_Scroll_2.config(command=sr_Canvas_2.yview)
                                sr_Canvas_2.bind("<Configure>", responsive_widgets2)
                                sr_Canvas_2.config(yscrollcommand=sr_Scroll_2.set)
                                sr_Canvas_2.grid(row=0,column=0,sticky='nsew')

                                sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
                                cust_label1 = Label(sr_Canvas_2,width=18,height=1,text="ADD CUSTOMER",font=('arial 25'),background='#1b3857',fg="white")
                                sr_Canvas_2.create_window(0,0,anchor="c",window=cust_label1,tags=("label1"))
                                sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

                                sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

                                cust_label2 = Label(sr_Canvas_2,width=20,height=1,text="Customer Information",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label2,tags=('label2'))

                                sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))

                                cust_label3 = Label(sr_Canvas_2,width=20,height=1,text="Title",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label3,tags=('label3'))

                                cust_title = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                                cust_title['values'] = ['Mr','Mrs','Miss','Ms',]
                                cust_title.current(0)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

                                cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

                                cust_fname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

                                cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

                                cust_lname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

                                cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

                                cust_company = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

                                cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

                                cust_location = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

                                cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

                                def select_GSTtype(event):
                                    if cust_gtype.get() == 'GST unregistered' or cust_gtype.get() == 'Consumer' or cust_gtype.get() == 'Overseas':
                                        sr_Canvas_2.itemconfig("label9",state='hidden')
                                        sr_Canvas_2.itemconfig("entry6",state='hidden')
                                    else:
                                        sr_Canvas_2.itemconfig("label9",state='normal')
                                        sr_Canvas_2.itemconfig("entry6",state='normal')

                                cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                                cust_gtype['values'] = ['Choose...','GST registered- Regular','GST registered- Composition','GST unregistered','Consumer','Overseas','SEZ',"Deemed exports - EOU's STP's EHTP's etc"]
                                cust_gtype.current(0)
                                cust_gtype.bind("<<ComboboxSelected>>",select_GSTtype)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

                                cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

                                gstinVar = StringVar()
                                cust_gin = Entry(sr_Canvas_2,textvariable=gstinVar,width=20,font=('arial 15'),background='#2f516f',foreground='grey')
                                cust_gin.insert(0,'29APPCK7465F1Z1')

                                def del_placeholder(event):
                                    if cust_gin.get() == '29APPCK7465F1Z1':
                                        cust_gin.delete(0,END)
                                        cust_gin.config(fg="white")
                                    else:
                                        pass

                                cust_gin.bind("<FocusIn>",del_placeholder)

                                def ret_placeholder(event):
                                    if cust_gin.get() == '':
                                        cust_gin.insert(0,'29APPCK7465F1Z1')
                                        cust_gin.config(fg="grey")
                                    else:
                                        pass
                                cust_gin.bind("<FocusOut>",ret_placeholder)
                                
                                def validate_gstin(value):
                                    pattern = r'[0-9]{2}[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[a-zA-Z]{1}[0-9a-zA-Z]{1}'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_gin.config(fg="white")
                                        return True

                                def invalid_gstin():
                                    cust_gin.config(fg="red")

                                valid_cmndGSTIN = (sr_Canvas_2.register(validate_gstin),'%P')
                                invalid_cmndGSTIN = (sr_Canvas_2.register(invalid_gstin),)
                                cust_gin.config(validate='focusout',validatecommand=valid_cmndGSTIN,invalidcommand=invalid_cmndGSTIN)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

                                cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

                                panVar = StringVar()
                                cust_pan = Entry(sr_Canvas_2,width=20,textvariable=panVar,font=('arial 15'),background='#2f516f',foreground='grey')
                                cust_pan.insert(0,'APPCK7465F')

                                def del_placeholder(event):
                                    if cust_pan.get() == 'APPCK7465F':
                                        cust_pan.delete(0,END)
                                        cust_pan.config(fg="white")
                                    else:
                                        pass

                                cust_pan.bind("<FocusIn>",del_placeholder)

                                def ret_placeholder(event):
                                    if cust_pan.get() == '':
                                        cust_pan.insert(0,'APPCK7465F')
                                        cust_pan.config(fg="grey")
                                    else:
                                        pass
                                cust_pan.bind("<FocusOut>",ret_placeholder)

                                def validate_pan(value):
                                    pattern = r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_pan.config(fg="white")
                                        return True

                                def invalid_pan():
                                    cust_pan.config(fg="red")

                                valid_cmndPAN = (sr_Canvas_2.register(validate_pan),'%P')
                                invalid_cmndPAN = (sr_Canvas_2.register(invalid_pan),)
                                cust_pan.config(validate='focusout',validatecommand=valid_cmndPAN,invalidcommand=invalid_cmndPAN)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

                                cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

                                emailVar = StringVar()
                                cust_email = Entry(sr_Canvas_2,textvariable=emailVar,width=20,font=('arial 15'),background='#2f516f',foreground='white')

                                def validate_email(value):
                                    pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_email.config(fg="white")
                                        return True

                                def invalid_email():
                                    cust_email.config(fg="red")

                                valid_cmndEMAIL = (sr_Canvas_2.register(validate_email),'%P')
                                invalid_cmndEMAIL = (sr_Canvas_2.register(invalid_email),)
                                cust_email.config(validate='focusout',validatecommand=valid_cmndEMAIL,invalidcommand=invalid_cmndEMAIL)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

                                cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

                                webVar = StringVar()
                                cust_web = Entry(sr_Canvas_2,textvariable=webVar,width=20,font=('arial 15'),background='#2f516f',foreground='white')

                                def validate_web(value):
                                    pattern = r'www.+[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_web.config(fg="white")
                                        return True

                                def invalid_web():
                                    cust_web.config(fg="red")

                                valid_cmndWEB = (sr_Canvas_2.register(validate_web),'%P')
                                invalid_cmndWEB = (sr_Canvas_2.register(invalid_web),)
                                cust_web.config(validate='focusout',validatecommand=valid_cmndWEB,invalidcommand=invalid_cmndWEB)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

                                cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

                                mobVar = StringVar()
                                cust_mob = Entry(sr_Canvas_2,textvariable=mobVar,width=20,font=('arial 15'),background='#2f516f',foreground='white')

                                def validate_mobile(value):
                                    pattern = r'[7-9][0-9]{9}'
                                    if re.fullmatch(pattern,value) is None:
                                        return False
                                    else:
                                        cust_mob.config(fg="white")
                                        return True

                                def invalid_mobile():
                                    cust_mob.config(fg="red")

                                valid_cmndMOB = (sr_Canvas_2.register(validate_mobile),'%P')
                                invalid_cmndMOB = (sr_Canvas_2.register(invalid_mobile),)
                                cust_mob.config(validate='focusout',validatecommand=valid_cmndMOB,invalidcommand=invalid_cmndMOB)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

                                cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

                                cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

                                cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=48,height=3,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

                                cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

                                cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

                                cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=48,height=3,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

                                cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

                                cust_city = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

                                cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

                                cust_state = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

                                cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

                                cust_city1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

                                cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

                                cust_state1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
                                #--
                                cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin Code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

                                cust_pin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

                                cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

                                cust_country = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

                                cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

                                cust_pin1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

                                cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

                                cust_country1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country1,tags=("entry20"))

                                def sameas_billaddress():
                                    if sameasVar.get() == True:
                                        bill_address = cust_st1.get("1.0","end-1c")
                                        bill_city = cust_city.get()
                                        bill_state = cust_state.get()
                                        bill_pin = cust_pin.get()
                                        bill_country = cust_country.get()

                                        cust_st2.delete("1.0","end-1c")
                                        cust_st2.insert("1.0",bill_address)
                                        cust_city1.delete(0,END)
                                        cust_city1.insert(0,bill_city)
                                        cust_state1.delete(0,END)
                                        cust_state1.insert(0,bill_state)
                                        cust_pin1.delete(0,END)
                                        cust_pin1.insert(0,bill_pin)
                                        cust_country1.delete(0,END)
                                        cust_country1.insert(0,bill_country)
                                    else:
                                        pass

                                sameasVar = BooleanVar()
                                cust_sameb = Checkbutton(sr_Canvas_2,variable=sameasVar,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857",command=sameas_billaddress)
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_sameb,tags=("check1"))

                                cust_label26 = Label(sr_Canvas_2,width=20,height=1,text="Same as billing address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label26,tags=('label26'))

                                termVar = BooleanVar()
                                cust_term = Checkbutton(sr_Canvas_2,variable=termVar,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
                                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_term,tags=("check2"))

                                cust_label27 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                                sr_Canvas_2.create_window(0,0,window=cust_label27,tags=('label27'))

                                def sr_create_newCustomer():
                                    title = cust_title.get()
                                    firstname = cust_fname.get()
                                    lastname = cust_lname.get()
                                    company = cust_company.get()
                                    location = cust_location.get()
                                    gsttype = cust_gtype.get()
                                    gstin = gstinVar.get()
                                    panno = panVar.get()
                                    email = emailVar.get()
                                    website = webVar.get()
                                    mobile = mobVar.get()
                                    street = cust_st1.get("1.0","end-1c")
                                    city = cust_city.get()
                                    state = cust_state.get()
                                    pincode = cust_pin.get()
                                    country = cust_country.get()
                                    shipstreet = cust_st2.get("1.0","end-1c")
                                    shipcity = cust_city1.get()
                                    shipstate = cust_state1.get()
                                    shippincode = cust_pin1.get()
                                    shipcountry = cust_country1.get()

                                    
                                    user_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    user_val = (nm_ent.get(),)
                                    fbcursor.execute(user_sql,user_val)
                                    user_data = fbcursor.fetchone()

                                    comp_sql = 'SELECT cid FROM app1_company WHERE id_id=%s'
                                    comp_val = (user_data[0],)
                                    fbcursor.execute(comp_sql,comp_val)
                                    comp_data = fbcursor.fetchone()
                                    cid  = comp_data[0]

                                    
                                    
                                    if gsttype == "GST unregistered" or gsttype == "Consumer" or gsttype == "Overseas":
                                        gstin = ''
                                        if validate_pan(panno) is False:
                                            pass 
                                        elif validate_email(email) is False: 
                                            pass
                                        elif validate_web(website) is False:
                                            pass 
                                        elif validate_mobile(mobile) is False:
                                            pass
                                        else:
                                            if termVar.get() == False:
                                                pass
                                            else:
                                                if gsttype == "Choose...":
                                                    pass
                                                else:
                                                    ins_cust_sql = "INSERT INTO app1_customer(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
                                                    ins_cust_val = (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid,)
                                                    fbcursor.execute(ins_cust_sql,ins_cust_val)
                                                    finsysdb.commit()
                                                    sr_Frame_2.destroy()
                                                    cust_sql = "SELECT firstname,lastname FROM app1_customer"
                                                    fbcursor.execute(cust_sql,)
                                                    cust_data = fbcursor.fetchall()

                                                    cust_list = []
                                                    if not cust_data:
                                                        cust_list.append('Select Customer')
                                                    else:
                                                        for c in cust_data:
                                                            cust_list.append(c[0] + " " + c[1])
                                                        cust_list.insert(0,'Select Customer')
                                                        es_custCombo["values"] = cust_list
                                                    sr_Frame_1.grid(row=0,column=0,sticky='nsew')
                                    elif gstin == '29APPCK7465F1Z1' or panno == 'APPCK7465F':
                                        pass
                                    else:
                                        if validate_gstin(gstin) is False: 
                                            pass
                                        elif validate_pan(panno) is False:
                                            pass 
                                        elif validate_email(email) is False: 
                                            pass
                                        elif validate_web(website) is False:
                                            pass
                                        elif validate_mobile(mobile) is False:
                                            pass
                                        else:
                                            if termVar.get() == False:
                                                pass
                                            else:
                                                if gsttype == "Choose...":
                                                    pass
                                                else:
                                                    ins_cust_sql = "INSERT INTO app1_customer(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
                                                    ins_cust_val = (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid,)
                                                    fbcursor.execute(ins_cust_sql,ins_cust_val)
                                                    finsysdb.commit()
                                                    sr_Frame_2.destroy()
                                                    cust_sql = "SELECT firstname,lastname FROM app1_customer"
                                                    fbcursor.execute(cust_sql,)
                                                    cust_data = fbcursor.fetchall()

                                                    cust_list = []
                                                    if not cust_data:
                                                        cust_list.append('Select Customer')
                                                    else:
                                                        for c in cust_data:
                                                            cust_list.append(c[0] + " " + c[1])
                                                        cust_list.insert(0,'Select Customer')
                                                        es_custCombo["values"] = cust_list
                                                    
                                
                                cust_save = Button(sr_Canvas_2,text="Submit Form",font=('arial 12 bold'),width=40,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0,command=lambda:sr_create_newCustomer())
                                sr_Canvas_2.create_window(0,0,window=cust_save,tags=("button1"))

                                def es_goBack():
                                    sr_Frame_2.grid_forget()
                                    

                                back_btn = Button(sr_Canvas_2,text='???  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:es_goBack())
                                sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button2"))

                            es_plus = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:sr_addCustomer_1())
                            sr_Canvas_1.create_window(0,0,window=es_plus,tags=("button5"))

                            es_label4 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label4,tags=('label22'))

                            es_email = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=es_email,tags=("entry13"))

                            es_label5 = Label(sr_Canvas_1,width=20,height=1,text="Billing Address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label5,tags=('label23'))

                            es_baddress = Text(sr_Canvas_1,width=20,font=('arial 15'),height=7,background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=es_baddress,tags=("entry14"))

                            es_label7 = Label(sr_Canvas_1,width=20,height=1,text="Place of Supply",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label7,tags=('label25'))

                            es_pofsupply = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=es_pofsupply,tags=("entry15"))

                            es_label7 = Label(sr_Canvas_1,width=20,height=1,text="Reference Number",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label7,tags=('label25ref'))
                            
                            est_entry_ref = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')                           
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry_ref,tags=("entry87ref"))

                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line17"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line18"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line19"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line20"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line21"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line22"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line23"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line24"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line25"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line26"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line27"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line28"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line29"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line81"))
                            sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line82"))

                            

                            es_label13 = Label(sr_Canvas_1,width=3,height=1,text="#",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label13,tags=('label31'))

                            es_label14 = Label(sr_Canvas_1,width=3,height=1,text="1",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label14,tags=('label32'))

                            es_label29 = Label(sr_Canvas_1,width=3,height=1,text="2",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label29,tags=('label64'))

                            es_label30 = Label(sr_Canvas_1,width=3,height=1,text="3",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label30,tags=('label65'))

                            es_label31 = Label(sr_Canvas_1,width=3,height=1,text="4",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label31,tags=('label66'))

                            es_label18 = Label(sr_Canvas_1,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label18,tags=('label33'))

                            es_label19 = Label(sr_Canvas_1,width=10,height=1,text="HSN",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label19,tags=('label34'))

                            es_label20 = Label(sr_Canvas_1,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label20,tags=('label35'))

                            es_label21 = Label(sr_Canvas_1,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label21,tags=('label36'))

                            es_label22 = Label(sr_Canvas_1,width=10,height=1,text="Price",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label22,tags=('label86'))

                            es_label23 = Label(sr_Canvas_1,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label23,tags=('label87'))

                            es_label24 = Label(sr_Canvas_1,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label24,tags=('label88'))

                            user_sql = "SELECT id FROM auth_user WHERE username=%s"
                            user_val = (nm_ent.get(),)
                            fbcursor.execute(user_sql,user_val)
                            user_data = fbcursor.fetchone()

                            comp_sql = 'SELECT * FROM app1_company WHERE id_id=%s'
                            comp_val = (user_data[0],)
                            fbcursor.execute(comp_sql,comp_val)
                            comp_data = fbcursor.fetchone()

                            get_inventory_sql = "SELECT * FROM app1_inventory WHERE cid_id=%s" 
                            get_inventory_val = (comp_data[0],)                      
                            fbcursor.execute(get_inventory_sql,get_inventory_val)
                            get_inventory_data = fbcursor.fetchall()

                            get_noninventory_sql = "SELECT * FROM app1_noninventory WHERE cid_id=%s" 
                            get_noninventory_val = (comp_data[0],)                      
                            fbcursor.execute(get_noninventory_sql,get_noninventory_val)
                            get_noninventory_data = fbcursor.fetchall()

                            get_bundle_sql = "SELECT * FROM app1_bundle WHERE cid_id=%s" 
                            get_bundle_val = (comp_data[0],)                      
                            fbcursor.execute(get_bundle_sql,get_bundle_val)
                            get_bundle_data = fbcursor.fetchall()

                            product_list = []

                            if not get_inventory_data:
                                pass
                            else:
                                for i in get_inventory_data:
                                    product_list.append(i[2])

                            if not get_noninventory_data:
                                pass
                            else:
                                for n in get_noninventory_data:
                                    product_list.append(n[2])

                            if not get_bundle_data:
                                pass
                            else:
                                for b in get_bundle_data:
                                    product_list.append(b[2])
                            
                            # product_list.insert(0,"Select Product")

                            def es_fetch_proDetails1(event):
                                pass

                            est_entry1 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry1['values'] = product_list
                            est_entry1.current(0)
                            est_entry1.bind("<<ComboboxSelected>>",es_fetch_proDetails1)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry1,tags=("combo5"))

                            est_entry2 = Entry(sr_Canvas_1,width=9,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry2,tags=("entry73"))

                            est_entry3 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry3,tags=("entry74"))

                            def est_calculateTotal1(event,s):
                                pass

                            est_entry4 = Spinbox(sr_Canvas_1,from_=0,to=100,width=7,font=('arial 15'),background='#2f516f',foreground='white',justify=RIGHT)
                            est_entry4.bind("<Key>",lambda event,sp = 1:est_calculateTotal1(event,sp))
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry4,tags=("entry75"))

                            est_entry5 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry5,tags=("entry76"))

                            est_entry6 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            est_entry6.delete(0,END)
                            est_entry6.insert(0,0)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry6,tags=("entry77"))
                            def calcu_cmd(event):
                                pass
                                    
                            est_entry7 = ttk.Combobox(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='black')
                            cplace_gstlist = ['Choose','28.0% GST(28%)','18.0% GST(18%)','12.0% GST(12%)','06.0% GST(06%)',
                                '05.0% GST(05%)','03.0% GST(03%)','0.25% GST(0.25%)','0.0% GST(0%)','Exempt GST(0%)','Out of Scope(0%)']
                            est_entry7['values'] = cplace_gstlist
                            est_entry7.current(0)
                            est_entry7.bind('<<ComboboxSelected>>',calcu_cmd)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry7,tags=("combo28"))

                            def es_fetch_proDetails2(event):
                                pass

                            est_entry11 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry11['values'] = product_list
                            est_entry11.current(0)
                            est_entry11.bind("<<ComboboxSelected>>",es_fetch_proDetails2)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry11,tags=("combo14"))

                            est_entry12 = Entry(sr_Canvas_1,width=9,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry12,tags=("entry78"))

                            est_entry13 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry13,tags=("entry79"))

                            est_entry14 = Spinbox(sr_Canvas_1,from_=0,to=100,width=7,font=('arial 15'),background='#2f516f',foreground='white',justify=RIGHT)
                            est_entry14.bind("<Key>",lambda event,sp = 2:est_calculateTotal1(event,sp))
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry14,tags=("entry80"))

                            est_entry15 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry15,tags=("entry81"))

                            est_entry16 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            est_entry16.delete(0,END)
                            est_entry16.insert(0,0)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry16,tags=("entry82"))

                            est_entry17 = ttk.Combobox(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry17['values'] = cplace_gstlist
                            est_entry17.current(0)
                            est_entry17.bind('<<ComboboxSelected>>',calcu_cmd)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry17,tags=("combo29"))

                            def es_fetch_proDetails3(event):
                                try:
                                    get_pro_sql = "SELECT * FROM app1_inventory WHERE name=%s AND cid_id=%s"
                                    get_pro_val = (est_entry18.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql,get_pro_val)
                                    get_pro_data = fbcursor.fetchone()
                                except:
                                    pass

                                try:
                                    get_pro_sql1 = "SELECT * FROM app1_noninventory WHERE name=%s AND cid_id=%s"
                                    get_pro_val1 = (est_entry18.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql1,get_pro_val1)
                                    get_pro_data1 = fbcursor.fetchone()
                                except:
                                    pass

                                try:
                                    get_pro_sql3 = "SELECT * FROM app1_bundle WHERE name=%s AND cid_id=%s"
                                    get_pro_val3 = (est_entry18.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql3,get_pro_val3)
                                    get_pro_data3 = fbcursor.fetchone()
                                except:
                                    pass

                                #--------------------------------------------------------
                                if get_pro_data is not None:
                                    try:
                                        sr_Canvas_1.itemconfig("label69",state='normal')
                                        es_label34.config(text="Available Qty : " + get_pro_data[7])
                                        est_entry19.delete(0,END)
                                        est_entry19.insert(0,get_pro_data[4])
                                        est_entry20.delete(0,END)
                                        est_entry20.insert(0,get_pro_data[11])
                                        est_entry22.delete(0,END)
                                        est_entry22.insert(0,get_pro_data[12])
                                    except:
                                        pass
                                elif get_pro_data1 is not None:
                                    try:
                                        sr_Canvas_1.itemconfig("label69",state='normal')
                                        es_label34.config(text="Available Qty : " + get_pro_data1[17])
                                        est_entry19.delete(0,END)
                                        est_entry19.insert(0,get_pro_data1[4])
                                        est_entry20.delete(0,END)
                                        est_entry20.insert(0,get_pro_data1[7])
                                        est_entry22.delete(0,END)
                                        est_entry22.insert(0,get_pro_data1[8])
                                    except:
                                        pass
                                else:
                                    try:
                                        sr_Canvas_1.itemconfig("label69",state='hidden')
                                        est_entry19.delete(0,END)
                                        est_entry19.insert(0,get_pro_data3[3])
                                        est_entry20.delete(0,END)
                                        est_entry20.insert(0,get_pro_data3[4])
                                        est_entry22.delete(0,END)
                                        est_entry22.insert(0,get_pro_data3[33])
                                    except:
                                        pass

                            est_entry18 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry18['values'] = product_list
                            est_entry18.current(0)
                            est_entry18.bind("<<ComboboxSelected>>",es_fetch_proDetails3)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry18,tags=("combo16"))

                            est_entry19 = Entry(sr_Canvas_1,width=9,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry19,tags=("entry83"))

                            est_entry20 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry20,tags=("entry84"))

                            est_entry21 = Spinbox(sr_Canvas_1,from_=0,to=100,width=7,font=('arial 15'),background='#2f516f',foreground='white',justify=RIGHT)
                            est_entry21.bind("<Key>",lambda event,sp = 3:est_calculateTotal1(event,sp))
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry21,tags=("entry85"))

                            est_entry22 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry22,tags=("entry86"))

                            est_entry23 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            est_entry23.delete(0,END)
                            est_entry23.insert(0,0)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry23,tags=("entry87"))

                            est_entry24 = ttk.Combobox(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry24['values'] = cplace_gstlist
                            est_entry24.current(0)
                            est_entry24.bind('<<ComboboxSelected>>',calcu_cmd)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry24,tags=("combo30"))

                            def es_fetch_proDetails4(event):
                                try:
                                    get_pro_sql = "SELECT * FROM app1_inventory WHERE name=%s AND cid_id=%s"
                                    get_pro_val = (est_entry25.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql,get_pro_val)
                                    get_pro_data = fbcursor.fetchone()
                                except:
                                    pass

                                try:
                                    get_pro_sql1 = "SELECT * FROM app1_noninventory WHERE name=%s AND cid_id=%s"
                                    get_pro_val1 = (est_entry25.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql1,get_pro_val1)
                                    get_pro_data1 = fbcursor.fetchone()
                                except:
                                    pass

                                try:
                                    get_pro_sql3 = "SELECT * FROM app1_bundle WHERE name=%s AND cid_id=%s"
                                    get_pro_val3 = (est_entry25.get(),comp_data[0])
                                    fbcursor.execute(get_pro_sql3,get_pro_val3)
                                    get_pro_data3 = fbcursor.fetchone()
                                except:
                                    pass

                                #--------------------------------------------------------
                                if get_pro_data is not None:
                                    try:
                                        sr_Canvas_1.itemconfig("label70",state='normal')
                                        es_label35.config(text="Available Qty : " + get_pro_data[7])
                                        est_entry26.delete(0,END)
                                        est_entry26.insert(0,get_pro_data[4])
                                        est_entry27.delete(0,END)
                                        est_entry27.insert(0,get_pro_data[11])
                                        est_entry29.delete(0,END)
                                        est_entry29.insert(0,get_pro_data[12])
                                    except:
                                        pass
                                elif get_pro_data1 is not None:
                                    try:
                                        sr_Canvas_1.itemconfig("label70",state='normal')
                                        es_label35.config(text="Available Qty : " + get_pro_data1[17])
                                        est_entry26.delete(0,END)
                                        est_entry26.insert(0,get_pro_data1[4])
                                        est_entry27.delete(0,END)
                                        est_entry27.insert(0,get_pro_data1[7])
                                        est_entry29.delete(0,END)
                                        est_entry29.insert(0,get_pro_data1[8])
                                    except:
                                        pass
                                else:
                                    try:
                                        sr_Canvas_1.itemconfig("label70",state='hidden')
                                        est_entry26.delete(0,END)
                                        est_entry26.insert(0,get_pro_data3[3])
                                        est_entry27.delete(0,END)
                                        est_entry27.insert(0,get_pro_data3[4])
                                        est_entry29.delete(0,END)
                                        est_entry29.insert(0,get_pro_data3[33])
                                    except:
                                        pass

                            est_entry25 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry25['values'] = product_list
                            est_entry25.current(0)
                            est_entry25.bind("<<ComboboxSelected>>",es_fetch_proDetails4)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry25,tags=("combo18"))

                            est_entry26 = Entry(sr_Canvas_1,width=9,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry26,tags=("entry88"))

                            est_entry27 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry27,tags=("entry89"))

                            est_entry28 = Spinbox(sr_Canvas_1,from_=0,to=100,width=7,font=('arial 15'),background='#2f516f',foreground='white',justify=RIGHT)
                            est_entry28.bind("<Key>",lambda event,sp = 4:est_calculateTotal1(event,sp))
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry28,tags=("entry90"))

                            est_entry29 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry29,tags=("entry91"))

                            est_entry30 = Entry(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f',foreground='white')
                            est_entry30.delete(0,END)
                            est_entry30.insert(0,0)
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry30,tags=("entry92"))

                            est_entry31 = ttk.Combobox(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='black')
                            est_entry31['values'] = cplace_gstlist
                            est_entry31.current(0)
                            est_entry31.bind('<<ComboboxSelected>>',calcu_cmd)
                            sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry31,tags=("combo31"))

                            es_label32 = Label(sr_Canvas_1,width=17,height=1,text="",font=('arial 8'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label32,state=HIDDEN,tags=('label67'))

                            es_label33 = Label(sr_Canvas_1,width=17,height=1,text="",font=('arial 8'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label33,state=HIDDEN,tags=('label68'))

                            es_label34 = Label(sr_Canvas_1,width=17,height=1,text="",font=('arial 8'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label34,state=HIDDEN,tags=('label69'))

                            es_label35 = Label(sr_Canvas_1,width=17,height=1,text="",font=('arial 8'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label35,state=HIDDEN,tags=('label70'))

                            es_label25 = Label(sr_Canvas_1,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label25,tags=('label40'))

                            es_label26 = Label(sr_Canvas_1,width=10,height=1,text="CGST",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label26,tags=('label41'))

                            es_label27 = Label(sr_Canvas_1,width=10,height=1,text="SGST",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label27,tags=('label42'))

                            est_entry8 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry8,tags=("entry23"))

                            est_entry9 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry9,tags=("entry24"))

                            est_entry10 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry10,tags=("entry25"))


                            es_label25 = Label(sr_Canvas_1,width=10,height=1,text="TCS",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label25,tags=('label43'))

                            tax_Combo = ttk.Combobox(sr_Canvas_1,width=8,font=('arial 15'))
                            tax_Combo["values"] = "cust_list"
                            tax_Combo.current(0)
                            tax_Combo.bind("<<ComboboxSelected>>","es_fetch_custDetails")
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=tax_Combo,tags=("tcs_sltr"))

                            es_label26 = Label(sr_Canvas_1,width=10,height=1,text="Roundoff",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label26,tags=('label44'))

                            es_label27 = Label(sr_Canvas_1,height=1,text="Estimate Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label27,tags=('label45'))



                            est_entry11 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry11,tags=("est_entry11"))

                            est_entry12 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry12,tags=("est_entry12"))

                            est_entry13 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry13,tags=("est_entry13"))

                            

                            save_btn = Button(sr_Canvas_1,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0,command=lambda:"es_saveEstimate()")
                            sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button7")) 

                            def sr_goBack():
                                sr_Canvas_1.grid_forget()
                                

                            back_btn = Button(sr_Canvas_1,text='???  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
                            sr_Canvas_1.create_window(0,0,window=back_btn,tags=("button3"))
                            #--------------
                            es_label6 = Label(sr_Canvas_1,width=20,height=1,text="Estimate Date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label6,tags=('label24'))

                            es_label28 = Label(sr_Canvas_1,width=20,height=1,text="Expiration Date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_1.create_window(0,0,window=es_label28,tags=('label435'))

                            cwidth = root.winfo_screenwidth()

                            es_estdate = DateEntry(sr_Canvas_1,width=19,date_pattern="yyyy-mm-dd",font=('arial 15'),background='#2f516f',foreground='white')

                            es_expdate = DateEntry(sr_Canvas_1,width=19,date_pattern="yyyy-mm-dd",font=('arial 15'),background='#2f516f',foreground='white') 

                            if cwidth > 1280:
                                sr_Canvas_1.create_window(495,442,anchor='nw',window=es_estdate,tags=("date"))
                                sr_Canvas_1.create_window(775,442,anchor='nw',window=es_expdate,tags=("date1"))
                            elif cwidth <= 1024:
                                sr_Canvas_1.create_window(370,455,anchor='nw',window=es_estdate,tags=("date"))
                                sr_Canvas_1.create_window(580,455,anchor='nw',window=es_expdate,tags=("date1"))
                            else:
                                sr_Canvas_1.create_window(465,407,anchor='nw',window=es_estdate,tags=("date"))
                                sr_Canvas_1.create_window(730,407,anchor='nw',window=es_expdate,tags=("date1"))

                        #--------------------------------------------------------------------Email Function

                        def rp_send_mails():

                            rp_sender_email = "saijuinfox@gmail.com"    
                            rp_sender_password = "eywcinveepcwchnn" 

                            rp_server = smtplib.SMTP('smtp.gmail.com', 587)
                            
                            rp_server.starttls()

                            rp_server.login(rp_sender_email, rp_sender_password)

                            
                            rp_carbcopy_info = rp_carcopyem_address.get()
                            

                            
                            rp_msg = MIMEMultipart()
                            rp_msg['Subject'] = rp_email_subject.get() 
                            
                            rp_mail_content  = rp_mframe.get('1.0','end-1c') 
                            rp_msg['From'] = rp_email_from.get()
                            rp_msg['To'] = rp_email_address.get()
                            
                                
                            rp_gettingimg=rp_lstfrm.get()
                            rp_lst_data = rp_gettingimg[1:-1].split(',')


                            rp_msg.attach(MIMEText(rp_mail_content, 'plain'))

                            for i in rp_lst_data:
                                if len(i.strip()[1:-1])>1:

                                    with open('images/'+ i.strip()[1:-1], "rb") as attachment:
                            
                                        rp_part = MIMEBase("application", "octet-stream")
                                        rp_part.set_payload(attachment.read())

                                        encoders.encode_base64(rp_part)
                                        rp_part.add_header('Content-Disposition', "attachment; filename= %s" % 'images/'+ i.strip()[1:-1]) 

                            
                                        rp_msg.attach(rp_part)
                                

                            rp_server.sendmail(rp_email_from.get(),rp_email_address.get(),rp_msg.as_string())
                            rp_server.sendmail(rp_email_from.get(), rp_carbcopy_info,rp_msg.as_string()) 

                        def rp_empsfile_image(event):
                                global rp_yawn
                                for i in rp_htcodeframe.curselection():
                                    print("hloo",rp_htcodeframe.get(i))
                                    rp_yawn=rp_htcodeframe.get(i)        
                                    edit_window_img = Toplevel()
                                    edit_window_img.title("View Image")
                                    edit_window_img.geometry("700x500")
                                    image = Image.open("images/"+rp_yawn)
                                    resize_image = image.resize((700, 500))
                                    image = ImageTk.PhotoImage(resize_image)
                                    rp_psimage = Label(edit_window_img,image=image)
                                    rp_psimage.photo = image
                                    rp_psimage.pack()


                        def op_file(event):
                            win32api.ShellExecute(0,"",rp_filenamez,None,".",0)
                            

                        def rp_UploadAction(event=None):
                                global rp_filenamez
                                rp_filenamez = askopenfilename(filetypes=(('PDF', '*.pdf',),("png file ",'.png'),("jpg file", ".jpg"),  ("All files", "*.*"),))
                                shutil.copyfile(rp_filenamez, os.getcwd()+'/images/'+rp_filenamez.split('/')[-1])
                                rp_htcodeframe.insert(0, rp_filenamez.split('/')[-1])
                                
                            
                        def rp_addemail_order(event):

                                rp_emailnow = fbcursor.fetchone()
                                rp_mailDetail=Toplevel()
                                rp_mailDetail.title("Send E-mail")
                                rp_mailDetail.geometry("1080x550")
                                rp_mailDetail.resizable(False, False)

                                
                                rp_email_Notebook = ttk.Notebook(rp_mailDetail)
                                rp_email_Frame = Frame(rp_email_Notebook, height=500, width=1080)
                                rp_account_Frame = Frame(rp_email_Notebook, height=550, width=1080)
                                rp_email_Notebook.add(rp_email_Frame, text="E-mail")
                                rp_email_Notebook.add(rp_account_Frame, text="Account")
                                rp_email_Notebook.place(x=0, y=0)

                                rp_messagelbframe=LabelFrame(rp_email_Frame,text="Message", height=500, width=730)
                                rp_messagelbframe.place(x=5, y=5)
                                global rp_email_address, rp_email_subject, rp_email_from,rp_email_pswrd,rp_carcopyem_address,rp_mframe,rp_htcodeframe,rp_lstfrm,rp_langs
                                rp_email_address = StringVar() 
                                rp_email_subject = StringVar()

                                rp_email_from = StringVar()
                                rp_email_pswrd = StringVar()
                                rp_carcopyem_address = StringVar()

                                rp_lbl_emailtoaddr=Label(rp_messagelbframe, text="Email to address").place(x=5, y=5)
                                rp_emailtoent=Entry(rp_messagelbframe, width=50,textvariable=rp_email_address)
                                rp_emailtoent.place(x=120, y=5)
                                
                                rp_sendemail_btn=Button(rp_messagelbframe, text="Send Email", width=10, height=1, command=rp_send_mails).place(x=600, y=10)

                                rp_lbl_carcopyto=Label(rp_messagelbframe, text="Carbon copy to").place(x=5, y=32)
                                rp_carcopyent=Entry(rp_messagelbframe, width=50,textvariable=rp_carcopyem_address)
                                rp_carcopyent.place(x=120, y=32)

                                rp_lbl_subject=Label(rp_messagelbframe, text="Subject").place(x=5, y=59)
                                rp_subent=Entry(rp_messagelbframe, width=50, textvariable=rp_email_subject)
                                rp_subent.place(x=120, y=59)
                                rp_subjectinsrt='ORD_'+str("")
                                rp_subent.delete(0,'end')
                                rp_subent.insert(0, rp_subjectinsrt)

                                

                                
                                style = ttk.Style()
                                style.theme_use('default')
                                style.configure('TNotebook.Tab', background="#213b52",foreground="white", width=60)
                                rp_mess_Notebook = ttk.Notebook(rp_messagelbframe)
                                rp_emailmessage_Frame =Frame(rp_mess_Notebook, height=350, width=710)
                                rp_htmlsourse_Frame = Frame(rp_mess_Notebook, height=350, width=710)
                                rp_mess_Notebook.add(rp_emailmessage_Frame, text="E-mail message")

                                rp_mess_Notebook.add(rp_htmlsourse_Frame, )
                                rp_mess_Notebook.place(x=5, y=90)
                                

                                

                                from tkinter import font,colorchooser
                                fontSize=16
                                fontStyle='Arial'
                                
                                def rp_font_style(event):
                                    global fontStyle
                                    fontStyle=font_family_variable.get()
                                    rp_mframe.config(font=(fontStyle,fontSize))

                                def rp_font_size(event):
                                    global fontSize
                                    
                                    fontSize=size_variable.get()
                                    
                                    
                                    rp_mframe.config(font=(fontStyle,fontSize))

                                def rp_bold_text():
                                    bold_font = font.Font(rp_mframe, rp_mframe.cget("font"))
                                    bold_font.configure(weight="bold")

                                    rp_mframe.tag_configure("bold", font=bold_font)

                                    current_tags = rp_mframe.tag_names("sel.first")

                                    if "bold" in current_tags:
                                        rp_mframe.tag_remove("bold", "sel.first", "sel.last")
                                    else:
                                        rp_mframe.tag_add("bold", "sel.first", "sel.last")    
                                
                                def rp_italic_text():
                                    italic_font = font.Font(rp_mframe, rp_mframe.cget("font"))
                                    italic_font.configure(slant="italic")

                                    rp_mframe.tag_configure("italic", font=italic_font)

                                    current_tags = rp_mframe.tag_names("sel.first")

                                    if "italic" in current_tags:
                                        rp_mframe.tag_remove("italic", "sel.first", "sel.last")
                                    else:
                                        rp_mframe.tag_add("italic", "sel.first", "sel.last")

                                def rp_underline_text():
                                    try:
                                        if rp_mframe.tag_nextrange('underline_selection', 'sel.first', 'sel.last') != ():
                                            rp_mframe.tag_remove('underline_selection', 'sel.first', 'sel.last')
                                        else:
                                            rp_mframe.tag_add('underline_selection', 'sel.first', 'sel.last')
                                            rp_mframe.tag_configure('underline_selection', underline=True)
                                    except TclError:
                                        pass

                                def rp_color_select():
                                    color=colorchooser.askcolor()[1]
                                    if color:
                                    # if color:

                                        color_font = font.Font(rp_mframe, rp_mframe.cget("font"))

                                        rp_mframe.tag_configure("colored", font=color_font, foreground=color)

                                        current_tags = rp_mframe.tag_names("sel.first")

                                    if "colored" in current_tags:
                                        rp_mframe.tag_remove("colored", "sel.first", "sel.last")
                                    else:
                                        rp_mframe.tag_add("colored", "sel.first", "sel.last")

                                def rp_align_right():
                                    data=rp_mframe.get(0.0,END)
                                    rp_mframe.tag_config('right',justify=RIGHT)
                                    rp_mframe.delete(0.0,END)
                                    rp_mframe.insert(INSERT,data,'right')

                                def rp_align_left():
                                    data=rp_mframe.get(0.0,END)
                                    rp_mframe.tag_config('left',justify=LEFT)
                                    rp_mframe.delete(0.0,END)
                                    rp_mframe.insert(INSERT,data,'left')

                                def rp_align_center():
                                    data=rp_mframe.get(0.0,END)
                                    rp_mframe.tag_config('center',justify=CENTER)
                                    rp_mframe.delete(0.0,END)
                                    rp_mframe.insert(INSERT,data,'center')

                                def add_link():
                                    
                                    
                                    hghf=rp_mframe.selection_get()
                                    content=hghf
                                    
                                    rp_mframe.insert(END, " "+content)
                                    
                                    
                                    
                                    
                                def callback(url):
                                    webbrowser.open_new_tab_url(url)

                                def addlinkbox():
                                    global top
                                    top = Toplevel()
                                    top.title('Hyperlink')
                                    top.geometry("400x100")
                                    hyp_lbl = LabelFrame(top,text="Hyperlink Information", height=80, width=300)
                                    hyp_lbl.place(x=10, y=5)

                                    hyp_lbl1 = Label(top,text="Type:")
                                    hyp_lbl1.place(x=18, y=24)
                                    
                                    def comb_select(event):
                                        hyper = cb_comb.get()
                                        if hyper == "(other)":
                                            hyp= Entry(top,width=35)
                                            hyp.place(x=90,y=55)
                                            hyp.insert(END,  "(other)")
                                        elif hyper == "file://":
                                            hyp= Entry(top,width=35)
                                            hyp.place(x=90,y=55)
                                            hyp.insert(END,  "file://")
                                        elif hyper == "ftp://":
                                            hyp= Entry(top,width=35)
                                            hyp.place(x=90,y=55)
                                            hyp.insert(END,  "ftp://") 
                                        elif hyper == "http://":
                                            hyp= Entry(top,width=35)
                                            hyp.place(x=90,y=55)
                                            hyp.insert(END,  "http://") 
                                        elif hyper == "https://":
                                            hyp= Entry(top,width=35)
                                            hyp.place(x=90,y=55)
                                            hyp.insert(END,  "https://") 
                                        elif hyper == "mailto:":
                                            hyp= Entry(top,width=35)
                                            hyp.place(x=90,y=55)
                                            hyp.insert(END,  "mailto:") 
                                        elif hyper == "telnet:":
                                            hyp= Entry(top,width=35)
                                            hyp.place(x=90,y=55)
                                            hyp.insert(END,  "telnet:")


                                    cb_comb = StringVar()
                                    cb1=ttk.Combobox(top,textvariable=cb_comb,width=15)
                                    cb1.grid(row=1,column=1,padx=90,pady=30)
                                    cb1['values']=('(other)','file://','ftp://','http://','https://','mailto:','news:','telnet:')
                                    cb1.current(0)
                                    cb1.bind('<<ComboboxSelected>>',comb_select)


                                    hyp_lbl2 = Label(top,text="URL:")
                                    hyp_lbl2.place(x=18, y=55)
                                    global rp_hyper
                                    rp_hyper = StringVar()
                                    
                                    hyp= Entry(top,textvariable=rp_hyper,width=35)
                                    hyp.place(x=90,y=55)

                                    

                                    hypbtn1 = Button(top,text="OK",width=10, command=add_link)
                                    hypbtn1.place(x=315,y=8)

                                    hypbtn2 = Button(top,text="Cancel",width=10)
                                    hypbtn2.place(x=315,y=35)

                                

                                rp_mframe=Text(rp_emailmessage_Frame,undo=True,width=84, bg="white", height=20)
                                rp_mframe.place(x=10,y=30)


                                rp_scrollbar1 = Scrollbar(rp_emailmessage_Frame,orient=VERTICAL,command=rp_mframe.yview)
                                rp_scrollbar2= Scrollbar(rp_mframe,orient=HORIZONTAL,command=rp_mframe.xview, width=0)
                                rp_scrollbar2.pack(fill=X,expand=True,side=BOTTOM,padx=310,pady=163)
                                #   rp_scrollbar2.place(x=0, y=310, height=20,width=670)
                                rp_mframe.config(xscrollcommand=rp_scrollbar2.set)
                                rp_mframe.config(yscrollcommand=rp_scrollbar1.set)
                                rp_scrollbar1.config(command=rp_mframe.yview)
                                rp_scrollbar1.place(x =690, y=0, height=360)
                                rp_scrollbar2.config(command=rp_mframe.xview)
                                

                                rp_btn1=Button(rp_emailmessage_Frame,width=20,height=20,compound = LEFT,image=selectall,command=lambda :rp_mframe.event_generate('<Control a>'))
                                rp_btn1.place(x=0, y=1)

                                        
                                rp_btn2=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut,command=lambda :rp_mframe.event_generate('<Control x>'))
                                rp_btn2.place(x=36, y=1)

                                rp_btn3=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy,command=lambda :rp_mframe.event_generate('<Control c>'))
                                rp_btn3.place(x=73, y=1)

                                rp_btn4=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste,command=lambda :rp_mframe.event_generate('<Control v>'))
                                rp_btn4.place(x=105, y=1)
                                rp_btn5=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo, command=lambda:rp_mframe.event_generate("<<Undo>>")).place(x=140, y=1)

                                rp_btn6=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo, command=lambda:rp_mframe.event_generate("<<Redo>>")).place(x=175, y=1)

                                rp_btn7=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold,command=rp_bold_text)
                                rp_btn7.place(x=210, y=1)

                                rp_btn8=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics,command=rp_italic_text)
                                rp_btn8.place(x=245, y=1)

                                rp_btn9=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline,command=rp_underline_text)
                                rp_btn9.place(x=280, y=1)

                                rp_btn10=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=left,command=rp_align_left)
                                rp_btn10.place(x=315, y=1)

                                rp_btn11=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=right,command=rp_align_right)
                                rp_btn11.place(x=350, y=1)

                                rp_btn12=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=center,command=rp_align_center)
                                rp_btn12.place(x=385, y=1)

                                rp_btn14=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove,command=lambda :rp_mframe.delete(0.0,END))
                                rp_btn14.place(x=455, y=1)
                                
                                rp_btn15=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=color,command=rp_color_select)
                                rp_btn15.place(x=420, y=1)
                                rp_btn16=Button(rp_emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink, command=addlinkbox)
                                rp_btn16.place(x=491, y=1)
                                global size_variable
                                size_variable=IntVar()

                                rp_dropcomp11 = ttk.Combobox(rp_emailmessage_Frame, width=6, textvariable=size_variable, values=tuple(range(8,17)))
                                
                                rp_dropcomp11.place(x=530, y=5)
                                
                                
                                font_family_variable=StringVar()
                                font_familyes=font.families()
                      
                                rp_dropcomp11.bind('<<ComboboxSelected>>', rp_font_size)
                                
                                rp_attachlbframe=LabelFrame(rp_email_Frame,text="Attachment(s)", height=350, width=280)
                                rp_attachlbframe.place(x=740, y=5)

                                rp_lstfrm=StringVar()  
                                rp_htcodeframe=Listbox(rp_attachlbframe, height=13, width=43,listvariable=rp_lstfrm, bg="white")
                                rp_htcodeframe.place(x=5, y=5)
                                rp_htcodeframe.bind('<Double-Button-1>' , op_file)

                                def rp_deslist():
                                    rp_laa=rp_htcodeframe.curselection()
                                    print("hloo",rp_htcodeframe.get(rp_laa))
                                    rp_yawn=rp_htcodeframe.get(rp_laa)        
                                    rp_htcodeframe.delete(ACTIVE)

                                rp_lbl_btn_info=Label(rp_attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
                                rp_btn17=Button(rp_attachlbframe, width=20, text="Add attachment file...", command=rp_UploadAction).place(x=60, y=260)
                                rp_btn18=Button(rp_attachlbframe, width=20, text="Remove attachment",command=rp_deslist).place(x=60, y=295)
                                rp_lbl_tt_info=Label(rp_email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
                                rp_lbl_tt_info.place(x=740, y=370)

                                rp_ready_frame=Frame(rp_mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
                                
                                rp_sendatalbframe=LabelFrame(rp_account_Frame,text="E-Mail(Sender data)",height=140, width=600)
                                rp_sendatalbframe.place(x=240, y=165 )
                                rp_lbl_sendermail=Label(rp_sendatalbframe, text="Company email address").place(x=5, y=10)
                                rp_sentent=Entry(rp_sendatalbframe, width=40, textvariable=rp_email_from)
                                rp_sentent.place(x=195, y=10)

                                rp_lbl_senderpswrd=Label(rp_sendatalbframe, text="Email Password").place(x=5, y=40)
                                rp_pswrdent=Entry(rp_sendatalbframe, width=40, textvariable=rp_email_pswrd,show="*")
                                rp_pswrdent.place(x=195, y=40)
                            
                        def edit_print():
                            from reportlab.pdfgen import canvas
                            from reportlab.lib.pagesizes import letter, inch
                            
                            path = filedialog.asksaveasfilename(initialdir=os.getcwd,title="Save File",filetypes=[('Pdf File', '*.pdf',)],defaultextension=".pdf")

                            

                            

                            from reportlab.pdfgen import canvas 
                            from reportlab.lib.colors import Color, black, green, grey
                            pdf = canvas.Canvas(path, pagesize=letter)
 
                            pdf.setFont('Helvetica-Bold',18)
                            pdf.drawString(50,730, "Sales")
                            pdf.drawString(460,730, "ESTIMATE")
                            
                            pdf.line(30,700,580,700)

                            
                            pdf.setFont('Helvetica-Bold',12)
                            pdf.drawString(460,710, "Estimate No:1080")
                            pdf.drawString(60,680, "From:")
                            pdf.drawString(330,680, "To:")
                            text="asdasdddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
                            wraped_text="\n".join(wrap(text,30))
                            htg=wraped_text.split('\n') 
                            vg=len(htg)
                            if vg>0:
                                pdf.drawString(60,660,htg[0])
                                if vg>1:
                                    pdf.drawString(60,640,htg[1])
                                    if vg>2:
                                        pdf.drawString(60,620,htg[2])
                                        if vg>3:
                                            pdf.drawString(60,600,htg[3])
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass    

                            text="asdasdddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
                            wraped_text="\n".join(wrap(text,30))
                            htg=wraped_text.split('\n') 
                            vg=len(htg)
                            if vg>0:
                                pdf.drawString(330,660,htg[0])
                                if vg>1:
                                    pdf.drawString(330,640,htg[1])
                                    if vg>2:
                                        pdf.drawString(330,620,htg[2])
                                        if vg>3:
                                            pdf.drawString(330,600,htg[3])
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass   

                            pdf.line(30,590,580,590)
                            pdf.drawString(50,575, "Estimate Date: 2022-01-05")
                            pdf.drawString(430,575, "Expiration: 2022-01-05 ")

                            

                            
                            pdf.setLineWidth(.3)
                      
                            pdf.line(30,560,580,560)
                            pdf.line(30,535,580,535)
                            pdf.drawString(80,545, "Item Description")
                            pdf.drawString(280,545, "Price")
                            pdf.drawString(380,545, "Quantity")
                            pdf.drawString(480,545, "Total")

                            

                            pdf.drawString(80,520, "Item Description")
                            pdf.drawString(280,520, "Price")
                            pdf.drawString(380,520, "Quantity")
                            pdf.drawString(480,520, "Total")

                            y=500

                            pdf.drawString(80,y, "Item Description")
                            pdf.drawString(280,y, "Price")
                            pdf.drawString(380,y, "Quantity")
                            pdf.drawString(480,y, "Total")

                            pdf.drawString(50,y-30, "Note:")

                            text="asdasdddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
                            wraped_text="\n".join(wrap(text,30))
                            htg=wraped_text.split('\n') 
                            vg=len(htg)
                            if vg>0:
                                pdf.drawString(50,y-50,htg[0])
                                if vg>1:
                                    pdf.drawString(50,y-70,htg[1])
                                    if vg>2:
                                        pdf.drawString(50,y-90,htg[2])
                                        if vg>3:
                                            pdf.drawString(50,y-110,htg[3])
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass 

                            pdf.drawString(380,y-30, "Subtotal:")
                            pdf.drawString(380,y-50, "CGST:")
                            pdf.drawString(380,y-70, "SGST:")

                            pdf.drawString(380,y-90, "Estimate Total:")

                            pdf.drawString(480,y-30, "10000")
                            pdf.drawString(480,y-50, "10000")
                            pdf.drawString(480,y-70, "10000")
                            pdf.line(380,y-78,580,y-78)

                            pdf.drawString(480,y-90, "10000")


                            pdf.save()
                            
                            win32api.ShellExecute(0,"",path,None,".",0) 

                        def resestms(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                            

                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("poly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("hline",dwidth/21,dheight/5,dwidth/1.055,dheight/5)
                            
                            r2 = 0
                            x11 = dwidth/8
                            x21 = dwidth/1.15
                            y11 = dheight/2.8
                            y21 = dheight/0.41


                            dcanvas.coords("poly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("label1",dwidth/2,dheight/8.24)
                            dcanvas.coords("button3",dwidth/28,dheight/3)
                            dcanvas.coords("act_btn1",dwidth/1.7,dheight/4)
                            dcanvas.coords("act_btn2",dwidth/1.5,dheight/4)
                            dcanvas.coords("act_btn3",dwidth/1.34,dheight/4)
                            dcanvas.coords("act_btn4",dwidth/1.21,dheight/4)
                            dcanvas.coords("act_btn5",dwidth/1.09,dheight/4)

                            #view page:
                            dcanvas.coords("labels1",dwidth/5,dheight/2.3)
                            dcanvas.coords("hline2",dwidth/6.8,dheight/1.8,dwidth/1.18,dheight/1.8)
                            dcanvas.coords("labels2",dwidth/1.26,dheight/2.3)
                            dcanvas.coords("labels3",dwidth/1.18,dheight/2)
                            dcanvas.coords("labels4",dwidth/4,dheight/1.6)
                            dcanvas.coords("labels4_1",dwidth/4.5,dheight/1.5)
                            dcanvas.coords("labels4_2",dwidth/4.5,dheight/1.4)
                            dcanvas.coords("labels5",dwidth/1.8,dheight/1.6)
                            dcanvas.coords("labels5_1",dwidth/1.85,dheight/1.5)
                            dcanvas.coords("labels5_2",dwidth/1.85,dheight/1.4)
                            dcanvas.coords("hline3",dwidth/6.8,dheight/1.1,dwidth/1.18,dheight/1.1)
                            dcanvas.coords("labels6",dwidth/6.8,dheight/1.08)
                            dcanvas.coords("labels7",dwidth/1.45,dheight/1.08)
                            dcanvas.coords("pre_tree",dwidth/6.8,dheight/1)
                            dcanvas.coords("labels8",dwidth/6.8,dheight/0.53)
                            dcanvas.coords("labels9",dwidth/6.8,dheight/0.51)
                            dcanvas.coords("labels10",dwidth/1.6,dheight/0.53)
                            dcanvas.coords("labels11",dwidth/1.3,dheight/0.53)
                            dcanvas.coords("labels12",dwidth/1.6,dheight/0.52)
                            dcanvas.coords("labels13",dwidth/1.3,dheight/0.52)

                            dcanvas.coords("labels14",dwidth/1.6,dheight/0.51)
                            dcanvas.coords("labels15",dwidth/1.3,dheight/0.51)
                            dcanvas.coords("labels16",dwidth/1.6,dheight/0.496) 
                            dcanvas.coords("labels17",dwidth/1.3,dheight/0.496)
                            dcanvas.coords("hline4",dwidth/1.63,dheight/0.498,dwidth/1.22,dheight/0.498)


                            

                            
                        estm_Frame.grid_rowconfigure(0,weight=1)
                        estm_Frame.grid_columnconfigure(0,weight=1)

                        estm_Scroll_1 = Scrollbar(estm_Frame,orient=VERTICAL)
                        estm_Scroll_1.grid(row=0,column=1,sticky='ns')
                        estm_Scroll_1.config(command=estm_Canvas_1.yview)
                        estm_Canvas_1.bind("<Configure>", resestms)
                        estm_Canvas_1.config(yscrollcommand=estm_Scroll_1.set)
                        estm_Canvas_1.grid(row=0,column=0,sticky='nsew')
                        def sr_goBack():
                            estm_Canvas_1.grid_forget()
                            

                        back_btn = Button(estm_Canvas_1,text='???  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
                        estm_Canvas_1.create_window(0,0,window=back_btn,tags=("button3"))


                        estm_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))

                        estm_label = Label(estm_Canvas_1,width=15,height=1,text="ESTIMATE",font=('arial 25'),background="#1b3857",fg="white")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="c",window=estm_label,tags=("label1"))
                        estm_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

                        act_btn1 = Button(estm_Canvas_1,text='Edit',width=10,height=1,background="#198fed",activebackground="#1476c5",foreground="white",activeforeground="white",bd=0,command=edit_estim_fn)
                        estm_Canvas_1.create_window(0,0,window=act_btn1,tags=("act_btn1")) 

                        act_btn2 = Button(estm_Canvas_1,text='Delete',width=10,height=1,background="#198fed",activebackground="#1476c5",foreground="white",activeforeground="white",bd=0,command=edit_print)
                        estm_Canvas_1.create_window(0,0,window=act_btn2,tags=("act_btn2")) 

                        act_btn3 = Button(estm_Canvas_1,text='PDF/Print',width=10,height=1,background="#198fed",activebackground="#1476c5",foreground="white",activeforeground="white",bd=0,command=edit_print)
                        estm_Canvas_1.create_window(0,0,window=act_btn3,tags=("act_btn3")) 

                        act_btn4 = ttk.Combobox(estm_Canvas_1,width=7,font=('arial 15'))
                        act_btn4['values'] = ['Share','Edit','Delete']
                        act_btn4.current(0)
                        act_btn4.bind("<<ComboboxSelected>>",rp_addemail_order)
                        estm_Canvas_1.create_window(0,0,window=act_btn4,tags=("act_btn4"))


                        act_btn5 = ttk.Combobox(estm_Canvas_1,width=7,font=('arial 15'))
                        act_btn5['values'] = ['Convert','Edit','Delete']
                        act_btn5.current(0)
                        act_btn5.bind("<<ComboboxSelected>>","estm_Actions")
                        estm_Canvas_1.create_window(0,0,window=act_btn5,tags=("act_btn5"))

                        estm_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="white",tags=("poly2"))

                        #view section 
                        labels1 = Label(estm_Canvas_1,width=15,height=1,text="Sales",font=('arial 12'),background="#198fed",fg="white")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="c",window=labels1,tags=("labels1"))

                        estm_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline2"))

                        labels2 = Label(estm_Canvas_1,width=15,height=1,text="ESTIMATE",font=('arial 12'),background="#198fed",fg="white")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="c",window=labels2,tags=("labels2"))

                        labels3 = Label(estm_Canvas_1,height=1,text="Estimate No. :1080",font=('arial 12'),background="white",fg="black", anchor="ne")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="ne",window=labels3,tags=("labels3"))

                        labels4 = Label(estm_Canvas_1,height=1,text="From:",font=('arial 12'),background="white",fg="black", anchor="ne")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="ne",window=labels4,tags=("labels4"))

                        labels4_1 = Label(estm_Canvas_1,width=30,height=1,text="Infox Technologies",font=('arial 12'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels4_1,tags=("labels4_1"))

                        labels4_2 = Label(estm_Canvas_1,width=30,height=5,text="Infox Technologies\n Carinival Infopark\n first floor' Kakkanad,\n ernakulam\n Kerala,682020",font=('arial 12'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels4_2,tags=("labels4_2"))


                        labels5 = Label(estm_Canvas_1,height=1,text="To:",font=('arial 12'),background="white",fg="black", anchor="ne")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="ne",window=labels5,tags=("labels5"))

                        labels5_1 = Label(estm_Canvas_1,width=30,height=1,text="Infox Technologies",font=('arial 12'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels5_1,tags=("labels5_1"))

                        labels5_2 = Label(estm_Canvas_1,width=30,height=5,text="Infox Technologies\n Carinival Infopark\n first floor' Kakkanad,\n ernakulam\n Kerala,682020",font=('arial 12'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels5_2,tags=("labels5_2"))

                        estm_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline3"))
                        labels6 = Label(estm_Canvas_1,height=1,text="Estimate Date: 2022-03-04",font=('arial 12'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels6,tags=("labels6"))

                        labels7 = Label(estm_Canvas_1,height=1,text="Expiration Date: 2022-03-04",font=('arial 12'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels7,tags=("labels7"))

                        estm_tree_style = ttk.Style()
                        estm_tree_style.theme_use("default")
                        estm_tree_style.configure("Treeview",background="white",foreground="black",rowheight=25,font=(None,11),fieldbackground="white")
                        estm_tree_style.configure("Treeview.Heading",background="white",activeforeground="black",foreground="black",font=(None,11))
                        inv_scrollbar_1 = Scrollbar(estm_Frame,orient="vertical")
                        
                        pre_tree = ttk.Treeview(estm_Canvas_1,height=20,columns=("0","1","2","3"),show="headings",yscrollcommand=inv_scrollbar_1.set)
                        pre_tree.column("0",width=330,anchor=CENTER)
                        pre_tree.column("1",width=200,anchor=CENTER)
                        pre_tree.column("2",width=200,anchor=CENTER)
                        pre_tree.column("3",width=200,anchor=CENTER)
                        
                
                        pre_tree.heading("0",text="Item Description")
                        pre_tree.heading("1",text="Price")
                        pre_tree.heading("2",text="Quantity")
                        pre_tree.heading("3",text="Total")
                        
                        estm_Canvas_1.create_window(0,0,window=pre_tree,anchor="nw",tags=("pre_tree"))
                        inv_scrollbar_1.grid(row=0,column=2, sticky='ns')

                        labels8 = Label(estm_Canvas_1,height=1,text="Note:",font=('arial 12'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels8,tags=("labels8"))

                        labels9 = Label(estm_Canvas_1,height=10,width=50,text="dsfffffffffffffffffffffffffffffffffffffffffffffffffffffdsfdsfdsfdfdsfsd",font=('arial 12'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels9,tags=("labels9"))

                        labels10 = Label(estm_Canvas_1,height=1,text="Sub Total:",font=('arial 12 bold'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels10,tags=("labels10"))

                        labels11 = Label(estm_Canvas_1,height=1,text="10000",font=('arial 12 bold'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels11,tags=("labels11"))

                        labels12 = Label(estm_Canvas_1,height=1,text="cgst:",font=('arial 12 bold'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels12,tags=("labels12"))

                        labels13 = Label(estm_Canvas_1,height=1,text="10000",font=('arial 12 bold'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels13,tags=("labels13"))

                        labels14 = Label(estm_Canvas_1,height=1,text="SGST:",font=('arial 12 bold'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels14,tags=("labels14"))

                        labels15 = Label(estm_Canvas_1,height=1,text="10000",font=('arial 12 bold'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels15,tags=("labels15"))

                        labels16 = Label(estm_Canvas_1,height=1,text="Estimate Total:",font=('arial 12 bold'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels16,tags=("labels16"))

                        labels17 = Label(estm_Canvas_1,height=1,text="10000",font=('arial 12 bold'),background="white",fg="black",anchor="nw")
                        estm_label_win = estm_Canvas_1.create_window(0,0,anchor="nw",window=labels17,tags=("labels17"))

                        estm_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline4"))




                    
                    estm_Canvas = Canvas(estm_Frame,bg='#2f516f',scrollregion=(0,0,700,1200))

                    estm_Frame.grid_rowconfigure(0,weight=1)
                    estm_Frame.grid_columnconfigure(0,weight=1)

                    estm_Scroll = Scrollbar(estm_Frame,orient=VERTICAL)
                    estm_Scroll.grid(row=0,column=1,sticky='ns')
                    estm_Scroll.config(command=estm_Canvas.yview)
                    estm_Canvas.bind("<Configure>", responsive_widgets_estm)
                    estm_Canvas.config(yscrollcommand=estm_Scroll.set)
                    estm_Canvas.grid(row=0,column=0,sticky='nsew')


                    estm_Canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))

                    estm_label = Label(estm_Canvas,width=15,height=1,text="ESTIMATE",font=('arial 25'),background="#1b3857",fg="white")
                    estm_label_win = estm_Canvas.create_window(0,0,anchor="c",window=estm_label,tags=("label1"))
                    estm_Canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

                    estm_Canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

                    srh_top = Entry(estm_Canvas, width=20, font=('Calibri 16'))
                    srh_top.insert(0,"Search")
                    srh_top.bind("<Button-1>",srh_fn)
                    estm_Canvas.create_window(0,0,window=srh_top,tags=("srh_top"))
                    

                    srh_btn6 = Button(estm_Canvas, image=srh_img, command="search_dash", bg="#213b52", fg="black",border=0)
                    estm_Canvas.create_window(0,0,window=srh_btn6,tags=("srh_btn6"))

                    estmt_srhCombo = ttk.Combobox(estm_Canvas,width=12,font=('arial 15'))
                    estmt_srhCombo['values'] = ['Actions','Edit','Delete']
                    estmt_srhCombo.current(0)
                    estmt_srhCombo.bind("<<ComboboxSelected>>","estm_Actions")
                    estm_Canvas.create_window(0,0,window=estmt_srhCombo,tags=("estmt_srhCombo"))

                    

                    estmt_actionCombo = ttk.Combobox(estm_Canvas,width=7,font=('arial 15'))
                    estmt_actionCombo['values'] = ['Actions','Edit','Delete']
                    estmt_actionCombo.current(0)
                    estmt_actionCombo.bind("<<ComboboxSelected>>","estm_Actions")
                    estm_Canvas.create_window(0,0,window=estmt_actionCombo,tags=("combo1"))

                    button_cmp = customtkinter.CTkButton(master=estm_Canvas,command=create_stm,text="New Estimate",bg="#213b52")
                    win_inv1 = estm_Canvas.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_estm"))



                    estm_tree_style = ttk.Style()
                    estm_tree_style.theme_use("default")
                    estm_tree_style.configure("Treeview",background="#2f516f",foreground="white",rowheight=25,font=(None,11),fieldbackground="#2f516f")
                    estm_tree_style.configure("Treeview.Heading",background="#1b3857",activeforeground="black",foreground="white",font=(None,11))
                    inv_scrollbar = Scrollbar(estm_Frame,orient="vertical")
                    
                    estm_tree = ttk.Treeview(estm_Canvas,height=30,columns=("0","1","2","3","4","5",),show="headings",yscrollcommand=inv_scrollbar.set)
                    estm_tree.column("0",width=150,anchor=CENTER)
                    estm_tree.column("1",width=200,anchor=CENTER)
                    estm_tree.column("2",width=200,anchor=CENTER)
                    estm_tree.column("3",width=300,anchor=CENTER)
                    estm_tree.column("4",width=200,anchor=CENTER)
                    estm_tree.column("5",width=200,anchor=CENTER)
               
                    estm_tree.heading("0",text="DATE")
                    estm_tree.heading("1",text="ESTIMATE NUMBER")
                    estm_tree.heading("2",text="REFERENCE No.")
                    estm_tree.heading("3",text="CUSTOMER NAME")
                    estm_tree.heading("4",text="STATUS")
                    estm_tree.heading("5",text="AMOUNT")

                    get_est_sql = "SELECT * FROM app1_estimate WHERE cid_id=%s"
                    get_est_val = (comp_data[0],)
                    fbcursor.execute(get_est_sql,get_est_val)
                    get_est_data = fbcursor.fetchall()
                    count=0
                    for e in get_est_data:
                            estm_tree.insert(parent='',index='end',values=(e[4],e[6],e[40],e[1],e[41],e[13]))
                    count+=1
                    estm_tree.bind('<Double-1>',row_selection)
                    estm_Canvas.create_window(0,0,window=estm_tree,anchor="nw",tags=("tree_main"))

                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Expenses Tab}
                    tab_exp = ttk.Notebook(tab4)
                    tab4_1 =  ttk.Frame(tab_exp)
                    tab4_2=  ttk.Frame(tab_exp)
                    tab_exp.add(tab4_1,compound = LEFT, text ='Expenses')
                    tab_exp.add(tab4_2,compound = LEFT, text ='Supliers')
                    tab_exp.pack(expand = 1, fill ="both")
                    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333{Pay Roll Tab}
                    tab_payroll = ttk.Notebook(tab5)
                    tab5_1 =  ttk.Frame(tab_payroll)
                    tab5_2=  ttk.Frame(tab_payroll)
                    
                    tab_payroll.add(tab5_1,compound = LEFT, text ='Employee')
                    tab_payroll.add(tab5_2,compound = LEFT, text ='Payslip')

                    tab_payroll.pack(expand = 1, fill ="both")

                    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Report Tab}

                    tab_report = ttk.Notebook(tab6)
                    tab6_1 =  ttk.Frame(tab_report)
                    tab6_2=  ttk.Frame(tab_report)
                    tab6_3 = ttk.Frame(tab_report)
                    tab6_4=  ttk.Frame(tab_report)

                    
                        
                    tab_report.add(tab6_1,compound = LEFT, text ='Profit & Loss')
                    tab_report.add(tab6_2,compound = LEFT, text ='Balance Sheet')
                    tab_report.add(tab6_3,compound = LEFT, text ='Accounts Receivables')
                    tab_report.add(tab6_4,compound = LEFT, text ='Accounts Payables')
                
                    tab_report.pack(expand = 1, fill ="both")

                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Taxes}

                    tab_tax = ttk.Notebook(tab7)
                    tab7_1 =  ttk.Frame(tab_tax)
                    tab7_2=  ttk.Frame(tab_tax)

                    tab_tax.add(tab7_1,compound = LEFT, text ='GST')
                    tab_tax.add(tab7_2,compound = LEFT, text ='New')

                    tab_tax.pack(expand = 1, fill ="both")

                    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Accounting}
                    tab_account = ttk.Notebook(tab8)
                    tab8_1 =  ttk.Frame(tab_account)
                    tab8_2=  ttk.Frame(tab_account)

                    tab_account.add(tab8_1,compound = LEFT, text ='Chart Of Accounts')
                    tab_account.add(tab8_2,compound = LEFT, text ='Reconcile')
                
                
                    tab_account.pack(expand = 1, fill ="both")
                    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Cash Management}
                    tab_cash = ttk.Notebook(tab10)
                    
                    tab10_1 =  ttk.Frame(tab_cash)
                    tab10_2=  ttk.Frame(tab_cash)
                    tab10_3 = ttk.Frame(tab_cash)

                    tab_cash.add(tab10_1,compound = LEFT, text ='Cash Position')
                    tab_cash.add(tab10_2,compound = LEFT, text ='Cash Flow Analyzer')
                    tab_cash.add(tab10_3,compound = LEFT, text ='Check Cash Flow')

                    tab_cash.pack(expand = 1, fill ="both")
                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                    # 
                    # {My Account}
                    
                    def search_dash():
                        if srh_top.get()=="Dashboard":
                            pass
                        else:
                            pass
                    srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
                    srh_top.insert(0,"Search")
                    srh_top.bind("<Button-1>",srh_fn)
                    srh_top.grid(row=2,column=1,padx=(30,0), pady=20,sticky='nsew')

                    srh_btn6 = Button(tp_lb_srh, image=srh_img, command=search_dash, bg="#213b52", fg="black",border=0)
                    srh_btn6.grid(row=2,column=4,padx=(0,30))
                    Sys_mains_frame=Frame(tab9, height=750,bg="#2f516f")
                    Sys_mains_frame.pack(fill=X)
                    
                else:
                    messagebox.showerror("Login Failed","Invalid username or password")
                    pass
    
#---------------------------------------------------------------------------------------------------------------Company Second Portion
def cmpny_crt2():
    

    cmp_name=cmp_nm.get()
    cmp_address=cmp_cmpn.get()
    cmp_ctys=cmp_cty.get()
    state=cmp_stat.get()
    cmp_pins=cmp_pin.get()
    cmp_emails=cmp_email.get()
    cmp_phs=cmp_ph.get()
    cmp_filess=cmp_files.get()
    if cmp_name is not None:
        sql_log_sql='select id from auth_user where username=%s'
        sql_log_sql_val=(sys_usr.get(),)
        
        fbcursor.execute(sql_log_sql,sql_log_sql_val,)
        id=fbcursor.fetchone()
        
        signup_cmp_sql="insert into app1_company(cname,caddress,city,state,pincode,cemail,phone,cimg,id_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
        signup_cmp_sql_val=(cmp_name,cmp_address,cmp_ctys,state,cmp_pins,cmp_emails,cmp_phs,cmp_filess,id[0])
        fbcursor.execute(signup_cmp_sql,signup_cmp_sql_val,)
        finsysdb.commit()
    else:
        messagebox.showerror("Company Creation Failed","Enter your company details")

    main_frame_cmpny.pack_forget()
    global main_frame_cmpny2,nm_nm2,industry_tp,cmp_type,bs_act_man,paid_typ
    main_frame_cmpny2=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny2.pack(fill=X,)

    cmpny_dt_frm2=Frame(main_frame_cmpny2, height=650, width=500,bg="white")
    cmpny_dt_frm2.pack(pady=105)

    def responsive_wid_cmp2(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("cmpny_hd1",dwidth/40,dheight/15)
        dcanvas.coords("nm_nm2",dwidth/6,dheight/5)
        dcanvas.coords("cmpny_cntry",dwidth/6,dheight/3.2)
        dcanvas.coords("cmpny_cntry2",dwidth/6,dheight/2.35)
        dcanvas.coords("r1",dwidth/2.2,dheight/1.8)
        dcanvas.coords("r2",dwidth/2.2,dheight/1.6)
        dcanvas.coords("cmpny_cntry3",dwidth/6,dheight/1.38)
        # dcanvas.coords("button_cmp2",dwidth/4.3,dheight/1.2)
        # dcanvas.coords("button_cmp3",dwidth/1.9,dheight/1.2)
        dcanvas.coords("button_cmp3",dwidth/2.8,dheight/1.1)
        

        dcanvas.coords("cmp_lbl1",dwidth/6,dheight/3.8)
        dcanvas.coords("cmp_lbl2",dwidth/6,dheight/2.7)
        dcanvas.coords("cmp_lbl3",dwidth/6,dheight/2)
        dcanvas.coords("cmp_lbl4",dwidth/6,dheight/1.46)
        

    lf_cmpy2= Canvas(cmpny_dt_frm2,height=650, width=500)
    lf_cmpy2.bind("<Configure>", responsive_wid_cmp2)
    lf_cmpy2.pack(fill=X)

    def name_ent2(event):
        if nm_nm2.get()=="Legal Business Name":
            nm_nm2.delete(0,END)
        else:
            pass


    cmpny_hd1=Label(lf_cmpy2, text="Let's Start Building Your FinsYs",font=('Calibri 28 bold'), fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_hd1, tag=("cmpny_hd1"))

    

    nm_nm2 = Entry(cmpny_dt_frm2, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm2.insert(0,"Legal Business Name")
    nm_nm2.bind("<Button-1>",name_ent2)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=nm_nm2, tag=("nm_nm2"))

    cmp_lbl1=Label(cmpny_dt_frm2, text="Your Industry",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl1, tag=("cmp_lbl1"))

    industry_tp= StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm2,textvariable=industry_tp,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Accounting Services','Consultants, doctors, Lawyers and similar','Information Tecnology','Manufacturing','Professional, Scientific and Technical Services','Restaurant/Bar and similar','Retail and Smilar','Other Finanacial Services')
   
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry, tag=("cmpny_cntry"))

    cmp_lbl2=Label(cmpny_dt_frm2, text="Company type",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl2, tag=("cmp_lbl2"))

    cmp_type = StringVar()
    cmpny_cntry2 = ttk.Combobox(cmpny_dt_frm2,textvariable=cmp_type,width=29,font=('Calibri 16'))
    
    cmpny_cntry2['values'] = ('Private Limited Company','Public Limited Company','Joint-Venture Company','Partnership Firm Company','One Person Company','Branch Office Company','Non Government Organization')
    
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry2, tag=("cmpny_cntry2"))
    
    cmp_lbl3=Label(cmpny_dt_frm2, text="Do you have an Accountant, Bookkeeper or Tax Pro ?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl3, tag=("cmp_lbl3"))

    bs_act_man=StringVar()
    r1=Radiobutton(cmpny_dt_frm2, text = "Yes", variable = bs_act_man, value ="Yes",font=('Calibri 16'))
    r1.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r1, tag=("r1"))

    r2=Radiobutton(cmpny_dt_frm2, text = "No", variable = bs_act_man, value ="No",font=('Calibri 16'))
    r2.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r2, tag=("r2"))


    cmp_lbl4=Label(cmpny_dt_frm2, text="How do you like to get paid?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl4, tag=("cmp_lbl4"))
    
    paid_typ = StringVar()
    cmpny_cntry3 = ttk.Combobox(cmpny_dt_frm2,textvariable=paid_typ,width=29,font=('Calibri 16'))
    cmpny_cntry3['values'] = ('Cash','Cheque','Credit card/Debit card','Bank Transfer','Paypal/Other service')
   
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry3, tag=("cmpny_cntry3"))
    def prev_funct():
        main_frame_cmpny.pack(fill=X,)

    # button_cmp2 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=prev_funct,text="Previous",bg="#213b52")
    # win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp2, tag=("button_cmp2"))
    button_cmp3 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=fun_sign_in,text="Submit",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp3, tag=("button_cmp3"))
#-------------------------------------------------------------------------------------------------------------------company creation

def cmpny_crt1():
    
    first_name=fst_nm.get()
    last_name=lst_nm.get()
    email=sys_em.get()
    username=sys_usr.get()
    password=sys_pass.get()
    con_password=sys_cf.get()
    join_dt=datetime.today()
    sql_signup='select * from auth_user'
    fbcursor.execute(sql_signup)
    check_none=fbcursor.fetchone()
    global main_frame_cmpny,cmp_nm,cmp_cmpn,cmp_cty,cmp_pin,cmp_email,cmp_ph,cmp_files,cmp_stat
    if check_none is not None:
        if check_none[4]!=username and check_none[1]!=password:
            
            if password==con_password and con_password==password :
                
                signup_sql="insert into auth_user(first_name,last_name,email,username,password,date_joined) VALUES(%s,%s,%s,%s,%s,%s)" #adding values into db
                signup_sql_val=(first_name,last_name,email,username,password,join_dt,)
                fbcursor.execute(signup_sql,signup_sql_val,)
                finsysdb.commit()
                try:
                    main_frame_cmpny2.pack_forget()
                except:
                    pass
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                
                main_frame_cmpny=Frame(root, height=750,bg="#213b52")
                main_frame_cmpny.pack(fill=X,)

                cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
                cmpny_dt_frm.pack(pady=50)

                def name_ent(event):
                    if cmp_nm.get()=="Company Name":
                        cmp_nm.delete(0,END)
                    else:
                        pass

                def cmp_add(event):
                    if cmp_cmpn.get()=="Company Address":
                            cmp_cmpn.delete(0,END)
                    else:
                        pass
                def cty_ent(event):
                    if cmp_cty.get()=="City":
                        cmp_cty.delete(0,END)
                    else:
                        pass

                def em_ent(event):
                    if cmp_email.get()=="Email":
                            cmp_email.delete(0,END)
                    else:
                        pass
                def ph_ent(event):
                    if cmp_ph.get()=="Phone Number":
                        cmp_ph.delete(0,END)
                    else:
                        pass

                def fil_ent(event):
                    sql_log_sql='select * from auth_user where username=%s'
                    vals=(sys_usr.get(),)
                    fbcursor.execute(sql_log_sql,vals)
                    check_logins=fbcursor.fetchone()
                    
                    cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                    logo_crp=cmp_logo.split('/',-1)
                    im1 = Image.open(r""+cmp_logo) 
                    im1 = im1.save("profilepic/propic"+str(check_logins[0])+".png")
                    
                    cmp_files.delete(0,END)
                    cmp_files.insert(0,logo_crp[-1])
                
                def responsive_wid_cmp1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
            

                    dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
                    dcanvas.coords("nm_nm",dwidth/2,dheight/5)
                    dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
                    dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
                    dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
                    dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
                    dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
                    dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
                    dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
                    dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


                lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
                lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
                lf_cmpy1.pack(fill=X)

                cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


                cmp_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_nm.insert(0,"Company Name")
                cmp_nm.bind("<Button-1>",name_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_nm, tag=("nm_nm"))

                cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cmpn.insert(0,"Company Address")
                cmp_cmpn.bind("<Button-1>",cmp_add)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

                cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cty.insert(0,"City")
                cmp_cty.bind("<Button-1>",cty_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

                cmp_stat = StringVar()
                cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=cmp_stat,width=29,font=('Calibri 16'))
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
                cmpny_cntry['values'] = ('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia And Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Croatia', 'Curacao', 'Cyprus', 'Czech Republic', 'Democratic Republic Of The Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle Of Man', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Libyan Arab Jamahiriya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Russian Federation', 'Rwanda', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre And Miquelon', 'Saint Vincent And The Grenadines', 'Samoa', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Taiwan', 'Tajikistan', 'Tanzania', 'Tanzania, United Republic Of', 'Thailand', 'Togo', 'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks And Caicos Islands', 'U.S. Virgin Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wallis And Futuna', 'Yemen', 'Zambia', 'Zimbabwe')
                cmpny_cntry.current(0)

                cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
                cmp_pin.delete(0,END)
                cmp_pin.insert(0,"Pincode")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))

                def validateb211(value):
        
                        """
                        Validat the email entry
                        :param value:
                        :return:
                        """
                        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                        if re.fullmatch(pattern, value) is None:
                            
                            return False

                        cmp_email.config(fg="black")
                        return True

                def on_invalidb211():
                        cmp_email.config(fg="red")
                        

                cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_email.insert(0,"Email")
                cmp_email.bind("<Button-1>",em_ent)
                vcmdb211 = (lf_cmpy1.register(validateb211), '%P')
                ivcmdb211 = (lf_cmpy1.register(on_invalidb211),)
                cmp_email.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

                cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_ph.insert(0,"Phone Number")
                cmp_ph.bind("<Button-1>",ph_ent)
                def validate_telb51(value):
        
                        pattern = r'^[0-9]\d{9}$'
                        if re.fullmatch(pattern, value) is None:
                            
                            return False
                        cmp_ph.config(fg="black")
                        return True

                def on_invalid_telb51():
                        cmp_ph.config(fg="red")
                        
                v_tel_cmdb51 = (lf_cmpy1.register(validate_telb51), '%P')
                iv_tel_cmdb51 = (lf_cmpy1.register(on_invalid_telb51),)
                cmp_ph.config(validate='focusout', validatecommand=v_tel_cmdb51, invalidcommand=iv_tel_cmdb51)

                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

                cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_files.insert(0,"No file Chosen")
                cmp_files.bind("<Button-1>",fil_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

                button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
            else:
                messagebox.showerror("Sign Up Failed","password and conform password does not match")
        else:
            messagebox.showerror("Sign Up Failed","Username and password already exist")
    else:
        if password==con_password and con_password==password :
                
                signup_sql="insert into auth_user(first_name,last_name,email,username,password) VALUES(%s,%s,%s,%s,%s)" #adding values into db
                signup_sql_val=(first_name,last_name,email,username,password,)
                fbcursor.execute(signup_sql,signup_sql_val,)
                finsysdb.commit()
                try:
                    main_frame_cmpny2.pack_forget()
                except:
                    pass
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                
                main_frame_cmpny=Frame(root, height=750,bg="#213b52")
                main_frame_cmpny.pack(fill=X,)

                cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
                cmpny_dt_frm.pack(pady=50)

                def name_ent(event):
                    if nm_nm.get()=="Company Name":
                        nm_nm.delete(0,END)
                    else:
                        pass

                def cmp_add(event):
                    if cmp_cmpn.get()=="Company Address":
                            cmp_cmpn.delete(0,END)
                    else:
                        pass
                def cty_ent(event):
                    if cmp_cty.get()=="City":
                        cmp_cty.delete(0,END)
                    else:
                        pass

                def em_ent(event):
                    if cmp_email.get()=="Email":
                            cmp_email.delete(0,END)
                    else:
                        pass
                def ph_ent(event):
                    if cmp_ph.get()=="Phone Number":
                        cmp_ph.delete(0,END)
                    else:
                        pass

                def fil_ent(event):
                    sql_log_sql='select * from auth_user where username=%s'
                    vals=(sys_usr.get(),)
                    fbcursor.execute(sql_log_sql,vals)
                    check_logins=fbcursor.fetchone()
                    cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                    logo_crp=cmp_logo.split('/',-1)
                    im1 = Image.open(r""+cmp_logo) 
                    im1 = im1.save("profilepic/propic"+str(check_logins[0])+".png")
                    
                    cmp_files.delete(0,END)
                    cmp_files.insert(0,logo_crp[-1])
                
                def responsive_wid_cmp1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
            

                    dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
                    dcanvas.coords("nm_nm",dwidth/2,dheight/5)
                    dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
                    dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
                    dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
                    dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
                    dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
                    dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
                    dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
                    dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


                lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
                lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
                lf_cmpy1.pack(fill=X)

                cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


                nm_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
                nm_nm.insert(0,"Company Name")
                nm_nm.bind("<Button-1>",name_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=nm_nm, tag=("nm_nm"))

                cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cmpn.insert(0,"Company Address")
                cmp_cmpn.bind("<Button-1>",cmp_add)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

                cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cty.insert(0,"City")
                cmp_cty.bind("<Button-1>",cty_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

                invset_bg_var = StringVar()
                cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
                cmpny_cntry['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
                cmpny_cntry.current(0)

                cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
                cmp_pin.delete(0,END)
                cmp_pin.insert(0,"Pincode")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))
            

                cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_email.insert(0,"Email")
                cmp_email.bind("<Button-1>",em_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

                cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_ph.insert(0,"Phone Number")
                cmp_ph.bind("<Button-1>",ph_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

                cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_files.insert(0,"No file Chosen")
                cmp_files.bind("<Button-1>",fil_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

                button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
        else:
                messagebox.showerror("Sign Up Failed","password and conform password does not match")
  
#--------------------------------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    try:
        bs_nm=nm_nm2.get()
        ind_type=industry_tp.get()
        com_typ=cmp_type.get()
        acount_manage=bs_act_man.get()
        paid_type=paid_typ.get()

        sql_log_sql='select id from auth_user where username=%s'
        sql_log_sql_val=(sys_usr.get(),)
            
        fbcursor.execute(sql_log_sql,sql_log_sql_val,)
        id=fbcursor.fetchone()
        signup_cmp_sql="update app1_company set bname=%s,industry=%s,ctype=%s,abt=%s,paid=%s  where id_id=%s" #adding values into db
        signup_cmp_sql_val=(bs_nm,ind_type,com_typ,acount_manage,paid_type,id[0],)
        fbcursor.execute(signup_cmp_sql,signup_cmp_sql_val,)
        finsysdb.commit()
    except:
        pass


    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass

    main_frame_signin.pack(fill=X,)
    
#---------------------------------------------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    
    global main_frame_signup,fst_nm,lst_nm,sys_em,sys_usr,sys_pass,sys_cf
    main_frame_signin.pack_forget()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    def responsive_wid_signup(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("round_signup",dwidth/2,-dheight/.5,dwidth/.7,dheight/.5)
        dcanvas.coords("sign_in_lb",dwidth/6,dheight/12)
        dcanvas.coords("fst_nm",dwidth/8.5,dheight/5)
        dcanvas.coords("lst_nm",dwidth/8.5,dheight/3.5)
        dcanvas.coords("sys_em",dwidth/8.5,dheight/2.7)
        dcanvas.coords("sys_usr",dwidth/8.5,dheight/2.2)
        dcanvas.coords("sys_pass",dwidth/8.5,dheight/1.85)
        dcanvas.coords("sys_cf",dwidth/8.5,dheight/1.6)
        dcanvas.coords("button_sign",dwidth/6,dheight/1.4)
        dcanvas.coords("lft_lab",dwidth/1.4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/1.52,dheight/10)
        dcanvas.coords("btn_signup2",dwidth/1.36,dheight/6.6)
        dcanvas.coords("label_img",dwidth/1.8,dheight/5)
        
        


    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.bind("<Configure>", responsive_wid_signup)
    lf_signup.pack(fill=X)

    lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_signup"))

    # #--------------------------------------------------------------------------------sign up section
    sign_in_lb=Label(lf_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_in_lb, tag=("sign_in_lb"))

    def nme(event):
        if fst_nm.get()=="Firstname":
            fst_nm.delete(0,END)
        else:
            pass

    def nme1(event):
        if lst_nm.get()=="Lastname":
            lst_nm.delete(0,END)
        else:
            pass
        
    def nme2(event):
        if sys_em.get()=="Email":
            sys_em.delete(0,END)
        else:
            pass
        
        
    def nme3(event):
        if sys_usr.get()=="Username":
            sys_usr.delete(0,END)
        else:
            pass
        
    def nme4(event):
        if sys_pass.get()=="Password":
            sys_pass.delete(0,END)
            messagebox.showerror("Password Format","The password length must be greater than or equal to 8 \n>The password must contain one or more uppercase characters\n>The password must contain one or more lowercase characters\n>The password must contain one or more numeric values\n>The password must contain one or more special characters")
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(lf_signup, width=25, font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=fst_nm, tag=("fst_nm"))

    lst_nm = Entry(lf_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lst_nm, tag=("lst_nm"))

    
    sys_em = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    def validateb211(value):
        
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value) is None:
                            
            return False

        sys_em.config(fg="black")
        return True

    def on_invalidb211():
        
        sys_em.config(fg="red")

    vcmdb211 = (lf_signup.register(validateb211), '%P')
    ivcmdb211 = (lf_signup.register(on_invalidb211),)
    sys_em.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_em, tag=("sys_em"))

    sys_usr = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_usr, tag=("sys_usr"))

    sys_pass = Entry(lf_signup, width=25, font=('Calibri 16'),)
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    def pas_val_fun(value):
        
        pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
        if re.fullmatch(pattern, value) is None:
                            
            return False

        sys_pass.config(fg="black")
        return True

    def pass_inval_fun():
        sys_pass.config(fg="red")

    pas_val = (lf_signup.register(pas_val_fun), '%P')
    pass_inval = (lf_signup.register(pass_inval_fun),)

    sys_pass.config(validate='focusout', validatecommand=pas_val, invalidcommand=pass_inval)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_pass, tag=("sys_pass"))

    sys_cf = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_cf, tag=("sys_cf"))

    button_sign = customtkinter.CTkButton(master=lf_signup, command=cmpny_crt1,text="Sign Up",bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button_sign, tag=("button_sign"))

    label_img = Label(lf_signup, image = sign_up,bg="#213b52", width=800,anchor="w")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=label_img, tag=("label_img"))
    
    

    lft_lab=Label(lf_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
    lft_lab2=Label(lf_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

    btn_signup2 = Button(lf_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn_signup2, tag=("btn_signup2"))


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)


def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

def sig_pass(event):
        if pass_ent.get()=="********":
            pass_ent.delete(0,END)
        else:
            pass


def responsive_wid_login(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("sign_inlb",dwidth/1.4,dheight/4)

        dcanvas.coords("nm_ent",dwidth/1.5,dheight/2.7)
        dcanvas.coords("pass_ent",dwidth/1.5,dheight/2.2)
        dcanvas.coords("button",dwidth/1.4,dheight/1.8)
        dcanvas.coords("round_login",-dwidth/2,-dheight/.5,dwidth/2,dheight/.5)
        dcanvas.coords("lft_lab",dwidth/4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/6,dheight/10)
        dcanvas.coords("btn2",dwidth/3.7,dheight/6.6)
        dcanvas.coords("img",dwidth/16,dheight/5.5)
    

lf_signup= Canvas(main_frame_signin,width=1366,height=750)
lf_signup.bind("<Configure>", responsive_wid_login)
lf_signup.pack(fill=X)

sign_inlb=Label(lf_signup, text="Sign In",font=('Calibri 30 bold'), fg="black")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_inlb, tag=("sign_inlb"))

nm_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=nm_ent, tag=("nm_ent"))

pass_ent = Entry(lf_signup, width=25, font=('Calibri 16'),show="*")
pass_ent.insert(0,"********")
pass_ent.bind("<Button-1>",sig_pass)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=pass_ent, tag=("pass_ent"))

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button, tag=("button"))

# #------------------------------------------------------------------------------------------------------------------------left canvas

lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_login"))

img = Label(lf_signup, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=img, tag=("img"))

lft_lab=Label(lf_signup, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
lft_lab2=Label(lf_signup, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn2, tag=("btn2"))

root.mainloop()