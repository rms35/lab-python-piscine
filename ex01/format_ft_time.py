#!/usr/bin/env python3

from datetime import datetime
try:
	now = datetime.now()
	epoch = datetime.fromtimestamp(0)
	ts = int(now.timestamp())
	string = epoch.strftime("%B %d, %Y")
	print(f"Seconds since {string}: {ts:,} or {ts:e} in scientific notation")
	ts = now.date()
	string = ts.strftime("%B %d, %Y")
	print(string)
except Exception as e:
	print(f"Error: {e}")