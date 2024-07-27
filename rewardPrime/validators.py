from django.core.validators import ValidationError

def isAdviceValidated(advice):
    if not advice:
            raise ValidationError("Please, provide any advice for capture this character.")
    if len(advice) <= 10:
          raise ValidationError("The advice must be at least 10 characters long.")

def isAmountValidated(amount):
      if amount < 0:
            raise ValidationError('Amount must be positive.')
      if amount < 1000:
            raise ValidationError('Amount must be greater than 1000 (not be cheapskate)')