### End to End Agentic AI project ###

## Deploying to Hugging Face with GitHub Actions

This repository uses GitHub Actions to deploy to Hugging Face automatically.

### Setup:
1. Go to [Hugging Face](https://huggingface.co/settings/tokens) and create a new token with `write` access.
2. In your GitHub repository, go to **Settings → Secrets and variables → Actions**.
3. Add a new secret:
   - Name: `HF_TOKEN`
   - Value: *(Paste your Hugging Face token here)*.
4. Push your changes to the `main` branch to trigger deployment.

### Deployment Workflow:
- Every push to `main` will automatically update the Hugging Face repository.
- If there are no changes, the action will skip the commit.