#!/bin/bash

header=`head -n 1 genesA.txt`
IFS=$'\t' read -a headerarray <<< "${header}"
tail -n +2 genesA.txt > gene1A.csv
while read -r line
do

	IFS=$'\t' read -a array <<< "${line}"


	 for i in ${!array[@]}; do


	   if   [ $i -eq 0 ];then
	      rowarray=()
		  id="${array[$i]}"
	   elif [ $i  -eq 1 ];then
	      name="${array[$i]}"

	   elif [ $i  -eq 2 ];then
	      entrez_id="${array[$i]}"
	   elif [ $i -eq 3 ];then
	      description="${array[$i]}"
	   elif [ $i -gt 3 ];then
			count=$(echo "($i - 4)%5"|bc)
			number=$(echo "($i - 4)/5"|bc)

			rowarray+=("${array[$i]}")
			headname=${headerarray[$i]}
#			echo "kk"$headname
			if [ $number -eq 1 ] && [ $count -eq 0 ]; then
			    #echo $id", "$number", "$entrez_id", "$description
			   printf '%s ,%s ,%s ,%s ,' "$id" "$name" "$entrez_id" 
			    unset 'rowarray[${#rowarray[@]}-1]'
			   for element in "${rowarray[@]}"
               do

					printf '%s ,' "$element"
               done

			   rowarray=()
			   rowarray+=("${array[$i]}")
			printf '\n'

			elif [ $number -gt 1 ] && [ $count -eq 0 ]; then

			      printf '%s ,%s ,%s ,%s ,' "$id" "$name" "$entrez_id"
				unset 'rowarray[${#rowarray[@]}-1]'
			   for element in "${rowarray[@]}"
               do

	                printf '%s ,' "$element"
               done
			   printf '\n'
			   rowarray=()
			   rowarray+=("${array[$i]}")

			fi

	   fi



       #printf "%s\t%s\n" "$i" "${array[$i]}"
     done
done < "gene1A.csv"
