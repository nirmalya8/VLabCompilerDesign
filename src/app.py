from flask import *  
from comment import check_comment
from identifier import check_identifier
from pattern_rules import check_pattern
from valoperator import operator_check
from lexical_analyzer import tokenize
app = Flask(__name__,static_folder='assets')  
  
@app.route('/')
def homepage_1():
    return render_template('index.html')

@app.route('/comment')
def comment_page():
    return render_template('comment.html')

@app.route('/sim1',methods = ['POST', 'GET'])  
def comment():  
   if request.method == 'POST':  
      inp = request.form['Input']
      result = check_comment(inp)   
      return render_template("sim_1.html",inp = inp,result = result)
   else: 
      return render_template("sim_1.html",inp="",result="")

@app.route('/identifier')
def val_identifier():
    return render_template('identifier.html')


@app.route('/sim2',methods = ['POST', 'GET'])  
def identifier():  
   if request.method == 'POST':  
      inp = request.form['Input']
      result = check_identifier(inp)
      print(result)   
      return render_template("sim_2.html",inp = inp,result = result)
   else: 
      return render_template("sim_2.html",inp="",result="")

@app.route('/stringPattern')
def stringPattern():
    return render_template('stringPattern.html')

@app.route('/sim3',methods = ['POST', 'GET'])
def pattern_check():
    if request.method == 'POST':  
      inp = request.form['Input']
      result = check_pattern(inp)
      print(result)   
      return render_template("sim_3.html",inp = inp,result = result)
    else: 
      return render_template("sim_3.html",inp="",result="") 


@app.route('/operator')
def operator():
    return render_template('operator.html')

@app.route('/sim4',methods = ['POST', 'GET'])
def check_operator():
    if request.method == 'POST':  
      inp = request.form['Input']
      result = operator_check(inp)
      print(result)   
      return render_template("sim_4.html",inp = inp,result = result)
    else: 
      return render_template("sim_4.html",inp="",result="")

@app.route('/lexical')
def lexical():
    return render_template('lexical.html')

@app.route('/sim5',methods = ['POST', 'GET'])
def tokens():
    if request.method == 'POST':  
      inp = request.form['Input']
      result = tokenize(inp)
      print(result)   
      return render_template("sim_5.html",inp = inp,result = result)
    else: 
      return render_template("sim_5.html",inp="",result="")

@app.route('/parse')
def parse():
    return render_template('parsetree.html')
 
     

if __name__ == '__main__':  
   app.run(debug = True)  