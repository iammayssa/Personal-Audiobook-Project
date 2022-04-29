import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title('Diabetes Predictions')

#Column 1
Preg=ttk.Label(win,text="Preg")
Preg.grid(row=0,column=0,sticky=tk.W)
Preg_var=tk.StringVar()
Preg_entrybox=ttk.Entry(win,width=16,textvariable=Preg_var)
Preg_entrybox.grid(row=0,column=1)
#Column 2
Plas=ttk.Label(win,text="Plas")
Plas.grid(row=1,column=0,sticky=tk.W)
Plas_var=tk.StringVar()
Plas_entrybox=ttk.Entry(win,width=16,textvariable=Plas_var)
Plas_entrybox.grid(row=1,column=1)
#Column 3
Pres=ttk.Label(win,text="Pres")
Pres.grid(row=2,column=0,sticky=tk.W)
Pres_var=tk.StringVar()
Pres_entrybox=ttk.Entry(win,width=16,textvariable=Pres_var)
Pres_entrybox.grid(row=2,column=1)
#Column 4
skin=ttk.Label(win,text="skin")
skin.grid(row=3,column=0,sticky=tk.W)
skin_var=tk.StringVar()
skin_entrybox=ttk.Entry(win,width=16,textvariable=skin_var)
skin_entrybox.grid(row=3,column=1)
#Column 5
test=ttk.Label(win,text="test")
test.grid(row=4,column=0,sticky=tk.W)
test_var=tk.StringVar()
test_entrybox=ttk.Entry(win,width=16,textvariable=test_var)
test_entrybox.grid(row=4,column=1)
#Column 6
mass=ttk.Label(win,text="mass")
mass.grid(row=5,column=0,sticky=tk.W)
mass_var=tk.StringVar()
mass_entrybox=ttk.Entry(win,width=16,textvariable=mass_var)
mass_entrybox.grid(row=5,column=1)
#Column 7
pedi=ttk.Label(win,text="pedi")
pedi.grid(row=6,column=0,sticky=tk.W)
pedi_var=tk.StringVar()
pedi_entrybox=ttk.Entry(win,width=16,textvariable=pedi_var)
pedi_entrybox.grid(row=6,column=1)
#Column 8
age=ttk.Label(win,text="age")
age.grid(row=7,column=0,sticky=tk.W)
age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=7,column=1)

import pandas as pd
DF = pd.DataFrame()
def action():
    global DB
    import pandas as pd
    DF = pd.DataFrame(columns=['Preg','Plas','Pres','skin','test','mass','pedi','age'])
    PREG=Preg_var.get()
    DF.loc[0,'Preg']=PREG
    PLAS=Plas_var.get()
    DF.loc[0,'Plas']=PLAS
    PRES=Pres_var.get()
    DF.loc[0,'Pres']=PRES
    SKIN=skin_var.get()
    DF.loc[0,'skin']=SKIN
    TEST=test_var.get()
    DF.loc[0,'test']=TEST
    MASS=mass_var.get()
    DF.loc[0,'mass']=MASS
    PEDI=pedi_var.get()
    DF.loc[0,'pedi']=PEDI
    AGE=age_var.get()
    DF.loc[0,'age']=AGE
print(DF.shape)
DB=DF

def Output():
    DB["Preg"] = pd.to_numeric(DB["Preg"])
    DB["Plas"] = pd.to_numeric(DB["Plas"])
    DB["Pres"] = pd.to_numeric(DB["Pres"])
    DB["skin"] = pd.to_numeric(DB["skin"])
    DB["test"] = pd.to_numeric(DB["test"])
    DB["mass"] = pd.to_numeric(DB["mass"])
    DB["pedi"] = pd.to_numeric(DB["pedi"])
    DB["age"] = pd.to_numeric(DB["age"])

output=Model.predict(DB) ## This is for a classification task
    ##### Add output here
    result = ##synthesized voice

 Predict_entrybox=ttk.Entry(win,width=16)
    Predict_entrybox.grid(row=20,column=1)
    Predict_entrybox.insert(1,## synthesized voice)
Predict_button=ttk.Button(win,text="Predict",command=Output)
Predict_button.grid(row=20,column=0)
win.mainloop()

