#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

sudo -H -u herp -- bash -c "ssh client@ks1 'sudo -u postgres pg_dump --clean -d wlndb | xz' | pv -cN Db-Fetch-Progress > db_dump_$(date +%Y-%m-%d).sql.xz"
sudo -H -u postgres -- bash -c "xz -d db_dump_$(date +%Y-%m-%d).sql.xz -c | pv -c | psql -d wlndb"
