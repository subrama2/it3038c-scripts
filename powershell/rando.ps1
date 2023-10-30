$RANDO=0 

$Logfile = "C:\logs\rando.log" 

 

for($i=0; $i -lt 5; $i++){ 

    $RANDO=Get-Random -Maximum 1000 -Minimum 1 

    Write-Host($RANDO) 

    Add-Content $LogFile "INFO: Random number is ${RANDO}" 

} 
$Machines = 'localhost' 

Foreach ($machine in $Machines)  

{ 
$Machines = 'localhost' 

Foreach ($machine in $Machines)  

{ 

$pt = (Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 3).CounterSamples.CookedValue 

    $sample = 1 

    foreach ($p in $pt) { 

        $date = Get-Date -Format g 

        "{3} - Sample {2}: CPU is at {0}% on {1}" -f [int]$p, $machine, $sample, $date | Out-File -Append C:\output.txt 

        $sample++ 

    } 

} 
} 