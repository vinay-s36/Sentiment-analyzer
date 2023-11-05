from backend.settings import MEDIA_ROOT
from .models import image
import easyocr
import os


def text(x):

    reader = easyocr.Reader(['en'])

    image3 = MEDIA_ROOT+'\\images\\'+x
    result = reader.readtext(image3)

    result

    extracted_test = ' '.join([res[1] for res in result])

    return (extracted_test)