# remove all systems that give large scatter of results
for f in *.csv
do
nf=`echo $f | rev | cut -d. -f3- | rev`.remove.db.csv
cp -f $f $nf
# non-relativistic
sed -i '/Ti2/d' $nf
sed -i '/VN/d' $nf
sed -i '/CrH/d' $nf
sed -i '/FeF/d' $nf 
sed -i '/FeO/d' $nf
sed -i '/CoH/d' $nf
sed -i '/NiH/d' $nf
sed -i '/CuH/d' $nf
# scalar-relativistic
sed -i '/MnH/d' $nf
sed -i '/Fe2/d' $nf
sed -i '/CoO/d' $nf
sed -i '/Ni2/d' $nf
# espresso
sed -i '/TiO/d' $nf
sed -i '/Cr2/d' $nf
sed -i '/CrN/d' $nf
sed -i '/Mn2/d' $nf
sed -i '/FeH/d' $nf
# vasp semicore
sed -i '/Sc2/d' $nf
sed -i '/ScN/d' $nf
sed -i '/TiN/d' $nf
sed -i '/V2/d' $nf
sed -i '/CrO/d' $nf
done
