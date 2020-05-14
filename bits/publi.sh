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
  --template=latex-ms.tex
  
google-chrome ../pdf/$FILENAME.pdf
