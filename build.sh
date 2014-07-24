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
    if [ ! -z ${BUILD_HTML} ]; then
        markdown ${FILE} > ${HTML}
    fi
    cat >> ${INDEX}.markdown <<< "[$(head -n1 ${FILE})](${FILE})  "
done

if [ ! -z ${BUILD_HTML} ]; then
    sed 's/markdown/html/' ${INDEX}.markdown | markdown > ${INDEX}.html
fi
