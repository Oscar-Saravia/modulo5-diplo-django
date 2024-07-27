from django.db import models

class StatusCharacter(models.TextChoices):
    ALIVE = 'Alive', 'Alive'
    DEAD = 'Dead', 'Dead'
    UNKNOWN = 'Unknown', 'Unknown'

class GenderCharacter(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'
    GENDERLESS = 'Genderless', 'Genderless'
    UNKNOWN = 'Unknown', 'Unknown'

class SearchStatus(models.TextChoices):
    ALIVE = 'Alive', 'Alive'
    DEAD = 'Dead', 'Dead'
    ANYWAY = 'Anyway', 'Anyway'
    

class Currency(models.TextChoices):
    USD = 'USD', 'US Dollar'
    BFL = 'BFL', 'Blemflarcks'
    FLB = 'FLB', 'Flurbo'
    SCM = 'SCM', 'Schmeckle'
    FPZ = 'FPZ', 'Frapprizzos'
    KBS = 'KBS', 'Kronobucks'
    GPF = 'GPF', 'Gazorpazorpfield'
    KCM = 'KCM', 'Kronometrics'
    ZFD = 'ZFD', 'Zibblefluds'
    SDG = 'SDG', 'Smidgens'
    GES = 'GPS', 'Greeps'
    BHS = 'BHS', 'Brohams'
    SPF = 'SPF', 'Shrumpflesh'
    PLT = 'PLT', 'Plutons'
    GBB = 'GBB', 'Gooble Boxes'
    FPC = 'FPC', 'Froopyland Credits'
    MIB = 'MIB', 'Miblons'
    PBF = 'PBF', 'Pebbles'
    CPF = 'CPF', 'Crystal Puffs'
    GFP = 'GFP', 'Greasy Gumflars'
    RBK = 'RBK', 'Ribbleblanks'