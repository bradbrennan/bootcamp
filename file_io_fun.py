import os

if os.path.isfile('gimme_phi.txt'):
    print('sorry, file exists.')
else:
    with open('gimme_phi.txt', 'w') as f:
        f.write('The golden ratio is ')
        f.write('{phi:.8f}'.format(phi=1.61803398875))
# .8 means 8 decimal places?
