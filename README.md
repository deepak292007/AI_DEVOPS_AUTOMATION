# AI_DEVOPS_AUTOMATION

# Feature: Dockerfile Generator Script

Author: Role E (Script Developer)

Branch: `feat/dockerfile-generator`

Status: Ready for Review

## 1. Summary

This branch introduces the `generate_dockerfile.py` script, which completes the first automation goal of Phase 2.

The purpose of this script is to automatically generate a complete, production-ready `Dockerfile` based on a pre-defined, team-approved template. This removes the risk of manual error and ensures every `Dockerfile` is consistent.

## 2. What I Did

Created `generate_dockerfile.py`: A Python script using argparse to handle command-line arguments.

Embedded Node.js Template: The script uses the final, working `Dockerfile` (created by Role C) as the golden template for the `node` app type.

Added Java Placeholder: A placeholder template for `java` is included, ready for when the team builds a Spring Boot app.

Tested Locally: The script was tested and successfully generates the correct `Dockerfile` when run.

## 3. How to Use (for Testing)

Make sure you are on this branch: git checkout dockerfile-generator  

Ensure you have Python 3 installed.

Run the script from your terminal:

python generate_dockerfile.py --type node


Expected Output:

A new file named Dockerfile will be created in your current directory.

The terminal will show a success message: Success! 'Dockerfile' for 'node' generated in /path/to/your/project
