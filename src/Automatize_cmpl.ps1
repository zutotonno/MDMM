Set-Location -Path E:\MDDM\Progetto\MDMM\dati

$current_folder = "inst_10_50_100_50_75_25_45_01_\"


$files = Get-ChildItem $current_folder -Filter *.cmpl
$sol_list = [System.Collections.ArrayList]@()
$mem_list = [System.Collections.ArrayList]@()
$time_list = [System.Collections.ArrayList]@()
$low_list = [System.Collections.ArrayList]@()
$gap_list = [System.Collections.ArrayList]@()
$instance_list = [System.Collections.ArrayList]@()
foreach ($f in $files){
    $curr_exec = cmpl $f.FullName
    $time_lines = $curr_exec | Select-String "time used"
    Write-Output $f
    Write-Output "*********************************"
    $current_time =  [decimal]$time_lines[0].Line.Split(":")[1].Split("secs")[0]
    $mem_line = $curr_exec | Select-String "Memory used"
    $current_mem =  [decimal]$mem_line[0].Line.Split(":")[1].Split("Mb")[0]
    $opt_lines = ($curr_exec | Select-String "time used" -Context 4 -SimpleMatch).Context.PreContext[0]
    $current_sol = [decimal]$opt_lines.Split("=")[1].Split(">=")[0]
    $low_sol_partial = $opt_lines.Split(">")[1].Split("%")[0].Split("=")[1]
    $low_sol_str = $low_sol_partial.Substring(0,$low_sol_partial.Length -6)
    $def_val = 0
    $low_sol = $current_sol
    $low_sol_parse = [decimal]::TryParse($low_sol_str, [ref]$def_val)
    if ($low_sol_parse){
        $low_sol = [decimal]$def_val
    }

    $gap = [decimal]$low_sol_partial.Substring($low_sol_partial.Length -6, 6)

    $sol_list.Add($current_sol)
    $mem_list.Add($current_mem)
    $time_list.Add($current_time)
    $low_list.Add($low_sol)
    $gap_list.Add($gap)
    $instance_list.Add($f.FullName)
}

$hash = @{instance=$instance_list;sol=$sol_list; low=$low_list; gap=$gap_list; time=$time_list; mem=$mem_list}
$file_name = $current_folder
$file_name += $current_folder.Substring(0,$current_folder.Length - 1)
$file_name += ".csv"
$hash.GetEnumerator() | Select-Object Name, @{n='Value'; e={$_.Value -join ', '}} | Export-Csv -NoTypeInformation -Path $file_name
