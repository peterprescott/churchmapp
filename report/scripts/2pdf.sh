pandoc -s report.md \
	-o report.pdf \
	-f markdown \
	-t pdf \
	--natbib \
	--pdf-engine=latexmk \
	--template=latex-ms.tex
