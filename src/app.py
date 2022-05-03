from flask import *  
from comment import check_comment
from identifier import check_identifier
from pattern_rules import check_pattern
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
# EXPERIMENT 2: CHECKING IDENTIFIER NAMES



# EXPERIMENT 2: LEXICAL ANALYZER

@app.route('/aim3')  
def aim_3():  
    title = "Lexical Analyser"
    aim="Break code into tokens"
    return render_template('aim.html',title = title,aim=aim)  
 
     

if __name__ == '__main__':  
   app.run(debug = True)  