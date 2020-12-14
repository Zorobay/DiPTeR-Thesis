## Setup instructions

I used `MiKTeX` as the LaTeX distribution and `TeXstudio` as the editor. The document should be compiled using `PDFLaTeX`.

### Installing Pygments

In order for `minted` to work, you need Python added to the `PATH` as well as the package `Pygments` from https://pygments.org/ installed (using `pip`).

#### Installing custom lexer
I have written a simple extension of the Python lexer, as I needed a few special keywords to be highlighted correctly. It can be installed as follows:

```
cd customlexer
python setup.py install
```
### Compile bibtex

In `TeXstudio`, go to *Tools* and click *Bibliography*.
