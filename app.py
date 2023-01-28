from flask import Flask,render_template


FAI=Flask(__name__)
@FAI.route('/hai')
def hai():
    return 'this is my first flask project'



@FAI.route('/wish/<name>')
def wish(name):
    return f'Hello how r u MR/MS {name}'

@FAI.route('/first')
def first():
    return render_template('first.html')
if __name__=='__main__':
    FAI.run(debug=True, host='192.168.105.140',port=5001)

