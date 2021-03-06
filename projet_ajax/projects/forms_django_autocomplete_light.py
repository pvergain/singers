#!/usr/bin/python
# -*- coding: utf8 -*-
"""The project's forms.

"""

from django import forms

from .models import Project

from dal import autocomplete


class ProjectFormDjangoAutocomplete(forms.ModelForm):
    """https://django-autocomplete-light.readthedocs.io/en/master/tutorial.html"""
    class Meta:
        model = Project
        fields = ('__all__')
        widgets = {
            'champion': autocomplete.ModelSelect2(
                url='projects:api_get_users',
                attrs={
                    # Set some placeholder
                    'data-placeholder': 'Choose your champion',
                    # Only trigger autocompletion after 3 characters have been typed
                    'data-minimum-input-length': 1,
                }
            )
        }