<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="plugin.video.ratomix"
       name="Ratomix"
       version="1.3"
       provider-name="Ratomix">
  <requires>
    <import addon="xbmc.python" version="2.1.0"/>
	<import addon="script.module.t0mm0.common" version="2.0.0"/>
    <import addon="script.module.beautifulsoup" version="3.2.1"/>
    <import addon="script.module.simple.downloader" version="0.9.4"/>
    <import addon="script.module.beautifulsoup4" />
    <import addon="script.module.simple.downloader" version="0.9.4"/>
    <import addon="script.module.requests" />
    <import addon="script.module.httplib2" />
    <import addon="script.module.youtube.dl" optional="true"/>
    <import addon="plugin.video.youtube" version="3.0.0"/>
    <import addon="script.module.urlresolver" optional="true"/>
    <import addon="script.module.simplejson" /> 
    <import addon="script.common.plugin.cache" version="2.5.2"/>
    <import addon="script.module.metahandler" version="2.5.1"/>

  </requires>
  <extension point="xbmc.python.pluginsource" library="default.py">
    <provides>video</provides>
  </extension>
  <extension point="xbmc.addon.metadata">
    <summary lang="en">Add-On Ratomixaddon </summary>
    <description lang="en">Add-On teste Ratomix</description>
    <platform>all</platform>
  </extension>
</addon>
