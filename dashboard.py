from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
from datetime import * 
import time
from math import *
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.state("zoomed")  # Fullscreen Mode

        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.jpg")
        # Title
        title = Label(self.root, text="Student Management System", padx=10, compound=LEFT, image=self.logo_dash,
                      font=("goudy old style", 30, "bold"), background="#033054", foreground="white").place(x=0, y=0, relwidth=1, height=70)

        # Menu Frame
        M_Frame = LabelFrame(self.root, text="Menus", font=("goudy old style", 18, "bold"), background="white", fg="#033054", bd=2)
        M_Frame.place(relx=0.01, rely=0.1, relwidth=0.98, height=80)

        # Adjusted button placement to fill the menu template
        total_buttons = 6
        button_spacing = 0.02  # Space between buttons
        button_width = (1 - (button_spacing * (total_buttons + 1))) / total_buttons  # Calculate width for each button

        Button(M_Frame, text="Course", font=("goudy old style", 16, "bold"), background="#0b5377", foreground="white",
               cursor="hand2", command=self.add_course).place(relx=button_spacing, rely=0.1, relwidth=button_width, relheight=0.8)

        Button(M_Frame, text="Student", font=("goudy old style", 16, "bold"), background="#0b5377", foreground="white",
               cursor="hand2", command=self.add_student).place(relx=button_spacing + (button_width + button_spacing) * 1, rely=0.1, relwidth=button_width, relheight=0.8)

        Button(M_Frame, text="Result", font=("goudy old style", 16, "bold"), background="#0b5377", foreground="white",
               cursor="hand2", command=self.add_result).place(relx=button_spacing + (button_width + button_spacing) * 2, rely=0.1, relwidth=button_width, relheight=0.8)

        Button(M_Frame, text="View Results", font=("goudy old style", 16, "bold"), background="#0b5377", foreground="white",
               cursor="hand2", command=self.add_report).place(relx=button_spacing + (button_width + button_spacing) * 3, rely=0.1, relwidth=button_width, relheight=0.8)

        Button(M_Frame, text="Logout", font=("goudy old style", 16, "bold"), background="#0b5377", foreground="white",
               cursor="hand2", command=self.logout).place(relx=button_spacing + (button_width + button_spacing) * 4, rely=0.1, relwidth=button_width, relheight=0.8)

        Button(M_Frame, text="Exit", font=("goudy old style", 16, "bold"), background="#0b5377", foreground="white",
               cursor="hand2", command=self.exit_).place(relx=button_spacing + (button_width + button_spacing) * 5, rely=0.1, relwidth=button_width, relheight=0.8)

        # Content Window
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((900, 400), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(relx=0.35, rely=0.25, relwidth=0.6, relheight=0.45)

        # Update Details
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE,
                                 background="#e43b06", foreground="white")
        self.lbl_course.place(relx=0.35, rely=0.72, relwidth=0.18, relheight=0.1)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE,
                                  background="#0676ad", foreground="white")
        self.lbl_student.place(relx=0.54, rely=0.72, relwidth=0.18, relheight=0.1)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE,
                                 background="#038074", foreground="white")
        self.lbl_result.place(relx=0.73, rely=0.72, relwidth=0.18, relheight=0.1)

        # Clock
        self.lbl = Label(self.root, text="\nWebCode Clock", font=("Book Antiqua", 25, "bold"), fg="white", compound=BOTTOM,
                         bg="#081923", bd=0)
        self.lbl.place(relx=0.01, rely=0.25, relwidth=0.3, relheight=0.5)

        self.working()
        # Footer
        footer = Label(self.root, text="SRMS-Student Management System\nContact Us for any Technical Issue: 94xxxxxxx2",
                       font=("goudy old style", 12), background="#262626", foreground="white").pack(side=BOTTOM, fill=X)
        self.update_details()

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

            self.lbl_course.after(200, self.update_details)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def working(self):
        now = datetime.now()
        h = now.hour % 12
        m = now.minute
        s = now.second
        hr = (h * 30) + (m * 0.5)
        min_ = (m * 6) + (s * 0.1)
        sec_ = s * 6
        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(1000, self.working)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.Resampling.LANCZOS)
        clock.paste(bg, (50, 50))

        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="#DF005E", width=4)
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="white", width=3)
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.root.destroy()
            os.system("Python login.py")

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()




