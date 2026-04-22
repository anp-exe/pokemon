# Pokemon Class Project

A small Python project that models Pokemon using object-oriented programming (OOP).

## Overview

This project defines a `Pokemon` class with attributes and methods to describe Pokemon and print their details.
It then creates three Pokemon instances (`BeeDrill`, `Pikachu`, and `Charmander`) and displays information for each one.

## Project Structure

- `pokemon.py` - Main script containing:
  - `Pokemon` class definition
  - Sample Pokemon instances
  - Method calls to display Pokemon details

## Features

- Stores Pokemon data:
  - Pokedex entry number
  - Name
  - Type(s)
  - Description
  - Caught status
- `speak()` method that returns the Pokemon name repeated twice
- `display_details()` method that prints a formatted summary of each Pokemon

## Requirements

- Python 3.x
- No external libraries needed

## How to Run

```zsh
cd /Users/anna/PycharmProjects/pokemon
python3 pokemon.py
```

## Code Notes

- The `speak()` method currently returns a string, but the return value is not printed in the script.
- The `display_details()` method prints output directly to the console.
- Pokemon types are stored as a list and displayed using `", ".join(self.types)`.

## Example Pokemon in This Project

- `BeeDrill` (`Poison`)
- `Pikachu` (`Electric`)
- `Charmander` (`Fire`)

## Possible Improvements

- Print the result of `speak()` so it appears in terminal output
- Add multiple types for Pokemon that have more than one type
- Add input-based creation of Pokemon instances
- Add validation (for example, ensuring `entry` is an integer)
- Add unit tests for class methods
