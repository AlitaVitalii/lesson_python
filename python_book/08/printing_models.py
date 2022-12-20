def print_models(unprinter_models, completed_models):
    while unprinter_models:
        current_desing = unprinter_models.pop()
        print(f'Printing model: {current_desing}')
        completed_models.append(current_desing)


def show_completed_models(completed_models):
    print('\nThe following have been printed')
    for i in completed_models:
        print(i)


unprinted_desing = ['phone', 'robot pendant', 'lanos']
completed_models = []

print_models(unprinted_desing[:], completed_models)
show_completed_models(completed_models)

print(unprinted_desing)