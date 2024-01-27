from django.forms import ModelForm
from .models import Group, Note


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']

# https://www.letscodemore.com/blog/how-to-add-class-and-other-atrributes-to-form-fields-in-django/
class NoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs['class'] = 'note-form-input'
        self.fields['title'].widget.attrs['placeholder'] = 'Note title...'
        self.fields['text'].widget.attrs['class'] = 'note-form-input note-form-input_text'
        self.fields['text'].widget.attrs['placeholder'] = 'Add text...'
        self.fields['group'].widget.attrs['class'] = 'note-form-input note-form-input_dropdown'

    class Meta: 
        model = Note
        fields = '__all__'