# jupytext --to Rmd demo.ipynb -o demo.Rmd
# mv demo.Rmd demo.pmd
# pweave -f pandoc demo.pmd
pandoc -s this.md \
  -o demo.html \
  -f markdown \
  -t html \
  --template=template.html \
  --css pandoc.css \
  --filter pandoc-citeproc \
  --bibliography ref.bib \
  --csl style.csl \
  --atx-headers \
  --webtex=https://latex.codecogs.com/png.latex? \
  #~ --toc -V --template=template.markdown \

pandoc -s this.md \
  -o demo.pdf \
  -f markdown \
  -t pdf \
  --css pandoc.css \
  --filter pandoc-citeproc \
  --bibliography churchmAPP.bib \
  --csl style.csl \
  --atx-headers \
  --webtex=https://latex.codecogs.com/png.latex? \
  
google-chrome demo.html
google-chrome demo.pdf
