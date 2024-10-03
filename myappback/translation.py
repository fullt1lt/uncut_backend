from modeltranslation.translator import translator, TranslationOptions
from .models import CategoryActivity, Doctors, ProcedureActivity


class CategoryActivityTranslationOptions(TranslationOptions):
    fields = ('title',) 


class ProcedureActivityTranslationOptions(TranslationOptions):
    fields = ('text',)
    
    
class DoctorsTranslationOptions(TranslationOptions):
    fields = ('specialization', 'name', 'about_myself', 'information',
            'specialty', 'education', 'experience', 'work_method', 'work_directions', 'skills',
            'professional_development', 'additional_professional_activity')
    
    

translator.register(ProcedureActivity, ProcedureActivityTranslationOptions)
translator.register(CategoryActivity, CategoryActivityTranslationOptions)
translator.register(Doctors, DoctorsTranslationOptions)
