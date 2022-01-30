import math
from tkinter import*
from tkinter import messagebox
from PIL import*

root = Tk()
pin = DoubleVar()
spl = DoubleVar()
nf = DoubleVar()
span = DoubleVar()
osnr = StringVar()
def calc_osnr():
    k = 58 + pin.get() - spl.get() - nf.get() - math.log10(span.get())
    osnr.set(f"OSNR is: {round(k,2)} dB")
winfow = root.geometry("400x400")
Label(root, text="OSNR calculation application", font="calibri 15").pack()
Label(root, text="Enter I/P dBm").pack(pady=3)
Entry(root, textvariable=pin).pack(pady=3)
Label(root, text="Enter Span Loss dB").pack(pady=3)
Entry(root, textvariable=spl).pack(pady=3)
Label(root, text="Enter Noise figure dB").pack(pady=3)
Entry(root, textvariable=nf).pack(pady=3)
Label(root, text="Enter Number of Span").pack(pady=3)
Entry(root, textvariable=span).pack(pady=3)


Button(root, text="Calculate OSNR", command=calc_osnr).pack(pady=7)
Entry(root, textvariable=osnr).pack(pady=3)
root.mainloop()