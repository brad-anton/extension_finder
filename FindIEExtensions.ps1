<#
.SYNOPSIS
  Dumps all install Internet Explorer Extensions (add-ons)

.DESCRIPTION
  Walks the registry to identify Internet Explorer Extensions for the currently logged in user

.INPUTS
  None

.OUTPUTS
  None (Screen Only)

.NOTES
  Version:        0.1
  Author:         @brad_anton (OpenDNS)
  Creation Date:  June 1, 2016
  Purpose/Change: Initial script development
  
.EXAMPLE
  
  FindIEExtensions.ps1
    DLL                                                                Name                                          CLSID                   
    ---                                                                ----                                          -----                   
    C:\Windows\System32\ieframe.dll                                    Microsoft Url Search Hook                     {CFBFAE00-17A6-11D0-9...
    C:\Windows\System32\msxml3.dll                                     XML DOM Document                              {2933BF90-7B36-11D2-B...
    C:\Windows\System32\Macromed\Flash\Flash.ocx                       Shockwave Flash Object                        {D27CDB6E-AE6D-11CF-9...
    C:\Windows\Downloaded Program Files\ieatgpc.dll                    GpcContainer Class                            {E06E2E99-0AA1-11D4-A...
    C:\Program Files\Microsoft Office\Office15\ONBttnIE.dll            Send to OneNote from Internet Explorer button {48E73304-E1D6-4330-9...
    C:\Program Files\Microsoft Office\Office15\ONBttnIELinkedNotes.dll Linked Notes button                           {FFFDC614-B694-4AE6-A...
#>

<#
    Utility Functions
#>

function Lookup-Clsid
{
    Param([string]$clsid)
    $CLSID_KEY = 'HKLM:\SOFTWARE\Classes\CLSID'

    If ( Test-Path $CLSID_KEY\$clsid) {
        $name = (Get-ItemProperty -Path $CLSID_KEY\$clsid).'(default)'
        $dll = (Get-ItemProperty -Path $CLSID_KEY\$clsid\InProcServer32).'(default)'
    }
    $name, $dll
}

function Make-Extension
{
    Param([string]$clsid, [string]$name, [string]$dll)
    
    $extension = New-Object PSObject -Prop (@{'CLSID' = $clsid;
                    'Name' = $name;
                    'DLL' = $dll })

    $extension
}

# Resulting list of Extension Properties 
$extensions = @()


<# 
    Extensions are identified in these Keys as properties containing the 
    CLSID.
#> 

$registry_keys = @( 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects',
                    'HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects',
                    'HKCU:\Software\Microsoft\Internet Explorer\UrlSearchHooks',
                    'HKLM:\Software\Microsoft\Internet Explorer\Toolbar',
                    'HKLM:\Software\Wow6432Node\Microsoft\Internet Explorer\Toolbar',
                    'HKCU:\Software\Microsoft\Internet Explorer\Explorer Bars',
                    'HKLM:\Software\Microsoft\Internet Explorer\Explorer Bars',
                    'HKCU:\Software\Wow6432Node\Microsoft\Internet Explorer\Explorer Bars',
                    'HKLM:\Software\Wow6432Node\Microsoft\Internet Explorer\Explorer Bars'
    )

ForEach ($key in $registry_keys) {
    If (Test-Path $key ) {
        $clsids = Get-Item -Path $key | Select-Object -Property Property | ForEach-Object Property
        ForEach ( $clsid in $clsids ) 
        {
            $name, $dll = Lookup-Clsid $clsid
            $extension = Make-Extension $clsid $name $dll
            $extensions += $extension
        }
    }
}



<# 
    Extensions are identified in these keys as subkeys named as the CLSID
#> 

$registry_keys = @( 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Ext\Stats' )

ForEach ($key in $registry_keys) {
    If (Test-Path $key ) {
        $clsids = Get-ChildItem $key -Name 
        ForEach ( $clsid in $clsids ) 
        {
            $name, $dll = Lookup-Clsid $clsid
            $extension = Make-Extension $clsid $name $dll
            $extensions += $extension
        }
    }
}


<#
    Extensions are identified in these keys as Values for the ClsidExtension
    Property within a subkeys named as some other ID.
#>

$registry_keys = @( 'HKCU:\Software\Microsoft\Internet Explorer\Extensions',
                    'HKLM:\Software\Microsoft\Internet Explorer\Extensions',
                    'HKCU:\Software\Wow6432Node\Microsoft\Internet Explorer\Extensions',
                    'HKLM:\Software\Wow6432Node\Microsoft\Internet Explorer\Extensions' )


ForEach ($key in $registry_keys) {
    If (Test-Path $key ) {
        $ids = Get-ChildItem $key -Name 
        ForEach ( $id in $ids ) 
        {
            $clsid = (Get-ItemProperty -Path $key\$id -Name ClsidExtension).'ClsidExtension'
            $name, $dll = Lookup-Clsid $clsid
            $extension = Make-Extension $clsid $name $dll
            $extensions += $extension
        }
    }
}

# Print Perty Table :)
$extensions | Format-Table