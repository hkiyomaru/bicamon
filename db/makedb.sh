#!/bin/sh

if [ -e cells.db ]; then
  echo "table cells already exists"
else
  ./scripts/createTable.py
  ./scripts/insert.py
fi
