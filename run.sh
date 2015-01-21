set -e  # stop after errors

# Update ASE:
cd ase
svn up

# Update CMR:
cd ../cmr
svn up
cd ..

html=html.tar.gz

changes=`(find ase -newer $html | grep -v .svn;
          find cmr -newer $html | grep -v .svn;
          find db-files -newer $html)`
if [ -n "$changes" ]
then
    cd cmr
    # Run Python scripts:
    PYTHONPATH=../ase:$PYTHONPATH python run.py copy

    # Build html:
    rm -rf build/*/*
    make html

    # Use https for mathjax:
    cd build
    find -name "*.html" | xargs \
	sed -i "s%http://cdn.mathjax.org%https://cdn.mathjax.org%"
    
    tar -czf $html html
    mv $html ../..
    cd ../..
fi
