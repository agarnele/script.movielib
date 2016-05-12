# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import json

__addon__               = xbmcaddon.Addon()
__addon_id__            = __addon__.getAddonInfo('id')

__trigger__ = {
    'Player.OnStop':                    __addon__.getSetting('OnStop'),
    'VideoLibrary.OnScanFinished':      __addon__.getSetting('OnScanFinished'),
    'VideoLibrary.OnCleanFinished':     __addon__.getSetting('OnCleanFinished'),
    'System.OnWake':                    __addon__.getSetting('OnWake')
}

class Monitor(xbmc.Monitor):

    def __init__(self):
        xbmc.Monitor.__init__(self)
                
        # start Movielib on KODI start
        if 'true' in __addon__.getSetting('OnStart'):
            xbmc.executebuiltin('XBMC.RunScript(' + __addon_id__ + ', 1)')
        
    def onNotification(self, sender, method, data):
    
        # start Movielib for update banner (Now Playing)
        if method == 'Player.OnPlay':
            data = json.loads(data)
            if 'item' in data and 'type' in data['item'] and 'id' in data['item']:
                xbmc.executebuiltin('XBMC.RunScript(' + __addon_id__ + ', 1, ' + str(data['item']['id']) + ', ' + data['item']['type'] + ')')
        
        # start Movielib on trigger
        if method in __trigger__.keys() and 'true' in __trigger__[method]:
            xbmc.executebuiltin('XBMC.RunScript(' + __addon_id__ + ', 1)')
        
monitor = Monitor()

while(not xbmc.abortRequested):
    xbmc.sleep(100)
    