#!/bin/bash

while getopts "f:hv" arg; do 
    case $arg in 
    f)
        filename=$OPTARG
        echo "Filename is $filename"
        ;;
    h)
        echo "Help content"
        ;;
    v)  echo "Verbose content"
        ;;
    
    *)  echo "Invalid argument"
        ;;

    esac
done
