from flask import Blueprint,request
from werkzeug.datastructures import CombinedMultiDict, MultiDict
from app.tools.CORS import crossdomain
from app.tools.Toolkit import respond
import requests
# Setting up access to this controller under '<OUR_AWESOME_DOMAIN>/data/*'
mod_api = Blueprint('data', __name__, url_prefix='/data')




'''
    The base method for this controller does not need to do anything.
    A list of methods is possible, but might make us vulnerable.
    So we just do something fun for the time being.
'''

@mod_api.route('/',methods=['POST','GET'])
@crossdomain(origin='*')
def base():
    response = {
                'message': "We don't make coffee. Try something else. How about an XKCD instead?",
                'alternative': 'https://c.xkcd.com/random/comic/',
                'status': "It's complicated",
                'http_status': 418
               }
    # Returning with the joke 418 status code, because why not
    return respond(response)





