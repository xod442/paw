

'''
2016 wookieware.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "1.0.0"
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Prototype"

Flask script that manages strains and stores
'''
from flask import Blueprint, render_template, request, redirect, session, url_for, abort
import uuid
import os
from utilities.get_token import token
# rom test2.models import Creds

main_app = Blueprint('main_app', __name__)

@main_app.route('/main', methods=('GET', 'POST'))
@main_app.route('/', methods=('GET', 'POST'))
@main_app.route('/index', methods=('GET', 'POST'))
def main():
    ''' This section for any database preprocesses and capture login creds
    '''
    # Do any preprocessing here
    return render_template('main/main1.html')


@main_app.route('/main_select', methods=('GET', 'POST'))
def main_select():
    ''' This section to authenticate the user
    '''
    # Do any preprocessing here

    # Pull to submit form variables
    hostip=request.form['hostip']
    app_id=request.form['app_id']
    app_secret=request.form['app_secret']

    # Get token
    result = token(app_id,app_secret,hostip)
    # Check if 200
    if result[1] == 200:
        return render_template('main/main_leaf.html')
    else:
        error='FAILED_TO_LOGIN....TRY AGAIN!'
        return render_template('error/error.html', error=error)





@main_app.route('/help', methods=('GET', 'POST'))
def help():

    return render_template('main/help.html')
