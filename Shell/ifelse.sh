read -p "Enter the value: " input ;
if [[ $input == "dry run" ]]
  then
    echo "dry run"
elif [[ $input == "terminate" ]]
  then
    echo "terminate"
fi
