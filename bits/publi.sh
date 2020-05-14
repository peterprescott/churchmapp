FILENAME=$1

pweave --format=pandoc \
	--output=../pandoc/$FILENAME.md \
	--figure-directory=../figures \
	../rmd/$FILENAME.Rmd

pandoc -s ../pandoc/$FILENAME.md \
	-o ../pdf/$FILENAME.pdf \
  -f markdown \
  -t pdf \
  --natbib \
  --pdf-engine=latexmk \
  --template=latex-ms.tex \


pandoc -s ../pandoc/$FILENAME.md \
  -o ../html/$FILENAME.html \
  -f markdown \
  -t html \
  --template=template.html \
  --css pandoc.css \
  --filter pandoc-citeproc \
  --bibliography refs.bib \
  --csl style.csl \
  --atx-headers \
  --webtex=https://latex.codecogs.com/png.latex? \
  # --toc -V --template=template.markdown \

  
google-chrome ../pdf/$FILENAME.pdf
google-chrome ../html/$FILENAME.html
