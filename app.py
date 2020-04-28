from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

def write_to_csv(data):
    with open('database2.csv', mode='a', newline='') as database2:
        Email = data['email']
        Subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|' ,quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([Email,Subject,message])

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        Email = data['email']
        Subject = data['subject']
        message = data['message']
        file = database.write(f'\n{Email},{Subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()

        write_to_csv(data)
        return redirect('/foo')
    else:
        return "something went wrong"

@app.route('/foo')
def foo():

    return render_template("thankyou.html")
