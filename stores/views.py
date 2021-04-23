
'''
 April 2018 wookieware.

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

Leaf - Graphical Ansible Workbench - stores manager - views
'''
#
'''
TODO: Fix the upload to look like template2
'''
#
#
from flask import Blueprint, render_template, request, redirect, session, url_for, abort, flash
import requests
import json


stores_app = Blueprint('stores_app', __name__)

@stores_app.route('/new', methods=('GET', 'POST'))
def new():
    """
    Adds a new stores to the stores database it offers user a window to type in a new stores.
    :param GET: The function returns a textbox to add new stores
    :param POST: The function will save the new stores to the database
    :return:GET a textbox, POST a database success/fail indication
    :rtype: Jinja template
    """

    return render_template('stores/newstore.html')

@stores_app.route('/list', methods=('GET', 'POST'))
def list():
    """
    Creates a list of all the storess in the stores database.
    :param GET: The function returns a list of storess
    :return:GET returns a list of storess.
    :rtype: Python Dictionary
    """
    from utilities.get_token import token
    stores='None'
    app_id='sample'
    app_secret='test'
    hostip='10.132.0.18'

    get_token = token(app_id,app_secret,hostip)
    token = get_token[0]

    # headers
    headers = {"Content-Type":"application/json", "X-APP-ID":app_id, "X-APP-TOKEN":token}

    # URL for requesting token
    # store_url = 'http://10.132.0.18:8088/stores/'
    store_url = 'http://'+hostip+':8088/stores/'

    # Make request
    stores = requests.get(store_url, headers=headers)
    stores = json.loads(stores.text)
    stores = stores['stores']

    print(stores)
    return render_template('stores/storelist.html', stores=stores)

@stores_app.route('/edit', methods=('GET', 'POST'))
def edit():
    """
    Select a stores by name and edit it's contents.
    :param GET: The function returns a list of stores names to a selector
    :param POST: The function displays the contents of the stores in a textbox
    :return:GET returns a list of stores names, POST presents stores details.
    :rtype: Jinja template
    """
    stores='None'
    return render_template('stores/storeseditselect.html', stores=stores)


@stores_app.route('/delete', methods=('GET', 'POST'))
def delete():
    """
    Delete a stores by name.
    :param GET: The function returns a list of stores names to a selector
    :param POST: The function displays the contents of the stores in a textbox
    :return:GET offers selection list, POST success or fail of the database delete
    :rtype: Jinja template
    """
    stores='None'
    return render_template('stores/storesdelete.html', stores=stores)

@stores_app.route('/bulk', methods=('GET', 'POST'))
def bulk():
    """
    Upload a stores from the users computer.
    :param GET: The function returns a list of stores names to a selector
    :param POST: The function displays the contents of the stores in a textbox
    :return:Get presents user with a Choose file button, POST uploads file to database
    :rtype: Jinja template
    """

    # Return file chooser
    return render_template('stores/storesupload.html')

@stores_app.route('/copy', methods=('GET', 'POST'))
def copy():
    """
    Copy a stores from the users computer.
    :param GET: The function returns a list of stores names to a selector
    :param POST: The function copies the selected stores to a new db record
    :return:Get presents user with a Choose file button, POST copies file to database
    :rtype: Jinja template
    """
    stores='None'
    return render_template('stores/storescopy.html', stores=stores)
