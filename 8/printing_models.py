unprinted_disigns = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_disigns:
    current_design = unprinted_disigns.pop()
    print(f'Printing model: {current_design}')
    completed_models.append(current_design)

print('\nThe following models have been done:')
for completed_model in completed_models:
    print(completed_model)