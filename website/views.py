from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Item, UserItemRelationship, User, Grades
from . import db
import sys

import json
from .forms import PurchaseItemForm, SellItemForm
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/tickets')
@login_required
def tickets():
    return render_template("tickets.html")

@views.route('/gradebook', methods=["GET", "POST"])
@login_required
def gradebook():
    if current_user.role == 0:  
        student_grades = Grades.query.filter_by(student_id=current_user.id).all()
        return render_template("gradebook.html", grades=student_grades, current_user=current_user)
    else:
        students = User.query.filter_by(role=0).all()
        if request.method == "POST":
            grade = request.form.get('grade')
            student_id = request.form.get('student_id')  
            subject = request.form.get('subject-select')
            new_grade = Grades(grade=grade, student_id=student_id, subject=subject, teacher_id=current_user.id)
            db.session.add(new_grade)
            db.session.commit()
        return render_template("gradebook.html", current_user=current_user, students=students)



@views.route('/calendar_to_do_list')
@login_required
def calendar_to_do_list():
    return render_template("to_do_list.html")

@views.route('/menu', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.budget >= (p_item_object.price):
                p_item_object.buy(current_user)
                new_relationship = UserItemRelationship(user_id = current_user.id, item_id = p_item_object.id)
                db.session.add(new_relationship)
                db.session.commit()
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}BGN", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}! You have {current_user.budget}BGN!", category='error')

        return redirect(url_for('views.market_page'))

    
    items = Item.query.filter_by()
    owned_items = Item.query.join(UserItemRelationship).join(User).filter(UserItemRelationship.user_id == current_user.id).all()
    return render_template('menu.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)

@views.route('/chat-with-teacher')
@login_required
def chat():
    return render_template('chat.html', current_user=current_user)

