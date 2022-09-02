from datetime import datetime

from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

##Solicitud de info para poner en HTML de check-out
@app.route('/checkout', methods=['POST'])         
def checkout():
    apple = request.form ['apple']
    strawberry = request.form['strawberry']
    blackberry = request.form['blackberry']
    raspberry = request.form['raspberry']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student = request.form['student_id']
    total = int(apple)+ int(strawberry) + int(blackberry) + int(raspberry)  ##suma total de productos
    today_date = datetime.now()
    date = today_date.strftime("%m/%d/%Y, %H:%M")
    print(f"Cobrando a {first_name} {last_name} por {total} frutas")
    return render_template("checkout.html", apple = apple, strawberry = strawberry, blackberry = blackberry, raspberry = raspberry, first_name = first_name, last_name = last_name, student = student, total = total, date = date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    