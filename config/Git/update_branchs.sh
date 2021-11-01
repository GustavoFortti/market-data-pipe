git checkout master
for i in indicator model model_ant new report synphony; do
    git checkout master dev-$i
    git merge master
    git add .
    git push -u origin dev-$i
    sleep 3
done