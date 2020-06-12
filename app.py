from flask_api import FlaskAPI
from flask import request
import re

app = FlaskAPI(__name__)


@app.route('/ban-list/', methods=['GET'])
def ban_list():
    if request.method == 'GET':
        return get_ban_list()


def get_ban_list():
    return get_list_from("blacklist.txt")


@app.route('/admin-list/', methods=['GET'])
def admin_list():
    if request.method == 'GET':
        return get_admins_list()


def get_admins_list():
    return get_list_from("mods.txt")


def get_list_from(file_name):
    ban_file = open(file_name)
    players = []
    for line in ban_file:
        obj = {'playerID': re.search(r'\d{17}', line)[0], 'comment': re.search(r'#.{1,}', line)[0][1:]}
        players.append(obj)
    print(players)
    return players



if __name__ == "__main__":
    app.run(debug=False)