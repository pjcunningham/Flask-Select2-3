# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2024, Paul Cunningham'

from flask_wtf import FlaskForm
from flask_select2_3.model.fields import AjaxSelectField, AjaxSelectMultipleField
from flask_select2_3.contrib.sqla.ajax import QueryAjaxModelLoader
from .models import db, Company


company_loader = QueryAjaxModelLoader(
    name='company',
    session=db.session,
    model=Company,
    fields=['name'],
    order_by=[Company.name.asc()],
    page_size=20,
    placeholder="Select a company"
)


class CompanyForm(FlaskForm):

    single_company = AjaxSelectField(
        loader=company_loader,
        label='Single Company',
        allow_blank=False
    )

    multiple_company = AjaxSelectMultipleField(
        loader=company_loader,
        label='Multiple Companies',
        allow_blank=False
    )

    single_company_allow_blank = AjaxSelectField(
        loader=company_loader,
        label='Single Company (blank allowed)',
        allow_blank=True,
    )
