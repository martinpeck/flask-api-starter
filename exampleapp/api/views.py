from . import api

@api.route('/', methods=['GET'])
def index():

    return {'hello': 'world'}

@api.route('/test', methods=['GET'])
def test():

    return {'hello': 'testing'}