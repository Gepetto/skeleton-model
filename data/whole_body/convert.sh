#!/bin/bash
echo conversion fichiers stl to obj

for i in *.stl
	do
		ctmconv $(basename $i .${i##*.}).stl $(basename $i .${i##*.}).obj
	done

