from enum import Enum
import pycountry

class Country(str, Enum):
    @classmethod
    def choices(cls):
        return [(country.alpha_2, country.name) for country in pycountry.countries]

    @classmethod
    def get_name(cls, code):
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else None

class ProductType(str, Enum):
    perfume = "PERFUME"
    eauDePerfum = "EAU DE PERFUM"
    eauDeToilette = "EAU DE TOILETTE"
    eauDeCologne = "EAU DE COLOGNE"
    eauFraiche = "EAU FRAICHE"
    afterShave = "AFTERSHAVE"
    mist = "Mist"

    @classmethod
    def choices(cls):
        return [(member.value, member.value) for member in cls] 

class Gender(str, Enum):
    Male = "male"
    Female = "female"
    Unisex = "unisex"

    @classmethod
    def choices(cls):
        return [(member.value, member.value) for member in cls] 

class Package(str, Enum):
    noPackage = "No Package"
    simple = "Simple"
    luxury = "Luxury"

    @classmethod
    def choices(cls):
        return [(member.value, member.value) for member in cls] 

class Fragrance(str, Enum):
    aromatic = "Aromatic"
    mediterranean = "Mediterranean"
    citrus = "Citrus"
    fruity = "Fruity"
    floral = "Floral"
    oriental = "Oriental"
    woody = "Woody"
    fresh = "Fresh"
    spicy = "Spicy"
    aquatic = "Aquatic"
    leather = "Leather"

    @classmethod
    def choices(cls):
        return [(member.value, member.value) for member in cls] 