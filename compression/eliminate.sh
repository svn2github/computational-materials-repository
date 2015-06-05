rm -f *remove*csv
# remove all systems that give large scatter of results
for f in *energies.csv
do
nf=`echo $f | rev | cut -d. -f3- | rev`.remove.db_energies.csv
cp -fv $f $nf
# missing aims tier2 atomic_zora scalar
sed -i '/^Sm,/d' $nf
sed -i '/^Eu,/d' $nf
sed -i '/^Gd,/d' $nf
sed -i '/^Tb,/d' $nf
sed -i '/^Dy,/d' $nf
sed -i '/^Ho,/d' $nf
sed -i '/^Er,/d' $nf
sed -i '/^Tm,/d' $nf
# restore nrel results
if ! test -z `echo $f | grep nrel`
then
cp -fv $f $nf
fi
done
# rocksalt individual codes
sed -i 's/He,.*/He,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Si,.*/Si,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Co,.*/Co,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Ni,.*/Ni,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Cu,.*/Cu,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Ga,.*/Ga,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Y,.*/Y,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Cd,.*/Cd,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Lu,.*/Lu,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/W,.*/W,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Ir,.*/Ir,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Pt,.*/Pt,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Au,.*/Au,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Hg,.*/Hg,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Tl,.*/Tl,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/Th,.*/Th,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
sed -i 's/No,.*/No,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' rocksalt.exciting.nrel.remove.db_energies.csv
# fcc individual codes
rs='nrel srel'
for r in $rs;
do
sed -i 's/Be,.*/Be,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Si,.*/Si,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/P,.*/P,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Co,.*/Co,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Cu,.*/Cu,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Ge,.*/Ge,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Se,.*/Se,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Cd,.*/Cd,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/In,.*/In,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Sb,.*/Sb,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Te,.*/Te,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/I,.*/I,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Xe,.*/Xe,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Cs,.*/Cs,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Ba,.*/Ba,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/La,.*/La,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Ce,.*/Ce,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Dy,.*/Dy,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Tm,.*/Tm,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Ir,.*/Ir,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Os,.*/Os,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Au,.*/Au,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Pt,.*/Pt,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Hg,.*/Hg,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Tl,.*/Tl,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Pb,.*/Pb,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Bi,.*/Bi,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/At,.*/At,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Po,.*/Po,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Rn,.*/Rn,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Fr,.*/Fr,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Ra,.*/Ra,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Ac,.*/Ac,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Pa,.*/Pa,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Bk,.*/Bk,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
sed -i 's/Es,.*/Es,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.elk.${r}.remove.db_energies.csv
done
#
sed -i 's/Pr,.*/Pr,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.exciting.nrel.remove.db_energies.csv
sed -i 's/Ir,.*/Ir,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.exciting.nrel.remove.db_energies.csv
sed -i 's/Pt,.*/Pt,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.exciting.nrel.remove.db_energies.csv
sed -i 's/Th,.*/Th,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.exciting.nrel.remove.db_energies.csv
sed -i 's/Am,.*/Am,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.exciting.nrel.remove.db_energies.csv
#
sed -i '/Tm/d' fcc.exciting.zora.remove.db_energies.csv
sed -i 's/Am,.*/Am,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.exciting.zora.remove.db_energies.csv
sed -i 's/Pu,.*/Pu,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' fcc.exciting.zora.remove.db_energies.csv
#
sed -i 's/Ne,.*/Ne,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Cs,.*/Cs,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Pr,.*/Pr,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i '/Tm/d' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Fr,.*/Fr,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Ra,.*/Ra,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Th,.*/Th,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/U,.*/U,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Pu,.*/Pu,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Am,.*/Am,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Cf,.*/Cf,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Es,.*/Es,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
sed -i 's/Fm,.*/Fm,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan/' 'fcc.exciting.iora*.remove.db_energies.csv'
