from django import forms
from app1.models import  Producto, TipoProducto, Usuario
from datetime import date
import re

class CategoriaForm(forms.ModelForm):
    nombreTipo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nombre de la categoría")
    descripcionTipo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Descripción de la categoría")
    fotoTipo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Imagen representativa de la categoría", required=False)

    class Meta:
        model = TipoProducto
        fields = ["nombreTipo", "descripcionTipo", "fotoTipo"]

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ','placeholder':' Ingrese Nombre del producto'}))
    marcaProduc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':' Ingrese Marca del producto'}))
    
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':' Numero de contacto'}))
    imagenProduc = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Suba una imagen del producto'}),required=False)
    kilage = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Kilage'}))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock'}))
    descuento = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Descuento'}))
    tipo = forms.ModelChoiceField(
        queryset=TipoProducto.objects.all(),
        empty_label="",
        widget=forms.Select(attrs={'class':'form-control'})
    )
    class Meta:
        model = Producto
        fields = ["nombre", "marcaProduc", "precio", "imagenProduc", "kilage", "stock", "descuento","tipo"]

class ClienteForm(forms.ModelForm):
    rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ej:19505446-0'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre'}))
    paterno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Paterno'}))
    materno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellido Materno'}),required=False)
    numeroContacto = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Numero de contacto'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingrese Email'}))
    nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre de Usuario'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese Contraseña'}))
    reclave = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Repetir Contraseña'}))
    fechaNaci = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'dia/mes/año','type':'date'}))
    
    
    def clean_rut(self):
        rut = self.cleaned_data['rut']
        
        regex_rut = r'^[0-9]+-[0-9kK]{1}$'
        if not re.match(regex_rut, rut):
            raise forms.ValidationError("El formato del RUT no es válido")
        
        numero, digito_verificador = rut.split("-")
        
        suma = 0
        multiplicador = 2
        
        for i in range(len(numero) - 1, -1, -1):
            suma += int(numero[i]) * multiplicador
            multiplicador = 2 if multiplicador == 7 else multiplicador + 1
            
        resto = suma % 11
        digito_calculado = 11 - resto
        if (digito_calculado == 11 and digito_verificador == "0") or \
            (digito_calculado == 10 and (digito_verificador == "K" or digito_verificador == "k")) or \
            digito_calculado == int(digito_verificador):
            return rut  # RUT válido
        else:
            raise forms.ValidationError("El RUT no es válido")

        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        
        if nombre and not nombre.isalpha() and ' ' not in nombre:
            raise forms.ValidationError('El nombre debe contener solo letras y espacios.')
        return nombre
    
    
    def clean_paterno(self):
        paterno = self.cleaned_data.get('paterno')
        if paterno and not paterno.isalpha() and ' ' not in paterno:
            raise forms.ValidationError('El Apellido paterno debe contener solo letras y espacios.')
        return paterno
        
    def clean_materno(self):
        materno = self.cleaned_data.get('materno')
        if materno and not materno.isalpha() and ' ' not in materno:
            raise forms.ValidationError('El Apellido materno debe contener solo letras y espacios.')
        return materno    
    
    def clean_numeroContacto(self):
        numero_telefono = self.cleaned_data['numeroContacto']

        if not numero_telefono.isdigit() or len(numero_telefono) != 9:
            raise forms.ValidationError('El número de teléfono debe contener exactamente 9 dígitos.')

        return numero_telefono
    
    def clean_contraseña(self):
        clave = self.cleaned_data['contraseña']

        if len(clave) < 6:
            raise forms.ValidationError('Clave muy debil')

        return clave   
    
    def clean_reclave(self):
        cleaned_data = super().clean()
        
        clave = cleaned_data.get('contraseña')
        reclave = self.cleaned_data['reclave']

        if len(reclave) < 6:
            raise forms.ValidationError('Clave muy debil')
        
        elif clave and reclave and clave != reclave:
            raise forms.ValidationError("Las contraseñas no coinciden. Por favor, vuelve a intentarlo.")


        return reclave    
            
    def clean_fechaNaci(self):
        fechaNaci = self.cleaned_data.get('fechaNaci')
        if fechaNaci > date.today():
            raise forms.ValidationError('La fecha de nacimiento no puede estar en el futuro.')
        
        edad_minima = 18
        if date.today().year - fechaNaci.year - ((date.today().month, date.today().day) < (fechaNaci.month, fechaNaci.day)) < edad_minima:
            raise forms.ValidationError(f'Debes tener al menos {edad_minima} años para registrarte.')
        
        return fechaNaci
    
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'paterno','materno','numeroContacto','email', 'nombre_usuario', 'contraseña','fechaNaci']