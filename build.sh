#! /bin/bash

> index.markdown
for FILE in *.markdown; do
    if [ "${FILE}" == 'index.markdown' ]; then
        continue
    fi
    # Compile markdown
    BARE=${FILE%%.*}
    HTML=${BARE}.html
    markdown ${FILE} > ${HTML}
    cat >> index.markdown <<< "[$(head -n1 ${FILE})](${HTML})  "
done

markdown index.markdown > index.html

