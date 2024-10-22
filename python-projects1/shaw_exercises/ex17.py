from sys import argv; from os.path import exists

script, from_file, to_file = argv

input(f"Copying from {from_file} to {to_file}...\nReady, hit RETURN to continue, CTRL-C to abort.\n>" )
(open(to_file, 'w')).write((open(from_file)).read())
print("Done.")
