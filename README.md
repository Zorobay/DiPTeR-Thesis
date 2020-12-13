## Setup instructions

I used `MiKTeX` as the LaTeX distribution and `TeXstudio` as the editor. The document should be compiled using `PDFLaTeX`.

### Installing Pygments

In order for `minted` to work, you need Python added to the `PATH` as well as the package `Pygments` from https://pygments.org/ installed (using `pip`).

#### Installing custom lexer
```
cd customlexer
python setup.py install
```
### Compile bibtex

In `TeXstudio`, go to *Tools* and click *Bibliography*.
