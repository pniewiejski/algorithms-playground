#!/bin/sh
# This scripts adds/overwrites the pre-commit hook in your local git repo
cat > .git/hooks/pre-commit <<EOL
#!/bin/sh
#
set -xe
./pretty-markdown.sh --check
EOL