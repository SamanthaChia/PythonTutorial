def city(name, country,population=''):
    if population:
        full_text = name.title() + ", " + country.title() + " - population " + population 
    else:
        full_text = name.title() + ", " + country.title()
    return full_text