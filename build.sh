#! /bin/bash

> index.markdown
for FILE in *.markdown; do
    # Compile markdown
    BARE=${FILE%%.*}
    HTML=${BARE}.html
    markdown ${FILE} > ${HTML}
    cat >> index.markdown <<< "[${BARE}](${HTML})"
done

markdown index.markdown > index.html

