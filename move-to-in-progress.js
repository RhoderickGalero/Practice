const { request } = require('@octokit/request');

async function main() {
  const token = process.env.PERSONAL_ACCESS_TOKEN;
  console.log('Token:', token);

  const eventData = JSON.parse(process.env.GITHUB_EVENT);
  const issueNumber = eventData.issue.number;
  console.log('Issue Number:', issueNumber);

  const octokit = request.defaults({
    headers: {
      authorization: `token ${token}`
    }
  });

  try {
    await octokit.patch(`/repos/${process.env.GITHUB_REPOSITORY}/issues/${issueNumber}`, {
      labels: ['In Progress']
    });

    console.log(`Issue #${issueNumber} moved to In Progress`);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
