const { Octokit } = require('@octokit/rest');

async function main() {
  const token = process.env.PERSONAL_ACCESS_TOKEN;
  const octokit = new Octokit({ auth: token });

  const issueNumber = JSON.parse(process.env.GITHUB_EVENT).issue.number;

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
