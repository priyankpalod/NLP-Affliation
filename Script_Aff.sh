echo "Script Started"
Directory=/users/user/Desktop/Palod
rm AllAffiliations.txt
for f in $Directory/pdfs/*.xml
do
    python $Directory/Aff_new.py<<EOF
$f
EOF
    python $Directory/printAff.py <<EOF
$f
EOF
echo $f " done"
done
gedit AllAffiliations.txt &
