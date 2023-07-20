import tkinter

#window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=250)
window.config(padx=20, pady=20)

def bmiCalculator():
    weight = entryWeight.get()
    height = entryHeight.get()

    if weight == "" or height == "":
        resultLabel.config(text="Enter both weight and height!")
    else:
        try:
            bmi = int(weight) / (int(height)/100)**2
            yourResult = resultBmi(bmi)
            resultLabel.config(text=yourResult)
        except:
            resultLabel.config(text="Just enter the number!")

def resultBmi(bmi):
    yourResult = f"Your BMI is {round(bmi,2)} You are "
    if bmi <= 18.5:
        yourResult += "underweight."
    elif 18.5 < bmi <= 24.9:
        yourResult += "normal."
    elif 25 <= bmi <= 29.9:
        yourResult += "overweight."
    elif 30 <= bmi <= 34.9:
        yourResult += "obese"
    else:
        yourResult+= "extremly obese."
    return yourResult

#interface
weightLabel = tkinter.Label(text="Enter Your Weight(kg)", font=("Arial", 9, "normal"))
weightLabel.config(padx=5,pady=5)
weightLabel.pack()

entryWeight = tkinter.Entry(width=10)
entryWeight.pack()

heightLabel = tkinter.Label(text="Enter Your Height(cm)", font=("Arial", 9, "normal"))
heightLabel.config(padx=5, pady=5)
heightLabel.pack()

entryHeight = tkinter.Entry(width=10)
entryHeight.pack()

calculateButton = tkinter.Button(text="Calculate", command=bmiCalculator)
calculateButton.pack()

resultLabel = tkinter.Label()
resultLabel.pack()

window.mainloop()