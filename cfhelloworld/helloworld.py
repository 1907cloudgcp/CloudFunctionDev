from flask import  Blueprint
hw = Blueprint('hw', __name__)


@hw.route('/', )
def hello_world():

    return jsonify({'Folder':'world'})

from flask import jsonify