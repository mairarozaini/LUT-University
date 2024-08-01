def main():
    from person import Person

    valtteri = Person("Valtteri", 34)
    kimi = Person("Kimi", 44)

    valtteri.introduce()
    kimi.introduce()

    kimi.celebrate_birthday()

    kimi.introduce()

main()

