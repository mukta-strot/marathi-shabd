## Project structure

The entire project (website) is made up of 3 parts.

1. **Home site** - the home page (index.md for now) <!-- and other basic documents
   -->
2. **Browse site** - static pages of words split further into topics, Basically
   all links under the Browse section on the home page. (`browse` folder on repo)
3. **Search site** - page where user can enter a word to search. Basically
	 the Search section on the home page. (`docs` folder in repo).

## Guidelines

### issues

- when working on any issue, please **assign** it to yourself, so that others
  know that someone is woring on it already.
- if any issue is unassigned, please assume that no one is working on it
  currently and you can take it up. Of course, you can always ask if there is
any doubt.

### pull requests

- Use the `develop` branch for sending PRs.


### coding guidelines
As much as possible, please try to follow these guidelines, as it makes for
better maintainability and re-usability of the code.

1. Add short comments
2. Follow the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) (gist given below)
  - Write programs that do one thing and do it well.
  - Write programs to work together.
  - Write programs to handle text streams, because that is a universal
    interface.

[Here](https://github.com/mukta-strot/marathi-shabd/issues/14#issuecomment-876212690) is some previous guidance regarding unix philosophy from this repo itself.

## How to

### Add/modify words

1. Edit the [database file](database/db.csv) for the words that are to be
   added/modified.
  - The `readme.md` in the `database` folder explains the format of the database.
2. Auto generate all "browse" markdown files affected due to above step.

```
> cd browse/scripts
> python3 main.py
```
3. Commit your changes and submit a PR.
