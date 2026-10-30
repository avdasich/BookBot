# BookBot

[Русская версия](README.ru.md)

BookBot is a simple command-line application written in Python that analyzes books and generates text statistics.

## Features

- Count the total number of words in a book.
- Count character occurrences, ignoring letter case.
- Sort characters by frequency.
- Generate a formatted report with word and character statistics.
- Analyze different text files using command-line arguments.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/avdasich/BookBot.git
cd BookBot
```

Run BookBot with a text file:

```bash
python3 main.py books/frankenstein.txt
```

You can also analyze other books:

```bash
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt
```

## Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...
============= END ===============
```

## Requirements

- Python 3.10 or newer
- No third-party dependencies

## Project Structure

```text
BookBot/
├── books/
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
├── main.py
├── stats.py
├── README.md
└── README.ru.md
```

## How It Works

BookBot reads a text file, counts its words and characters, and sorts the character statistics by frequency. The final report displays only alphabetic characters, ordered from most common to least common.