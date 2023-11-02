from tkinter import *
from tkinter import messagebox
from country_list import *
import pymysql
import mysql.connector



#Initialiazing the Instance and giving its size, geometry and title. 
windows = Tk()
windows.title('Personal Registration Form')
windows.geometry('540x640+200+10')
windows.resizable(0,0)

#These define commands for the Checkbuttons 
def show1():
    PasswordEntry.configure(show='#')
    check1.configure(command=hide1)

def hide1():
    PasswordEntry.configure(show='')
    check1.configure(command=show1)

def show2():
    ConfirmPasswordEntry.configure(show='#')
    check2.configure(command=hide2)

def hide2():
    ConfirmPasswordEntry.configure(show='')
    check2.configure(command=show2)

#This function defines the Entry Fields 
def submit():
    if First_Name_Entry.get() == '':
        messagebox.showerror('Please Enter your First Name')
    
    elif Last_Name_Entry.get() == '':
        messagebox.showerror('Please Enter Your Last Name')
    
    elif EmailEntry.get() == '':
        messagebox.showerror('Please Enter Your Email')
    
    elif gender.get() == '':
        messagebox.showerror('Please Select Your Gender')
    
    elif OM.get() == '':
        messagebox.showerror('Please Select Your Country')
    
    elif UsernameEntry.get() == '':
        messagebox.showerror('Please Enter Your Username')
    
    elif PasswordEntry.get() == '':
        messagebox.showerror('Please Enter Your Password')
    
    elif ConfirmPasswordEntry.get() == '':
        messagebox.showerror('Please Confirm Your Password')
    
    elif ConfirmPasswordEntry.get() != PasswordEntry.get():
        messagebox.showerror('Passwords Do Not Match')

    else:
        db = pymysql.connect(host='localhost', user='root', password='Anotheronedown12', port=3306, database='Personal_Registration_Form')
        cur = db.cursor()

#This block creates the query for the database and executes it. 
    try:
            Query = 'create database Personal_Registration_Form'
            cur.execute(Query)
            Query = 'Use Personal_Registration_Form'
            cur.execute(Query)        
            query = 'create table P_details(id int auto_increment primary key not null, firstname varchar(40),'\
                    'lastname varchar(40), email varchar(40), gender varchar(10), country varchar(40), username varchar(40), password varchar(40),'\
                    'confirmpassword varchar(40))'
            cur.execute(query)
            messagebox.showinfo('Success', 'Fields created successfully') 
        
        
    except:
            cur.execute('use Personal_Registration_Form')
            query = 'insert into P_details(firstname, lastname, email, gender, country, username, password, confirmpassword) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(query, (First_Name_Entry.get(), Last_Name_Entry.get(), EmailEntry.get(), gender.get(), OM.get(), UsernameEntry.get(), PasswordEntry.get(), ConfirmPasswordEntry.get()))
            db.commit()
            db.close()
            messagebox.showinfo('Successful Registration')

            First_Name_Entry.delete(0, END)
            Last_Name_Entry.delete(0, END)
            EmailEntry.delete(0, END)
            gender.set(0)
            OM.set(0)
            UsernameEntry.delete(0, END)
            PasswordEntry.delete(0, END)
            ConfirmPasswordEntry.delete(0, END)


   
#Section for assigning data to variables in the entry fields
firstname = StringVar()
lastname = StringVar()
email = StringVar()
gender = StringVar()
username = StringVar()
password = StringVar()
confirmpassword = StringVar()
OM = StringVar()
    
#Frame
frame = Frame(windows, width=610, height=640, bg='black', border=8)
frame.place(x=0, y=0)

#List of countries to be used in the login form. 
country = Country = [
    ('US', 'United States'),
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AS', 'American Samoa'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    ('AQ', 'Antarctica'),
    ('AG', 'Antigua And Barbuda'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AW', 'Aruba'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia And Herzegowina'),
    ('BW', 'Botswana'),
    ('BV', 'Bouvet Island'),
    ('BR', 'Brazil'),
    ('BN', 'Brunei Darussalam'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),
    ('CA', 'Canada'),
    ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),
    ('CF', 'Central African Rep'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CX', 'Christmas Island'),
    ('CC', 'Cocos Islands'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),
    ('CK', 'Cook Islands'),
    ('CR', 'Costa Rica'),
    ('CI', 'Cote D`ivoire'),
    ('HR', 'Croatia'),
    ('CU', 'Cuba'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),
    ('DJ', 'Djibouti'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('TP', 'East Timor'),
    ('EC', 'Ecuador'),
    ('EG', 'Egypt'),
    ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'),
    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('ET', 'Ethiopia'),
    ('FK', 'Falkland Islands (Malvinas)'),
    ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GF', 'French Guiana'),
    ('PF', 'French Polynesia'),
    ('TF', 'French S. Territories'),
    ('GA', 'Gabon'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),
    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GR', 'Greece'),
    ('GL', 'Greenland'),
    ('GD', 'Grenada'),
    ('GP', 'Guadeloupe'),
    ('GU', 'Guam'),
    ('GT', 'Guatemala'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),
    ('HN', 'Honduras'),
    ('HK', 'Hong Kong'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JP', 'Japan'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'),
    ('KI', 'Kiribati'),
    ('KP', 'Korea (North)'),
    ('KR', 'Korea (South)'),
    ('KW', 'Kuwait'),
    ('KG', 'Kyrgyzstan'),
    ('LA', 'Laos'),
    ('LV', 'Latvia'),
    ('LB', 'Lebanon'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libya'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('MO', 'Macau'),
    ('MK', 'Macedonia'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MU', 'Mauritius'),
    ('YT', 'Mayotte'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia'),
    ('MD', 'Moldova'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolia'),
    ('MS', 'Montserrat'),
    ('MA', 'Morocco'),
    ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NL', 'Netherlands'),
    ('AN', 'Netherlands Antilles'),
    ('NC', 'New Caledonia'),
    ('NZ', 'New Zealand'),
    ('NI', 'Nicaragua'),
    ('NE', 'Niger'),
    ('NG', 'Nigeria'),
    ('NU', 'Niue'),
    ('NF', 'Norfolk Island'),
    ('MP', 'Northern Mariana Islands'),
    ('NO', 'Norway'),
    ('OM', 'Oman'),
    ('PK', 'Pakistan'),
    ('PW', 'Palau'),
    ('PA', 'Panama'),
    ('PG', 'Papua New Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),
    ('PH', 'Philippines'),
    ('PN', 'Pitcairn'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('PR', 'Puerto Rico'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('RW', 'Rwanda'),
    ('KN', 'Saint Kitts And Nevis'),
    ('LC', 'Saint Lucia'),
    ('VC', 'St Vincent/Grenadines'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'Sao Tome'),
    ('SA', 'Saudi Arabia'),
    ('SN', 'Senegal'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'),
    ('SO', 'Somalia'),
    ('ZA', 'South Africa'),
    ('ES', 'Spain'),
    ('LK', 'Sri Lanka'),
    ('SH', 'St. Helena'),
    ('PM', 'St.Pierre'),
    ('SD', 'Sudan'),
    ('SR', 'Suriname'),
    ('SZ', 'Swaziland'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('SY', 'Syrian Arab Republic'),
    ('TW', 'Taiwan'),
    ('TJ', 'Tajikistan'),
    ('TZ', 'Tanzania'),
    ('TH', 'Thailand'),
    ('TG', 'Togo'),
    ('TK', 'Tokelau'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad And Tobago'),
    ('TN', 'Tunisia'),
    ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('UK', 'United Kingdom'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VU', 'Vanuatu'),
    ('VA', 'Vatican City State'),
    ('VE', 'Venezuela'),
    ('VN', 'Viet Nam'),
    ('VG', 'Virgin Islands (British)'),
    ('VI', 'Virgin Islands (U.S.)'),
    ('EH', 'Western Sahara'),
    ('YE', 'Yemen'),
    ('YU', 'Yugoslavia'),
    ('ZR', 'Zaire'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe')
]

OM.set('Select Country')


# Designing Labels and Entry Fields
heading  = Label(frame, text='Personal Registration Form', fg='#97ffff', bg='black', font=('Calibre', 20, 'bold'))
heading.place(x=90, y=3)

First_Name = Label(frame, text='First Name:', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
First_Name.place(x=10, y=80)

First_Name_Entry = Entry(frame, width=30, borderwidth=2)
First_Name_Entry.place(x=240, y=80)

Last_Name = Label(frame, text='Last Name:', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
Last_Name.place(x=10, y=110)

Last_Name_Entry = Entry(frame, width=30, borderwidth=2)
Last_Name_Entry.place(x=240, y=110)

Email = Label(frame, text='Email:', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
Email.place(x=10, y=150)

EmailEntry = Entry(frame, width=30, borderwidth=2)
EmailEntry.place(x=240, y=150)

Gender = Label(frame, text='Gender:', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
Gender.place(x=10, y=200)

gender.set(0)

genderRadio1 = Radiobutton(frame, text='Male', width=4, variable=gender, value='Male', font='Tahoma 13 bold')
genderRadio1.place(x=240, y=200)

genderRadio2 = Radiobutton(frame, text='Female', variable=gender, value='Female', font='Tahoma 13 bold')
genderRadio2.place(x=340, y=200)

countryLabel = Label(frame, text='Country', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
countryLabel.place(x=10, y=250)

countryLabelDropdown = OptionMenu(frame, OM, *country)
countryLabelDropdown.place(x=240, y=250)

countryLabelDropdown.config(width=18, font=('Calibre', 13, 'bold'), fg='black')

Username = Label(frame, text='Username', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
Username.place(x=10, y=300)

UsernameEntry = Entry(frame, width=30, borderwidth=2)
UsernameEntry.place(x=240, y=300)

Password = Label(frame, text='Password', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
Password.place(x=10, y=350)

PasswordEntry = Entry(frame, width=30, borderwidth=2)
PasswordEntry.place(x=240, y=350)

ConfirmPassword = Label(frame, text='Confirm Password', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
ConfirmPassword.place(x=10, y=400)

ConfirmPasswordEntry = Entry(frame, width=30, borderwidth=2)
ConfirmPasswordEntry.place(x=240, y=400)

check1 = Checkbutton(frame, bg='black', command=show1)
check1.place(x=420, y=350)

check2 = Checkbutton(frame, bg='black', command=show2)
check2.place(x=420, y=400)

Submitbutton = Button(frame, text='Submit', width=15, borderwidth=5, height=2, bg='#7f7fff', cursor='hand2', border=2,
                        font=('#57a1f8', 16, 'bold'), fg='white', command=submit)
Submitbutton.place(x=150, y=500)


windows.mainloop()