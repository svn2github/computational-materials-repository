cd /tmp
svn co https://svn.fysik.dtu.dk/projects/ase/trunk ase
cd ase
wget https://cmr.fysik.dtu.dk/_downloads/dcdft.db
PYTHONPATH=.:$PYTHONPATH PATH=tools:$PATH ase-db dcdft.db calculator=aims,basis=tight,relativistic=scalar -i dcdft_aims_tight.db
wget https://svn.fysik.dtu.dk/projects/cmr2/trunk/dcdft/extract.py
python extract.py dcdft_aims_tight.db
wget https://molmod.ugent.be/sites/default/files/Delta_v3-0.zip
unzip -p Delta_v3-0.zip  history.tar.gz > history.tar.gz
tar zxf history.tar.gz
sed '1,/with tight/d;/with light/,$d'  history/AIMS-history.txt > web.txt
diff -w web.txt dcdft_aims_tight.db_raw.txt
