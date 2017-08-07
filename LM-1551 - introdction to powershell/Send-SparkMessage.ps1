<#

.SYNOPSIS
Send-SparkMessage, Send a Spark Message to a Spark Room

.DESCRIPTION
Send-SparkMessage, Send a Spark Message to a Spark Room

.NOTES
John McDonough, Cisco Systems, Inc. (jomcdono)

.PARAMETER SparkApiToken
Your Spark API Token

.PARAMETER SparkRoomName
A Spark Room Name 

.PARAMETER SparkMessage
The Spark Message you wish to Send

.EXAMPLE
Send-SparkMessage.ps1 -SparkApiToken "ZDNiZmFiOWEtN2Y3Zi00YjI3LWI3NWItYmNkNzQxOTUyYmZiNWQ0ZTY5N2ItOTlj" -SparkRoomName "DevNet Express DCI Event Room" -SparkMessage "Hi how's the DevNet Express DCI event"

#>
param(
  [Parameter(Mandatory=$true,HelpMessage="Enter your Spark API Token - put in double quotes `" please.")]
    [string] $SparkApiToken,

  [Parameter(Mandatory=$true,HelpMessage="Enter a Spark Room Name - put in double quotes `" please.")]
    [string] $SparkRoomName,
    
  [Parameter(Mandatory=$true,HelpMessage="Enter a message - put in double quotes `" please.")]
    [string] $SparkMessage
);
# Set up the Header

    $headers = @{"Authorization" = "Bearer $SparkApiToken"; "Content-Type" = "application/json"; "Acccept" = "application/json"}
  
    $sparkRoomId = Invoke-RestMethod -Uri https://api.ciscospark.com/v1/rooms -Headers $headers | %{$_.items | ?{$_.title -eq $SparkRoomName} |  Select-Object id}

    $sparkRoomId

    Invoke-RestMethod -Uri https://api.ciscospark.com/v1/messages -Method POST -Headers $headers -Body $('{"roomId":"' + $sparkRoomId.id + '", "text": "' + $SparkMessage + '"}')