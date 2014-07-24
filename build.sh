#! /bin/bash

INDEX='README'

> README.markdown
for FILE in *.markdown; do
    if [ "${FILE}" == "${INDEX}.markdown" ]; then
        continue
    fi
    # Compile markdown
    BARE=${FILE%%.*}
    HTML=${BARE}.html
    markdown ${FILE} > ${HTML}
    cat >> ${INDEX}.markdown <<< "[$(head -n1 ${FILE})](${HTML})  "
done

markdown ${INDEX}.markdown > ${INDEX}.html

