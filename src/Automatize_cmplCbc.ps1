$culture = [cultureinfo]::GetCultureInfo('en-US')
    
$style = [Globalization.NumberStyles]::Float

$dir = dir D:\Lavoro\GitHub\MDMM\dati\datibuoni\dati1NewCbc
foreach($d in $dir)
{
	$path = Join-Path -Path $d.FullName -ChildPath "*"
	$dir2 = dir $path
	foreach($d2 in $dir2)
	{
		$current_folder = $d2.FullName
		$files = Get-ChildItem $current_folder -Filter *.cmpl
		$sol_list = [System.Collections.ArrayList]@()
		$time_list = [System.Collections.ArrayList]@()
		$low_list = [System.Collections.ArrayList]@()
		$instance_list = [System.Collections.ArrayList]@()
		foreach ($f in $files){
			$curr_exec = cmpl $f.FullName
			$time_lines = $curr_exec | Select-String "Total time"
			Write-Output $f
			Write-Output "*********************************"
			$current_time =  [decimal]$time_lines[-1].Line.Split("(")[1].Split(":")[1].Split("(")[0]
			$opt_lines = ($curr_exec | Select-String $time_lines[-1] -Context 12 -SimpleMatch).Context.PreContext[0]
			$current_sol = [decimal]$opt_lines.Split(":")[1]
			$low_sol = $current_sol
			$sol_list.Add($current_sol)
			$time_list.Add($current_time)
			$low_list.Add($low_sol)
			$instance_list.Add($f.FullName)
		}

		$hash = @{instance=$instance_list;sol=$sol_list; low=$low_list; time=$time_list}
		$file_name = $current_folder.FullName
		
		$file_name += $current_folder.Substring(0,$current_folder.Length)
		$file_name += ".csv"
		Write-Output "???????????????????????????"
		Write-Output $file_name
		$hash.GetEnumerator() | Select-Object Name, @{n='Value'; e={$_.Value -join '; '}} | Export-Csv -NoTypeInformation -Path $file_name
	}
}


##$current_folder = "inst_10_50_100_50_75_25_45_01_\"


##$files = Get-ChildItem $current_folder -Filter *.cmpl

