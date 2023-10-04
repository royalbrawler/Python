from random import choice

capital = "Sofia"

bird = "Kulvach"

flower = "Roza"

song = "Stara Planina"


def randomfunfact():
    funfacts = [
        "Plovdiv is Europe's oldest inhabited city.",
        "The ancient Bulgarian calendar was declared the most accurate in the world by UNESCO in 1976.",
        "In Bulgaria was founded the oldest golden treasure.",
        "Sofia, the capital of Bulgaria, was founded 7000 years ago."
    ]

    index = choice("0123")

    print("==FUN FACT:", funfacts[int(index)])


if __name__ == "__main__":  # true
    randomfunfact()
