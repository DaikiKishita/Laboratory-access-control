cd frontend
curl -sL https://deb.nodesource.com/setup_14.x | bash - && apt-get install -y nodejs && apt-get install -y npm && npm install -g @vue/cli && npm install --force && npm run build