import os
import argparse
import platformdirs

parser = argparse.ArgumentParser(description = 'GUMX binary manager')
parser.add_argument('--set', help = 'Set a specific binary location')

args = parser.parse_args()

if args.set:
    # Set a custom binary path
    dir = platformdirs.user_data_dir('gumx')
    os.makedirs(dir, exist_ok = True)
    
    with open(os.path.join(dir, 'executable'), 'w') as file:
        file.write(os.path.abspath(args.set))

else:
    # Install and/or display gum installation
    import gumx
    print(gumx.consts.INSTALL)

# EOF