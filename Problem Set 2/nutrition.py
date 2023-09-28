# Create main function to output results
def main():
    prompt = input('Item: ').casefold()
    lof(prompt)

# Create list function to define list of fruits (lof)
def lof(s):
    fruits = {
        'apple' : '130',
        'avocado' : '50',
        'banana' : '110',
        'cantaloupe' : '50',
        'grapefruit' : '60',
        'grapes' : '90',
        'honeydew melon' : '50',
        'kiwifruit' : '90',
        'lemon' : '15',
        'lime' : '20',
        'nectarine' : '60',
        'orange' : '80',
        'peach' : '60',
        'pear' : '100',
        'pineapple' : '50',
        'plums' : '70',
        'strawberries' : '50',
        'sweet cherries' : '100',
        'tangerine' : '50',
        'watermelon' : '80',
    }
    # Return calories of fruit
    if s in fruits:
        calories = fruits[s]
        print(f'Calories: {calories}')
    else:
        print(end="")


main()
