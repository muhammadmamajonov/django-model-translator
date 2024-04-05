
# Django Model Translator —  Documentation

django-model-translator **django model**lardagi bir nechta tilli **field**larni tarjima qilish uchun vosita <br>
django-model-translator a tool for translating multilingual **fields** in **django models**

## Installation

```sh
pip install django-model-translator
```


## Using
#### Sozlash / Settings
O'rnatib bo'lgandan keyin **settings.py** faylidagi **INSTALLED_APPS** listiga qo'shishingiz kerak <br>
After installation you need to add to **INSTALLED_APPS** list in **settings.py** file

```py
INSTALLED_APPS = [
    ...
    'django_model_translator'
]
```
**INSTALLED_APPS**ga qo'shib bo'lganningizdan keyin settings.py fayliga quyidagilarni kiritishingiz kerak <br>
After adding to **INSTALLED_APPS** you need to add the following to your settings.py file
```py
DEFAULT_LANGUAGE = 'uz'
ALL_LANGUAGES = ['uz', 'en']
```
**DEFAULT_LANGUAGE** —  asosiy til, agar mavjud bo'lmagan til berilsa modellar shu tilga tarjima qilinadi <br>
**DEFAULT_LANGUAGE** — default language, if a non-existent language is given, the models will be translated into that language <br>
**ALL_LANGUAGES** — Mavjud bo'lgan barcha tillar ro'yxati <br>
**ALL_LANGUAGES** — List of all available languages

#### Model yozish / Model writing
**models.py** faylidagi modellaringizdagi tarjima qilinadigan **field**larni quyidagicha yozishingiz kerak <br>
You should write the translatable **fields** in your models in the **models.py** file as follows
```py
class Book(models.Model):
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    desc_uz = models.TextField()
    desc_en = models.TextField()
```

#### Serializer yozish / Writing a serializer
```py
from main.models import Book
from django_model_translator import TranslatableModelSerializer

class BookSerializer(TranslatableModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        translatable_fields = ['name', 'desc']
```
**translatable_fields**ga fieldlarning asos nomlarini yozasiz, bizning modelimizda **'name'** va **'desc'** degan ikkita tarjima qilinadigan ma'lumot bor. <br>
In **translatable_fields** you write the base names of the fields, in our model there are two translatable data **'name'** and **'desc'**.
### Endi bu serializerni bemalol ishlatishingiz mumkin
### Now you can use this serializer with ease