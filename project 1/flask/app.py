from datetime import datetime
from random import choice, randint
import string
from flask import Flask
from flask import render_template, request, flash, redirect, url_for
from db import initialize_db

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shortlink.sqlite3'
db = initialize_db(app)

from models import ShortUrls

with app.app_context():
    db.create_all()


def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        if not url:
            return redirect(url_for('index'))

        short_id = generate_short_id(8)

        new_link = ShortUrls(original_url=url, short_id=short_id, created_at=datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/random')
def random():
    link = ShortUrls.query.all()
    if link:
        return redirect(link[randint(0, len(link)-1)].original_url)
    else:
        return redirect(url_for('index'))

@app.route('/<short_id>')
def redirect_url(short_id):
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        return redirect(link.original_url)
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()