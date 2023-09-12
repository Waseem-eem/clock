from flask import  Flask , render_template
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def home():
    now = datetime.now()
    current_time = now.strftime("%H: %M :%S")
    current_date = now.strftime("%D")
    current_day = now.strftime("%A")
    return render_template("index.html",time=current_time, date=current_date, day=current_day)

now = datetime.now()
current_time = now.strftime("%H: %M :%S")
if __name__ == "__main__":
    app.run(debug=True)

