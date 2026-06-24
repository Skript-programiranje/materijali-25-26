#!/usr/bin/bash

usage() {
    echo "Usage: ./log_report.sh (--count|--statuses|--errors) <log_file>
        ./log_report.sh --top <log_file> <n>
        ./log_report.sh --redact <log_file> <output_file>"
    exit 1
}

if [ "$#" -lt 2 ]; then
    usage
fi

option="$1"
input_file="$2"

if ! [ -f "$input_file" ]; then
    usage
fi

case "$option" in
    "--count")
        if [ "$#" -ne 2 ]; then
            usage
        fi

        grep -E '^[^#]' "$input_file" |
        wc -l
    ;;
    "--statuses")
        if [ "$#" -ne 2 ]; then
            usage
        fi

        grep -E '^[^#]' "$input_file" |
        cut -d'|' -f5 |
        sort |
        uniq -c |
        sed -E 's/^\s*([0-9]+)\s+([0-9]+)/\2 \1/g'
    ;;
    "--errors")
        if [ "$#" -ne 2 ]; then
            usage
        fi

        grep -E '^[^|]*\|[^|]*\|[^|]*\|[^|]*\|[4-5][0-9]{2}' "$input_file" |
        cut -d'|' -f1,3,4,5 |
        sed -E 's/\|/ /g'
    ;;
    "--top")
        if [ "$#" -ne 3 ] || ! [[ "$3" =~ ^[0-9]+$ ]]; then
            usage
        fi

        N="$3"
        grep -E '^[^#]' "$input_file" |
        cut -d'|' -f4 |
        sort |
        uniq -c |
        sort -nr |
        sed -E 's/^\s+//g' |
        head -n "$N"
    ;;
    "--redact")
        if [ "$#" -ne 3 ]; then
            usage
        fi

        out_file="$3"
        sed -E 's/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[REDACTED]/g' "$input_file" >"$out_file"
    ;;
    *)
        usage
    ;;
esac
