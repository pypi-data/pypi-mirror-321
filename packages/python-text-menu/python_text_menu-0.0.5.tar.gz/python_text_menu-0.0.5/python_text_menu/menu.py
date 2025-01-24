
def ask_option(options_lenght: int, input_text='Select an option: ') -> int:
    try:
        choice = input(f'{input_text}')
        while True:
            if choice.isdigit():
                choice = int(choice)
                if choice in range(1, options_lenght + 2):
                    return choice
            choice = input('Select a valid option: ')
    except KeyboardInterrupt:
        print()
        return options_lenght + 1


def print_menu(options: list, sep=None, title='Menu'):
    """
    Parameters
    ----------
    title: Title to print before the options (default='Menu')
    bar: Separator to print between title and the options
    options: List of string to print
    input_text: Text to print after options (default='Select an option:')

    Returns
    -------
    Number of option selected starting from 1 (String)

    """
    print(f'{title}:')
    if sep:
        print(sep)
    for indx, o in enumerate(options):
        print(f'[{indx + 1}] {o}')
    print(f'[{len(options)+1}] Exit')
