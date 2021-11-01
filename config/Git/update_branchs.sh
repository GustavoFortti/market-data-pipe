git checkout master
for i in indicator model model_ant new report synphony; do
    git checkout master dev-$i
    git merge master
    sleep 3
done

# git checkout dev-indicator
# git checkout dev-model
# git merge master
# git checkout dev-model_ant
# git merge master
# git checkout dev-new
# git merge master
# git checkout dev-report
# git merge master
# git checkout dev-synphony
# git merge master