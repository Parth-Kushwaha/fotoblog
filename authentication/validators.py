from django.core.exceptions import ValidationError

class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Your password does not contain letters',
                code='password-no-letter'
            )
    
    def get_help_text(self):
        return ('Your password must contain at least 1 uppercase and 1 lowercase letter')

