set -e  # stop after errors

# Update ASE:
cd ase
svn up

# Update CMR:
cd ../cmr
svn up

# Run Python scripts:
cd ../cmr
PYTHONPATH=../ase:$PYTHONPATH python run.py copy

# Build html:
rm -rf build/*/*
make html

# Use https for mathjax:
cd build
find -name "*.html" | xargs \
    sed -i "s%http://cdn.mathjax.org%https://cdn.mathjax.org%"
    
tar -czf html.tar.gz html
mv html.tar.gz ../..
cd ../..
