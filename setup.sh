#!/bin/bash

echo "[*] Installing Python dependencies..."
pip install -r requirements.txt

echo "[*] Starting metrics exporter..."
python3 monitor/exporter.py
