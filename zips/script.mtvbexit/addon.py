import time
import xbmc
import os
import xbmcgui
import urllib2

HOME     = xbmc.translatePath('special://userdata/')
iddata   = os.path.join(HOME, 'networksettings.xml')

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Exit / Reboot[/COLOR][/B]', [
    '[B][COLOR=green]Run House Keeper and Reboot[/COLOR][/B]',
    '[B][COLOR=green]Exit Kodi[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 


def function1():

    if os.path.exists(iddata):
        with open(iddata, 'r') as mymega:
            userid=mymega.read()
        try: response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&die=1').read()
        except: pass
    xbmc.executebuiltin('RunAddon(script.program.megatvhousekeeper3)')

def function2():
    xbmc.executebuiltin("Notification(CerebroTV,Closing SPMC/Kodi, Will take a few seconds,7000,)")
    xbmc.sleep(1000)
    if os.path.exists(iddata):
        with open(iddata, 'r') as mymega:
            userid=mymega.read()
        try: response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&die=1').read()
        except: pass
    xbmc.executebuiltin('ActivateWindow(10001,"plugin://plugin.close.kodi/?description&fanart=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.close.kodi%5cfanart.jpg&iconimage=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.close.kodi%5cresources%5cart%5cforce.png&mode=10&name=Close%20System%20(Recommended)&url=fclose",return)')

menuoptions()