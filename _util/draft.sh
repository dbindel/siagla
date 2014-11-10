#!/bin/sh
cat > _draft/$1.md <<EOF
---
title: 
date: 
author: 
comments: true
---
EOF

vi _draft/$1.md
