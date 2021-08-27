#!/bin/bash
function dwn() {
    mkdir -p "${1%/*}"
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
function mrg() {
    PR=$(echo "$1" | sed 's|R|P|')
    if [ -f "$PR" ]; then
        TD=$(echo "$1" | sed 's|R||')
        if [ ! -f "$TD" ]; then
            pdfunite "$PR" "$1" "$TD" 2>/dev/null
            if [ $? -eq 0 ]; then
                rm "$1"
                rm "$PR"
                echo "[MV] ${TD#*/} = $(basename $1) + $(basename $PR)"
            fi
        fi
    fi
}
function dup() {
    OT=$(echo "$1" | sed 's|L|I|')
    if [ -f "$OT" ]; then
        cmp "$1" "$OT" > /dev/null
        if [ $? -eq 0 ]; then
            FL=$(echo "$1" | sed 's|L||')
            mv "$1" "$FL"
            rm "$OT"
            echo "[MV] ${FL#*/} = $(basename $1) = $(basename $OT)"
        fi
    fi
}
mkdir -p examenes
cd examenes

# A1 CSSTIC
if [ -d "A1" ]; then
   echo "A1 ya existe, borrelo si quiere volver a descargarlo"
else
dwn A1/2015-1I 'https://sede.inap.gob.es/documents/59312/1776402/Examen_definitivo_plantilla_definitiva.pdf/85baf6cb-524c-059f-8f34-9873a0a7e144'
dwn A1/2015-2I 'https://sede.inap.gob.es/documents/59312/1776402/The%2520trust%2520machine.pdf/8b790ae3-1cc2-b49f-feda-abe72f1a656d'
dwn A1/2015-4I 'https://sede.inap.gob.es/documents/59312/1776402/examen_4ejercicio_TIC_2015_154AB89SD658.pdf/498e23b4-8e13-ed55-fbf4-fb85f4eae165'
dwn A1/2015-1L 'https://sede.inap.gob.es/documents/59312/1772422/Examen_definitivo_plantilla_definitiva.pdf/f6553fa6-6ffe-2db0-e04f-049c2f8e76d0'
dwn A1/2015-2L 'https://sede.inap.gob.es/documents/59312/1772422/The%2520trust%2520machine.pdf/ffbbfff4-20b0-371f-59a7-97cdf4079d72'
dwn A1/2015-3L 'https://sede.inap.gob.es/documents/59312/1772422/examen_3ejercicio_TIC_2015.pdf/61c5adcf-b551-919a-831b-f7f0699cdd9e'
dwn A1/2015-4L 'https://sede.inap.gob.es/documents/59312/1772422/examen_4ejercicio_TIC_2015_154AB89SD658.pdf/276be380-d205-429c-8a4f-55c61220c420'
dwn A1/2016-1I 'http://sede.inap.gob.es/documents/59312/1759489/PlantillaDefinitivaPrimerEjercicio_154AB89SD658.pdf/a76e3e15-8425-c4f3-fad9-8f83a4a4ff8c'
dwn A1/2016-2I 'http://sede.inap.gob.es/documents/59312/1759489/Texto%2520traducci%25c3%25b3n%2520publicaci%25c3%25b3n.pdf/b7af5da2-c51c-5ca3-56b2-52c0063f637d'
dwn A1/2016-4I 'http://sede.inap.gob.es/documents/59312/1759489/Enunciadocuartoejercicioyanexos-IMPRIMIR_154AB89SD658.pdf/a62659de-4c87-c787-e243-ad6c5a027856'
dwn A1/2016-1L 'http://sede.inap.gob.es/documents/59312/1787737/PlantillaDefinitivaPrimerEjercicio_154AB89SD658.pdf/1992f379-c8f6-e9f0-6043-0b611c1f6a8c'
dwn A1/2016-2L 'http://sede.inap.gob.es/documents/59312/1787737/Texto%2520traducci%25c3%25b3n%2520publicaci%25c3%25b3n.pdf/b77d08f3-2c1c-5ce8-96b7-515f6c8f870a'
dwn A1/2016-3L 'http://sede.inap.gob.es/documents/59312/1787737/Enunciados%2520Tercer%2520Ejercicio%2520publicaci%25c3%25b3n.pdf/3d25d423-b2d7-7820-4a3e-89d31da92580'
dwn A1/2016-4L 'http://sede.inap.gob.es/documents/59312/1787737/Enunciadocuartoejercicioyanexos-IMPRIMIR_154AB89SD658.pdf/4a502cf1-41a5-ec12-7815-0c475e2a15b7'
dwn A1/2017-1I_a 'http://sede.inap.gob.es/documents/59312/1752528/01aEjercicio1ModeloAPlantillaDEFINITIVA_154AB89SD658.pdf/0dcb9bbf-f197-ed81-bb71-2cb191b249f6'
dwn A1/2017-1I_b 'http://sede.inap.gob.es/documents/59312/1752528/01bEjercicio1ModeloBPlantillaDEFINITIVA_154AB89SD658.pdf/ca1873ca-8850-5c2b-a6bd-067d99984ea9'
dwn A1/2017-3I 'http://sede.inap.gob.es/documents/59312/1752528/2018-07-21Ejercicio3_154AB89SD658.pdf/ea1e4767-99bc-8e0a-38ae-a43d76b24247'
dwn A1/2017-1L_a 'http://sede.inap.gob.es/documents/59312/1742049/01aEjercicio1ModeloAPlantillaDEFINITIVA_154AB89SD658.pdf/6d12f752-f307-0d3a-5001-da545b9d14e9'
dwn A1/2017-1L_b 'http://sede.inap.gob.es/documents/59312/1742049/01bEjercicio1ModeloBPlantillaDEFINITIVA_154AB89SD658.pdf/eeae06c8-6fbd-e949-b362-41cd747d5929'
dwn A1/2017-3L 'http://sede.inap.gob.es/documents/59312/1742049/2018-07-21Ejercicio3_154AB89SD658.pdf/41cdbb7b-9c22-1560-4e68-dbd531a41f6f'
dwn A1/2017-4L 'http://sede.inap.gob.es/documents/59312/1742049/2018-12-15Ejercicio4_154AB89SD658.pdf/ee9e7a70-f800-c093-a7a3-9f8a3b70100f'
dwn A1/2018-1I 'http://sede.inap.gob.es/documents/59312/1765323/PlantilladefinitivaderespuestasCSTIC1ejercicio_154AB89SD658.pdf/9780b0d2-f6a7-ef8f-73d7-4daedaddd522'
dwn A1/2018-3I 'http://sede.inap.gob.es/documents/59312/1765323/2019-09-14Ejercicio3_154AB89SD658.pdf/7ce05f88-7864-68d7-fe6c-89334a31e34d'
dwn A1/2018-1L 'http://sede.inap.gob.es/documents/59312/1763823/PlantilladefinitivaderespuestasCSTIC1ejercicio_154AB89SD658.pdf/0e7b9f72-dac8-c305-a295-ebcaafa237e2'
dwn A1/2018-3L 'http://sede.inap.gob.es/documents/59312/1763823/2019-09-14Ejercicio3_154AB89SD658.pdf/f9356500-8822-56f1-e4a3-ea20effb71b1'
dwn A1/2018-4L 'http://sede.inap.gob.es/documents/59312/1763823/2019-12-21_Ejercicio_4_154AB89SD658.pdf/e6cb06dd-ff4f-dc6b-d2a7-dffd0b7db2bd'
dwn A1/2019-1.1I 'https://sede.inap.gob.es/documents/59312/1863988/Plantilla+Definitiva+Respuestas+Primer+Ejercicio+Ordinario+2019_.pdf/3cb1db5f-a78b-b0ac-caa3-a6cbcf18542f'
dwn A1/2019-1.2I 'https://sede.inap.gob.es/documents/59312/1863988/PlantillaCorrectoraDefinitiva_Examen+Extraordinario+2019.pdf/4d5354b5-3d3d-0dc2-324c-226c268a77e5'
dwn A1/2019-3I 'https://sede.inap.gob.es/documents/59312/1863988/CSSTIAE+-+Tercer+Ej+-+Enunciado_154AB89SD658.pdf/3275d6f0-2f38-d991-f8cc-c0513cdf0089'
dwn A1/2019-1.1L 'https://sede.inap.gob.es/documents/59312/1863992/Plantilla+Definitiva+Respuestas+Primer+Ejercicio+Ordinario+2019_.pdf/13a25068-7a54-67b9-fc4a-ad05f4acd51a'
dwn A1/2019-1.2L 'https://sede.inap.gob.es/documents/59312/1863992/PlantillaCorrectoraDefinitiva_Examen+Extraordinario+2019.pdf/1e40f204-6efb-77a7-64c7-07f21d79516f'
dwn A1/2019-3L 'https://sede.inap.gob.es/documents/59312/1863992/CSSTIAE+-+Tercer+Ej+-+Enunciado_154AB89SD658.pdf/2ed378ff-becb-b856-d64c-be7e3af3a5d9'
fi

# A2 GSI
if [ -d "A2" ]; then
   echo "A2 ya existe, borrelo si quiere volver a descargarlo"
else
dwn A2/2003-1IP 'http://www.zonacondeduque.com/B_ejer_1_promo_AGE_2003.doc'
dwn A2/2003-1IR 'http://www.zonacondeduque.com/B_sol_1_promo_AGE_2003.doc'
dwn A2/2003-1LP 'http://www.zonacondeduque.com/B_ejer_1_libre_AGE_2003.pdf'
dwn A2/2003-1LR 'http://www.zonacondeduque.com/B_sol_1_libre_AGE_2003.doc'
dwn A2/2004-1IP 'http://www.zonacondeduque.com/B_ejer_1_promo_AGE_2004.doc'
dwn A2/2004-1IR 'http://www.zonacondeduque.com/B_sol_1_promo_AGE_2004.doc'
dwn A2/2004-2I 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2004.pdf'
dwn A2/2004-1L 'http://www.zonacondeduque.com/B_ejer_sol_1_AGE_2004.pdf'
dwn A2/2004-3L 'http://www.zonacondeduque.com/B_ejer_3_AGE_2004.pdf'
dwn A2/2005-1IP 'http://www.zonacondeduque.com/B_ejer_1_promo_AGE_2005.doc'
dwn A2/2005-1IR 'http://www.zonacondeduque.com/B_sol_1_promo_AGE_2005.pdf'
dwn A2/2005-2I 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2005.pdf'
dwn A2/2005-1L 'http://www.zonacondeduque.com/B_ejer_sol_1_AGE_2005.pdf'
dwn A2/2005-2L 'http://www.zonacondeduque.com/B_ejer_2_AGE_2005.pdf'
dwn A2/2005-3L 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2005.pdf'
dwn A2/2006-1IP 'http://www.zonacondeduque.com/B_ejer_1_promo_AGE_2006.doc'
dwn A2/2006-1IR 'http://www.zonacondeduque.com/B_sol_1_promo_AGE_2006.pdf'
dwn A2/2006-2I 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2006.pdf'
dwn A2/2006-1LP 'http://www.zonacondeduque.com/B_ejer_sol_1_libre_AGE_2006.pdf'
dwn A2/2006-1LR 'http://www.baquedano.es/plant_prov.pdf'
dwn A2/2006-2L 'http://www.zonacondeduque.com/B_ejer_2_AGE_2006.pdf'
dwn A2/2006-3L 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2006.pdf'
dwn A2/2007-1IP 'http://www.zonacondeduque.es/B_ejer_1_promo_AGE_2007.rtf'
dwn A2/2007-1IR 'http://www.zonacondeduque.es/B_plan_prov_promo_AGE_2007.pdf'
dwn A2/2007-2I 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2007.pdf'
dwn A2/2007-1LP 'http://www.zonacondeduque.com/B_ejer_sol_1_libre_AGE_2007.pdf'
dwn A2/2007-1LR 'http://www.zonacondeduque.es/B_plan_prov_libre_AGE_2007.pdf'
dwn A2/2007-2L 'http://www.zonacondeduque.com/B_ejer_2_libre_AGE_2007.pdf'
dwn A2/2007-3L 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2007.pdf'
dwn A2/2008-1IP 'http://www.zonacondeduque.com/B_ejer_1_promo_AGE_2008.pdf'
dwn A2/2008-1IR 'http://www.zonacondeduque.com/B_sol_1_promo_AGE_2008.pdf'
dwn A2/2008-2I_3 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2008.pdf'
dwn A2/2008-2I_4 'http://www.baquedano.es/B_supu_IV_promo_AGE_2008.pdf'
dwn A2/2008-1LP 'http://www.baquedano.es/B_ejer_1_libre_AGE_2008.pdf'
dwn A2/2008-1LR 'http://www.zonacondeduque.com/B_sol_1_libre_AGE_2008.pdf'
dwn A2/2008-2L 'http://www.zonacondeduque.com/B_ejer_2_libre_AGE_2008.pdf'
dwn A2/2008-3L 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2008.pdf'
dwn A2/2009-1IP 'http://www.baquedano.es/B_ejer_1_promo_AGE_2009.pdf'
dwn A2/2009-1IR 'http://www.baquedano.es/B_sol_1_promo_AGE_2009.pdf'
dwn A2/2009-2I 'http://www.baquedano.es/B_ejer_2_promo_AGE_2009.pdf'
dwn A2/2009-1LP 'http://www.baquedano.es/B_ejer_1_libre_AGE_2009.pdf'
dwn A2/2009-1LR 'http://www.baquedano.es/B_sol_provi_1_libre_AGE_2009.pdf'
dwn A2/2009-3L 'http://www.baquedano.es/B_ejer_3_libre_AGE_2009.pdf'
dwn A2/2010-1IP 'http://www.zonacondeduque.es/B_ejer_1_promo_AGE_2010.pdf'
dwn A2/2010-1IR 'http://www.zonacondeduque.es/B_sol_1_promo_AGE_2010.pdf'
dwn A2/2010-2I 'http://www.zonacondeduque.es/B_ejer_2_promo_AGE_2010.pdf'
dwn A2/2010-1LP 'http://www.baquedano.es/B_ejer_1_libre_AGE_2010.pdf'
dwn A2/2010-1LR 'http://www.baquedano.es/B_sol_provi_1_libre_AGE_2010.pdf'
dwn A2/2010-3L 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2010.pdf'
dwn A2/2011-1IP 'http://www.zonacondeduque.com/B_ejer_1_promo_AGE_2011.pdf'
dwn A2/2011-1IR 'http://www.baquedano.es/B_sol_1_promo_AGE_2011.pdf'
dwn A2/2011-2I 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2011.pdf'
dwn A2/2011-1LP 'http://www.zonacondeduque.com/B_ejer_1_libre_AGE_2011.pdf'
dwn A2/2011-1LR 'http://www.baquedano.es/B_sol_1_libre_AGE_2011.pdf'
dwn A2/2011-3L 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2011.pdf'
dwn A2/2013-1IP 'http://www.zonacondeduque.com/B_ejer_1_promo_AGE_2013.pdf'
dwn A2/2013-1IR 'http://www.zonacondeduque.com/B_sol_1_promo_AGE_2013.pdf'
dwn A2/2013-2I 'http://www.zonacondeduque.com/B_ejer_2_promo_AGE_2013.pdf'
dwn A2/2013-1LP 'http://www.zonacondeduque.com/B_ejer_1_libre_AGE_2013.pdf'
dwn A2/2013-1LR 'http://www.zonacondeduque.com/B_sol_1_libre_AGE_2013.pdf'
dwn A2/2013-3L 'http://www.zonacondeduque.com/B_ejer_3_libre_AGE_2013.pdf'
dwn A2/2014-1IP 'https://sede.inap.gob.es/documents/59312/1775844/Examen%2520GSI-PI%25202014.pdf/94e3d78a-84d0-568f-0c02-bc5adab33186'
dwn A2/2014-1IR 'https://sede.inap.gob.es/documents/59312/1775844/Plantilla_definitiva%2520GSI-PI%25202014.pdf/1ee4e63a-e80d-8828-9f19-c219062aba0b'
dwn A2/2014-2I 'https://sede.inap.gob.es/documents/59312/1775844/GSIPI%2520SEGUNDO%2520OEP%25202014.pdf/6253a52e-949d-26c5-57dd-e3828ada0754'
dwn A2/2014-1LP 'https://sede.inap.gob.es/documents/59312/1741568/Examen%2520GSI-L%25202014.pdf/f55a7e28-a545-2291-7c3e-f183f263a0f0'
dwn A2/2014-1LR 'https://sede.inap.gob.es/documents/59312/1741568/Plantilla_definitiva%2520GSI-L%25202014.pdf/c98d5b64-4823-8ba6-4ea0-678f8029103a'
dwn A2/2014-2L 'https://sede.inap.gob.es/documents/59312/1741568/GSILI%2520SEGUNDO%2520OEP%25202014.pdf/29eb19b1-acca-e4e7-5a19-dc392da9bf5c'
dwn A2/2014-3L 'https://sede.inap.gob.es/documents/59312/1741568/GSILI%2520TERCERO%2520OEP%25202014%2520.pdf/9b4017b6-186f-f629-7816-78871d92ee0b'
dwn A2/2015-1I 'https://sede.inap.gob.es/documents/59312/1756216/Plantilla_definitiva%2520GSI-PI%2520%25c2%25b7%25201%25c2%25ba%2520Ejercicio%25202015.pdf/b733b813-7533-ab28-0d4c-f18e6a443451'
dwn A2/2015-2I 'https://sede.inap.gob.es/documents/59312/1756216/2015GSIPISEGUNDOOEP2015_154AB89SD658.pdf/98ebc880-13a4-2aac-52ec-158cf55e592f'
dwn A2/2015-1L 'https://sede.inap.gob.es/documents/59312/1788282/Plantilla_definitiva%2520GSI-L%2520%25c2%25b7%25201%25c2%25ba%2520Ejercicio%25202015.pdf/587abe99-be3c-4902-cbb2-5e28c8a50c73'
dwn A2/2015-2L 'https://sede.inap.gob.es/documents/59312/1788282/2015GSILIsegundocompleto_154AB89SD658.pdf/95218836-54d8-e8f9-67f0-b086f1a9859b'
dwn A2/2015-3L 'https://sede.inap.gob.es/documents/59312/1788282/GSI-LI-3ej.pdf/2ecf8d9f-82dc-608a-4efb-83d171ca063f'
dwn A2/2016-1IP 'https://sede.inap.gob.es/documents/59312/1745533/GSI%2520PI%252016.pdf/d1653568-4e56-7d5d-8168-8b5ac1c9a5ce'
dwn A2/2016-1IR 'https://sede.inap.gob.es/documents/59312/1745533/Plant_def_GSI-P_1_ejer_2016_154AB89SD658.pdf/6d53c18b-1215-dd1e-ec5e-9c14129026d3'
dwn A2/2016-2I 'https://sede.inap.gob.es/documents/59312/1745533/Cuestionario%252016SUGSI-PI.pdf/cb2be95b-2762-f3d2-2bfc-da643508854b'
dwn A2/2016-1LP 'https://sede.inap.gob.es/documents/59312/1764368/GSI%2520LI%252016.pdf/0d0badf2-9cc4-131b-a56a-c554716a7199'
dwn A2/2016-1LR 'https://sede.inap.gob.es/documents/59312/1764368/Plant_def_GSI-L_1_ejer_2016_154AB89SD658.pdf/55376621-0a77-d314-8fb3-2965ca1d956a'
dwn A2/2016-2L 'https://sede.inap.gob.es/documents/59312/1764368/2016%2520GSI-LI%25202%25c2%25ba%2520ejercicio.pdf/32ebef91-6869-dff6-6a22-4009747a4a01'
dwn A2/2016-3L 'https://sede.inap.gob.es/documents/59312/1764368/Supuesto2016_GSI-L_3EJ.pdf/1850e017-a477-5afa-e518-659eb5108c82'
dwn A2/2017-1IP 'https://sede.inap.gob.es/documents/59312/1766732/GSI%2520PI%25202017.pdf/040068a0-7b66-8a2d-2319-9f8fdc95b9e7'
dwn A2/2017-1IR 'https://sede.inap.gob.es/documents/59312/1766732/Plant_DefGSI-P1EJER_154AB89SD658.pdf/ae439a12-7f31-5adc-bec4-0cee5f24f264'
dwn A2/2017-2I 'https://sede.inap.gob.es/documents/59312/1766732/GSI-PIEnunciadoSegundo_154AB89SD658.pdf/2492605c-f5ed-e747-639c-5008161b94f3'
dwn A2/2017-1LP 'https://sede.inap.gob.es/documents/59312/1782867/GSI%2520LI%25202017.pdf/c2f3a332-59db-7d74-dfc6-7952368ef143'
dwn A2/2017-1LR 'https://sede.inap.gob.es/documents/59312/1782867/Plant_DefGSI-L1EJER_154AB89SD658.pdf/d2db3e22-9bc9-cc06-e528-07a8a478fb2b'
dwn A2/2017-2L 'https://sede.inap.gob.es/documents/59312/1782867/GSI-LEnunciadoSegundo_154AB89SD658.pdf/cf545381-e4df-6b74-0947-ceeea226aecc'
dwn A2/2017-3L 'https://sede.inap.gob.es/documents/59312/1782867/GSIL3EJ_154AB89SD658.pdf/3104b1b0-acce-dd3a-3e1e-5945f88d3330'
dwn A2/2018-1IP 'https://sede.inap.gob.es/documents/59312/1791385/SKM_C284e19102210060.pdf/90e4ee41-fd86-c725-c035-50c77361e6a5'
dwn A2/2018-1IR 'https://sede.inap.gob.es/documents/59312/1791385/Plantilla_def_GSI-P1ejer_154AB89SD658.pdf/e03e90c3-0764-1513-b947-64a9437f0931'
dwn A2/2018-2I 'https://sede.inap.gob.es/documents/59312/1791385/CUESTIONARIO%2520GSI%2520PI%2520SEGUNDO%2520EJERCICIO%2520OEP%25202018_154AB89SD658.pdf/22908dd2-2082-db31-c278-9dc935b4af59'
dwn A2/2018-1LP 'https://sede.inap.gob.es/documents/59312/1767342/03GSILI_154AB89SD658.pdf/3dd75634-4e55-4f6d-80a3-4bf20af1431e'
dwn A2/2018-1LR 'https://sede.inap.gob.es/documents/59312/1767342/Plantilla_def_GSI-L1ejer_154AB89SD658.pdf/c3adfef7-4330-05b0-a30a-672bceadd0d2'
dwn A2/2018-2L 'https://sede.inap.gob.es/documents/59312/1767342/CUESTIONARIO%2520GSI%2520LI%2520SEGUNDO%2520EJERCICIO%2520OEP%25202018_154AB89SD658.pdf/525a88ae-2a77-162d-59b8-c378db245d7b'
dwn A2/2018-3L 'https://sede.inap.gob.es/documents/59312/1767342/EXAMEN_3jer_GSILI_+OEP18_154AB89SD658.pdf/97634bc6-7c4d-122c-b239-ef2d0fb70399'
fi

# C1 TAI
if [ -d "C1" ]; then
   echo "C1 ya existe, borrelo si quiere volver a descargarlo"
else
dwn C1/2014-1IP 'https://sede.inap.gob.es/documents/59312/1763136/Examen%2520TAI-PI%25202014.pdf/e1988412-4b83-fcc9-343b-1b9da8a3c37e'
dwn C1/2014-1IR 'https://sede.inap.gob.es/documents/59312/1763136/Plantilla_definitiva%2520TAI-PI%25202014.pdf/106d31ea-c5d9-72a1-81ca-35f49b496712'
dwn C1/2015-1IP 'https://sede.inap.gob.es/documents/59312/1751002/Examen%2520TAI-PI%2520OEP%25202015.pdf/cbf7b050-ce54-2453-840d-a9d69a6b27ec'
dwn C1/2015-1IR 'https://sede.inap.gob.es/documents/59312/1751002/Plantilla_definitiva_TAI-PI.pdf/50c915f8-3ab4-7aea-e421-17444b1688f6'
dwn C1/2015-1L 'https://sede.inap.gob.es/documents/59312/1781726/Plant_def_TAI_L_%25201_ejer_154AB89SD658.pdf/95daefd5-7bc8-51f2-7058-c1b97d854af0'
dwn C1/2015-2LP 'https://sede.inap.gob.es/documents/59312/1781726/TAI-LI_2%25c2%25baEJ.pdf/cb48d6aa-b40f-4e75-1d80-92773e59de59'
dwn C1/2015-2LR 'https://sede.inap.gob.es/documents/59312/1781726/PLANT-DEF-TAI-L-2-EJER_154AB89SD658.pdf/61a9afcf-2552-4f6d-7fc2-609df1c2d6d1'
dwn C1/2016-1IP 'https://sede.inap.gob.es/documents/59312/1780758/TA%2520PI%252016.pdf/95b80084-97d2-e91a-8632-d64929c5812e'
dwn C1/2016-1IR 'https://sede.inap.gob.es/documents/59312/1780758/Plant_def_TAI-P_ej_unico_2016_154AB89SD658.pdf/bc768c4f-1a68-8e96-fb2e-d27c767b75d9'
dwn C1/2016-1LP 'https://sede.inap.gob.es/documents/59312/1784359/TAI%2520LI%252016.pdf/9269bf1e-d58c-f74e-8fef-7b6fcf49f0b8'
dwn C1/2016-1LR 'https://sede.inap.gob.es/documents/59312/1784359/Plant_defiTAI-L_1_2016_154AB89SD658.pdf/adaaf7cb-557a-13cf-0105-282091bcdf50'
dwn C1/2016-2LP 'https://sede.inap.gob.es/documents/59312/1784359/TAI%2520LI%252016%25202%25c2%25ba%2520EJERCICIO.pdf/4ea7283c-3166-d63d-270a-9c9c350f877c'
dwn C1/2016-2LR 'https://sede.inap.gob.es/documents/59312/1784359/Plan_def_TAI-L_%25202_ejr_2016.pdf/3dceb93a-4299-15d3-3d1d-49e8cbaf0270'
dwn C1/2017-1IP 'https://sede.inap.gob.es/documents/59312/1774459/TAI%2520PI%25202017.pdf/e6a6c6c7-f263-36c9-93ac-0214f3875c4f'
dwn C1/2017-1IR 'https://sede.inap.gob.es/documents/59312/1774459/Plantilla_definit-ejerc-unico-TAI-P_154AB89SD658.pdf/68de1674-244e-1d27-9083-c66fb44e3680'
dwn C1/2017-1LP 'https://sede.inap.gob.es/documents/59312/1768188/TAI%2520LI%25202017.pdf/9a020f13-bc8a-de32-ad89-157b79012125'
dwn C1/2017-1LR 'https://sede.inap.gob.es/documents/59312/1768188/Plant_DefTAI-L1EJER_154AB89SD658.pdf/24db2ced-793f-b81d-73b3-91428c94afee'
dwn C1/2017-2LP 'https://sede.inap.gob.es/documents/59312/1768188/EnunciadoTAI-L_154AB89SD658.pdf/06e3139d-f735-0594-336d-46635d115a98'
dwn C1/2017-2LR 'https://sede.inap.gob.es/documents/59312/1768188/Plantilla_definitiva%2520TAI-L%2520%25c2%25b7%2520Segundo%2520ejercicio%25202017.pdf/d8d88307-9343-9972-e58b-b31d28ff6665'
dwn C1/2018-1IP 'https://sede.inap.gob.es/documents/59312/1777270/08TAIPI_154AB89SD658.pdf/5b93e5e5-86bc-a169-8128-d3f8f073d9f2'
dwn C1/2018-1IR 'https://sede.inap.gob.es/documents/59312/1777270/Plantilla_defTAI-Pejerunico_154AB89SD658.pdf/0120eadc-9877-2a4c-51dd-02b625d9ef79'
dwn C1/2018-1LP 'https://sede.inap.gob.es/documents/59312/1790179/07TAIL_154AB89SD658.pdf/4c0b46eb-c8ff-1c9c-0749-06aab6f0a9e1'
dwn C1/2018-1LR 'https://sede.inap.gob.es/documents/59312/1790179/Plantilla_defTAI-L1ejer_154AB89SD658.pdf/a546831b-fe61-6dd4-230b-5171c13b27df'
dwn C1/2018-2LP 'https://sede.inap.gob.es/documents/59312/1790179/CUESTIONARIO__SEGUNDO_EJERCICIO_TAILI_%2520OEP_2018_154AB89SD658.pdf/a1909d6d-18d0-9b4b-d2ad-ebb02bd7ed8c'
dwn C1/2018-2LR 'https://sede.inap.gob.es/documents/59312/1790179/2jer_Plantilla_definitiva%2520TAILI_OEP2018__154AB89SD658.pdf/005c1328-6fb4-3a56-81db-acaa79c356d3'
fi

find . -name '*L*' -type f -print0 |
while IFS= read -r -d '' FL; do
  dup "$FL"
done
find . -name '*R*.pdf' -type f -print0 |
while IFS= read -r -d '' FL; do
  mrg "$FL"
done
