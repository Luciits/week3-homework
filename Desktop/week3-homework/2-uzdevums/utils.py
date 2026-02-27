# Virkņu funkcijas

def capitalize(text): 
    """
    Pārveido texta pirmo burtu par lielo, pārējos par mazajiem.

    Args:
        text(str): Teksts, ko apstrādāt.

    Return:
       str:Apstrādātais tekts.
    Raises:
        TypeError: ja ievade nav virkne.
    Example:
        >>> capitalize("hello WORLD")
        'Hello world'
    """
    # 1. Validācija (pārbaudām vai tas ir teksts)
    if not isinstance(text, str):
        raise TypeError("Ievadei jābūt (str)!")
    # 2. Tīra funkcija (nav print tikai return)
    return text.capitalize()
def truncate(text, max_len=20):
    """
    Apgriež tekstu kad  tas ir garāks par 20 simboliem un pievieno "..."

    Args:
      text(str): Teksts ko apstrādā.
      max_len(int): Maksimālais simbolu skaits. Noklusējums ir 20.
    return:
       str: Saīsināts teksts ar "..." vai orģinālais teksts.
    Raises:
        TypeError: ja ievade nav virkne.
    Example: 
        >>> turncate("Šis tekts ir par garu")
        'Šis tekts ir par ...'
    """
    # 1. Validācija (pārbauda vai tas ir teksts)
    if not isinstance(text, str):
        raise TypeError("Iveadei jābūt (str)!")
    if not isinstance(max_len, int) or max_len < 0:
        raise ValueError("Teksta garumam jābūt pozitīvam!")
    # 2. Loģika ar tīru funkciju
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text
def count_words(text):
    """
    Atgriež vārdu skaitu virknē

    Args:
       text(str): Teksts kurā saskaitīt vārdus

    Raises:
        TypeError: ja ievade nav virkne.

    Example:
        >>> count_words("Cik garš es esmu?")
        4
    """
    if not isinstance(text, str):
        raise TypeError("Ievadei jābūt (str)!")
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

 # Skaitļu funkcijas

def clamp(num, min_value=0, max_value=100):
    """
    Saņem skaitli un atgriež to vērtību robežās

    Args:
      num(int): Skaitlis kuru atgriest robežu vērtībā
      min_value: Minimālā robežas vērtība.
      max_value: Maksimālā robežas vērtība.
    Raises: 
        TypeError: ja ievade nav skaitlis
    Example:
        >>> clamp(5, 1, 4)
        4
    """
    if not isinstance(num, (int, float)) and isinstance(min_value, (int, float)) and isinstance(max_value, (int, float)):
        raise TypeError("Visiem parametriem (num, min_value, max_value) jābūt skaitļiem!")
    return max(min(num, max_value), min_value)
def is_prime(num):
    """
    Pārbauda vai skaitlis ir pirmskaitlis un atgrieš bool

    Args:
      num(int): skaitlis kuru pārbauda.
      true: ir pirmskaitlis.
      false: nav pirmskaitlis.
    Raises: 
        TypeError: ja ievade nav skaitlis
        ValueError: ja nav vesels skaitlis
    Example:
         >>> is_prime(3)
         True
    """
    if not isinstance(num, (int, float)):
        raise TypeError("Ievadi jābūt skaitlim!")
    if isinstance(num, float):
        raise ValueError("Ievadei jābūt veselam skaitlim!")
    if num < 0:
        raise ValueError("Pirmskaitlim jābūt veselam skaitlim!")
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Skaitļu funkcijas

def is_prime(num): # Funkcija, kas saņem skaitli un atgriež True, ja skaitlis ir pirmskaitlis, un False, ja nav
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def factorial(n): # Funkcija, kas saņem skaitli un atgriež tā faktoriālu
    if n < 0 :
        return "Input must be a non-negative integer."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result    

# Sarakstu funkcijas

def total(numbers): # Funkcija, kas saņem sarakstu ar skaitļiem un atgriež to summu
    for i in numbers:
        if not isinstance(i, (int, float)):
            return "Error, All elements must be numbers"
    result = 0
    for num in numbers:
        result += num
    return result
def average(numbers): # Funkcija kas saņem sarakstu un atgriež to vidējo vērtību
    if not numbers:
        return 0
    for x in numbers:
        if not isinstance(x, (int, float)):
            raise TypeError("all elements must be numbers")
    return total(numbers) / len(numbers)


