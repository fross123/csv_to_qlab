---
sidebar_position: 1
---

# Welcome!

I have been working on a solution to a problem that arises constantly when utilizing the popular software QLab to trigger lights, sound, and projections from the same workspace.

To be able to facilitate these triggers, you usually need to put all of the MIDI and/or OSC cues in the workspace manually. The problem with this is that it is unnecessarily time consuming. You are creating a list that has already been created in your light board or in a spreadsheet, and since they are only “trigger” cues, they do not have the same subtle differences required of sound or video cues. It boils down to pretty much, “LX 12 GO”, “PQ 122 GO”.

As a solution, I wrote this application that takes a csv spreadsheet file and imports that “trigger” data rapidly and accurately.

:::note
Keep in mind this project is still in development and may have bugs or issues.
:::

:::tip
I recommend testing on an empty QLab workspace and copying the created cues into your working QLab workspace to avoid potential issues.
:::