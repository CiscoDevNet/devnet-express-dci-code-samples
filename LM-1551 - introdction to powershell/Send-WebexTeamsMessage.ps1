<#

.SYNOPSIS
Send-WebexTeamsMessage, Send a Message to a Webex for Teams Room

.DESCRIPTION
Send-WebexTeamsMessage, Send a Message to a Webex for Teams Room

.NOTES
John McDonough, Cisco Systems, Inc. (jomcdono)

.PARAMETER apiToken
Your Webex for Teams API Token

.PARAMETER roomName
A Webex for Teams Room Name

.PARAMETER message
The Webex for Teams Message you wish to Send

.EXAMPLE
Send-WebexTeamsMessage.ps1 -ApiToken "ZDNiZmFiOWEtN2Y3Zi00YjI3LWI3NWItYmNkNzQxOTUyYmZiNWQ0ZTY5N2ItOTlj" -RoomName "DevNet Express DCI Event Room" -Message "I have completed the Introduction to PowerShell Mission"

#>
param(
  [Parameter(Mandatory=$true,HelpMessage="Enter your API Token - put in double quotes `" please.")]
    [string] $apiToken,

  [Parameter(Mandatory=$true,HelpMessage="Enter a Room Name - put in double quotes `" please.")]
  [AllowEmptyString()]
    [string] $roomName,

  [Parameter(Mandatory=$true,HelpMessage="Enter a message - put in double quotes `" please.")]
  [AllowEmptyString()]
    [string] $message
);

# Set up support for ssl and tls
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Ssl3 -bor [System.Net.SecurityProtocolType]::Tls -bor [System.Net.SecurityProtocolType]::Tls11 -bor [System.Net.SecurityProtocolType]::Tls12

# Set up the header
    $headers = @{"Authorization" = "Bearer $apiToken"; "Content-Type" = "application/json"; "Acccept" = "application/json"}

    try {
        # Get the Id of the Room
        if ($roomName.Length -gt 0) {
            
            $webResponse = Invoke-WebRequest -Uri https://api.ciscospark.com/v1/rooms -Headers $headers
            $roomId = $webResponse.Content | ConvertFrom-Json | %{$_.items | ?{$_.title -eq $roomName} |  Select-Object id}
            
            if ($roomId.Length -eq 0 -and ($webResponse.Headers["Link"].Split(';')[1] -eq ' rel="next"')) {
                While($true) {

                    $nextLink = $webResponse.Headers["Link"].Split(';')[0].replace("<","").replace(">","")
                    $webResponse = Invoke-WebRequest -Uri $nextLink -Headers $headers
                    $roomId = $webResponse.Content | ConvertFrom-Json | %{$_.items | ?{$_.title -eq $roomName} |  Select-Object id}
                    if ($roomId.id.Length -gt 0 -or $webResponse.Headers["Link"].Length -eq 0) {break}
                }
            }

        } else {
            Write-Host "Please specify a Room."
            exit
        }
        } else {
            Write-Host -ForegroundColor Red "Room: `"$roomName`" was not found!"
        }
    } catch {
        Write-Host "There seems to be a problem!"
        Write-Host "StatusCode:" $_.Exception.Response.StatusCode.value__
        Write-Host "StatusDescription:" $_.Exception.Response.StatusDescription
        exit
    }
