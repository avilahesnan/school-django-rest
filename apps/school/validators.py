from validate_docbr import CPF
import re


def cpf_valid(cpf):
    '''
    Checks if the CPF is valid.

    Returns:
        True or False.
    '''

    model = r'^\d{3}(\.?\d{3})?(\.?\d{3})?-?\d{2}$'
    response = re.match(model, cpf)
    if response:
        check_cpf = CPF()
        return check_cpf.validate(cpf)
    return response


def rg_valid(rg):
    '''
    Checks if the rg is valid.

    Returns:
        True or False.
    '''

    return len(rg) == 9


def phone_valid(phone):
    '''
    Checks if the phone is valid.

    Returns:
        True or False.
    '''

    model = r'^\(\d{2}\)\ ?9?\d{4}\-?\d{4}$'
    response = re.match(model, phone)
    return response
