# ---------- STAGE 1: Build Frontend if exists ----------
FROM node:20-alpine AS frontend-build

WORKDIR /app

# Copy entire repo
COPY . .

# If client folder exists, build it
RUN if [ -d "my-app/client" ]; then \
      cd my-app/client && \
      npm install && \
      npm run build ; \
    fi

# ---------- STAGE 2: Backend ----------
FROM node:20-alpine

WORKDIR /app

COPY . .

# Install backend dependencies if server exists
RUN if [ -d "my-app/server" ]; then \
      cd my-app/server && \
      npm install ; \
    elif [ -f "package.json" ]; then \
      npm install ; \
    fi

# Copy built frontend into backend public folder if exists
RUN if [ -d "my-app/client/build" ] && [ -d "my-app/server" ]; then \
      mkdir -p my-app/server/public && \
      cp -r my-app/client/build/* my-app/server/public/ ; \
    fi

# Expose default port
EXPOSE 3000

# Smart start command
CMD if [ -f "my-app/server/index.js" ]; then \
      node my-app/server/index.js ; \
    elif [ -f "index.js" ]; then \
      node index.js ; \
    else \
      echo "No valid entry point found." && exit 1 ; \
    fi
