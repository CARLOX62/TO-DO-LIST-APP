from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task
from functools import wraps
from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

tasks_bp = Blueprint('tasks', __name__, url_prefix='')

# ✅ Proper login_required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in first.", "warning")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    due_date = DateField('Due Date', format='%Y-%m-%d')
    priority = SelectField('Priority', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Medium')
    category = SelectField('Category', choices=[('Work', 'Work'), ('Study', 'Study'), ('Personal', 'Personal'), ('Other', 'Other')], default='Personal')
    submit = SubmitField('Add Task')

# ✅ Protected routes

@tasks_bp.route('/')
@tasks_bp.route('/tasks')
@login_required
def view_tasks():
    user_id = session['user_id']
    search = request.args.get('search', '')
    status_filter = request.args.get('status', '')
    priority_filter = request.args.get('priority', '')
    category_filter = request.args.get('category', '')

    query = Task.query.filter_by(user_id=user_id)

    if search:
        query = query.filter(Task.title.contains(search))
    if status_filter:
        query = query.filter_by(status=status_filter)
    if priority_filter:
        query = query.filter_by(priority=priority_filter)
    if category_filter:
        query = query.filter_by(category=category_filter)

    tasks = query.all()

    # Today's focus: tasks due today or overdue
    today = datetime.utcnow().date()
    todays_tasks = [t for t in tasks if t.due_date and t.due_date.date() <= today and t.status != 'Done']

    # Statistics
    done_this_week = len([t for t in tasks if t.status == 'Done' and t.created_at >= datetime.utcnow() - timedelta(days=7)])

    form = TaskForm()  # Create form instance for CSRF token

    return render_template('tasks.html', tasks=tasks, todays_tasks=todays_tasks, done_this_week=done_this_week, search=search, status_filter=status_filter, priority_filter=priority_filter, category_filter=category_filter, form=form, csrf_token=form.csrf_token.current_token)


@tasks_bp.route('/add', methods=['POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        user_id = session['user_id']
        t = Task(
            title=form.title.data,
            user_id=user_id,
            due_date=form.due_date.data,
            priority=form.priority.data,
            category=form.category.data
        )
        db.session.add(t)
        db.session.commit()
        flash('Task added', 'success')
    else:
        flash('Task title cannot be empty', 'danger')
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=session['user_id']).first_or_404()
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.due_date = form.due_date.data
        task.priority = form.priority.data
        task.category = form.category.data
        db.session.commit()
        flash('Task updated', 'success')
        return redirect(url_for('tasks.view_tasks'))
    return render_template('edit_task.html', form=form, task=task)


@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=session['user_id']).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted', 'info')
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
@login_required
def toggle_status(task_id):
    task = Task.query.filter_by(id=task_id, user_id=session['user_id']).first()
    if task:
        if task.status == 'Pending':
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Done"
        else:
            task.status = 'Pending'
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/clear', methods=['POST'])
@login_required
def clear_tasks():
    Task.query.filter_by(user_id=session['user_id']).delete()
    db.session.commit()
    flash('All your tasks cleared!', 'info')
    return redirect(url_for('tasks.view_tasks'))
