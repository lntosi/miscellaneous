Miscellaneous
=============

## script_rsync
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

## moc_files.py
1) Enter the number of files to generate: 5
2) Enter the size of each file in GB: 2
3) The destination folder is hardcoded.
4) Test files are created in the specified destination folder.
