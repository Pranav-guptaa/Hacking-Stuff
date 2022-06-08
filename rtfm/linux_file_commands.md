# Linux File Commands
```
diff file1 file2 : compare files

rm -rf dir : force delete of dir

shred -f -u file : overwrite/delete file

touch -t 200203121212 file : set file timestamp 

touch -t YYYYMMDDHHSS file

sudo fdisk -l : list connected drives

md5sum -t file : compute md5 hash for a file

echo -n "str" | md5sum : generate md5 hash

sha1sum file : SHA1 hash of file

sort -u file : sort/show unique lines

grep -c "str" file : count lines/words/occurences of string in th file

tar -cf file.tar files : create .tar from files

tar -xf file.tar : extract .tar

tar -czf file.tar.gz files : create .tar.gz

tar -xzf file.tar.gz : extract .tar.gz

tar -cjf file.tar.bz2 files : create .tar.bz2

tar -xjf file.tar.bz2 : extract .tar.bz2

gzip file : compress file

gzip -d file/gz : decompress file

upx : compress or expand executable files

zip -r zipfilename.zip {Directory} : this zips all the files in the directory

zip -r ziping.zip . : zips the files of the current directory into ziping.zip

find -i -name file -type .pdf : finds pdf files ----> not able to find the exact command
```


