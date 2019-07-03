<!DOCTYPE html>
<html>
<head><title> nexus configuration</title> </head>
<style>
.switch{
	width:  120%;
	background-color: #E8A41B;
}
.cu {
	width: 120%;
	background-color: #E8A41B;
}
.cus1 {
	width: 120%;
	background-color: #E8A41B;
}
.body{
	background-color: #ECD3A1;
}
.submit{
	background-color: #E8A41B;
}
</style>
<body class="body">
<center>
<br>
<h4> NEXUS CONFIGURATION </h4>
<br>
<form action="action.php" method="post" target="_blank">
<table>
<tr><td>
<label for="switch" > Please select number of Switches : </label></td>
<td><select name="switch" class="switch" >
<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>
<option value="4">4</option>
<option value="5">5</option>
<option value="6">6</option>
<option value="7">7</option>
<option value="8">8</option>
<option value="9">9</option>
<option value="10">10</option>
<option value="11">11</option>
</select></td></tr>
<tr><td><label for="voda_cu" > Please select number of CU for Vodafone : </label></td>
<td><select name="voda_cu" id="voda_cu" class="cu" >
<option value="0">0</option>
<option value="1">1</option>
<option value="2">2</option>
</select></td></tr>
<tr><td><label for="o2_cu" > Please select number of CU for O2 : </label></td>
<td><select name="o2_cu" id="o2_cu" class="cu" >
<option value="0">0</option>
<option value="1">1</option>
<option value="2">2</option>
</select></td></tr>
<tr><td><label for="ee_cu" > Please select number of CU for EE : </label></td>
<td><select name="ee_cu" id="ee_cu"class="cu" >
<option value="0">0</option>
<option value="1">1</option>
<option value="2">2</option>
</select></td></tr>
<tr><td><label for="3uk_cu" > Please select number of CU for 3UK : </label></td>
<td><select name="3uk_cu" id="3uk_cu" class="cu" >
<option value="0">0</option>
<option value="1">1</option>
<option value="2">2</option>
</select></td></tr>
<tr><td> <button type="submit" class="submit"> GENERATE </button></td><td></td></tr>
</table>
</form>	
</center>
</body>
</html>
