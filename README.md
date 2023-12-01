### Automated Input Retrieval/Submission

**You need to provide your adventofcode.com session cookie in the
`lib/cookie.txt` file !**

Check online [how to retrieve your session cookie](https://support.pentest-tools.com/en/scans-tools/how-to-get-the-session-cookie)
if you don't know how to do it already.

`start.py` is the file in charge of automatically downloading
the challenge input in the YEAR/DAY/input.txt file.

`start.sh` is the file that is setting up everything.
It creates the appropriate folder, copy the template,
call `start.py` to retrieve the challenge input, and open
my editor (`$EDITOR`) directly on the newly created solution file.

Note that this script is only made to run on my computer (on NixOS).
You may want to change it for your needs.


The `lib/aoc.py` module provides a `submit` function which allows you
to automatically submit an answer to today's challenge.
Again, this relies on your session cookie to work.

You can specify the year/day/level for most of the scripts, and most of them
will default on today's challenge.

I also have a Vim (my code editor) macro setup to run my code with the
`input.txt` file as standard input:
```vim
autocmd filetype python nnoremap <F5> :!python % < input.txt<CR>
```

### My Solutions

I mostly write my codes using Python, because that is how I code the fastest.

I use UltiSnips a lot when I code to submit faster, but I usually cleanup my
code before pushing them to this repository.

### My Leaderboard

Compare your time with me!
My personal leaderboard code is `1561553-5170a789`.

You may also find me on [Prologin](https://prologin.org/)'s leaderboard
and [EPITA](https://www.epita.fr/)'s leaderboard.
