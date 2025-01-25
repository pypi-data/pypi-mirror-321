# string_ops.py
def reverse_string(s: str) -> str:
    """Inverse la chaîne de caractères."""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Compte le nombre de voyelles dans la chaîne."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def capitalize_words(s: str) -> str:
    """Met en majuscule la première lettre de chaque mot."""
    return ' '.join(word.capitalize() for word in s.split())