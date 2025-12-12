# flylo
Grabs prices for flights from Dallas to most major airports in the US. Stores information in a DB as well as maintains distribution list for daily/weekly/monthly udpates.

## Developer Setup

1. Install [pyenv](https://github.com/pyenv/pyenv).
2. Install [poetry](https://python-poetry.org/docs/)
3. Clone the repo and navigate to the project root in your terminal.
4. Run the command `pyenv install`.
5. Run the command `poetry install --no-root`.

To run files you can either:
- Run `poetry shell` and then `python test.py`
- Run `peotry run python test.py`

If you choose to run `poetry shell` first, when you are done developing you can type `exit` in your terminal to exit the shell.

### Environment

Create a `.env` file in the project root.

TODO: More details to follow
