from flask_api import FlaskAPI
from flask import request, render_template
import json

import re

app = FlaskAPI(__name__)


@app.route('/ban-list/', methods=['GET'])
def ban_list():
    if request.method == 'GET':
        return get_ban_list()


def get_ban_list():
    return get_list_from("blacklist.txt")


def get_list_from(file_name):
    ban_file = open(file_name)
    players = []
    for line in ban_file:
        comment = re.search(r'#.{1,} - ', line)[0][1:-3]
        reason = re.search(r' - .{1,}', line)[0][3:]
        obj = {'playerID': re.search(r'\d{17}', line)[0], 'comment': comment, 'reason': reason }
        players.append(obj)
    print(players)
    return json.dumps(players)


@app.route('/')
def home():
    return render_template('index.html', update_time=1500)


if __name__ == "__main__":
    app.run(debug=False)