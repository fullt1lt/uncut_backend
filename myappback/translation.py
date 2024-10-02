from modeltranslation.translator import translator, TranslationOptions
from .models import CategoryActivity, ProcedureActivity


class CategoryActivityTranslationOptions(TranslationOptions):
    fields = ('title',) 


class ProcedureActivityTranslationOptions(TranslationOptions):
    fields = ('text',)
    
    

translator.register(ProcedureActivity, ProcedureActivityTranslationOptions)
translator.register(CategoryActivity, CategoryActivityTranslationOptions)
