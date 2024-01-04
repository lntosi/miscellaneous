Miscellaneous
=============

# script_rsync #
1) Make the files executable:
```shell
chmod +x script_rsync.sh
```
2) It is possible to run the script at the time of system boot:
```shell
crontab -e
```
3) Add this line:
```shell
@reboot /PATH/script_rsync.sh
```
