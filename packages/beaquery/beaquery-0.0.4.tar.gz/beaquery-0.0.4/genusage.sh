#! /bin/sh
#set -ex


D=src/beaquery


for i in \
    beafixedassets.py \
    beagdpbyind.py \
    beaiip.py \
    beainputoutput.py \
    beaissta.py \
    beaistrade.py \
    beaita.py \
    beamne.py \
    beanipa.py \
    beaniud.py \
    bearegional.py \
    beaugdpbyind.py \
    beaqueryq.py; do
     echo
     f=$(echo $i | cut -f1 -d.)
     echo '##'
     echo "## $f"
     echo '##'
     # python $D/$i -h |sed 's/ /&nbsp;/g'
     python $D/$i -h
     echo
done | while read line; do
    echo "$line<br/>"
done | sed 's/[.]py//'

