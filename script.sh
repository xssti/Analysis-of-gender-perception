while true; do
    python3 scraping_articles.py
    if [ $? -eq 0 ]; then
        break
    fi
    echo 'Code failed, Retrying....'
    sleep 5
done
echo "Sucessfully executed!!"
