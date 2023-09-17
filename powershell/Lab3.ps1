function getIP{
(Get-NetIPAddress).IPv4Address | Select-String "192*"

}
function getVersion{
$Host.Version.Major
}
function getUserType{
Get-LocalUser | Select-String "Admin*"
}



$IP = getIP
$Version = getVersion
$HostName = hostname
$Date = Get-Date -DisplayHint Date
$Type = getUserType

$Body = "This machine's IP is $IP. User is $Type. HostName is $HostName. PowerShell Version $Version. Today's Date is Tuesday, $Date."
$Body | Out-File C:\Lab3_Output