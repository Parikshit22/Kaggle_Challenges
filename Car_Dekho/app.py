from flask import Flask,render_template,request
import model
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def action():
    Year = int(request.form['Year'])
    Present_Price=float(request.form['Present_Price'])
    Kms_Driven=int(request.form['Kms_Driven'])
    Owner=int(request.form['Owner'])
    Fuel_Type=request.form['Fuel_Type']
    if(Fuel_Type=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif(Fuel_Type=='Diesel'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    else:
 	    Fuel_Type_Petrol=0
 	    Fuel_Type_Diesel=0
    Year=2020-Year
    Seller_Type_Individual=request.form['Seller_Type_Individual']
    if(Seller_Type_Individual=='Individual'):
 	    Seller_Type_Individual=1
    else:
 	    Seller_Type_Individual=0	
    Transmission_Mannual=request.form['Transmission_Mannual']
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0
    int_val = [Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel,Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]
    int_val = [int(x) for x in int_val]
    result = model.predict(int_val)
    return render_template('index.html',prediction_test = f"The Price of car would be {result}")


if __name__ == "__main__":
	app.run(debug = True)