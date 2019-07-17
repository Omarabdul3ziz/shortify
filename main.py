import module, sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)


conn = conn = sqlite3.connect('module.db', check_same_thread=False)
c = conn.cursor()


@app.route('/', methods=['GET', 'POST'])
@app.route('/input', methods=['GET', 'POST'])
def get_link():
    return render_template('input.html')


@app.route('/output', methods=['GET', 'POST'])
def give_link():
    #print(str(request.form))
    #return ""
    long_url = request.args.get('long_url')
    print(long_url)
    mini = module.shortify(long_url)
    maxi = module.longify(mini)
    return render_template('output.html',long_url= 'https://'+''.join(maxi) ,short_url = mini )