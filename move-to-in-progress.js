const fetch = require('node-fetch'); // Add this line issue #25
const { Octokit } = require('@octokit/rest');

async function main() {
  const token = process.env.PERSONAL_ACCESS_TOKEN;
  console.log('Token:', token);

  const eventData = JSON.parse(process.env.GITHUB_EVENT);
  const issueNumber = eventData.issue.number;
  console.log('Issue Number:', issueNumber);

  const octokit = new Octokit({
    auth: `token ${token}`,
    request: {
      fetch: require('node-fetch') // Provide the fetch implementation
    }
  });

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
