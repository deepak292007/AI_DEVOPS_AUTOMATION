FROM node:20-alpine

WORKDIR /app

COPY . .

# Install root deps (if any)
RUN npm install

# Install & build frontend
RUN cd my-app/client && npm install && npm run build

# Install server deps
RUN cd my-app/server && npm install

EXPOSE 3000

CMD ["node", "my-app/server/index.js"]