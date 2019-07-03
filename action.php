<?php
	#echo "akshay";
	$nos = $_POST['switch'];
	$noc_voda = $_POST['voda_cu'];
	$noc_o2 = $_POST['o2_cu'];
	$noc_ee = $_POST['ee_cu'];
	$noc_3uk = $_POST['3uk_cu'];
	echo $nos,$noc_voda,$noc_o2,$noc_ee,$noc_3uk;
	echo(shell_exec("/bin/bash ./script.sh $nos $noc_voda $noc_o2 $noc_ee $noc_3uk 2>&1"));
	#echo(system("/usr/bin/python3 ./nexus_switch_configuration.py $nos $noc_voda $noc_o2 $noc_ee $noc_3uk 2>&1"));
	#echo(system("C:/Users/achoudhary/AppData/Local/Programs/Python/Python37/python.exe ./nexus_switch_configuration.py $nos $noc_voda $noc_o2 $noc_ee $noc_3uk 2>&1"));
?>
	
