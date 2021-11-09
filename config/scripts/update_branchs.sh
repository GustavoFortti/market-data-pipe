git checkout premaster
git pull
for i in indicator model premodel new report; do
    git checkout dev-$i
    git merge premaster
    git add .
    git commit -m 'marge with premaster'
    git push -u origin dev-$i
    sleep 3
done
git checkout premaster