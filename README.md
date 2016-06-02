# Extension Finder

Attempts to find installed browser extensions (sometimes called add-ons or plug-ins, depending on the browser).

## Features
Lists all available information for a given extension. Currently supports:

* Chrome
* Internet Explorer (Windows Only)

All features were tested on Windows 8.1 and MacOSX 10.11

## Install

With the repository cloned, create a virtual environment:

```
cd extension_finder
virtualenv venv
```

Activate the VirtualEnv on  MacOSX with:
```
source venv/bin/activate
```

Activate it on Windows with:
```
venv\Scripts\activate
```

Then install all requirements:
```
pip install -r requirements.txt
```

## Usage

Just run `extension_finder.py` from within the virtual environment.

### Chrome Preferences JSON

Chrome will store all of its Extension information within a `Preferences` file, if `extension_finder` 
can locate this file, you'll get good info from it:

```
$ python extension_finder.py

version    name                                    id
---------  --------------------------------------  --------------------------------
0.1        Chrome                                  mgndgikekgjfcpckkfioiadnlibdjbkf
1.0.1      Cisco WebEx Extension                   jlhmfgmfgeifomenelglieieghnjghma
14.1       Google Drive                            apdfllckaahabafndbhieahigkjlhalf
0.2.3      Spotify - Music for every moment        cnkjkdjlofllcpbemipjbcpfnglbgieh
0.2        Web Store                               ahfgeienlihckogmohjhadlkjgocpleb
3.0.15     Readability                             oknpjjbmpnndlpmnhmekjpocelpnlfdi
1.1        Google Sheets                           felcaaldnbdncclmgdcncolpebgiejap
1.2.0      Google Hangouts                         nkeimhogjdpnpccoofpliimaahmaaome
1.0        Google Network Speech                   neajdppkdcdipfabeoofebfddakdcjhd
0.9.38     CryptoTokenExtension                    kmendfapggjehodndflmmgagdbamhnfd
                                                   bepbmhgboaologfdajaanbcjmnhjmhfn
0.0.1.4    Hotword triggering                      nbpagnldghgfoolbancepceaanlmhfmd
0.1        Cloud Print                             mfehgcgbbipciphmccgaenjidiccnmng
34         feedly                                  hipbfijinpcgfogaopmgehiegacbhmob
1.0.8      Evernote Web                            lbfehkoinhhcknnbdgnnmjhiladcgbol
1.0        Feedback                                gfdkimpbcpahaombhbimeihdjnejgicl
1.4        Google Docs Offline                     ghbmnnjooekpmoecnnnilnnbdlolhkhi
2.0.6      Google Translate                        aapbdbdomjkkjkaonfhkkikfgjllcleb
0.9        Google Slides                           aapocclcgogkmnckokdopfmhonfmgoek
1          Chrome PDF Viewer                       mhjfbmdgcfjbbpaeojofohoefgiehjai
0.1        Bookmark Manager                        eemcgdkfndhakfknompkggombfjjjeno
0.2        Settings                                ennkphjdgehloodpbhlhldgbnhmacadg
0.0.1      GaiaAuthExtension                       mfffpogegjflfpflabcdkioaeobkgjik
8.1        Gmail                                   pjkljhegncpnkpknbcohdijeoejaedia
0.0.0.30   Google Search                           coobgpohoikkiipiblmjeljniedjpjpf
1.0.0.0    Chrome Web Store Payments               nmmhkkegccagdldgiimedpiccmgmieda
1.0.3      Slack                                   jeogkiiogjbmhklcnbgkdcjoioegiknm
4.2.8      YouTube                                 blpcfgokakmgnkcojhhkbfbldkacnbeo
0.9        Google Docs                             aohghmighlieiainnegkcijnfilokake
```

### Chrome Manifest.json Files

If `extension_finder.py` cannot find the `Preferences` file, it will traverse the home directory of the 
user it is being run under looking for `manifest.json` files. These often contain less rich information,
but do give you some idea of whats installed. The extension IDs can also be looked up in the Chrome extension
store. Note that you'll get a warning message that it could not parse the Chrome Preferences JSON.

```
C:\\extension_finder\\> python extension_finder.py
[+] Could not parse the Chrome Preferences JSON, falling back to extensions directory
version    name              id
---------  ----------------  --------------------------------
0.9        __MSG_appName__   aapocclcgogkmnckokdopfmhonfmgoek
0.9        __MSG_appName__   aohghmighlieiainnegkcijnfilokake
14.1       __MSG_appName__   apdfllckaahabafndbhieahigkjlhalf
4.2.8      __MSG_appName__   blpcfgokakmgnkcojhhkbfbldkacnbeo
1.1        __MSG_appName__   felcaaldnbdncclmgdcncolpebgiejap
1.4        __MSG_extName__   ghbmnnjooekpmoecnnnilnnbdlolhkhi
1.0.0.0    __MSG_APP_NAME__  nmmhkkegccagdldgiimedpiccmgmieda
8.1        __MSG_appName__   pjkljhegncpnkpknbcohdijeoejaedia
```

### Internet Explorer

Internet Explorer stores all of its extension information in the registry, which makes it straightforward to dump:

```
C:\\extension_finder\\> python extension_finder.py
path                                                                name                                           id
------------------------------------------------------------------  ---------------------------------------------  --------------------------------------
C:\Windows\System32\ieframe.dll                                     Microsoft Url Search Hook                      {CFBFAE00-17A6-11D0-99CB-00C04FD64497}
C:\Program Files\Microsoft Office\Office15\ONBttnIE.dll             Send to OneNote from Internet Explorer button  {48E73304-E1D6-4330-914C-F5F514E3486C}
C:\Program Files\Microsoft Office\Office15\ONBttnIELinkedNotes.dll  Linked Notes button                            {FFFDC614-B694-4AE6-AB38-5D6374584B52}
%SystemRoot%\System32\msxml3.dll                                    XML DOM Document                               {2933BF90-7B36-11D2-B20E-00C04F983E60}
C:\Windows\System32\Macromed\Flash\Flash.ocx                        Shockwave Flash Object                         {D27CDB6E-AE6D-11CF-96B8-444553540000}
C:\Windows\Downloaded Program Files\ieatgpc.dll                     GpcContainer Class                             {E06E2E99-0AA1-11D4-ABA6-0060082AA75C}
```

## PowerShell

Since not everyone uses Python on Windows, there is also a `FindIEExtensions.ps1` PowerShell script. To run it simply:

```
PS C:\Users\User\Desktop\extension_finder> .\FindIEExtensions.ps1

DLL                                                                Name                                          CLSID
---                                                                ----                                          -----
C:\Windows\System32\ieframe.dll                                    Microsoft Url Search Hook                     {CFBFAE00-17A...
C:\Windows\System32\msxml3.dll                                     XML DOM Document                              {2933BF90-7B3...
C:\Windows\System32\Macromed\Flash\Flash.ocx                       Shockwave Flash Object                        {D27CDB6E-AE6...
C:\Windows\Downloaded Program Files\ieatgpc.dll                    GpcContainer Class                            {E06E2E99-0AA...
C:\Program Files\Microsoft Office\Office15\ONBttnIE.dll            Send to OneNote from Internet Explorer button {48E73304-E1D...
C:\Program Files\Microsoft Office\Office15\ONBttnIELinkedNotes.dll Linked Notes button                           {FFFDC614-B69...
```
