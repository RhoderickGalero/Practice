const { Octokit } = require('@octokit/rest');

async function main() {
  const token = process.env.PERSONAL_ACCESS_TOKEN;
  const octokit = new Octokit({ auth: token });

  const issueNumber = process.env.GITHUB_EVENT_PATH
    ? require('fs').readFileSync(process.env.GITHUB_EVENT_PATH, 'utf8')
    : '{}';

  try {
    await octokit.issues.update({
      owner: process.env.GITHUB_REPOSITORY.split('/')[0],
      repo: process.env.GITHUB_REPOSITORY.split('/')[1],
      issue_number: JSON.parse(issueNumber).issue.number,
      labels: ['In Progress']
    });

    console.log(`Issue #${JSON.parse(issueNumber).issue.number} moved to In Progress`);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
