# See https://blog.abclarke.com/tag/humble-poetry/
all_possible_peoples = ["Russian", "Ukranian", "American", "Chinese", "Irish", "British",
                        "Christian", "Muslim", "Agnostic", "Jewish", "Buddhist",
                        "Gay", "Lesbian", "Cis", "Transgender",
                        "Democrat", "Republican", "Progressive",
                        "imperfect", "..."]


def i_love(other_people, people_i_feel_anger_towards):
    if other_people in people_i_feel_anger_towards:
        return False
    else:
        return True


def profess_love(people_i_feel_anger_towards, people_i_identify_as):
    for other_people in all_possible_peoples:
        if other_people in people_i_identify_as:
            print(f"I am {other_people}, and I love all {other_people} people, despite our failures.")
        else:
            if i_love(other_people, people_i_feel_anger_towards):
                print(f"I am not {other_people}, yet I love all {other_people} people, despite their failings.")
            else:
                print(f"I have no love for {other_people} people.")


if __name__ == '__main__':
    people_i_feel_anger_towards = [
        "Russian", # How can you let your leaders justify this 'special operation"
        "Republican", # How can you let your leaders justify storming the capital?
        "..."
        ]
    people_i_identify_as = [
        "American", "Irish", "Agnostic", "Cis", "imperfect"
    ]
    profess_love(people_i_feel_anger_towards, people_i_identify_as)
