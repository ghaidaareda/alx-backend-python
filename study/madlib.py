def madlib():
    name = input('Enter your name: ')
    city = input('Enter the capital of a country: ')
    animal = input('Enter an animal that is not a mammal: ')
    color = input('Enter a color: ')
    story = f"I'm {name} from {city}. I love to tell stories about my adventures in the jungle, where I once saw a {color} {animal}."
    print(story)

if __name__ == "__main__":
    madlib()