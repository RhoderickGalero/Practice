const { Octokit } = require('@octokit/rest');
const fetch = require('node-fetch');

async function main() {
  const token = process.env.PERSONAL_ACCESS_TOKEN;
  const octokit = new Octokit({
    auth: `token ${token}`,
    request: { fetch },
  });

  const issueNumber = process.env.GITHUB_EVENT_PATH
    ? JSON.parse(require('fs').readFileSync(process.env.GITHUB_EVENT_PATH, 'utf8')).issue.number
    : null;

  if (!issueNumber) {
    console.error('No issue number found.');
    return;
  }

  try {
    await octokit.issues.update({
      owner: process.env.GITHUB_REPOSITORY.split('/')[0],
      repo: process.env.GITHUB_REPOSITORY.split('/')[1],
      issue_number: issueNumber,
      labels: ['In Progress']
    });

    console.log(`Issue #${issueNumber} moved to In Progress`);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
