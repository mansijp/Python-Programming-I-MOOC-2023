def formatted(my_list: list):
    formattedStrings = []
    for i in range(len(my_list)):
        formattedStrings.append(f"{my_list[i]:.2f}")
    return (formattedStrings)

if __name__ == "__main__":
    formatted([1.234, 0.3333, 0.11111, 3.446])


# ------- to remove automatically added spaces using commas, add sep="" -------
    # print("Hi", name, "your age is", age, "years", sep="")
    # HiMarkyour age is37years
    # print("Hi", name, "your age is", age, "years", sep="\n") separates based on lines

# ------- Format specifier -------
    # print(f"The number is {number:.2f}")
    # The number is 0.33

# ------ String formatting in tables -------
    # for name in names:
        # print(f"{name:15} centre {name:>15}")
    # Steve           centre           Steve
    # Jean            centre            Jean
    # Katherine       centre       Katherine
    # Paul            centre            Paul
