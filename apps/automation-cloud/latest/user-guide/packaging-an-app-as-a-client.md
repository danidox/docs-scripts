---
title: "Packaging an App as a Client"
visible: true
slug: "packaging-an-app-as-a-client"
---

UiPath Apps are designed to be run in the browser but you can create a Windows executable to run them as well. To run a UiPath App as a Windows client executable, simply create an Electron wrapper that points to the production URL of an app. We've created a sample below to make this easy for you to use.

## Creating a Windows Executable for a UiPath App

1. Download the UiPath Apps Client Sample from GitHub and copy the files to a local directory, i.e. `C:\UiPathAppSample`.

**View:** https://github.com/UiPath/AppsClientSample
2. Modify the sample to meet your needs. Here are some of the key modifications:
   * icon.png - replace this with any icon you wish.
     :::note
     It is best if the icon is square.
     :::
   * main.js
   * RUNTIME_URL (line 7) - change this to point to the production URL of your App
   * Window Parameters (lines 18-27) - change these parameters to meet the needs of your app
   * package.json
   * displayName (line 3) - this will be used as the EXE name of your app
3. Open a command prompt and navigate to the directory containing the files.
4. Run `npm install` to install the node packages needed to build the app.
5. Run `npm run start` to open the app as a window client (this is good for testing the app).
6. Run `npm run dist` to build the app and package it with a Setup file. This will result in an EXE in the **dist** subdirectory (i.e. `dist\UiPath Apps sample Setup 1.2.0.exe`) which can be distributed to your users.