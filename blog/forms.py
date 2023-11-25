from django import forms
from .models import PostModel

class PostForm(forms.Form):
    title = forms.CharField(label="Tieu de", max_length=100, required=True)
    summary = forms.CharField(label="Tom tat",max_length=500)
    content = forms.CharField(label="Noi dung",widget=forms.Textarea)

    def save(self):
        model = PostModel(
            title = self.cleaned_data["title"],
            summary = self.cleaned_data["summary"],
            content = self.cleaned_data["content"],
        ) 
        model.save()
        
        
class PostModelForm(forms.ModelForm):
    class Meta: 
        model = PostModel
        fields = ["title","summary","content"]
    
