# Django CRUD 총정리

## 01. 기본 시작

pip install django

pip list

django-admin startporject ~

python manage.py startapp ~

> INSTALLED_APPS에 추가할 앱들 추가ㅊ

처음 만들면 app들에는 urls.py가 없고 프로젝트에는 view.py가 없다

### 1-1 variable

변수는 사용함 {{ variable }} + filter에 대해 공부

### 1- 2 상속 

setting.py > TEMPLATES 에 [BASE/DIR / '템플릿'] 필수

### 1-3 Url 재지정

각 앱의 아래에 urls.py를 만들어주고 from . import views

안의 각각의 ulr 지정.  Variable Routing을 활용하여 'hello/<str:name>/' 등과 같이 활용

원래의 함수에는 include 추가. name을 맨뒤에 추가하여 활용(url로 편하게 이동하기 위함)

app_name을 지정하여 함수 가기 편하게해줌 > ex) articles:index

### 1-4 migrate

python mange.py makemigrations

migrate



## 02. Model

artilces/models.py

```
class Article(models.Modle):
	title = models.CharFiedl(max_length=10)
	content = models.TextField()
	created_at = models.DataTimeField(auto_now_add=True)
	updated_at = models.DataTimeField(auto_now=True)
	
	def __str__(self):
		return self.title
```

Article.objects.all() = 다불러오기

## 03 CRUD

### 3 - 0 필요한 것들

Csrf > post요청시 필요함

### 3-1 Create

```
def create(request):
	title = request.POST.get('title')
	content = request.POST.get('content')
	
	aritcle = Article(title=title, content=content)
	article.save()
	return redirect('articles:index')
	
from action='{% url 'articles:create'%}' method='POST'
csrf token
```



### 3-2 Read

```
artilce = Article.objects.get(pk=1)
article = Article.objects.all()
```



### 3-3 update

```
article = Article.objects.get(pk=1)

article.tilte = 'byebye'
article.save()
```



### 3-4 delete

```
article = Article.objects.get(pk=1)
article.delete()
```

### 04. Admin

### 4-1 admin 생성

```
python manage.py createsuperuser
```

articles/admin.py

```
from .models import Article(추가작성)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title'...)
admin.site.register(Article)
```



## 05 Form

forms.py 생성

```
from django import forms

class ArticleForm(forms.Form):
	title = forms.CharField(max_length=10)
	content = forms.CharFile()

articles/views.py

def new(request):
	form = ArticleForm()
	context = {
		'form' : form
	}
	
form.as_p

```

## 06 ModelForm

```python
from django import forms
from .models import article

class ArticleForm(forms.ModelForm)

	class Meta:
        model = Article
        fields = '__all__'
        
# modelfrom 활용시
# articles/views.py

def create(request):
    if request.method == 'POST':
    	form = ArticleForm(request.POST)
    	if form.is_vaild():
        	article = form.save()
        	return redirect('article:detial', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' = form,
    }
    return render(request, 'articles/create,html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
       	return redirect('articles:index')
   return redirect('articles:detail', aritlce.pk)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        from = ArticleForm(request.POST, instance=article)
       	if from.is_valid():
            form.save()
            return redirect('articles:detial', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article,
    }
    retrun render(request, 'articles/update.html', context)
```

## 07 HTTP request

```python
from django.shortcuts import get_object_or_404()
from django.views.decorators.http import require_http_methods, require_POST

@require_http_mehtods(['GET','POST'])

def detail(request, pk):
    article = get_object_or_404(Article. pk=pk)

```

## 08 STATIC FILES

먼저 django.contrib.staticfiles가 installed_apps에 포함되어 있는지 확인

setting,py STATIC_URL 정의

```python
STATIC_ROOT = BASE_DIR / 'staticfiles'

python manage.py collecstatic

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE/DIR / 'static'
]
```

## 09 유저 업로드를 위한 정적 파일

```python
# modles.py 에 추가

class MyModel(models.Model):
    
    upload = models.FileFiled(upload_to='uploads/')
    
    upload = models.FileFiled(upload_to='uploads/%Y/%m/%d')
```

### 10

```

```

