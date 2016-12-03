
all: test README.md

test:
	python flisttest.py > .test.out

README.md: README.md.header .test.out
	( cat README.md.header ; \
	    echo '```' ; \
	    cat .test.out ; \
	    echo '```' ) \
	    > README.md

