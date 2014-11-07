#!/bin/sh

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
awk '
/start_date:/ { $3 = "12:00:00" }
/end_date:/ { $3 = "12:00:00" }
{ print }' tmp.md > _meetings/$DATE-$1.md
rm tmp.md
echo "Wrote _meetings/$DATE-$1.md"
