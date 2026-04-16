#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 test_file_name" >&2
    exit 1
fi

case "$1" in
    *javni*|*public*|*example*|*sample*)
        echo "public"
        ;;
    *)
        echo "private"
        ;;
esac
