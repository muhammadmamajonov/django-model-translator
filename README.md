
## Django Model Translator -- Foydalanish qo'llanmasi

install django-model-translator **django model**lardagi bir nechta tilli **field**larni tarjima qilish uchun vosita

## Installation

```sh
pip install django-model-translator
```


## Using
#### Sozlash
O'rnatib bo'lgandan keyin **settings.py** faylidagi **INSTALLED_APPS** listiga qo'shishingiz kerak

```py
INSTALLED_APPS = [
    ...
    'django_model_translator'
]
```
**INSTALLED_APPS**ga qo'shib bo'lganningizdan keyin settings.py fayliga quyidagilarni kiritishingiz kerak
```py
DEFAULT_LANGUAGE = 'uz'
ALL_LANGUAGES = ['uz', 'en']
```
 **DEFAULT_LANGUAGE** --  asosiy til, agar mavjud bo'lmagan til berilsa shu tilga tarjima qilinadi \n
 **ALL_LANGUAGES** -- Mavjud bo'lgan barcha tillar ro'yxati

#### Model yozish
**models.py** faylidagi modellaringizdagi tarjima qilinadigan **field**larni quyidagicha yozishingiz kerak
```py
class Book(models.Model):
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    desc_uz = models.TextField()
    desc_en = models.TextField()
```

#### Serializer yozish
```py
from main.models import Book
from django_model_translator import TranslatableModelSerializer

class BookSerializer(TranslatableModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        translatable_fields = ['name', 'desc']
```
**translatable_fields**ga fieldlarning asos nomlarini yozasiz, bizning modelimizda **'name'** va **'desc'** degan ikkita tarjima qilinadigan ma'lumot bor.

### Endi bu serializerni bemalol ishlatishingiz mumkin