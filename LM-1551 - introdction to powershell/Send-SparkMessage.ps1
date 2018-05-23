<#

.SYNOPSIS
Send-WebexTeamsMessage, Send a Webex Teams Message to a Webex Teams Room

.DESCRIPTION
Send-WebexTeamsMessage, Send a Webex Teams Message to a Webex Teams Room

.NOTES
John McDonough, Cisco Systems, Inc. (jomcdono)

.PARAMETER WebexTeamsApiToken
Your Webex Teams API Token

.PARAMETER WebexTeamsRoomName
A Webex Teams Room Name

.PARAMETER WebexTeamsMessage
The Webex Teams Message you wish to Send

.EXAMPLE
Send-WebexTeamsMessage.ps1 -WebexTeamsApiToken "ZDNiZmFiOWEtN2Y3Zi00YjI3LWI3NWItYmNkNzQxOTUyYmZiNWQ0ZTY5N2ItOTlj" -WebexTeamsRoomName "DevNet Express DCI Event Room" -WebexTeamsMessage "Hi how's the DevNet Express DCI event"

#>
param(
  [Parameter(Mandatory=$true,HelpMessage="Enter your Webex Teams API Token - put in double quotes `" please.")]
    [string] $WebexTeamsApiToken,

  [Parameter(Mandatory=$true,HelpMessage="Enter a Webex Teams Room Name - put in double quotes `" please.")]
  [AllowEmptyString()]
    [string] $WebexTeamsRoomName,

  [Parameter(Mandatory=$true,HelpMessage="Enter a message - put in double quotes `" please.")]
  [AllowEmptyString()]
    [string] $WebexTeamsMessage
);

# Set up the Header

    $headers = @{"Authorization" = "Bearer $WebexTeamsApiToken"; "Content-Type" = "application/json"; "Acccept" = "application/json"}

    try {
        # Get the Id of the Webex Teams Room
        if ($WebexTeamsRoomName.Length -gt 0) {
            $webexteamsRoomId = Invoke-RestMethod -Uri https://api.ciscospark.com/v1/rooms -Headers $headers | %{$_.items | ?{$_.title -eq $WebexTeamsRoomName} |  Select-Object id}
        } else {
            Write-Host "Please specify a Webex Teams Room."
            exit
        }

        # Send a Message to the Webex Teams Room
        if ($webexteamsRoomId) {
            if ($WebexTeamsMessage.Length -gt 0) {
                $invokeRestResponse = Invoke-RestMethod -Uri https://api.ciscospark.com/v1/messages -Method POST -Headers $headers -Body $('{"roomId":"' + $webexteamsRoomId.id + '", "text": "' + $WebexTeamsMessage + '"}')
                if ($invokeRestResponse.id) {
                    Write-Host "The message was sucessfully sent"
                }
            } else {
                Write-Host "Please specify a Message."
                exit
            }
        } else {
            Write-Host -ForegroundColor Red "Webex Teams Room: `"$WebexTeamsRoomName`" was not found!"
        }
    } catch {
        Write-Host "There seems to be a problem!"
        Write-Host "StatusCode:" $_.Exception.Response.StatusCode.value__
        Write-Host "StatusDescription:" $_.Exception.Response.StatusDescription
        exit
    }
