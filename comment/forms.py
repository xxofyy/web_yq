# -*- coding: UTF-8 -*-
# @Project -> File   ：website -> forms.py
# @IDE    ：PyCharm
# @Author ：YX
# @Date   ：2020/6/11 11:05

from django import forms
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(widget=CKEditorWidget())