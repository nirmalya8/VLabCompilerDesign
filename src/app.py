from flask import *  
from comment import check_comment
from identifier import check_identifier
app = Flask(__name__)  
  
# @app.route('/')
def homepage_1():
    ''' Homepage '''
    pass

# EXPERIMENT 1: Checking Comments
@app.route('/aim1')  
def aim_1():
    return render_template('aim_1.html')#,title = title,aim = aim)  

@app.route('/theory1')
def theory_1():
    pass

@app.route('/procedure1')
def procedure_1():
    pass

@app.route('/sim1',methods = ['POST', 'GET'])  
def comment():  
   if request.method == 'POST':  
      inp = request.form['Input']
      result = check_comment(inp)   
      return render_template("sim_1.html",inp = inp,result = result)
   else: 
      return render_template("sim_1.html",inp="",result="")

# EXPERIMENT 2: CHECKING IDENTIFIER NAMES


@app.route('/aim2')  
def aim_2():  
    aim= "To check for valid identifiers"
    title =  "Check Identifier"
    return render_template('aim.html',title = title,aim= aim)   

@app.route('/theory2')
def theory_2():
    pass
    return ""

@app.route('/procedure2')
def procedure_2():
    pass
    return ""

@app.route('/sim2',methods = ['POST', 'GET'])  
def identifier():  
   if request.method == 'POST':  
      inp = request.form['Input']
      result = check_identifier(inp)
      print(result)   
      return render_template("sim_2.html",inp = inp,result = result)
   else: 
      return render_template("sim_2.html",inp="",result="") 


# EXPERIMENT 2: LEXICAL ANALYZER

@app.route('/aim3')  
def aim_3():  
    title = "Lexical Analyser"
    aim="Break code into tokens"
    return render_template('aim.html',title = title,aim=aim)  
 
     

if __name__ == '__main__':  
   app.run(debug = True)  