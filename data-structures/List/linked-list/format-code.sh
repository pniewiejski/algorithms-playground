set -xe
for DIR in ./
do
    find $DIR -regex '.*\.[ch]p*' -exec clang-format -style=file -i {} \;
done 
