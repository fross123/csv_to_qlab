#!/usr/bin/env python3
"""Entry point for PyInstaller GUI builds"""
from app.application import app
import webview

if __name__ == "__main__":
    webview.create_window("CSV to QLab", app, frameless=True, width=300, height=465)
    webview.start()
