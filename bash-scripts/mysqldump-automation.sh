#!/bin/bash
if [[ $UID -ne 0 ]]; then
  sudo -p 'Restarting as root, password: ' bash $0 "$@"
  exit $?
fi
databases=$(mysql <<EOF
SHOW DATABASES;
EOF
)
for db in $databases; do
    if [ $db != "mysql" ] && [ $db != "information_schema" ] && [ $db != "Database" ];then
        echo dumping $db
	mysqldump $db > /data/home/customer/backup-${db}.sql
    fi
done

