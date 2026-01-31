from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from matplotlib.ticker import MaxNLocator
from datetime import datetime
import numpy as np
from tkinter import filedialog
from matplotlib.backends.backend_pdf import PdfPages

class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("CRIMINAL MANAGEMENT SYSTEM")
        self.root.state('zoomed')

        # variables-
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nick_name = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birth_mark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()

        # ------------------------Title------------------------
        lbl_title = Label(
            self.root,
            text="CRIMINAL MANAGEMENT SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="gold",
            anchor="w",
            padx=160
        )
        lbl_title.place(x=0, y=0, width=1530, height=60)

        # Date and Time
        lbl_datetime = Label(
                self.root,
                font=("times new roman", 14, "bold"),
                bg="black",
                fg="white",
                justify=RIGHT
        )
        lbl_datetime.place(relx=1.0, y=0, width=200, height=60, anchor='ne')

        def update_datetime():
                current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                lbl_datetime.config(text=current_time)
                lbl_datetime.after(1000, update_datetime)

        update_datetime()

        # ------------------------LOGO IMAGE------------------------
        try:
            img_logo = Image.open("V:\Download\Project For College\IMAGE\LOGO2.png")
            img_logo = img_logo.resize((80, 60), Image.Resampling.LANCZOS)  
            self.photoimg_logo = ImageTk.PhotoImage(img_logo)

            self.logo = Label(self.root, image=self.photoimg_logo, bg="black")
            self.logo.place(x=50, y=3, width=55, height=55)
        except:
            self.logo = Label(self.root, text="LOGO", font=("arial", 12, "bold"), bg="black", fg="white")
            self.logo.place(x=20, y=3, width=55, height=55)

        # ------------------------FRAME IMAGE------------------------
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        img_frame.place(x=0, y=60, width=1530, height=140)

        # Create placeholder images if actual images are not found
        try:
            img1 = Image.open("V:\Download\Project For College\IMAGE\IMG1.jpg")
            img1 = img1.resize((540, 160), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
        except:
            img1 = Image.new('RGB', (540, 160), color='#2c3e50')
            self.photoimg1 = ImageTk.PhotoImage(img1)

        self.img1 = Label(img_frame, image=self.photoimg1)
        self.img1.place(x=0, y=0, width=540, height=160)

        try:
            img2 = Image.open("V:\Download\Project For College\IMAGE\IMG2.jpg")
            img2 = img2.resize((540, 160), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
        except:
            img2 = Image.new('RGB', (540, 160), color='#34495e')
            self.photoimg2 = ImageTk.PhotoImage(img2)

        self.img2 = Label(img_frame, image=self.photoimg2)
        self.img2.place(x=540, y=0, width=540, height=160)

        try:
            img3 = Image.open("V:\Download\Project For College\IMAGE\IMG3.jpg")
            img3 = img3.resize((540, 160), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
        except:
            img3 = Image.new('RGB', (540, 160), color='#7f8c8d')
            self.photoimg3 = ImageTk.PhotoImage(img3)

        self.img3 = Label(img_frame, image=self.photoimg3)
        self.img3.place(x=1080, y=0, width=540, height=160)

        # ----------------------------Main Frame----------------------------
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=0, y=200, width=1530, height=590)

        # ----------------------------Upper Frame----------------------------
        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Criminal Information",
        font=("times new roman", 11, "bold"),fg='red',bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=270)

        # Labels and Entries
        # Case ID
        caseid = Label(upper_frame, text="Case ID:", font=("arial", 11, "bold"), bg="white")
        caseid.grid(row=0, column=0, padx=2, sticky=W)

        caseentery = ttk.Entry(upper_frame,textvariable=self.var_case_id, width=22, font=("arial", 11, "bold"))
        caseentery.grid(row=0, column=1, padx=2, sticky=W)

        # Criminal NO
        lbl_criminal_no = Label(upper_frame, text="Criminal No:", font=("arial", 12, "bold"), bg="white")
        lbl_criminal_no.grid(row=0, column=2, padx=2, sticky=W, pady=7)

        txt_criminal_no = ttk.Entry(upper_frame,textvariable=self.var_criminal_no, width=22, font=("arial", 11, "bold"))
        txt_criminal_no.grid(row=0, column=3, padx=2, sticky=W, pady=7)

        # Criminal Name
        lbl_name = Label(upper_frame, text="Name:", font=("arial", 12, "bold"), bg="white")
        lbl_name.grid(row=1, column=0, padx=2, sticky=W, pady=7)

        txt_name = ttk.Entry(upper_frame,textvariable=self.var_name, width=22, font=("arial", 11, "bold"))
        txt_name.grid(row=1, column=1, padx=2, sticky=W, pady=7)

        # Nick Name
        lbl_nick_name = Label(upper_frame, text="Nick Name:", font=("arial", 12, "bold"), bg="white")
        lbl_nick_name.grid(row=1, column=2, padx=2, sticky=W, pady=7)

        txt_nick_name = ttk.Entry(upper_frame,textvariable=self.var_nick_name, width=22, font=("arial", 11, "bold"))
        txt_nick_name.grid(row=1, column=3, padx=2, sticky=W, pady=7)

        # Arrest Date
        lbl_arrest_date = Label(upper_frame, text="Arrest Date:", font=("arial", 12, "bold"), bg="white")
        lbl_arrest_date.grid(row=2, column=0, padx=2, sticky=W, pady=7)

        txt_arrest_date = ttk.Entry(upper_frame,textvariable=self.var_arrest_date, width=22, font=("arial", 11, "bold"))
        txt_arrest_date.grid(row=2, column=1, padx=2, sticky=W, pady=7)

        # Date of Crime
        lbl_date_of_crime = Label(upper_frame, text="Date of Crime:", font=("arial", 12, "bold"), bg="white")
        lbl_date_of_crime.grid(row=2, column=2, padx=2, sticky=W, pady=7)

        txt_date_of_crime = ttk.Entry(upper_frame,textvariable=self.var_date_of_crime, width=22, font=("arial", 11, "bold"))
        txt_date_of_crime.grid(row=2, column=3, padx=2, sticky=W, pady=7)

        # Address
        lbl_address = Label(upper_frame, text="Address:", font=("arial", 12, "bold"), bg="white")
        lbl_address.grid(row=3, column=0, padx=2, sticky=W, pady=7)

        txt_address = ttk.Entry(upper_frame,textvariable=self.var_address, width=22, font=("arial", 11, "bold"))
        txt_address.grid(row=3, column=1, padx=2, sticky=W, pady=7)

        # Age
        lbl_age = Label(upper_frame, text="Age:", font=("arial", 12, "bold"), bg="white")
        lbl_age.grid(row=3, column=2, padx=2, sticky=W, pady=7)

        txt_age = ttk.Entry(upper_frame,textvariable=self.var_age, width=22, font=("arial", 11, "bold"))
        txt_age.grid(row=3, column=3, padx=2, sticky=W, pady=7)

        # Occupation
        lbl_occupation = Label(upper_frame, text="Occupation:", font=("arial", 12, "bold"), bg="white")
        lbl_occupation.grid(row=4, column=0, padx=2, sticky=W, pady=7)

        txt_occupation = ttk.Entry(upper_frame,textvariable=self.var_occupation, width=22, font=("arial", 11, "bold"))
        txt_occupation.grid(row=4, column=1, padx=2, sticky=W, pady=7)

        # Birth Mark
        lbl_birth_mark = Label(upper_frame, text="Birth Mark:", font=("arial", 12, "bold"), bg="white")
        lbl_birth_mark.grid(row=4, column=2, padx=2, sticky=W, pady=7)

        txt_birth_mark = ttk.Entry(upper_frame,textvariable=self.var_birth_mark, width=22, font=("arial", 11, "bold"))
        txt_birth_mark.grid(row=4, column=3, padx=2, sticky=W, pady=7)

        # Crime Type
        lbl_crime_type = Label(upper_frame, text="Crime Type:", font=("arial", 12, "bold"), bg="white")
        lbl_crime_type.grid(row=0, column=4, padx=2, sticky=W, pady=7)

        txt_crime_type = ttk.Entry(upper_frame,textvariable=self.var_crime_type, width=22, font=("arial", 11, "bold"))
        txt_crime_type.grid(row=0, column=5, padx=2, sticky=W, pady=7)

        # Father Name
        lbl_father_name = Label(upper_frame, text="Father Name:", font=("arial", 12, "bold"), bg="white")
        lbl_father_name.grid(row=1, column=4, padx=2, sticky=W, pady=7)

        txt_father_name = ttk.Entry(upper_frame,textvariable=self.var_father_name, width=22, font=("arial", 11, "bold"))
        txt_father_name.grid(row=1, column=5, padx=2, sticky=W, pady=7)

        # Wanted
        lbl_wanted = Label(upper_frame, text="Wanted:", font=("arial", 12, "bold"), bg="white")
        lbl_wanted.grid(row=3, column=4, padx=2, sticky=W, pady=7)

        # Radio Button Gender
        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        radio_frame_gender.place(x=710, y=90, width=180, height=30)

        # Gender
        lbl_gender = Label(upper_frame, text="Gender:", font=("arial", 12, "bold"), bg="white")
        lbl_gender.grid(row=2, column=4, padx=2, sticky=W, pady=7)

        male = Radiobutton(radio_frame_gender,variable=self.var_gender, text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,padx=5,sticky=W)
        self.var_gender.set('male')

        female = Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,padx=5,sticky=W)

        # Radio Button Wanted
        radio_frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        radio_frame_wanted.place(x=710, y=130, width=180, height=30)

        yes = Radiobutton(radio_frame_wanted,variable=self.var_wanted, text='Yes',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,padx=5,sticky=W)
        self.var_wanted.set('yes')

        no = Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,padx=5,sticky=W,pady=2)

        # Buttons Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=5, y=200, width=630, height=45)

        # add button
        btn_add = Button(button_frame,command=self.add_data, text="Record Save", font=("arial", 13, "bold"), bg="blue", fg="white", width=14)
        btn_add.grid(row=0, column=0, padx=3 , pady=5)

        # update button
        btn_update = Button(button_frame,command=self.update_data, text="Update", font=("arial", 13, "bold"), bg="green", fg="white", width=14)
        btn_update.grid(row=0, column=1, padx=3 , pady=5)

        # Delete button
        btn_Delete = Button(button_frame,command=self.delete_data, text="Delete", font=("arial", 13, "bold"), bg="red", fg="white", width=14)
        btn_Delete.grid(row=0, column=2, padx=3 , pady=5)

        # Clear button
        btn_clear = Button(button_frame,command=self.clear_data, text="Clear", font=("arial", 13, "bold"), bg="orange", fg="white", width=14)
        btn_clear.grid(row=0, column=3, padx=3 , pady=5)

        # ----------------------------Background Right Side Image----------------------------
        try:
            img_crime = Image.open("V:\Download\Project For College\IMAGE\IMG4.jpg")
            img_crime = img_crime.resize((500, 250), Image.Resampling.LANCZOS)
            self.photoimgcrime = ImageTk.PhotoImage(img_crime)
        except:
            img_crime = Image.new('RGB', (500, 250), color='#3498db')
            self.photoimgcrime = ImageTk.PhotoImage(img_crime)

        self.img_crime = Label(upper_frame, image=self.photoimgcrime)
        self.img_crime.place(x=1000, y=0, width=500, height=240)

        # ----------------------------Down Frame----------------------------
        down_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Criminal information Table",
        font=("times new roman", 11, "bold"),fg='red',bg='white')
        down_frame.place(x=10, y=280, width=1500, height=300)

        # ----------------------------Search record----------------------------
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE,text="Search Criminal Record",
        font=("times new roman", 11, "bold"),fg='red',bg='white')
        search_frame.place(x=10, y=5, width=1480, height=70)

        search_by = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_by.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.var_com_search = StringVar()
        combo_search_box = ttk.Combobox(search_frame,textvariable=self.var_com_search, font=("arial", 11, "bold"), state="readonly", width=18)
        combo_search_box["value"] = ("Select Option", "case_id", "criminal_no", "name", "crime_type", "gender", "wanted")
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        self.var_search = StringVar()
        search_txt = ttk.Entry(search_frame,textvariable=self.var_search, width=18, font=("arial", 11, "bold"))
        search_txt.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        # Search Button
        btn_search = Button(search_frame,command=self.search_data, text="Search", font=("arial", 13, "bold"), bg="green", fg="white", width=12)
        btn_search.grid(row=0, column=3, padx=5 , pady=5)

        # Show All Button
        btn_all = Button(search_frame,command=self.fetch_data, text="Show All", font=("arial", 13, "bold"), bg="blue", fg="white", width=12)
        btn_all.grid(row=0, column=4, padx=5 , pady=0)

        # Show Charts Button
        btn_charts = Button(search_frame,command=self.show_charts, text="Show Analytics", font=("arial", 13, "bold"), bg="purple", fg="white", width=14)
        btn_charts.grid(row=0, column=5, padx=5 , pady=0)

        # Export Excel Button - FIXED
        btn_export = Button(search_frame,command=self.export_to_excel, text="Export Excel", font=("arial", 13, "bold"), bg="darkorange", fg="white", width=12)
        btn_export.grid(row=0, column=6, padx=5 , pady=0)

        crimeagency = Label(search_frame, text="NATIONAL CRIME AGENCY", font=("arial", 24, "bold"), bg="white", fg="crimson")
        crimeagency.grid(row=0, column=7, padx=10, pady=0, sticky=W)

        # ----------------------------Table Frame----------------------------
        table_frame = Frame(down_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=70, width=1480, height=210)

        # ----------------------------Scroll Bar----------------------------
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, column=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1", text="Case ID")
        self.criminal_table.heading("2", text="Criminal No")
        self.criminal_table.heading("3", text="Name")
        self.criminal_table.heading("4", text="Nick Name")
        self.criminal_table.heading("5", text="Arrest Date")
        self.criminal_table.heading("6", text="Date of Crime")
        self.criminal_table.heading("7", text="Address")
        self.criminal_table.heading("8", text="Age")
        self.criminal_table.heading("9", text="Occupation")
        self.criminal_table.heading("10", text="Birth Mark")
        self.criminal_table.heading("11", text="Crime Type")
        self.criminal_table.heading("12", text="Father Name")
        self.criminal_table.heading("13", text="Gender")
        self.criminal_table.heading("14", text="Wanted")

        self.criminal_table["show"] = "headings"
        self.criminal_table.column("1", width=100)
        self.criminal_table.column("2", width=100)
        self.criminal_table.column("3", width=100)
        self.criminal_table.column("4", width=100)
        self.criminal_table.column("5", width=100)
        self.criminal_table.column("6", width=100)
        self.criminal_table.column("7", width=100)      
        self.criminal_table.column("8", width=100)
        self.criminal_table.column("9", width=100)
        self.criminal_table.column("10", width=100)
        self.criminal_table.column("11", width=100)
        self.criminal_table.column("12", width=100)
        self.criminal_table.column("13", width=100)
        self.criminal_table.column("14", width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)
        self.criminal_table.bind("<ButtonRelease>", self.get_cursor)
        self.criminal_table.bind("<Double-1>", self.show_criminal_details)
        
        # Fetch initial data
        self.fetch_data()

    # ------------------------------------Enhanced Chart Functions------------------------------------
    def get_chart_data(self):
        """Fetch data from database for chart generation"""
        try:
            conn = mysql.connector.connect(host="localhost", username="root", 
                                         password="12345678", database="criminal_management")
            query = "SELECT crime_type, gender, wanted, age, occupation FROM criminal"
            df = pd.read_sql_query(query, conn)
            conn.close()
            
            # Convert age to numeric
            df['age'] = pd.to_numeric(df['age'], errors='coerce')
            return df
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch chart data: {str(e)}")
            return None

    def show_charts(self):
        """Display enhanced charts in a new window"""
        data = self.get_chart_data()
        if data is None or data.empty:
            messagebox.showinfo("Info", "No data available for charts. Add some records first.")
            return

        # Create new window for charts
        chart_window = Toplevel(self.root)
        chart_window.title("CRIMINAL DATA ANALYTICS DASHBOARD")
        chart_window.geometry("1200x800")
        chart_window.configure(bg='white')
        chart_window.state('zoomed')

        # Title for the dashboard
        dashboard_title = Label(chart_window, text="📊 CRIMINAL DATA ANALYTICS DASHBOARD", 
                               font=("arial", 20, "bold"), bg="white", fg="darkblue")
        dashboard_title.pack(pady=10)

        # Create notebook for multiple charts
        notebook = ttk.Notebook(chart_window)
        notebook.pack(fill=BOTH, expand=True, padx=15, pady=15)

        # -------------------------------------------------------------------------
        # Tab 1: Crime Analysis
        # -------------------------------------------------------------------------
        frame1 = Frame(notebook, bg='white')
        notebook.add(frame1, text="Crime Analysis")

        # Create sub-frames for multiple charts in crime analysis
        crime_top_frame = Frame(frame1, bg='white')
        crime_top_frame.pack(fill=BOTH, expand=True, side=TOP)
        
        crime_bottom_frame = Frame(frame1, bg='white')
        crime_bottom_frame.pack(fill=BOTH, expand=True, side=BOTTOM)

        # Chart 1A: Crime Type Distribution (Bar Chart)
        fig1, ax1 = plt.subplots(figsize=(12, 6))
        crime_counts = data['crime_type'].value_counts()
        
        # Use different colors for each bar
        colors = plt.cm.Set3(np.linspace(0, 1, len(crime_counts)))
        bars = ax1.bar(range(len(crime_counts)), crime_counts.values, color=colors, edgecolor='black', width=0.7)
        
        ax1.set_title('Crime Type Distribution', fontsize=18, fontweight='bold', pad=20)
        ax1.set_xlabel('Crime Type', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Number of Cases', fontsize=14, fontweight='bold')
        ax1.set_xticks(range(len(crime_counts)))
        ax1.set_xticklabels(crime_counts.index, rotation=45, ha='right', fontsize=10)
        
        # Add data labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=10)
        
        # Add data labels inside bars (for better visibility)
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax1.text(bar.get_x() + bar.get_width()/2., height/2,
                        f'{int(height)}', ha='center', va='center', 
                        fontweight='bold', fontsize=9, color='white')
        
        ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax1.grid(axis='y', alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        canvas1 = FigureCanvasTkAgg(fig1, crime_top_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        # Chart 1B: Crime Type Distribution (Pie Chart)
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        crime_counts_pie = data['crime_type'].value_counts().head(8)  # Show top 8
        
        # Create pie chart with percentage labels
        wedges, texts, autotexts = ax2.pie(crime_counts_pie.values, 
                                          labels=crime_counts_pie.index,
                                          autopct=lambda p: f'{p:.1f}%\n({int(p/100*crime_counts_pie.sum())})',
                                          startangle=90,
                                          colors=plt.cm.Paired(np.linspace(0, 1, len(crime_counts_pie))),
                                          textprops={'fontsize': 9},
                                          explode=[0.05]*len(crime_counts_pie))
        
        ax2.set_title('Top Crime Types (Percentage)', fontsize=8, fontweight='bold', pad=20)
        
        # Make percentage labels bold
        for autotext in autotexts:
            autotext.set_fontweight('bold')
            autotext.set_fontsize(8)
            autotext.set_color('white')
        
        plt.tight_layout()
        canvas2 = FigureCanvasTkAgg(fig2, crime_top_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        # -------------------------------------------------------------------------
        # Tab 2: Demographic Analysis
        # -------------------------------------------------------------------------
        frame2 = Frame(notebook, bg='white')
        notebook.add(frame2, text="Demographic Analysis")

        # Create sub-frames
        demo_top_frame = Frame(frame2, bg='white')
        demo_top_frame.pack(fill=BOTH, expand=True, side=TOP)
        
        demo_bottom_frame = Frame(frame2, bg='white')
        demo_bottom_frame.pack(fill=BOTH, expand=True, side=BOTTOM)

        # Chart 2A: Enhanced Age Distribution with proper column labels
        fig3, ax3 = plt.subplots(figsize=(14, 6))
        
        # Create age groups with proper labels
        bins = [0, 18, 25, 35, 45, 55, 65, 100]
        age_labels = ['Under 18', '18-25', '26-35', '36-45', '46-55', '56-65', '65+']
        
        # Create age groups
        age_groups = pd.cut(data['age'].dropna(), bins=bins, labels=age_labels, right=False)
        age_group_counts = age_groups.value_counts().sort_index()
        
        # Create bar chart with age groups
        colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(age_group_counts)))
        bars = ax3.bar(age_group_counts.index, age_group_counts.values, 
                      color=colors, edgecolor='black', width=0.6)
        
        ax3.set_title('Age Distribution of Criminals', fontsize=18, fontweight='bold', pad=20)
        ax3.set_xlabel('Age Groups', fontsize=14, fontweight='bold')
        ax3.set_ylabel('Number of Criminals', fontsize=14, fontweight='bold')
        
        # Add data labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom', 
                    fontweight='bold', fontsize=11, color='darkblue')
        
        # Add value labels inside bars for better visibility
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax3.text(bar.get_x() + bar.get_width()/2., height/2,
                        f'{int(height)}', ha='center', va='center', 
                        fontweight='bold', fontsize=10, color='white')
        
        # Add percentage labels below each bar
        total_ages = age_group_counts.sum()
        for i, count in enumerate(age_group_counts.values):
            percentage = (count / total_ages * 100) if total_ages > 0 else 0
            ax3.text(i, -0.5, f'{percentage:.1f}%', ha='center', va='top', 
                    fontweight='bold', fontsize=9, color='green')
        
        # Customize grid and ticks
        ax3.grid(axis='y', alpha=0.3, linestyle='--')
        ax3.yaxis.set_major_locator(MaxNLocator(integer=True))
        
        plt.tight_layout()
        canvas3 = FigureCanvasTkAgg(fig3, demo_top_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Chart 2B: Gender Distribution Analysis
        fig4, (ax4a, ax4b) = plt.subplots(1, 2, figsize=(12, 5))
        

        # Stacked bar chart for gender vs wanted status
        gender_wanted = pd.crosstab(data['gender'], data['wanted'])
        colors_wanted = ['#FF6B6B', '#4ECDC4']
        

        # -------------------------------------------------------------------------
        # Tab 3: Status Analysis
        # -------------------------------------------------------------------------
        frame3 = Frame(notebook, bg='white')
        notebook.add(frame3, text="Status Analysis")

        fig5, (ax5a, ax5b) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Chart 3A: Wanted Status Distribution with enhanced visualization
        wanted_counts = data['wanted'].value_counts()
        colors_wanted = {'yes': '#FF6B6B', 'no': '#4ECDC4'}
        bar_colors = [colors_wanted.get(label, '#888888') for label in wanted_counts.index]
        
        bars_wanted = ax5a.bar(wanted_counts.index, wanted_counts.values, 
                              color=bar_colors, edgecolor='black', width=0.4)
        
        ax5a.set_title('Wanted Status Distribution', fontsize=18, fontweight='bold', pad=20)
        ax5a.set_xlabel('Wanted Status', fontsize=14, fontweight='bold')
        ax5a.set_ylabel('Number of Criminals', fontsize=14, fontweight='bold')
        

        
        # Add data labels inside bars
        for bar in bars_wanted:
            height = bar.get_height()
            if height > 0:
                ax5a.text(bar.get_x() + bar.get_width()/2., height/2,
                         f'{int(height)}', ha='center', va='center', 
                         fontweight='bold', fontsize=10, color='white')
        
        ax5a.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax5a.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Chart 3B: Occupations of Criminals (Top 10)
        if 'occupation' in data.columns and not data['occupation'].isnull().all():
            occupation_counts = data['occupation'].value_counts().head(10)
            colors_occupation = plt.cm.tab20c(np.linspace(0, 1, len(occupation_counts)))
            
            bars_occupation = ax5b.barh(range(len(occupation_counts)), occupation_counts.values, 
                                       color=colors_occupation, edgecolor='black', height=0.6)
            
            ax5b.set_title('💼 Top 10 Occupations of Criminals', fontsize=18, fontweight='bold', pad=20)
            ax5b.set_xlabel('Number of Criminals', fontsize=14, fontweight='bold')
            ax5b.set_ylabel('Occupation', fontsize=14, fontweight='bold')
            ax5b.set_yticks(range(len(occupation_counts)))
            ax5b.set_yticklabels(occupation_counts.index, fontsize=10)
            
            # Add data labels at the end of bars
            for i, (bar, count) in enumerate(zip(bars_occupation, occupation_counts.values)):
                ax5b.text(count + 0.5, bar.get_y() + bar.get_height()/2,
                         f'{count}', ha='left', va='center', 
                         fontweight='bold', fontsize=10, color='darkblue')
            
            # Add percentage labels
            total_occupations = occupation_counts.sum()
            for i, count in enumerate(occupation_counts.values):
                percentage = (count / total_occupations * 100) if total_occupations > 0 else 0
                ax5b.text(count/2, i, f'{percentage:.1f}%', ha='center', va='center', 
                         fontweight='bold', fontsize=9, color='white')
            
            ax5b.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax5b.grid(axis='x', alpha=0.3, linestyle='--')
        else:
            ax5b.text(0.5, 0.5, 'No Occupation Data Available', 
                     ha='center', va='center', fontsize=14, fontweight='bold')
            ax5b.set_title('Occupations Data Not Available', fontsize=16, fontweight='bold')
    
        plt.tight_layout()
        canvas5 = FigureCanvasTkAgg(fig5, frame3)
        canvas5.draw()
        canvas5.get_tk_widget().pack(fill=BOTH, expand=True, padx=10, pady=10)

        # -------------------------------------------------------------------------
        # Tab 4: Statistical Summary
        # -------------------------------------------------------------------------
        frame4 = Frame(notebook, bg='white')
        notebook.add(frame4, text="Statistical Summary")

        # Create a summary statistics frame
        summary_frame = Frame(frame4, bg='white', bd=2, relief=GROOVE)
        summary_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Calculate statistics
        total_cases = len(data)
        avg_age = data['age'].mean()
        median_age = data['age'].median()
        std_age = data['age'].std()
        most_common_crime = data['crime_type'].mode()[0] if not data['crime_type'].mode().empty else "N/A"
        crime_frequency = data['crime_type'].value_counts().iloc[0] if not data['crime_type'].value_counts().empty else 0
        wanted_count = data['wanted'].value_counts().get('yes', 0)
        wanted_percentage = (wanted_count / total_cases * 100) if total_cases > 0 else 0
        male_count = data['gender'].value_counts().get('male', 0)
        female_count = data['gender'].value_counts().get('female', 0)
        male_percentage = (male_count / total_cases * 100) if total_cases > 0 else 0
        female_percentage = (female_count / total_cases * 100) if total_cases > 0 else 0
        
        # Create labels for statistics
        stats_title = Label(summary_frame, text="📈 CRIMINAL DATA STATISTICS SUMMARY", 
                           font=("arial", 18, "bold"), bg="white", fg="darkblue")
        stats_title.pack(pady=20)
        
        # Statistics grid
        stats_grid = Frame(summary_frame, bg='white')
        stats_grid.pack(pady=20)
        
        # Create statistics labels with better formatting
        stats_data = [
            ("📊 Total Cases:", f"{total_cases:,}", "#2c3e50"),
            ("📅 Average Age:", f"{avg_age:.1f} years", "#e74c3c"),
            ("📅 Median Age:", f"{median_age:.1f} years", "#e67e22"),
            ("📊 Age Std Dev:", f"{std_age:.1f} years", "#d35400"),
            ("🔍 Most Common Crime:", f"{most_common_crime} ({crime_frequency})", "#27ae60"),
            ("⚠️ Wanted Criminals:", f"{wanted_count:,} ({wanted_percentage:.1f}%)", "#c0392b"),
            ("👨 Male Criminals:", f"{male_count:,} ({male_percentage:.1f}%)", "#3498db"),
            ("👩 Female Criminals:", f"{female_count:,} ({female_percentage:.1f}%)", "#e84393"),
            ("📈 Youngest Criminal:", f"{data['age'].min():.0f} years", "#9b59b6"),
            ("📉 Oldest Criminal:", f"{data['age'].max():.0f} years", "#34495e"),
            ("📊 Age Range:", f"{data['age'].max() - data['age'].min():.0f} years", "#16a085"),
            ("📅 Data Points:", f"{len(data)} records", "#2c3e50")
        ]
        
        for i, (label, value, color) in enumerate(stats_data):
            row = i // 2
            col = i % 2
            
            stat_frame = Frame(stats_grid, bg='white')
            stat_frame.grid(row=row, column=col, padx=20, pady=10, sticky=W)
            
            lbl_stat = Label(stat_frame, text=label, font=("arial", 12, "bold"), 
                            bg="white", fg=color, width=25, anchor='w')
            lbl_stat.pack(side=LEFT)
            
            val_stat = Label(stat_frame, text=value, font=("arial", 12, "bold"), 
                            bg="white", fg="#2c3e50", width=20, anchor='w')
            val_stat.pack(side=LEFT)
        
        # Add a pie chart for quick overview
        fig6, ax6 = plt.subplots(figsize=(6, 6))
        
        # Create a simple overview pie chart
        overview_labels = ['Male', 'Female', 'Wanted', 'Not Wanted']
        overview_values = [
            male_count,
            female_count,
            wanted_count,
            total_cases - wanted_count
        ]
        
        # Filter out zero values
        overview_data = [(label, value) for label, value in zip(overview_labels, overview_values) if value > 0]
        if overview_data:
            labels, values = zip(*overview_data)
            colors_overview = ['#66B2FF', '#FF9999', '#FF6B6B', '#4ECDC4']
            
            wedges_overview, texts_overview, autotexts_overview = ax6.pie(
                values, labels=labels, autopct='%1.1f%%', startangle=90,
                colors=colors_overview[:len(values)], textprops={'fontsize': 10},
                explode=[0.05]*len(values)
            )
            
            ax6.set_title('Quick Overview', fontsize=16, fontweight='bold', pad=20)
            
            # Style the labels
            for autotext in autotexts_overview:
                autotext.set_fontweight('bold')
                autotext.set_fontsize(9)
                autotext.set_color('white')
        
        plt.tight_layout()
        
        # Create frame for the pie chart
        pie_frame = Frame(summary_frame, bg='white')
        pie_frame.pack(pady=20)
        
        canvas6 = FigureCanvasTkAgg(fig6, pie_frame)
        canvas6.draw()
        canvas6.get_tk_widget().pack()

        # Add control buttons
        btn_frame = Frame(chart_window, bg='white')
        btn_frame.pack(pady=10)
        
        btn_export_pdf = Button(btn_frame, text="📄 Export as PDF", 
                               command=lambda: self.export_charts_pdf([fig1, fig2, fig3, fig4, fig5, fig6]), 
                               font=("arial", 12, "bold"), bg="#27ae60", fg="white", width=18)
        btn_export_pdf.pack(side=LEFT, padx=5)
        
        btn_export_images = Button(btn_frame, text="🖼️ Export Images", 
                                  command=lambda: self.export_charts_images([fig1, fig2, fig3, fig4, fig5, fig6]), 
                                  font=("arial", 12, "bold"), bg="#3498db", fg="white", width=18)
        btn_export_images.pack(side=LEFT, padx=5)
        
        btn_refresh = Button(btn_frame, text="🔄 Refresh Data", 
                            command=lambda: self.refresh_charts(chart_window), 
                            font=("arial", 12, "bold"), bg="#9b59b6", fg="white", width=18)
        btn_refresh.pack(side=LEFT, padx=5)
        
        btn_close = Button(btn_frame, text="❌ Close Dashboard", 
                          command=chart_window.destroy, 
                          font=("arial", 12, "bold"), bg="#e74c3c", fg="white", width=18)
        btn_close.pack(side=LEFT, padx=5)

    def export_charts_pdf(self, figures):
        """Export all charts as PDF"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
                initialfile="criminal_analytics_report.pdf"
            )
            
            if filename:
                with PdfPages(filename) as pdf:
                    for fig in figures:
                        pdf.savefig(fig, bbox_inches='tight')
                
                messagebox.showinfo("Success", f"✅ Report exported successfully to:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Failed to export PDF: {str(e)}")

    def export_charts_images(self, figures):
        """Export all charts as individual images"""
        try:
            folder_path = filedialog.askdirectory(title="Select folder to save images")
            
            if folder_path:
                chart_names = [
                    "crime_type_distribution.png",
                    "crime_type_pie.png",
                    "age_distribution.png",
                    "gender_analysis.png",
                    "status_analysis.png",
                    "statistical_summary.png"
                ]
                
                for i, (fig, name) in enumerate(zip(figures, chart_names)):
                    filepath = f"{folder_path}/{name}"
                    fig.savefig(filepath, dpi=300, bbox_inches='tight')
                
                messagebox.showinfo("Success", f"✅ Charts exported successfully to:\n{folder_path}")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Failed to export images: {str(e)}")

    def refresh_charts(self, window):
        """Refresh charts with updated data"""
        window.destroy()
        self.show_charts()

    def show_criminal_details(self, event):
        """Show detailed view of selected criminal"""
        try:
            cursor_row = self.criminal_table.focus()
            content = self.criminal_table.item(cursor_row)
            data = content["values"]
            
            if data:
                detail_window = Toplevel(self.root)
                detail_window.title("Criminal Details")
                detail_window.geometry("600x500")
                detail_window.configure(bg='white')
                
                # Title
                title = Label(detail_window, text="🔍 CRIMINAL DETAILED VIEW", 
                            font=("arial", 18, "bold"), bg="white", fg="darkblue")
                title.pack(pady=10)
                
                # Create a frame for details
                details_frame = Frame(detail_window, bg='white', bd=2, relief=GROOVE)
                details_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
                
                # Define fields
                fields = [
                    ("Case ID:", data[0]),
                    ("Criminal No:", data[1]),
                    ("Name:", data[2]),
                    ("Nick Name:", data[3]),
                    ("Arrest Date:", data[4]),
                    ("Date of Crime:", data[5]),
                    ("Address:", data[6]),
                    ("Age:", data[7]),
                    ("Occupation:", data[8]),
                    ("Birth Mark:", data[9]),
                    ("Crime Type:", data[10]),
                    ("Father Name:", data[11]),
                    ("Gender:", data[12]),
                    ("Wanted:", data[13])
                ]
                
                # Display fields
                for i, (label, value) in enumerate(fields):
                    frame = Frame(details_frame, bg='white')
                    frame.pack(fill=X, padx=10, pady=5)
                    
                    lbl = Label(frame, text=label, font=("arial", 11, "bold"), 
                              bg="white", fg="#2c3e50", width=15, anchor='w')
                    lbl.pack(side=LEFT)
                    
                    val = Label(frame, text=value, font=("arial", 11), 
                              bg="white", fg="#34495e", width=30, anchor='w')
                    val.pack(side=LEFT)
                
                # Close button
                btn_close = Button(detail_window, text="Close", command=detail_window.destroy,
                                 font=("arial", 12, "bold"), bg="#e74c3c", fg="white", width=20)
                btn_close.pack(pady=10)
        except Exception as e:
            pass

    # FIXED: Excel Export Function
    def export_to_excel(self):
        """Export data to Excel file"""
        try:
            # Connect to database
            conn = mysql.connector.connect(
                host="localhost", 
                username="root", 
                password="12345678", 
                database="criminal_management"
            )
            
            # Query to get all data
            query = "SELECT * FROM criminal"
            df = pd.read_sql_query(query, conn)
            conn.close()
            
            if df.empty:
                messagebox.showinfo("Info", "No data to export")
                return
            
            # Ask user for save location
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",  # Changed to .csv
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],  # Removed Excel option
                initialfile="criminal_data_export.csv",  # Changed to .csv
                title="Save Data File"
            )
# ... rest of your code ...
            
            if filename:  # User didn't cancel
                # Export based on file extension
                if filename.endswith('.csv'):
                    df.to_csv(filename, index=False)
                else:
                    # For Excel, we need to create an Excel writer
                    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False, sheet_name='Criminal_Data')
                        
                        # Get workbook and worksheet for formatting
                        workbook = writer.book
                        worksheet = writer.sheets['Criminal_Data']
                        
                        # Auto-adjust column widths
                        for column in worksheet.columns:
                            max_length = 0
                            column_letter = column[0].column_letter
                            for cell in column:
                                try:
                                    if len(str(cell.value)) > max_length:
                                        max_length = len(str(cell.value))
                                except:
                                    pass
                            adjusted_width = min(max_length + 2, 30)
                            worksheet.column_dimensions[column_letter].width = adjusted_width
                
                messagebox.showinfo("Success", f"✅ Data exported successfully to:\n{filename}")
                
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"❌ Failed to connect to database: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Failed to export data: {str(e)}")

    # ------------------------------------Data Base MYSQL------------------------------------
    def add_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="criminal_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nick_name.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birth_mark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_wanted.get()
                    ))
                
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo("Success", "✅ Criminal record has been added successfully")
            except Exception as es:
                messagebox.showerror("Error", f"❌ Due To:{str(es)}")

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="criminal_management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from criminal")
            data = my_cursor.fetchall()
            
            if len(data) != 0:
                self.criminal_table.delete(*self.criminal_table.get_children())
                for i in data:
                    self.criminal_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception as e:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345678")
                my_cursor = conn.cursor()
                my_cursor.execute("CREATE DATABASE IF NOT EXISTS criminal_management")
                my_cursor.execute("USE criminal_management")
                my_cursor.execute("""
                    CREATE TABLE IF NOT EXISTS criminal (
                        case_id VARCHAR(50) PRIMARY KEY,
                        criminal_no VARCHAR(50),
                        name VARCHAR(100),
                        nick_name VARCHAR(100),
                        arrest_date VARCHAR(50),
                        date_of_crime VARCHAR(50),
                        address VARCHAR(255),
                        age VARCHAR(10),
                        occupation VARCHAR(100),
                        birth_mark VARCHAR(100),
                        crime_type VARCHAR(100),
                        father_name VARCHAR(100),
                        gender VARCHAR(10),
                        wanted VARCHAR(10)
                    )
                """)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Database created. Add some records to see data.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create database: {str(e)}")

    def get_cursor(self, event=""):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        data = content["values"]
        
        if data:
            self.var_case_id.set(data[0])
            self.var_criminal_no.set(data[1])
            self.var_name.set(data[2])
            self.var_nick_name.set(data[3])
            self.var_arrest_date.set(data[4])
            self.var_date_of_crime.set(data[5])
            self.var_address.set(data[6])
            self.var_age.set(data[7])
            self.var_occupation.set(data[8])
            self.var_birth_mark.set(data[9])
            self.var_crime_type.set(data[10])
            self.var_father_name.set(data[11])
            self.var_gender.set(data[12])
            self.var_wanted.set(data[13])

    def update_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this criminal record")
                if Update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="criminal_management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""update criminal set criminal_no=%s,name=%s,nick_name=%s,arrest_date=%s,date_of_crime=%s,
                                        address=%s,age=%s,occupation=%s,birth_mark=%s,crime_type=%s,father_name=%s,
                                        gender=%s,wanted=%s WHERE case_id=%s""", (
                                        self.var_criminal_no.get(),
                                        self.var_name.get(),
                                        self.var_nick_name.get(),
                                        self.var_arrest_date.get(),
                                        self.var_date_of_crime.get(),
                                        self.var_address.get(),
                                        self.var_age.get(),
                                        self.var_occupation.get(),
                                        self.var_birth_mark.get(),
                                        self.var_crime_type.get(),
                                        self.var_father_name.get(),
                                        self.var_gender.get(),
                                        self.var_wanted.get(),
                                        self.var_case_id.get()
                                        ))
                    conn.commit()
                    self.fetch_data()
                    self.clear_data()
                    conn.close()
                    messagebox.showinfo("Success", "✅ Criminal record successfully updated")
            except Exception as es:
                messagebox.showerror("Error", f"❌ Due To:{str(es)}")

    def delete_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this criminal record")
                if delete:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="criminal_management")
                    my_cursor = conn.cursor()
                    sql = "delete from criminal where case_id=%s"
                    val = (self.var_case_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "✅ Successfully deleted criminal record")
                    self.clear_data()                      
            except Exception as es:
                messagebox.showerror("Error", f"❌ Due To:{str(es)}")

    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nick_name.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birth_mark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("male")
        self.var_wanted.set("yes")

    def search_data(self):
        if self.var_com_search.get() == "" or self.var_com_search.get() == "Select Option":
            messagebox.showerror("Error", "Select search by option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="criminal_management")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from criminal where " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showinfo("Info", "No records found")
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}")

if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()