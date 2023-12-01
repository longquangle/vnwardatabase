from flask import render_template, request
from vnwardatabase.models import Data
from vnwardatabase.forms import SearchBar
from vnwardatabase import app

dbheader = ['ID', 'Branch', 'Rank', 'Grade', 'First', 'Middle', \
            'Last', 'City', 'State', 'Panel', 'Birth', 'Start', \
            'Incident', 'Casualty', 'Age', 'Location', 'Remains',\
            'Type', 'Reason', 'Details']

# global variable to keep track of the current query, only update when either search or reset
current_data = []

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])

def home():
    searchbar = SearchBar()
    if len(current_data) == 0:
        current_data.append(Data.query)
    if searchbar.validate_on_submit():
        if searchbar.submit.data:
            current_data[0] = Data.query.filter(Data.first.contains(searchbar.first.data) & 
                                    Data.middle.contains(searchbar.middle.data) & 
                                    Data.last.contains(searchbar.last.data) & 
                                    Data.city.contains(searchbar.city.data) & 
                                    Data.state.contains(searchbar.state.data))
            data = current_data[0].paginate(page=1, per_page=10)
        elif searchbar.reset.data:
            current_data[0] = Data.query
            data = current_data[0].paginate(page=1, per_page=10)
    else:
        page = request.args.get('page', 1, type=int)
        data = current_data[0].paginate(page=page, per_page=10)
    return render_template('home.html', 
                        title='Home', 
                        dbheader=dbheader, 
                        searchbar=searchbar, 
                        data=data, 
                        data_count=current_data[0].count())

@app.route("/data")
def data():
    return render_template('data.html', title='Data')