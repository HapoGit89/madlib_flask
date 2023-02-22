from stories import *

from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def show_form():
    return render_template('home.html', words= story.prompts)


@app.route('/story')
def show_story():
    answers = {x:y for (x,y) in request.args.items()}
    story_text = story.generate(answers)
    return render_template('story.html', story= story_text)