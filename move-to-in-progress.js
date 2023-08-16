const { Octokit } = require('@octokit/rest');

async function main() {
  const token = process.env.PERSONAL_ACCESS_TOKEN;
  console.log('Token:', token); // Add this line to print the token
  const octokit = new Octokit({ auth: `token ${token}` });

  const eventData = JSON.parse(process.env.GITHUB_EVENT);
  const issueNumber = eventData.issue.number;
  console.log('Issue Number:', issueNumber); // Add this line to print the issue number

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
