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

## Note

If using Overleaf, at least at the start of 2020, they used an old version of the `CormorantGaramond` font package, which had some visual bugs. This can be fixed by putting the font files in the root directory. These files were removed in, and can be retrieved from, the commit with hash `73f6c560a9178a89c22332e4139460e62392d880`.