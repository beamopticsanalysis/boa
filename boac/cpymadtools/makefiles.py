files = (
    'coupling',
    'matching',
    'ptc',
    'track',
    'twiss',
    'utils',)

for ff in files:
    with open(ff + '.py', 'w') as f:
        f.write(
            f'from pyhdtoolkit.cpymadtools.{ff} import *\n')

