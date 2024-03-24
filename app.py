from flask import Flask, render_template,request,redirect,url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

app.secret_key = '3280151'

# Authentication
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

# Open the Google Sheet
sheet = gc.open_by_key('1i2nI1P2LF6V9BXuii73hkj3W09JM7THSAdj4ETzY6VU')  # Replace with your sheet's key
worksheet = sheet.get_worksheet(0)  # Select the first worksheet

@app.route('/')
def hello():
   sno=worksheet.get_values("A2:A25")
   data = worksheet.get_values("A2:D25")
   return render_template("index.html" , sno=sno ,data=data)

@app.route('/sala01')
def admin():
    return render_template("admin.html")
 
@app.route('/change' , methods=['POST'])
def change():
   teamname=request.form["teamname"]
   score=request.form['score']
   btnval=request.form['btn']
   
   team_cells = {
    "A": "f2",
    "B": "f3",
    "C": "f4",
    "D":"f5",
    "E":"f6",
   "F": "f7",
   "G": "f8",
   "H": "f9",
   "I": "f10",
   "J": "f11",
   "K": "f12",
   "L": "f13",
   "M": "f14",
   "N": "f15",
   "O": "f16",
   "P": "f17",
   "Q": "f18",
   "R": "f19",
   "S": "f20",
   "T": "f21",
   "U": "f22",
   "V": "f23",
   "W": "f24",
   "X": "f25",
}
   try:
      scoreint=int(score)
      cell_reference = team_cells[teamname]
      score_value = int(worksheet.acell(cell_reference).value)
   except KeyError:
      return "Invalid team name"
   
   if btnval == "+":
      final = score_value + scoreint
   else:
      final = score_value - scoreint
      
   addcell=cell_reference[1:]
   addcell1=int(addcell)
   print(addcell1)
   worksheet.update_cell(addcell1,7, final)
   return redirect(url_for("admin"))
   
   
   # if teamname=="A" or teamname=="a":
   #    if btnval=="+":
   #       scoreint=int(score)
   #       score_value = worksheet.acell('f2').value
   #       score_value_int=int(score_value)
   #       final=score_value_int+scoreint
   #       worksheet.update_cell(2,6, final)
   #       return redirect(url_for("admin"))
   #    else:
   #       scoreint=int(score)
   #       score_value = worksheet.acell('f2').value
   #       score_value_int=int(score_value)
   #       final=score_value_int-scoreint
   #       worksheet.update_cell(2,6, final)
   #       return redirect(url_for("admin"))
      
   # elif teamname=="B" or teamname=="b":
   #    if btnval=="+":
   #       scoreint=int(score)
   #       score_value = worksheet.acell('f3').value
   #       score_value_int=int(score_value)
   #       final=score_value_int+scoreint
   #       worksheet.update_cell(3,6, final)
   #       return redirect(url_for("admin"))
   #    else:
   #       scoreint=int(score)
   #       score_value = worksheet.acell('f3').value
   #       score_value_int=int(score_value)
   #       final=score_value_int-scoreint
   #       worksheet.update_cell(3,6, final)
   #       return redirect(url_for("admin"))
      


   
if __name__ == '__main__':
    app.run(debug=True)