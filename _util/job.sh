#!/bin/sh

if [ "$#" -ne 1 ]; then
  echo "Syntax: job.sh tag"
  exit 1
fi

cat > tmp.md <<EOF
---
title: 
page:
posted:
closes:
---

EOF

vi tmp.md
DATE=`awk '/posted:/ { print $2 }' tmp.md`
if [ -z $DATE ]; then
  echo "Could not find date"
  exit
fi

awk '
/posted:/ { $3 = "12:00:00" }
/closes:/ { $3 = "12:00:00" }
{ print }' tmp.md > _jobads/$DATE-$1.md
rm tmp.md
echo "Wrote _jobads/$DATE-$1.md"
