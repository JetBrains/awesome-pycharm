====================
Working With Imports
====================

What’s something you do all the time in Python? Import modules from
packages. Not just that, you also fiddle with the formatting to make
the style fascists happy. And remove unused imports. And bunches of
other janitorial tasks.

Let PyCharm be your janitor. PyCharm has tons of support to take over
this mundane drudgery, from auto-import to re-organizing your import
lines.

This is both super-helpful and underappreciated. Let’s solve that with
a deep dive on PyCharm’s import support.

Zen Coding
==========

You’re coding away, in the zen flow, and then...you want to use the
`requests` library. It’s installed in your virtualenv, you just need to
import it. So away you go, up to the top of the file, looking for the right
place to import it.

****  you can `Ctrl+Space` twice and then type any object from you project
sources or dependencies, e.g. `requests` or some function name `foo` and
PyCharm will create an import for you on the fly.

Let PyCharm do it for you. Type `requests.` and hit `Alt-Enter`, then
choose to `Import this name` (or, if you’re in a test, import it locally
if you’re a purist.) Without leaving the cursor position, PyCharm will
generate the import, in the right spot, merging with an existing import
if necessary:

** animated gif **

PyCharm calls this the <a href=”https://www.jetbrains.com/help/pycharm/creating-imports.html”>Import Assistant</a>. You stay where you are, it manages the import.

Maybe this popup annoys you and you want to manually trigger it with
`Alt-Enter`. PyCharm makes it very convenient, via Hector in the bottom
right, to  disable the popup by de-selecting `Import popup`:

** animated gif **

Generating the import is half the annoyance. Equally frustrating? Constant
gardening of the long list of imports: re-grouping, re-sorting, and pruning
unused imports. Janitorial work like that is what PyCharm lives for.

Use the `Optimize Imports` action to let PyCharm do these three activities
(grouping, sorting, pruning.) You can trigger this action with `Ctrl-Alt-O`
but I generally use `Find Action`. The result: nice import lines:

** animated gif **

PyCharm can <a href=”https://www.jetbrains.com/help/pycharm/optimizing-imports.html#optimize-imports-in-current-file”>optimize
imports in a single file</a>. But you can also optimize imports
<a href=”https://www.jetbrains.com/help/pycharm/optimizing-imports.html#optimize-imports-in-project”>across
the entire project</a>. Select the folder at your project root, then trigger
`Optimize Imports` (from the menu, the shortcut, or Find Action):

** animated gif **

Working with Packages
=====================

That’s two drudgeries in the bag already -- generating imports and gardening
the import list. Here’s another: what if you don’t have `requests` installed
yet?

We saw with imports the zen mode: you start typing and tell PyCharm to do the
work. Same here: start your import, hit `Alt-Enter`, and choose
`Install package requests`:

** animated gif **

This is explained further in the <a
href=”https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html”>tip on
the help page</a>.

Thus, in the middle of using the import, rather than interrupt your flow,
tell PyCharm to go install the package into your project interpreter. As a
bonus, if you have a `requirements.txt` registered with your project:

** animated gif **

...then PyCharm will record this package as an entry. That’s a nice flow.

Import Preferences
==================


PyCharm follows PEP 8’s <a
href=”https://www.python.org/dev/peps/pep-0008/#imports”>guidance on
import style</a>. For example, PyCharm will warn you if you have an import
mixed into your module code, instead of at the top. By default,
`Optimize Imports` will do the grouping and sorting from PEP 8. And
finally, if you generate another import from an already-imported package,
PyCharm will add the new symbol to the existing import line.

What if you want some flexibility? PyCharm’s project preferences let you
change sorting and the joining behavior:

** screenshot of Find Action, Opt Imp, choose preference, highlight the choices **

I have a colleague who wants easier-to-track diffs by putting each import on
its own line. PyCharm lets you toggle this setting, switching from joining
imports to splitting them:

** screenshot of before/after on that preference

JavaScript Too
==============

But wait, there’s more. If you do frontend development (JavaScript, HTML,
CSS) in PyCharm Professional, then you get all of this and even a little
more, on that side of the fence.

ES6 modules support import-on-demand:

** animated gif **

ES6 uses quotes for the package identifier. Perhaps you want single-quotes.
There’s a project preference for that:

** animated gif of setting the preference, then generating an import **

Some TypeScript linters are picky about spacing inside brackets on named
imports. There’s a preference to handle that:

** animated gif: warning about spacing, change the preference, reformat **

As you’d expect, `Optimize Imports` sorts and prunes in JavaScript:

** animated gif **

Perhaps your project uses ESLint to manage styles. Sure is a drag, keeping
your `.eslintrc` statement about imports and your IDE preferences in sync.
PyCharm Professional will ask you if you want to import styles from your
`.eslintrc` file:

** animated gif about .eslintrc import style **

Narrated Video
==============

We often say that a big part of PyCharm’s value is how it does the janitorial
work for you. Managing imports is a perfect example of that.

If you’d like to see this in more of an end-to-end fashion, below is a
narrated video walkthrough.


