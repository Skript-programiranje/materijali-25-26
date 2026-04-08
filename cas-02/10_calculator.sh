#!/bin/bash

if [ $# -ne 3 ]; then
	echo "Usage: $0 x <operation> y"
	exit 1
fi

if [ "$2" = '+' ]; then
	echo "$(( $1 + $3 ))"
elif [ "$2" = '-' ]; then
	echo "$(( $1 - $3 ))"
elif [ "$2" = '*' ]; then
	echo "$(( $1 * $3 ))"
elif [ "$2" = '/' ]; then
	echo "$(( $1 / $3 ))"
elif [ "$2" = '%' ]; then
	echo "$(( $1 % $3 ))"
else
	echo "Unkown operation!"
	exit 1
fi

