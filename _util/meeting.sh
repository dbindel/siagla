#!/bin/sh

if [ "$#" -ne 1 ]; then
  echo "Syntax: meeting.sh tag"
  exit 1
fi

cat > tmp.md <<EOF
---
title: 
page:
start_date:
end_date:
where:
type:
---

EOF

vi tmp.md
DATE=`awk '/start_date:/ { print $2 }' tmp.md`
if [ -z $DATE ]; then
  echo "Could not find date"
  exit
fi

awk '
/start_date:/ { $3 = "12:00:00" }
/end_date:/ { $3 = "12:00:00" }
{ print }' tmp.md > _meetings/$DATE-$1.md
rm tmp.md
echo "Wrote _meetings/$DATE-$1.md"
