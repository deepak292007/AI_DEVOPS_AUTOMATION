FROM node:20-alpine

WORKDIR /my-app

# Copy entire project
COPY . .

# Install everything using root controller
RUN npm install

# Build frontend if it exists
RUN npm run build || echo "No client build step"

EXPOSE 3000


CMD ["npm", "start"]
