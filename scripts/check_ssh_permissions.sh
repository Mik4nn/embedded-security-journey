#!/bin/bash
# Quick system overview script: checking ssh permissions

for file in ~/.ssh/*; do 
    file_perm=$(stat -c "%a" "$file")
    
    if [[ "$file" == *.pub || "$file" == */known_hosts* ]]; then
        if [[ "$file_perm" != 600 && "$file_perm" != 644 ]]; then
            echo "Warning: $file has incorrect permissions ($file_perm)"
        else 
            echo "$file has correct permissions ($file_perm)"
        fi
    else 
        if [ "$file_perm" != 600 ]; then
            echo "Warning: $file has incorrect permissions ($file_perm)"
        else 
            echo "$file has correct permissions ($file_perm)"
        fi
    fi
done
