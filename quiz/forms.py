from django import forms
from django.utils.safestring import mark_safe

class QuizForm(forms.Form):
    q1 = forms.ChoiceField(
        label=mark_safe(
            "Veamos qué tanto me conoces y nos conoces bb, te amo<br><br>"
            "¿Qué comida nunca me cansa?"
        ),
        choices=[
            ("1", "Pizza"),
            ("2", "Carne asada"),
            ("3", "Chilaquiles"),
        ],
        widget=forms.RadioSelect
    )

    q2 = forms.ChoiceField(
        label="¿Qué serie/película podría ver mil veces?",
        choices=[
            ("1", "Yellowstone"),
            ("2", "Brooklyn 99"),
            ("3", "Friends"),
        ],
        widget=forms.RadioSelect
    )

    q3 = forms.ChoiceField(
        label="¿Qué canción me pega directo al corazón?",
        choices=[
            ("1", "Ansiedad"),
            ("2", "Sigo aqui"),
            ("3", "Yours"),
        ],
        widget=forms.RadioSelect 
        )

    q4 = forms.ChoiceField(
        label="¿Qué defecto mío me pesa más?",
        choices=[
            ("1", "Inseguridad"),
            ("2", "Atrabancado"),
            ("3", "Indisciplinado"),
        ],
        widget=forms.RadioSelect 
        )
    
    q5 = forms.ChoiceField(
        label="¿Cómo demuestro cariño sin palabras?",
        choices=[
            ("1", "Actos de servicio"),
            ("2", "Regalos"),
            ("3", "Contacto fisico"),
        ],
        widget=forms.RadioSelect 
        )  
      
    q6 = forms.ChoiceField(
        label="¿Qué día nos conocimos?",
        choices=[
            ("1", "8 de Noviembre 2023"),
            ("2", "2 de Noviembre 2023"),
            ("3", "5 de Noviembre 2023"),
        ],
        widget=forms.RadioSelect 
        )
    
    q7 = forms.ChoiceField(
        label="¿Snack para ver pelis?",
        choices=[
            ("1", "Chips,Tostitos y Carne Seca"),
            ("2", "Pizza y vino"),
            ("3", "Boneless"),
        ],
        widget=forms.RadioSelect 
        )
    q8 = forms.ChoiceField(
        label="¿Como le decimos al dinero?",
        choices=[
            ("1", "Biyuyo"),
            ("2", "Cash"),
            ("3", "Pastita"),
        ],
        widget=forms.RadioSelect 
        )
    
    q9 = forms.ChoiceField(
        label="¿Que apodo te puse?",
        choices=[
            ("1", "Pi"),
            ("2", "Pilar"),
            ("3", "Fri"),
        ],
        widget=forms.RadioSelect 
        )  
      
    q10 = forms.ChoiceField(
        label="¿Por qué te amo tanto?",
        choices=[
            ("1", "Descomunal belleza"),
            ("2", "Alma"),
            ("3", "Todas las anteriores"),
        ],
        widget=forms.RadioSelect 
        )   