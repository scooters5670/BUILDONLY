import urlparse , sys , re
import urllib , urllib2
from urlparse import parse_qsl
import requests
import xml . etree . ElementTree as ET
import xbmcaddon , os
import base64
import xbmcgui
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
IiII1IiiIiI1 = dict ( urlparse . parse_qsl ( sys . argv [ 2 ] . replace ( '?' , '' ) ) )
if 40 - 40: oo * OoO0O00
IIiIiII11i = IiII1IiiIiI1 . get ( 'action' )
if 51 - 51: oOo0O0Ooo * I1ii11iIi11i
I1IiI = IiII1IiiIiI1 . get ( 'content' )
if 73 - 73: OOooOOo / ii11ii1ii
O00ooOO = IiII1IiiIiI1 . get ( 'name' )
if 47 - 47: oO0ooO % iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
o0oO0 = IiII1IiiIiI1 . get ( 'url' )
if 100 - 100: i11Ii11I1Ii1i
Ooo = IiII1IiiIiI1 . get ( 'image' )
if 56 - 56: ooO00oOoo - O0OOo
II1Iiii1111i = IiII1IiiIiI1 . get ( 'fanart' )
if 25 - 25: oO0o0ooO0
oo00000o0 = xbmcaddon . Addon ( ) . getAddonInfo ( "path" )
if 34 - 34: i11Ii11I1Ii1i % II111iiii % iIii1I11I1II1 % i11Ii11I1Ii1i * iiIIIII1i1iI / I1ii11iIi11i
def Iiii ( st ) :
 import re
 st = re . sub ( '\[.+\]' , '' , st )
 import string
 OOO0O = 0
 for oo0ooO0oOOOOo in st :
  if oo0ooO0oOOOOo in 'lij|\' ' : OOO0O += 37
  elif oo0ooO0oOOOOo in '![]fI.,:;/\\t' : OOO0O += 50
  elif oo0ooO0oOOOOo in '`-(){}r"' : OOO0O += 60
  elif oo0ooO0oOOOOo in '*^zcsJkvxy' : OOO0O += 85
  elif oo0ooO0oOOOOo in 'aebdhnopqug#$L+<>=?_~FZT' + string . digits : OOO0O += 95
  elif oo0ooO0oOOOOo in 'BSPEAKVXY&UwNRCHD' : OOO0O += 112
  elif oo0ooO0oOOOOo in 'QGOMm%W@' : OOO0O += 135
  else : OOO0O += 50
 return int ( OOO0O * 6.5 / 100 )
 if 71 - 71: ooO00oOoo
def O0OoOoo00o ( Heading = xbmcaddon . Addon ( ) . getAddonInfo ( 'name' ) ) :
 iiiI11 = xbmc . Keyboard ( '' , Heading )
 iiiI11 . doModal ( )
 if ( iiiI11 . isConfirmed ( ) ) :
  return iiiI11 . getText ( )
  if 91 - 91: OOooOOo / II111iiii . ii11ii1ii + iI1Ii11111iIi
def iI11 ( url ) :
 if 17 - 17: OOooOOo
 import webbrowser
 if 64 - 64: oO0o0ooO0 % i1IIi % OoooooooOO
 i1iIIi1 = webbrowser . open
 ii11iIi1I = xbmc . executebuiltin
 iI111I11I1I1 = lambda OOooO0OOoo : xbmc . getCondVisibility ( str ( OOooO0OOoo ) )
 iIii1 = lambda OOooO0OOoo : ii11iIi1I ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( OOooO0OOoo ) )
 if 71 - 71: oOo0O0Ooo
 oO0O = 'System.Platform.Android'
 if 70 - 70: OoO0O00 % OoO0O00 . i11Ii11I1Ii1i % oOo0O0Ooo * OOooOOo % oO0ooO
 if iI111I11I1I1 ( oO0O ) : iIii1 ( base64 . b64decode ( url ) )
 else : i1iIIi1 ( base64 . b64decode ( url ) )
 if 23 - 23: i11iIiiIii + oo
 if 68 - 68: I1ii11iIi11i . oO0ooO . i11iIiiIii
def II ( ) :
 if 14 - 14: OoO0O00 . oo / oO0o0ooO0
 if 38 - 38: II111iiii % i11iIiiIii . O0OOo - iI1Ii11111iIi + oO0o0ooO0
 import sys
 if 66 - 66: OoooooooOO * OoooooooOO . iI1Ii11111iIi . i1IIi - iI1Ii11111iIi
 o0o00ooo0 = 'aHR0cHM6Ly9vZmZzaG9yZXBsdWdpbnMuY29tL3BvcnRhbC9hcHBsaWNhdGlvbi5waHA/aWQ9cGx1Z2luLnZpZGVvLkZURkE='
 oo0Oo00Oo0 = 'NjgxNjBlYTAzOWU3YjJi'
 oOOO00o = base64 . b64decode ( 'aHR0cDovL29mZnNob3JlcGx1Z2lucy5jb20vcG9ydGFsL2FwaS5waHA/cGluPSVzJmtleT0=' ) + base64 . b64decode ( oo0Oo00Oo0 )
 O0O00o0OOO0 = 'W0NPTE9SIGJsdWVdSW4gb3JkZXIgdG8gY29udGludWUgcGxlYXNlWy9DT0xPUl0gW0NPTE9SIHdoaXRlXVtCXVZFUklGWVsvQl1bL0NPTE9SXSBbQ09MT1IgYmx1ZV15b3VyIGRldmljZSBieSBnZXR0aW5nIGFbL0NPTE9SXVtDT0xPUiB3aGl0ZV1bQl0gRlJFRSBQSU5bL0JdWy9DT0xPUl1bQ09MT1IgYmx1ZV0gZnJvbSBvdXIgd2Vic2l0ZSBhbmQgZW50ZXJpbmcgdGhlIHBpbiBvbiB0aGUgbmV4dCBwcm9tdC4gIFsvQ09MT1JdW0NPTE9SIHdoaXRlXVtCXXwgICB3d3cub2Zmc2hvcmVwbHVnaW5zLmNvbS9wb3J0YWwvYXBwc1svQl1bL0NPTE9SXQ=='
 if 27 - 27: O0 % i1IIi * oO0ooO + i11iIiiIii + OoooooooOO * i1IIi
 o0oo0o0O00OO = base64 . b64decode ( O0O00o0OOO0 )
 o0oO = xbmcaddon . Addon ( ) . getAddonInfo
 I1i1iii = xbmcaddon . Addon ( ) . getSetting ( 'pin' )
 i1iiI11I = lambda OOooO0OOoo : base64 . b64decode ( str ( OOooO0OOoo ) )
 iiii = lambda OOooO0OOoo : requests . get ( oOOO00o % ( OOooO0OOoo ) ) . text . strip ( )
 oO0o0O0OOOoo0 = lambda OOooO0OOoo : xbmcaddon . Addon ( ) . setSetting ( base64 . b64decode ( 'cGlu' ) , OOooO0OOoo )
 IiIiiI = lambda OOooO0OOoo : xbmcgui . Dialog ( ) . yesno ( o0oO ( 'name' ) , OOooO0OOoo , yeslabel = "Get A Pin" , nolabel = 'Cancel' )
 I1I = bool ( iiii ( I1i1iii ) == base64 . b64decode ( 'UGluIFZlcmlmaWVk' ) )
 if 80 - 80: I1ii11iIi11i - oOo0O0Ooo
 if I1I : return
 else :
  if 87 - 87: oO0ooO / ii1II11I1ii1I - i1IIi * iI1Ii11111iIi / OoooooooOO . O0
  if 63 - 63: oOo0O0Ooo * oO0ooO - iiIIIII1i1iI * O0
  if 17 - 17: ii11ii1ii % II111iiii
  if 13 - 13: ooO00oOoo % I1ii11iIi11i - i11iIiiIii . oo + II111iiii
def II111ii1II1i ( ) :
 OoOo00o = urllib . urlopen ( "https://gist.githubusercontent.com/Biggyoz/c84b100698e48b62a53e7521e84e75b2/raw" ) . read ( )
 print "req.version = " + OoOo00o
 if OoOo00o == None :
  return 0
 else :
  return int ( OoOo00o )
  if 70 - 70: iiIIIII1i1iI * ii11ii1ii
def i1II1 ( ) :
 from resources . lib . indexers import hub
 print "hub.version = " + str ( hub . version )
 print "github.version = " + str ( II111ii1II1i ( ) )
 if hub . version < II111ii1II1i ( ) :
  OoOo00o = urllib . urlopen ( "https://gist.github.com/anonymous/ad13e976007e0b3857f591eb0686c7d9" ) . read ( )
  print "code got, updating NOW"
  if OoOo00o == None :
   print "Something went wrong!"
  else :
   print "hubfile.path = " + os . path . join ( oo00000o0 , "resources" , "lib" , "indexers" , "hub.py" )
   with open ( os . path . join ( oo00000o0 , "resources" , "lib" , "indexers" , "hub.py" ) , "wb" ) as OoO0O0 :
    OoO0O0 . write ( OoOo00o )
II ( )
if 21 - 21: oOo0O0Ooo * iIii1I11I1II1 % oO0ooO * i1IIi
if IIiIiII11i == None :
 from resources . lib . indexers import hub
 hub . indexer ( ) . root ( )
 if 16 - 16: O0 - ooO00oOoo * iIii1I11I1II1 + iiIIIII1i1iI
elif IIiIiII11i == 'directory' :
 from resources . lib . indexers import hub
 hub . indexer ( ) . get ( o0oO0 )
 if 50 - 50: II111iiii - O0OOo * ii11ii1ii / ooO00oOoo + OOooOOo
elif IIiIiII11i == 'qdirectory' :
 from resources . lib . indexers import hub
 hub . indexer ( ) . getq ( o0oO0 )
 if 88 - 88: oO0o0ooO0 / ooO00oOoo + iiIIIII1i1iI - II111iiii / O0OOo - I1ii11iIi11i
elif IIiIiII11i == 'xdirectory' :
 from resources . lib . indexers import hub
 hub . indexer ( ) . getx ( o0oO0 )
 if 15 - 15: ii11ii1ii + I1ii11iIi11i - OoooooooOO / iI1Ii11111iIi
elif IIiIiII11i == 'developer' :
 from resources . lib . indexers import hub
 hub . indexer ( ) . developer ( )
 if 58 - 58: i11iIiiIii % ii1II11I1ii1I
elif IIiIiII11i == 'tvtuner' :
 from resources . lib . indexers import hub
 hub . indexer ( ) . tvtuner ( o0oO0 )
 if 71 - 71: iI1Ii11111iIi + O0OOo % i11iIiiIii + ii11ii1ii - i11Ii11I1Ii1i
elif 'youtube' in str ( IIiIiII11i ) :
 from resources . lib . indexers import hub
 hub . indexer ( ) . youtube ( o0oO0 , IIiIiII11i )
 if 88 - 88: I1ii11iIi11i - oOo0O0Ooo % iI1Ii11111iIi
elif IIiIiII11i == 'play' :
 from resources . lib . indexers import hub
 hub . player ( ) . play ( o0oO0 , I1IiI )
 if 16 - 16: oo * oO0ooO % i11Ii11I1Ii1i
elif IIiIiII11i == 'browser' :
 from resources . lib . indexers import hub
 hub . resolver ( ) . browser ( o0oO0 )
 if 86 - 86: oo + oO0o0ooO0 % i11iIiiIii * oO0ooO . O0OOo * ii1II11I1ii1I
elif IIiIiII11i == 'search' :
 from resources . lib . indexers import hub
 hub . indexer ( ) . search ( )
 if 44 - 44: oO0ooO
elif IIiIiII11i == 'addSearch' :
 from resources . lib . indexers import hub
 hub . indexer ( ) . addSearch ( o0oO0 )
 if 88 - 88: ooO00oOoo % oO0o0ooO0 . II111iiii
elif IIiIiII11i == 'delSearch' :
 from resources . lib . indexers import hub
 hub . indexer ( ) . delSearch ( )
 if 38 - 38: OOooOOo
elif IIiIiII11i == 'queueItem' :
 from resources . lib . modules import control
 control . queueItem ( )
 if 57 - 57: O0 / oO0ooO * ooO00oOoo / I1ii11iIi11i . II111iiii
elif IIiIiII11i == 'openSettings' :
 from resources . lib . modules import control
 control . openSettings ( )
 if 26 - 26: iiIIIII1i1iI
elif IIiIiII11i == 'urlresolverSettings' :
 from resources . lib . modules import control
 control . openSettings ( id = 'script.module.urlresolver' )
 if 91 - 91: oOo0O0Ooo . ii11ii1ii + oOo0O0Ooo - iiIIIII1i1iI / OoooooooOO
elif IIiIiII11i == 'addView' :
 from resources . lib . modules import views
 views . addView ( I1IiI )
 if 39 - 39: ii11ii1ii / O0OOo - II111iiii
elif IIiIiII11i == 'downloader' :
 from resources . lib . modules import downloader
 downloader . downloader ( )
 if 98 - 98: ii11ii1ii / ii1II11I1ii1I % oO0ooO . I1ii11iIi11i
elif IIiIiII11i == 'addDownload' :
 from resources . lib . modules import downloader
 downloader . addDownload ( O00ooOO , o0oO0 , Ooo )
 if 91 - 91: oO0ooO % OoO0O00
elif IIiIiII11i == 'removeDownload' :
 from resources . lib . modules import downloader
 downloader . removeDownload ( o0oO0 )
 if 64 - 64: ii1II11I1ii1I % iiIIIII1i1iI - ooO00oOoo - oO0ooO
elif IIiIiII11i == 'startDownload' :
 from resources . lib . modules import downloader
 downloader . startDownload ( )
 if 31 - 31: ii1II11I1ii1I - II111iiii . ii1II11I1ii1I
elif IIiIiII11i == 'startDownloadThread' :
 from resources . lib . modules import downloader
 downloader . startDownloadThread ( )
 if 18 - 18: OOooOOo
elif IIiIiII11i == 'stopDownload' :
 from resources . lib . modules import downloader
 downloader . stopDownload ( )
 if 98 - 98: iiIIIII1i1iI * iiIIIII1i1iI / iiIIIII1i1iI + ii1II11I1ii1I
elif IIiIiII11i == 'statusDownload' :
 from resources . lib . modules import downloader
 downloader . statusDownload ( )
 if 34 - 34: O0OOo
elif IIiIiII11i == 'trailer' :
 from resources . lib . modules import trailer
 trailer . trailer ( ) . play ( O00ooOO )
 if 15 - 15: ii1II11I1ii1I * O0OOo * OoO0O00 % i11iIiiIii % I1ii11iIi11i - iI1Ii11111iIi
elif IIiIiII11i == 'clearCache' :
 from resources . lib . modules import cache
 cache . clear ( )
