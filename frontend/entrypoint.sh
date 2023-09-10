#!/bin/bash

cd /workspace

if [ "$NODE_INSTALL" != "false" ]
then
    echo "installing node_modules"
    npm install
fi

echo "starting app"
npm start

exit 0