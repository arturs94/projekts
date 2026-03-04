def check_age(age: int) -> int:
    if not isinstance(age, int):
        raise ValueError("Vecumam jābūt skaitlim")
    if age < 0:
        raise ValueError("Vecums nevar būt negatīvs")
    return age


if __name__ == "__main__":
    try:
        age = 18
        valid_age = check_age(age)

        if valid_age < 18:
            print("Aizliegts!")
        else:
            print("Welcome!")
            
    except ValueError as e:
        print("Kļūda:", e)
