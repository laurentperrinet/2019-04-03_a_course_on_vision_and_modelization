default: print
# yk8KybcbfzYh
SRC=2019-03-25_HDR_RobinBaures

edit:
	atom $(SRC).py

html:
	#python3 $(SRC).py $(SRC).html
	python3 $(SRC).py index.html

page:
	python3 $(SRC).py
	cat /tmp/wiki.txt |pbcopy
	open https://invibe.net/cgi-bin/index.cgi/Presentations/$(SRC)?action=edit

show: html
#	open -a firefox $(SRC).html
	open /Applications/Safari.app/Contents/MacOS/Safari $(SRC).html

github: html
	git commit --dry-run -am 'Test' | grep -q -v 'nothing to commit' && git commit -am' updating slides'
	git push
	open https://laurentperrinet.github.io/$(SRC)

print: html
	open -a /Applications/Chromium.app https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true
	#open "https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true"
