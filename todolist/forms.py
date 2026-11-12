from django import forms


class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45, 
        widget=forms.TextInput(
            attrs={'id' : 'new-todo', 'placeholder' : 'Введи что надо сделать', 'name' : 'title', 'autocomplete' : 'off', 'type' : 'text'}
        )
    )