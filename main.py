from persons.person import Person

def main():
    person_1 = Person()
    print(person_1.life_expectancy)

    person_2 = Person()
    person_2.life_expectancy = 80
    print(person_2.life_expectancy)

if __name__ == '__main__':
    main()