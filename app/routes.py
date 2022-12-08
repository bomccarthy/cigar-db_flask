from app import app
from flask import render_template, request
from flask_login import current_user
from app.models import Cigars, Cigar_smdb, User
from .models import User
from flask_sqlalchemy import SQLAlchemy
from flask_jsonpify import jsonify

@app.route('/')
def homePage():
    users = User.query.all()

    return render_template('index.html', users=users)

@app.get('/api/cigars')
def getCigarAPI():
    cigars = Cigars.query.all()
    all_cigars = [cigar.to_dict() for cigar in cigars]
    return {
        'status': 'ok',
        'data': all_cigars,
        'total_results': len(all_cigars)
    }

@app.get('/api/cigars/<int:cigar_id>')
def getSingleCigerAPI(cigar_id):
    cigar = Cigars.query.get(cigar_id)
    if cigar:
        return {
            'status': 'ok',
            'data': cigar.to_dict()
        }
    return {
            'status': 'not ok',
            'message': 'That Cigar does not exist. Try again.'
    }

@app.get('/api/cigar_smdb')
def getCigar_smdbAPI():
    cigars = Cigar_smdb.query.all()
    all_cigars = [cigar.to_dict() for cigar in cigars]
    return {
        'status': 'ok',
        'data': all_cigars,
        'total_results': len(all_cigars)
    }

@app.route('/api/cigar_smdb/<int:page_num>')
def getCigar_smdbAPIperPage(page_num):
    cigars = Cigar_smdb.query.paginate(per_page=10, page=page_num, error_out=True)
    all_cigars = [cigar.to_dict() for cigar in cigars]
    return {
        'status': 'ok',
        'data': all_cigars,
        'total_results': len(all_cigars)
    }

@app.get('/api/cigars/cigar/<string:name>')
def filterCigarByName(cigar):
    cigar_filter = '%' + cigar + '%'
    print(cigar_filter)
    filtered_cigars = Cigars.query.filter(Cigars.cigar.ilike(cigar_filter)).all()
    new_cigars = [filtered_cigar.to_dict() for filtered_cigar in filtered_cigars]
    return {
        'status': 'ok',
        'data': new_cigars,
        'total_results': len(new_cigars)
    }

@app.get('/api/cigars/shape/<string:shape>')
def filterCigarByShape(shape):
    cigar_filter = '%' + shape + '%'
    filtered_cigars = Cigars.query.filter(Cigars.shape.ilike(cigar_filter)).all()
    new_cigars = [filtered_cigar.to_dict() for filtered_cigar in filtered_cigars]
    return {
        'status': 'ok',
        'data': new_cigars,
        'total_results': len(new_cigars)
    }

@app.get('/api/cigars/search')
def filterCigarByLength():
    lst_args = []
    args = request.args
    print (args) # For debugging
    for a in args:
        print(a)
        lst_args.append(a)
    print(lst_args)
    no2 = args[lst_args[0]]
    print(no2)
    