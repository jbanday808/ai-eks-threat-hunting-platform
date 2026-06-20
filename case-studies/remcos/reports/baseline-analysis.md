# Remcos RAT Baseline Analysis

## Overview

A 60-second Noriben baseline capture was performed before Remcos RAT analysis. This baseline represents normal system activity and will be used to compare future malware behavior.

## Lab Environment

- Windows 11 Enterprise VM
- Noriben v2.0.4
- Microsoft Sysinternals Procmon
- Python 3.13
- Output Folder: C:\Analysis\Remcos

## Tools Used

- Noriben
- Procmon
- PowerShell
- VS Code

## Baseline Findings

The baseline capture showed normal system activity, including:

- Windows service activity
- Splunk Universal Forwarder activity
- Microsoft Defender activity
- AMA monitoring activity
- File creation events
- Registry activity
- Network activity

## Screenshots

- `img/remcos/remcos-noriben-baseline-report.png`
- `img/remcos/remcos-noriben-timeline.csv.png`
- [Updated repository structure](../../../img/remcos/remcos-project-folders.png)

## Purpose of Baseline

This baseline helps separate normal system activity from future Remcos RAT behavior.

## Summary

Noriben and Procmon were successfully configured, and a clean baseline capture was completed before malware behavior analysis.
