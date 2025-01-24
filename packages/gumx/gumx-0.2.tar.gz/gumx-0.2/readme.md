# GUMX
An over-engineered Python lib for [Gum](https://github.com/charmbracelet/gum).
```
pip install gumx
```

## Binary management
The Gum binary is automatically installed from the original Gum repository when launching the module.
- You can see the location of the binary with the `gumx` command.
- If you want to specify a custom binary, use `gumx --set path/to/gum`.

## Usage
This is quickstart guide. See the See the [Gum tutorial](https://github.com/charmbracelet/gum#tutorial) for advanced info. All functions and arguments have type hints ease of use.

```py
# Import library (Gum is automatically installed on first run here)
import gumx

# Pick item(s) in a list
response = gumx.choose(['blue', 'red', 'green'], header = 'Favorite color?')

# Confirm an actiono
assert gumx.confirm('Are you sure?', default = False)

# Select a file from a tree
file = gumx.file('.', style = {'height': 5})

# Prompt the user
password = gumx.input(prompt = 'Enter the password', password = True)

# Display a long file
gumx.pager('LICENSE')

# Make a fuzzy search
number = gumx.search(
    list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    prompt = 'Whats your favorite letter?'
)

# Display a spinner
with gumx.spin():
    # Do a long task
    time.sleep(5)

# Prompt the user (multiple lines)
desc = gumx.write(header = 'Commit description', char_limit = 72)
```

## TODO
- [ ] Implement the `gum style` command
- [ ] Fix `gumx.spin`
- [ ] Optimize `gumx.pager`
- [ ] Test binary installer on all platforms

## LICENSE
GUMX is licensed under the MIT license. See the `LICENSE` file.