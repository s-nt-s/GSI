#!/bin/bash
function dwn() {
    DR=$(dirname "$1")
    if [ ! -z "$DR" ] && [ "$DR" != "." ] && [ ! -e "$DR" ]; then
        mkdir -p "DR"
    fi
    fil="$1"
    url="$2"
    ext="${url##*.}"
    if [[ " pdf doc docx rtf " =~ " ${ext} " ]]; then
        fil="${fil}.${ext}"
    else
        fil="${fil}.pdf"
    fi
    wget -q --no-check-certificate -O "$fil" $url
    if [ $? -eq 0 ]; then
        echo "[OK] $fil"
    else
        echo "[KO] $fil $url"
    fi
}

mkdir -p supuestos
cd supuestos

dwn 2004_A2.int 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2004.pdf'
dwn 2004_A2.lib 'http://www.zonacondeduque.com/B_ejer_3_AGE_2004.pdf'
dwn 2005_A2.int 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2005.pdf'
dwn 2005_A2.lib 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2005.pdf'
dwn 2006_A2.int 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2006.pdf'
dwn 2006_A2.lib 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2006.pdf'
dwn 2007_A2.int 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2007.pdf'
dwn 2007_A2.lib 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2007.pdf'
dwn 2008_A2.int_b3 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2008.pdf'
dwn 2008_A2.int_b4 'http://www.baquedano.es/B_supu_IV_promo_AGE_2008.pdf'
dwn 2008_A2.lib 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2008.pdf'
dwn 2009_A2.int 'http://www.baquedano.es/B_ejer_2_promo_AGE_2009.pdf'
dwn 2009_A2.lib 'http://www.baquedano.es/B_ejer_3_libre_AGE_2009.pdf'
dwn 2010_A2.int 'http://www.zonacondeduque.es/B_ejer_2_promo_AGE_2010.pdf'
dwn 2010_A2.lib 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2010.pdf'
dwn 2011_A2.int 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2011.pdf'
dwn 2011_A2.lib 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2011.pdf'
dwn 2013_A2.int 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2013.pdf'
dwn 2013_A2.lib 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2013.pdf'
dwn 2014_A2.int 'https://sede.inap.gob.es/documents/59312/1775844/GSIPI%2520SEGUNDO%2520OEP%25202014.pdf/6253a52e-949d-26c5-57dd-e3828ada0754'
dwn 2014_A2.lib 'https://sede.inap.gob.es/documents/59312/1741568/GSILI%2520TERCERO%2520OEP%25202014%2520.pdf/9b4017b6-186f-f629-7816-78871d92ee0b'
dwn 2015_A2.int 'https://sede.inap.gob.es/documents/59312/1756216/2015GSIPISEGUNDOOEP2015_154AB89SD658.pdf/98ebc880-13a4-2aac-52ec-158cf55e592f'
dwn 2015_A2.lib 'https://sede.inap.gob.es/documents/59312/1788282/GSI-LI-3ej.pdf/2ecf8d9f-82dc-608a-4efb-83d171ca063f'
dwn 2016_A2.int 'https://sede.inap.gob.es/documents/59312/1745533/Cuestionario%252016SUGSI-PI.pdf/cb2be95b-2762-f3d2-2bfc-da643508854b'
dwn 2016_A2.lib 'https://sede.inap.gob.es/documents/59312/1764368/Supuesto2016_GSI-L_3EJ.pdf/1850e017-a477-5afa-e518-659eb5108c82'
dwn 2017_A2.int 'https://sede.inap.gob.es/documents/59312/1766732/GSI-PIEnunciadoSegundo_154AB89SD658.pdf/2492605c-f5ed-e747-639c-5008161b94f3'
dwn 2017_A2.lib 'https://sede.inap.gob.es/documents/59312/1782867/GSIL3EJ_154AB89SD658.pdf/3104b1b0-acce-dd3a-3e1e-5945f88d3330'
dwn 2018_A2.int 'https://sede.inap.gob.es/documents/59312/1791385/CUESTIONARIO%2520GSI%2520PI%2520SEGUNDO%2520EJERCICIO%2520OEP%25202018_154AB89SD658.pdf/22908dd2-2082-db31-c278-9dc935b4af59'
dwn 2018_A2.lib 'https://sede.inap.gob.es/documents/59312/1767342/EXAMEN_3jer_GSILI_+OEP18_154AB89SD658.pdf/97634bc6-7c4d-122c-b239-ef2d0fb70399'