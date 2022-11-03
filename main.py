import tkinter
import tkintermapview
import phonenumbers
from key import key

from phonenumbers import geocoder, carrier

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import*

from opencage.geocoder import OpenCageGeocode

root = tkinter.Tk()
root.geometry("500x500")

labell = Label(text= "Tele tracker Nummer")
labell.pack()

def getResult():
    num = number.get("1.0", END)
    try:
            num1 = phonenumbers.parse(num)
    except:
            messagebox.showerror("Error", "Nummerbox ist Leer, Nummer eingeben!!")


    location = geocoder.description_for_number(num1, "de")
    service_provider = carrier.name_for_number(num1, "en")

    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    my_label = LabelFrame(root)
    my_label.pack(pady=20)

    map_widget = tkintermapview.TkinterMapView(my_label, width=450, height=450, corner_radius=0)
    map_widget.set_position(lat, lng)
    map_widget.set_marker(lat, lng, text = "Hand Standort")
    map_widget.set_zoom(10)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack()

    adr = tkintermapview.convert_coordinates_to_address(lat, lng)


    result.insert(END,"Die Landesnummer ist:" + location )
    result.insert(END, "\nDie Nummer der Simkarte ist:" + service_provider)

    result.insert(END, "\nBreitengrad ist:" + str(lat))
    result.insert(END, "\nLängenengrad ist:" + str(lng))

    result.insert(END, "\nDie Straße ist:" + adr.street)
    result.insert(END, "\nDie Stadt ist:" + adr.city)
    result.insert(END, "\nDie Prostleitzahl ist:" + adr.postal)

number = Text(height=1)
number.pack()

style = Style()
style.configure("TButton", font=('calibri', 20, 'bold'), borderwidth='4')
style.map('TButton', foreground = [('active', '!disabled', 'green')],
                    background = [('active', 'black')])


button = Button(text="Suche", command=getResult)
button.pack(pady =10, padx=100)

result = Text(height=7)
result.pack()

root.mainloop()
