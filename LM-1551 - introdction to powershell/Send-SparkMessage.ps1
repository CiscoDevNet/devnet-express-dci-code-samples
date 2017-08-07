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
  [AllowEmptyString()]
    [string] $SparkRoomName,
    
  [Parameter(Mandatory=$true,HelpMessage="Enter a message - put in double quotes `" please.")]
  [AllowEmptyString()]
    [string] $SparkMessage
);

# Set up the Header

    $headers = @{"Authorization" = "Bearer $SparkApiToken"; "Content-Type" = "application/json"; "Acccept" = "application/json"}
  
    try {
        # Get the Id of the Spark Room
        if ($SparkRoomName.Length -gt 0) {
            $sparkRoomId = Invoke-RestMethod -Uri https://api.ciscospark.com/v1/rooms -Headers $headers | %{$_.items | ?{$_.title -eq $SparkRoomName} |  Select-Object id}
        } else {
            Write-Host "Please specify a Spark Room."
            exit
        }

        # Send a Message to the Spark Room
        if ($sparkRoomId) {
            if ($SparkMessage.Length -gt 0) {
                $invokeRestResponse = Invoke-RestMethod -Uri https://api.ciscospark.com/v1/messages -Method POST -Headers $headers -Body $('{"roomId":"' + $sparkRoomId.id + '", "text": "' + $SparkMessage + '"}')
                if ($invokeRestResponse.id) {
                    Write-Host "The message was sucessfully sent"
                }
            } else {
                Write-Host "Please specify a Message."
                exit
            }
        } else {
            Write-Host -ForegroundColor Red "Spark Room: `"$SparkRoomName`" was not found!"
        }
    } catch {
        Write-Host "There seems to be a problem!"
        Write-Host "StatusCode:" $_.Exception.Response.StatusCode.value__ 
        Write-Host "StatusDescription:" $_.Exception.Response.StatusDescription
        exit
    }