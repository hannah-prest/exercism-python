"""bottle song"""
def recite(start, take=1):
    """bottle song"""
    translations = (
        "No",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten"
    )
    result = []
    stop = start-take
    for bottle in range(start, stop, -1):
        plural = "" if bottle == 1 else "s"
        current = translations[bottle]
        next = translations[bottle-1].lower()
        next_plural = "" if bottle-1 == 1 else "s"
        on_the_wall = f"{current} green bottle{plural} hanging on the wall,"
        result.append(on_the_wall)
        result.append(on_the_wall)
        result.append(f"And if one green bottle should accidentally fall,")
        result.append(f"There'll be {next} green bottle{next_plural} hanging on the wall.")
        if bottle-1 > stop:
            result.append(f"")

    return result
