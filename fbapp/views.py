from flask import Flask, render_template
from . import *


app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')
@app.route('/result/')
def result():
    description = """
      Toi, tu n'as pas peur d'être seul ! Les grands espaces et les aventures sont faits pour toi. D'ailleurs, Koh Lanta est ton émission préférée ! Bientôt tu partiras les cheveux au vent sur ton radeau. Tu es aussi un idéaliste chevronné. Quelle chance !
  """
    return render_template('result.html', user_name = "eder", user_image=url_for('static', filename='tmp/cover_111823112767411.jpg'),
                          description=description, blur=True)


if __name__ == "__main__":
    app.run(port=8012)