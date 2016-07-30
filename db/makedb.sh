#!/bin/bash

echo "Build database..."
pushd ./db/

if [ -e cells.db ]; then
	echo "Removing the existing database..."
	rm cells.db
	echo "Completed."
fi

echo "Creating database tables..."
./scripts/createTable.py
echo "Completed."

echo "Inserting data..."
./scripts/insert.py
echo "Completed."

popd
