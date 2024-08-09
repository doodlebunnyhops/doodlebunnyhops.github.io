
# for f in ../*; do
#     if [ $f != "../archive" ]; then
#         # echo "$f"
#         testDate=$(sed -nr 's/date: ([0-9]{4}-[0-9]{2}-[0-9]{2})/\1/p' $f)
#         # title=$(sed -nr 's/date: ([0-9]{4}-[0-9]{2}-[0-9]{2})/\1/p' $f)
#         # aliases:
#         # - /blog/10-13-23.md
#         year=$(date -d $(echo $testDate) +'%Y')
#         month=$(date -d $(echo $testDate) +'%B')

#         echo 'Year: ' $year
#         echo 'Month: ' $month

#         if [ ! -d $year ]; then
#             mkdir -p $year/$month
#         elif [ ! -d $year/$month ]; then
#             mkdir -p $year/$month
#         fi

#         # move file to new folder
#         mv $f $year/$month/
#     fi
# done

#years folders
for y in *; do
    year=$(echo $y | sed -nr "s/.*\///p")
    if [ -d $y ]; then
        if ! test -f $y/_index.md; then
            echo writing year $y/_index.md
            # echo -e "---\ntitle: $year Archive\nnoindex: true\ndescription: "Archived Blogs about Brookhaven RP Updates, exciting news, and new findings"\ntype: blog_archive\n---" > $y/_index.md
            echo -e "---\ntitle: $year\nnoindex: true\ndescription: Archived Blogs about Brookhaven RP Updates, exciting news, and new findings\ntype: blog_archive\n---\n\n\n\n{{% children sort="date" showhidden=true description=false containerstyle="ul" style="li"  depth=2 %}}" > $y/_index.md
        fi
        # month folders
        for m in $y/*; do
            month=$(echo $m | sed -nr "s/.*\///p")
            if [ -d $m ]; then
                if ! test -f $m/_index.md; then
                    echo writing month $m/_index.md
                    # echo -e "---\ntitle: $m Archive\nnoindex: true\ndescription: "Archived Blogs about Brookhaven RP Updates, exciting news, and new findings"\ntype: blog_archive\n---" > $m/_index.md
                    echo -e "---\ntitle: $month\nnoindex: true\ndescription: Archived Blogs about Brookhaven RP Updates, exciting news, and new findings\ntype: blog_archive\n---\n\n\n\n{{% children sort="date" showhidden=true description=true style="h2"  depth=3 %}}" > $m/_index.md
                fi
            fi
        done
    fi
done
