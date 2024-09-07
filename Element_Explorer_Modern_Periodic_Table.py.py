'''
                            [Element Explorer - (Modern Periodic Table) {EEmpt}]
                                    Programming language used --> Python  
'''
import periodictable
from mendeleev import element
import tkinter as tk
from tkinter import filedialog, messagebox

def info():
    try:
        atomic_number_str = entry.get()
        atomic_number = int(atomic_number_str)
        et = periodictable.elements[atomic_number]

        list = []
        list.append("\n\n\n < Element Explored >\n\n\n")
        list.append("\n\n\n !! ****************************************************************************************************  !! \n\n\n")

        list.append(f"      01.     Name                     :    {et.name}")       # Name
        list.append(f"      02.     Symbol                   :    {et.symbol}")     # Symbol
        list.append(f"      03.     Atomic Number            :    {et.number}")     # Atomic Number
        list.append(f"      04.     Atomic Weight/Mass       :    {et.mass} u")       # Atomic Weight/Mass
        list.append(f"      05.     Density                  :    {et.density} mg/m^3")    # Density

        '''Extra Info. --> using mendeleev library !!'''
        ei = element(et.symbol) # ei = element info.

        list.append(f"      06.     Group/Family             :     {ei.group}")     # Group/Family
        list.append(f"      07.     Period                   :     {ei.period}")    # Period
        list.append(f"      08.     Block                    :     {ei.block}")     # Block
        list.append(f"      09.     Series                   :     {ei.series}")    # Series
        list.append(f"      10.     Number of Electrons      :     {ei.electrons}") # No. of Electrons
        list.append(f"      11.     Number of Protons        :     {ei.protons}")   # No. of Protons
        list.append(f"      12.     Number of Neutrons       :     {ei.neutrons}")  # No. of Neutrons
        list.append(f"      13.     Electronic Configuration :     {ei.econf}")     # Electronic Configuration
        list.append(f"      14.     Isotopes                 :     {et.isotopes}")  # Isotopes
        list.append(f"      15.     Melting Point            :     {ei.melting_point} K")   # Melting Point
        list.append(f"      16.     Boiling Point            :     {ei.boiling_point} K")   # Boiling Point
        list.append(f"      17.     Specific Heat            :     {ei.specific_heat} J/g K")  # Specific Heat
        list.append(f"      18.     Discovery Year           :     {ei.discovery_year}")        # Discovery Year
        list.append(f"      19.     Discovery Location       :     {ei.discovery_location}")    # Discovery Location
        list.append(f"      20.     Discoverers              :     {ei.discoverers}")           # Discoverers                     
        list.append(f"      21.     Radioactive Element ?")                                     # Radioactivity
        if et.number > 83:                              
            list.append(f"\n                X--------------------Radioactive Element--------------------X   ")
        else:
            list.append(f"\n                X--------------------Not a Radioactive Element--------------------X ")

        list.append("\n")
        list.append("\n\n\n !! **************************************************************************************************** !! \n\n\n")

    except:
        messagebox.showwarning('''!! Error !!''', '''Please enter the correct Atomic Number 
to explore the properties of the elements.
!! Hint : 1>= Atomic Number <= 118 !! ''')
        
    # output_label.config(text="\n".join(list),font=("Helvetica",10,"bold"))
    # output_label.place()
    global langs
    global listbox
    global lbs

    langs=(list)
    var=tk.Variable(value=langs)
    listbox = tk.Listbox(root, listvariable=var, 
                    height=8, selectmode=tk.BROWSE)
    listbox.pack(padx=50,pady=5,expand=True, fill=tk.BOTH)
    lbs.append(listbox) 

lbs=[]  #lbs --> Total listboxes
def clear_list_boxes():
    for listbox in lbs:
        listbox.destroy()

# GUI Main Window
root = tk.Tk()
root.title("Element Explorer - (Modern Periodic Table)")
root.geometry("800x630")  
root.resizable(True,True)

# GUI Components
label = tk.Label(root, text = "!! Dive into the world of elements with Element Explorer !!",font=("Helvetica",10,"bold"))
label.pack(padx=20,pady=20)

# Enter Atomic Number
label = tk.Label(root, text = "Enter Atomic Number : ")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Buttons
run_button = tk.Button(root, text = "Get Information", command = info)
run_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear All", command=clear_list_boxes)
clear_button.pack(padx=10,pady=20,side=tk.RIGHT)

# Bottom Message
output_label = tk.Label(root, text = "      <<<<<<<<<<      Element Explorer - (Modern Periodic Table)     >>>>>>>>>>   ")
output_label.pack(padx=150,side=tk.BOTTOM)

output_label = tk.Label(root, text = " ")
output_label.pack()

root.mainloop()

'''********************END OF THE CODE********************'''