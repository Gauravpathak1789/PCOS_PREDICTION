from flask import Flask, render_template, request, app, Response
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


applications = Flask(__name__)
app=applications
scaler=pickle.load(open("Model/scaler_pcos.pkl","rb"))
model=pickle.load(open("Model/pcos_log.pkl","rb"))


@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        Age=int(request.form.get("Age (yrs)"))
        BMI= float(request.form.get('BMI'))
        Cycle= int(request.form.get('Cycle(R/I)'))
        FSH= float(request.form.get('FSH(mIU/mL)'))
        AMH= float(request.form.get('AMH(ng/mL)'))
        LH= float(request.form.get('LH(mIU/mL)'))
        Waist_Hip_Ratio= float(request.form.get('Waist:Hip Ratio'))
        Follicle_No_L= float(request.form.get('Follicle No. (L)'))
        Follicle_No_R= float(request.form.get('Follicle No. (R)'))
        FSH_div_LH= float(request.form.get('FSH/LH'))
       



        new_data=scaler.transform([[Age,BMI,Cycle,FSH,AMH,LH,Waist_Hip_Ratio,Follicle_No_L,Follicle_No_R,FSH_div_LH]])
        predict=model.predict(new_data)
       
        if predict[0] ==1 :
            result = 'PCOS-YES'
        else:
            result ='NO-PCOS'
            
        return render_template('home.html',result=result[0:])

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")