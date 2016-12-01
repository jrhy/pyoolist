
all: test README.md

test:
	python flisttest.py > .test.out

README.md: README.md.template .test.out
	( cat README.md.template ; \
	    echo '```' ; \
	    cat .test.out ; \
	    echo '```' ) \
	    > README.md

