FROM node:20-alpine

WORKDIR /app

COPY . .

# Install & build frontend
RUN cd my-app/client && npm install --silent && npm run build

# Install server deps
RUN cd my-app/server && npm install --silent

EXPOSE 3000

CMD ["node", "my-app/server/index.js"]
