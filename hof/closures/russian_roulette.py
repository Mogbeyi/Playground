def roulette(n):
    count = 0
    click = n - 1

    def wrapper():
        nonlocal count, click

        if count < click:
            count += 1
            return "click"
        elif count == click:
            count += 1
            return "bang"
        else:
            return "reload to play again"

    return wrapper

russian_roulette = roulette(5)
print(russian_roulette())  # click
print(russian_roulette())  # click
print(russian_roulette())  # click
print(russian_roulette())  # click
print(russian_roulette())  # bang
print(russian_roulette())  # reload to play again
print(russian_roulette())  # reload to play again

