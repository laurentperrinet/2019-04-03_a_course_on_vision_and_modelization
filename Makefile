default: github

SRC=2019-04-03_a_course_on_vision_and_modelization

edit:
	atom $(SRC).py

html:
	#python3 $(SRC).py $(SRC).html
	python3 $(SRC).py index.html

figure1_a: figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg
	rsvg-convert figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg -f png -d 450 -p 450 -o figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.png

figure1_b: figures/boutin-franciosini-ruffier-perrinet-19_figure1_b.svg
	rsvg-convert figures/boutin-franciosini-ruffier-perrinet-19_figure1_b.svg -f png -d 450 -p 450 -o figures/boutin-franciosini-ruffier-perrinet-19_figure1_b.png

figure1_c: figures/boutin-franciosini-ruffier-perrinet-19_figure1_c.svg
	rsvg-convert figures/boutin-franciosini-ruffier-perrinet-19_figure1_c.svg -f png -d 450 -p 450 -o figures/boutin-franciosini-ruffier-perrinet-19_figure1_c.png

figure1: figures/boutin-franciosini-ruffier-perrinet-19_figure1.svg
	rsvg-convert figures/boutin-franciosini-ruffier-perrinet-19_figure1.svg -f png -d 450 -p 450 -o figures/boutin-franciosini-ruffier-perrinet-19_figure1.png

figures: figure1 figure1_a figure1_b figure1_c

page:
	python3 $(SRC).py
	cat /tmp/talk.bib |pbcopy
	atom ~/pool/blog/perrinet_curriculum-vitae_tex/LaurentPerrinet_Presentations.bib
	# academic ...

show: html
#	open -a firefox $(SRC).html
	open /Applications/Safari.app/Contents/MacOS/Safari  index.html

github: html
	git commit --dry-run -am 'Test' | grep -q -v 'nothing to commit' && git commit -am' updating slides'
	git push
	open https://laurentperrinet.github.io/$(SRC)

print: html
	/Applications/Chromium.app/Contents/MacOS/Chromium --headless --disable-gpu --print-to-pdf=$(SRC).pdf "https://laurentperrinet.github.io/$(SRC)/?print-pdf"
	#open -a /Applications/Chromium.app https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true
	#open "https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true"
