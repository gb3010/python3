#!/bin/bash

while getops "v:h" arg do 
    case $arg in 
      v)
        echo "Entered value is $OPTARG"
        ;;
      h) echo "Sample text"
        ;;
    esac
done 

