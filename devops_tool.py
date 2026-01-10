import argparse
import os

# --- TEMPLATES ---

# Final approved Dockerfile (Role C)
node_dockerfile = """
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
"""

# The Master Pipeline (Updated with official Docker Actions and path filters)
# Note: We use quadruple braces {{{{ }}}} to allow Python's .format() to work 
# while keeping GitHub's ${{ }} syntax intact.
node_pipeline_template = """
name: Build & Push Docker Image

on:
  push:
    branches:
      - main
    paths:
      - Dockerfile
      - package.json
      - package-lock.json
      - index.js
      - .github/workflows/**

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: CI Build Validation
        run: |
          echo "CI pipeline is working"
          ls -la

      # Debug secrets presence (Validated by Role D)
      - name: Debug Docker secrets
        run: |
          if [ -z "${{{{ secrets.DOCKER_USERNAME }}}}" ]; then echo "DOCKER_USERNAME is EMPTY"; else echo "DOCKER_USERNAME exists"; fi
          if [ -z "${{{{ secrets.DOCKER_PASSWORD }}}}" ]; then echo "DOCKER_PASSWORD is EMPTY"; else echo "DOCKER_PASSWORD exists"; fi

      # Build Docker image
      - name: Build Docker Image
        run: |
          docker build -t {repo}:${{{{ github.run_number }}}} .

      # Tag image as latest
      - name: Tag Docker Image as latest
        run: |
          docker tag {repo}:${{{{ github.run_number }}}} {repo}:latest

      # Login using OFFICIAL Docker action (Important Fix from Role D)
      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{{{ secrets.DOCKER_USERNAME }}}}
          password: ${{{{ secrets.DOCKER_PASSWORD }}}}

      # Push images
      - name: Push Docker Image
        run: |
          docker push {repo}:${{{{ github.run_number }}}}
          docker push {repo}:latest
"""

# --- LOGIC ---

def generate_files(app_type, repo_name):
    """Generates the Dockerfile and the GitHub Actions Workflow."""
    
    print(f"🚀 AI DevOps Copilot: Starting automation for {app_type}...")

    # 1. Create the Dockerfile
    try:
        with open("Dockerfile", "w") as f:
            f.write(node_dockerfile.strip())
        print("✅ Created Dockerfile")
    except Exception as e:
        print(f"❌ Error creating Dockerfile: {e}")

    # 2. Create the .github/workflows directory if it doesn't exist
    try:
        os.makedirs(os.path.join(".github", "workflows"), exist_ok=True)
        
        # 3. Create the Workflow file
        # We format the template with the specific repo name
        workflow_path = os.path.join(".github", "workflows", "generated_pipeline.yml")
        formatted_workflow = node_pipeline_template.strip().format(repo=repo_name)
        
        with open(workflow_path, "w") as f:
            f.write(formatted_workflow)
        print(f"✅ Created {workflow_path}")
    except Exception as e:
        print(f"❌ Error creating directory or workflow file: {e}")

    print(f"\nSummary: Your {app_type} app is now ready to be pushed to {repo_name}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DevOps Automation Tool")
    parser.add_argument(
        "-t", "--type", 
        choices=['node'], 
        required=True,
        help="The application type (e.g., 'node')"
    )
    parser.add_argument(
        "-r", "--repo",
        default="chetanasivadurga/ai-devops",
        help="The Docker Hub repository path"
    )
    args = parser.parse_args()
    
    generate_files(args.type, args.repo)