# CLI Game  -- Drop Tokens

## Installation Choice 1 

### Run program in virtual environment
#### Dependency
- pip3
- virtualenvs


Local Build, Test, Style Checker and Documatation
```
git clone https://github.com/vivian5668/CLI_game_drop_token.git
cd CLI_game_drop_token
make release
../virtualenvs/drop_token/bin/start
```
### Local Test
```
cd drop_token
make test
```
## Installation Choice 2
### Install from github directly
```
pip3 install -U -e git+https://github.com/vivian5668/CLI_game_drop_token#egg=drop-token
```
type `start` in the terminal to start the game


# Quick Tutorial
- Please specify board size 2-9
    -  `4`
 - type a command choosing from: BOARD, PUT, GET, HELP, EXIT --->
   - `BOARD`
 - type a command choosing from: BOARD, PUT position[INT], GET, HELP, EXIT --->
   - `PUT 3`
  

## To-do List
- write docstring for classes and functions
- complete HELP text
- add ASCII visuals for better user experience
- write more tests
- make user-input checks more robust

