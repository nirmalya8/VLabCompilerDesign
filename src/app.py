from flask import *  
from comment import check_comment
from identifier import check_identifier
app = Flask(__name__)  
  
@app.route('/aim1')  
def aim_1():
    aim = "To check for comments"
    title = "Check Comment"
    return render_template('aim.html',title = title,aim = aim)  

@app.route('/aim2')  
def aim_2():  
    aim= "To check for valid identifiers"
    title =  "Check Identifier"
    return render_template('aim.html',title = title,aim= aim)   

@app.route('/aim3')  
def aim_3():  
    title = "Lexical Analyser"
    aim="Break code into tokens"
    return render_template('aim.html',title = title,aim=aim)  
 
@app.route('/sim1',methods = ['POST', 'GET'])  
def comment():  
   if request.method == 'POST':  
      result = request.form['Input']
      result = check_comment(result)   
      return render_template("simulation-page.html",result = result)
   else: 
      return render_template("simulation-page.html",result="")    

if __name__ == '__main__':  
   app.run(debug = True)  