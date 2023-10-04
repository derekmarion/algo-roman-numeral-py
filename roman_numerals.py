def to_roman(num):
    output = ""
    romanNumeralToArabic = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }
    romanNumeralPriorityOrder = [
        "M",
        "CM",
        "D",
        "CD",
        "C",
        "L",
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I",
    ]
    for numeral in romanNumeralPriorityOrder:
      quantity = num // romanNumeralToArabic[numeral] #note use of // division operator to enforce int. otherwise will return float and break logic
      if quantity > 0:
          i = quantity
          while i > 0:
              output += numeral
              num -= romanNumeralToArabic[numeral]
              i -= 1
          if num == 0:
              return output