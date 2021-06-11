#!/bin/bash

source /Users/ganeshbabuj/rdp2win/rdp2win.config 

PORT="3389"  #Default local port to tunnel through

function usage()
{
    echo "Usage: rdp2win -c client -i ip [ -p port ]"
}


NoOfArgs=0
while getopts ":c:i:p:" opt
do 
    case $opt in 
    c) CLIENT=$OPTARG; ((NoOfArgs++)) ;;
    i) IP=$OPTARG    ; ((NoOfArgs++)) ;;
    p) PORT=$OPTARG   ;;
    \?) usage          ;;
    esac
done 

function RDP_Tunnel()
{
    PATH=${KEYS_PATH}
    COMMAND="/usr/bin/ssh -f -N -i ${PATH}/${CLIENT}/product-${CLIENT}-prod.pem -L ${PORT}:${IP}:3389 centos@${CLIENT}-bst.product.saascloud.com"
    echo $COMMAND > ssh_command.sh
    /bin/sh ssh_command.sh
}


if [ $NoOfArgs -ne 2 ] && [ $NoOfArgs -ne 0 ]
    then
        echo "Not all the mandatory aruments are provided."
elif [ $NoOfArgs -ge 2 ]
    then
        RDP_Tunnel
else 
    echo > /dev/null
fi

