#!/bin/bash

cd /home/liikt/discord/TAS/

PULL=`git pull`

if [[ ${PULL} != 'Already up-to-date.' ]]; then
    ./kill.sh || true
    ./daemonize
    echo -e '\nRestarted The All Seeing\n----------------------------------\n' >> log/tas
    echo 'restarted'
fi
