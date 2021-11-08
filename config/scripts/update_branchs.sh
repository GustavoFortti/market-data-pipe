git checkout master
git pull
for i in indicator model model_ant new report; do
    git checkout dev-$i
    git merge master
    git add .
    git commit -m 'marge with master'
    git push -u origin dev-$i
    sleep 3
done
git checkout master