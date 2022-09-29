from importlib.metadata import requires
from django import forms
from django.forms import ModelForm

from projeto import settings

from .models import Curriculo
from .models import Endereco
from .models import Telefone
from .models import Link
from .models import Escolaridade
from .models import Historico
from .models import Curso
from .models import Aplicacao

from .models import Vaga

# "This class is a subclass of the DateInput class, and it overrides the input_type attribute to be
# 'date' instead of 'text'."
# 
# Now, let's use this new class in our form
class DateInput(forms.DateInput):
    input_type = 'date'

# "This is a form that has a single field, name, which is a CharField with a maximum length of 100
# characters."
# 
# The first argument to a Field class is required and is the field's label (a string). The label will
# be displayed to the user in a manner appropriate to the field type. For example, in a form rendered
# as HTML, the label will be wrapped in a <label> tag
class NameForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)

# I want to create a form based on the Curriculo model, and I want to exclude all fields from the
# form.
class CurriculoForm(ModelForm):
    class Meta:
        model = Curriculo
        exclude = []

# "I want to create a form based on the Endereco model, and I want to exclude all fields from the
# form."
# 
# The exclude list is a list of fields that you don't want to include in the form. In this case, we
# want to include all fields, so we leave the list empty
class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        exclude = []

# "This is a form that will be used to create or update a Telefone object."
# 
# The Meta class is used to tell Django which model should be used to create this form (model =
# Telefone)
class TelefoneForm(ModelForm):
    class Meta:
        model = Telefone
        exclude = []

# "This is a form that will be used to create or edit a Link object."
# 
# The Meta class is a special class that tells Django which model to use to create this form (model =
# Link). The exclude variable is a list of fields that won't be used. Since we want all the fields in
# our model to be used, we set this to an empty list
class LinkForm(ModelForm):
    class Meta:
        model = Link
        exclude = []

# It's a ModelForm that uses the Escolaridade model, excludes nothing, and uses a DateInput widget for
# the inicio and fim fields
class EscolaridadeForm(ModelForm):
    class Meta:
        model = Escolaridade
        exclude = []
        widgets = {
            'inicio': DateInput(),
            'fim': DateInput(),
        }

# It's a subclass of ModelForm that uses the Historico model and excludes no fields
class HistoricoForm(ModelForm):
    class Meta:
        model = Historico
        exclude = []
        widgets = {
            'inicio': DateInput(),
            'fim': DateInput(),
        }

# "I want to use the Curso model, but I want to exclude the 'id' field, and I want to use a DateInput
# widget for the 'inicio' and 'fim' fields."
# 
# The exclude list is a list of fields that you don't want to include in the form. In this case, we
# don't want to include the 'id' field because it's an auto-incrementing primary key, and we don't
# want to include it in the form because it will be automatically generated when we save the form
class CursoForm(ModelForm):
    class Meta:
        model = Curso
        exclude = []
        widgets = {
            'inicio': DateInput(),
            'fim': DateInput(),
        }

# I want to create a form based on the Vaga model, but I don't want to include the publicar and
# concluida fields, and I want to use checkboxes (instead of the default <code>&lt;select&gt;</code>
# widget) for the categoria field.
class VagaForm(ModelForm):
    class Meta:
        model = Vaga
        exclude = ['publicar', 'concluida']
        widgets = {
            'categoria': forms.CheckboxSelectMultiple(),
        }

# The VagaFormEdit class inherits from ModelForm, and it's Meta class specifies the model to use, the
# fields to exclude, and the widgets to use
class VagaFormEdit(ModelForm):
    class Meta:
        model = Vaga
        exclude = []
        widgets = {
            'categoria': forms.CheckboxSelectMultiple(),
        }

# "This is a form for the Aplicacao model, and it should exclude the curriculos and vagas fields."
# Now, let's create a form for the Vaga model
class AplicacaoForm(ModelForm):
    class Meta:
        model = Aplicacao
        exclude = ['curriculos', 'vagas']