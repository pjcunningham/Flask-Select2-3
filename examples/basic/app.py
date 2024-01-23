# coding: utf-8
from __future__ import unicode_literals

__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2018, Paul Cunningham'

from flask import Flask, render_template, flash
from faker import Faker
from flask_bootstrap import Bootstrap
from flask_select2_3 import Select2
from .models import db, Company
from .forms import company_loader, CompanyForm


app = Flask(__name__)
# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
db.init_app(app)
select2 = Select2()

select2.init_app(app)
select2.add_loader(loader=company_loader)


# Flask views
@app.route('/', methods=['GET', 'POST'])
def index():
    _form = CompanyForm()

    if _form.validate_on_submit():

        flash(
            f"Single Company selected : {_form.single_company.data.name}",
            category='success'
        )

        flash(
            f"Multiple Companies selected : {','.join(c.name for c in _form.multiple_company.data)}",
            category='success'
        )

        if _form.single_company_allow_blank.data:

            flash(
                f"Single Company (blank allowed) selected : {_form.single_company.data.name}",
                category='success'
            )

        else:

            flash(
                "Single Company (blank allowed) nothing selected.",
                category='danger'
            )

    return render_template('index.html', form=_form)


@app.cli.command("build-sample-db")
def build_sample_db():

    db.drop_all()
    db.create_all()

    fake = Faker()

    # add 2000 companies
    db.session.bulk_insert_mappings(
        Company,
        [
            dict(
                name=fake.company(),
                description=fake.paragraph(nb_sentences=fake.random.randint(1, 10))
            )
            for _ in range(2000)
        ]
    )

    db.session.commit()

